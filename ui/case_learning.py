# ui/case_learning.py

import streamlit as st

from data.cases import CASE_LIBRARY
from data.constants import ANATOMY
from data.terms import (
    ncs_amplitude_latency,
    emg_case_label,
    special_term_label,
)
from engine.inference import split_findings_by_domain, summarize_abnormal_findings
from ui.navigation import render_bottom_navigation
from helpers import side_to_korean, lesion_side_index, color_class_for_text
from formatters import html_escape


def _patient_side_to_display(side):
    return side_to_korean(side)


def _get_value_for_lesion_side(values, side):
    """
    좌/우 tuple에서 병변측 결과를 가져옵니다.
    양측이면 None을 반환하여 별도 양측 표로 처리합니다.
    """
    idx = lesion_side_index(side)

    if idx is None:
        return None

    if len(values) > idx:
        return values[idx]

    return values[0] if values else ""


def _render_learning_frame(selected):
    """
    사례 학습 모드의 공통 사고 프레임.
    요청사항 반영:
    - 사례 학습은 수치표보다 임상 추론 중심.
    - 진폭/잠복기 기준에는 '정상측 대비' 문구를 포함.
    - 침근전도는 사례 학습에서는 단순화하고, 실제 전위명은 기준 팁에서 설명.
    """
    if "뇌졸중" in selected:
        st.markdown(
            """
            <div class="warn-card">
                <div class="finding-highlight" style="color:#7c3aed;">🎓 학생용 사고 프레임: H-반사와 경직 평가</div>
                <div class="case-bullet">1. H-반사는 말초 운동신경 전도검사라기보다 척수 단일시냅스 반사고리의 흥분성을 보는 검사입니다.</div>
                <div class="case-bullet">2. 위운동신경세포 병변 이후에는 척수 반사 흥분성이 증가하여 H-반사 진폭 또는 H/M 비율이 증가할 수 있습니다.</div>
                <div class="case-bullet">3. 물리치료 중재 전후 H/M 비율 변화를 비교하면 경직 완화 정도를 정량적으로 설명하는 데 도움이 됩니다.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    if "눈꺼풀" in selected or "얼굴" in selected:
        st.markdown(
            """
            <div class="warn-card" style="border-left-color:#0d9488; background:#f0fdfa;">
                <div class="finding-highlight" style="color:#0d9488;">🎓 학생용 사고 프레임: 얼굴신경 및 눈깜빡반사 판독</div>
                <div class="case-bullet">1. 얼굴신경마비에서는 자극 방향과 반응측을 나누어 말초 얼굴신경, 삼차신경 들신경 경로, 뇌줄기 반사 회로를 구분합니다.</div>
                <div class="case-bullet">2. 얼굴신경 운동반응의 진폭 감소는 정상측 대비 운동축삭 손상 정도를 추정하는 데 도움이 됩니다.</div>
                <div class="case-bullet">3. 급성기 침근전도는 아직 비정상 자발전위가 나타나지 않을 수 있으므로 발병 시기와 함께 해석해야 합니다.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    st.markdown(
        """
        <div class="warn-card">
            <div class="finding-highlight" style="color:#b45309;">🎓 사례 학습용 근전도 판독 기준 팁</div>
            <div class="case-bullet">1. <b>진폭 감소</b>: 병변측 진폭이 정상측 대비 약 50% 이하로 감소하면 축삭 손상 또는 심한 전도차단 가능성을 의심합니다.</div>
            <div class="case-bullet">2. <b>잠복기 지연</b>: 병변측 잠복기가 정상측 대비 약 130% 이상 길어지면 말이집탈락 또는 국소 포착성 전도 지연 가능성을 의심합니다.</div>
            <div class="case-bullet">3. <b>감각신경활동전위 보존</b>: 신경뿌리병증은 뒤뿌리신경절보다 몸쪽 병변이므로 말초 감각신경활동전위가 보존되는 경우가 많습니다.</div>
            <div class="case-bullet">4. <b>비정상 자발전위</b>: 실제 전위명으로는 fibrillation potential, positive sharp wave, fasciculation potential 등이 있으며, 사례 학습 표에서는 이해를 돕기 위해 간략화해 표시합니다.</div>
            <div class="case-bullet">5. <b>운동단위 동원감소</b>: 수의수축 시 동원 가능한 운동단위 수가 줄어든 상태로, 운동축삭 손상 또는 하위운동신경계 병변을 시사합니다.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_patient_card(selected, patient):
    side = _patient_side_to_display(patient.get("side", "-"))

    st.markdown('<div class="info-card">', unsafe_allow_html=True)
    st.markdown(
        f'<div class="case-title-mobile">👤 환자 사례: {html_escape(selected)}</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f"""
        <div class="case-subtitle-mobile">
            <span class="label-strong">연령/성별:</span>
            <span class="result-value">{html_escape(patient.get("age", "-"))}세 / {html_escape(patient.get("sex", "-"))}</span>
            &nbsp;|&nbsp;
            <span class="label-strong">병변측:</span>
            <span class="result-value">{html_escape(side)}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)


def _render_symptoms(patient):
    st.markdown('<div class="case-section-label">🗣️ 주요 증상</div>', unsafe_allow_html=True)

    symptoms_html = "".join(
        [f'<div class="case-bullet">• {html_escape(symptom)}</div>' for symptom in patient.get("symptoms", [])]
    )

    st.markdown(
        f'<div class="case-text-block">{symptoms_html}</div>',
        unsafe_allow_html=True,
    )


def _render_physical_exam(patient):
    """
    요청사항 반영:
    - 반사 검사 항목은 더 굵게 표시합니다.
    """
    st.markdown('<div class="case-section-label">🧪 이학적 검사결과</div>', unsafe_allow_html=True)

    exam_html = []

    for section_name, items in patient.get("physical_exam", {}).items():
        section_name_escaped = html_escape(section_name)
        is_reflex_section = "반사" in section_name_escaped

        exam_html.append(
            f'<div class="finding-highlight" style="color:#475569;">[{section_name_escaped}]</div>'
        )

        for item in items:
            item_escaped = html_escape(item)
            parts = item_escaped.split(":", 1)

            if len(parts) == 2:
                label = parts[0].strip()
                value = parts[1].strip()

                if is_reflex_section:
                    exam_html.append(
                        f"""
                        <div class="case-bullet">
                            <span class="label-strong" style="font-weight:900!important; color:#0f172a!important;">{label}:</span>
                            <span class="result-value"> {value}</span>
                        </div>
                        """
                    )
                else:
                    exam_html.append(
                        f"""
                        <div class="case-bullet">
                            <span class="label-strong">{label}:</span>
                            <span class="result-value"> {value}</span>
                        </div>
                        """
                    )
            else:
                if is_reflex_section:
                    exam_html.append(
                        f'<div class="case-bullet" style="font-weight:800; color:#0f172a;">• {item_escaped}</div>'
                    )
                else:
                    exam_html.append(f'<div class="case-bullet">• {item_escaped}</div>')

    st.markdown(
        f'<div class="case-text-block">{"".join(exam_html)}</div>',
        unsafe_allow_html=True,
    )


def _render_simple_table(headers, rows):
    thead = "".join([f"<th>{html_escape(h)}</th>" for h in headers])

    tbody_rows = []

    for row in rows:
        cells = []

        for idx, col in enumerate(row):
            col_text = "" if col is None else str(col)
            css_class = "left" if idx == 0 else ""
            color_class = color_class_for_text(col_text) if idx > 0 else ""

            cells.append(
                f'<td class="{css_class} {color_class}">{html_escape(col_text)}</td>'
            )

        tbody_rows.append(f"<tr>{''.join(cells)}</tr>")

    return (
        '<div class="edu-table-wrap">'
        '<table class="edu-table">'
        f"<thead><tr>{thead}</tr></thead>"
        f"<tbody>{''.join(tbody_rows)}</tbody>"
        "</table>"
        "</div>"
    )


def _render_ncs_block(title, findings, side):
    """
    사례 학습용 NCS 표.
    요청사항 반영:
    - 판단 열 삭제
    - 진폭/잠복기에는 감소, 지연, 정상 범위 등만 기재
    - 괄호 설명 삭제
    """
    if not findings:
        return

    st.markdown(f'<div class="case-section-label">{html_escape(title)}</div>', unsafe_allow_html=True)

    if side in {"양측", "양쪽"}:
        rows = []

        for item, values in findings.items():
            left = values[0] if len(values) > 0 else ""
            right = values[1] if len(values) > 1 else ""

            left_parsed = ncs_amplitude_latency(left)
            right_parsed = ncs_amplitude_latency(right)

            rows.append(
                [
                    item,
                    left_parsed.get("amplitude", ""),
                    left_parsed.get("latency", ""),
                    right_parsed.get("amplitude", ""),
                    right_parsed.get("latency", ""),
                ]
            )

        html = _render_simple_table(
            ["검사 신경", "좌측 진폭", "좌측 잠복기", "우측 진폭", "우측 잠복기"],
            rows,
        )
    else:
        rows = []

        for item, values in findings.items():
            lesion_value = _get_value_for_lesion_side(values, side)
            parsed = ncs_amplitude_latency(lesion_value)

            rows.append(
                [
                    item,
                    parsed.get("amplitude", ""),
                    parsed.get("latency", ""),
                ]
            )

        html = _render_simple_table(
            ["검사 신경", "진폭", "잠복기"],
            rows,
        )

    st.markdown(html, unsafe_allow_html=True)
    st.markdown(
        '<div class="table-note">※ 사례 학습에서는 실제 수치 대신 병변측의 핵심 변화만 간략화하여 표시합니다. 구체 기준은 위 판독 기준 팁을 참고합니다.</div>',
        unsafe_allow_html=True,
    )


def _render_emg_block(title, findings, side):
    """
    사례 학습용 침근전도 표.
    요청사항 반영:
    - 판단 열 삭제
    - 실제 전위명 대신 비정상 자발전위/운동단위 동원감소 등으로 단순화
    - 자세한 생리학적 해석은 통합 해석에서 설명
    """
    if not findings:
        return

    st.markdown(f'<div class="case-section-label">{html_escape(title)}</div>', unsafe_allow_html=True)

    if side in {"양측", "양쪽"}:
        rows = []

        for item, values in findings.items():
            left = values[0] if len(values) > 0 else ""
            right = values[1] if len(values) > 1 else ""

            left_parsed = emg_case_label(left)
            right_parsed = emg_case_label(right)

            rows.append(
                [
                    item,
                    left_parsed.get("rest", ""),
                    left_parsed.get("volition", ""),
                    right_parsed.get("rest", ""),
                    right_parsed.get("volition", ""),
                ]
            )

        html = _render_simple_table(
            ["검사 근육", "좌 휴식 시", "좌 수의수축 시", "우 휴식 시", "우 수의수축 시"],
            rows,
        )
    else:
        rows = []

        for item, values in findings.items():
            lesion_value = _get_value_for_lesion_side(values, side)
            parsed = emg_case_label(lesion_value)

            rows.append(
                [
                    item,
                    parsed.get("rest", ""),
                    parsed.get("volition", ""),
                ]
            )

        html = _render_simple_table(
            ["검사 근육", "휴식 시", "수의수축 시"],
            rows,
        )

    st.markdown(html, unsafe_allow_html=True)
    st.markdown(
        '<div class="table-note">※ 사례 학습에서는 침근전도 전위명을 모두 나열하기보다 병변 위치 추론에 필요한 수준으로 단순화했습니다.</div>',
        unsafe_allow_html=True,
    )


def _render_reflex_block(title, findings, side):
    if not findings:
        return

    st.markdown(f'<div class="case-section-label">{html_escape(title)}</div>', unsafe_allow_html=True)

    rows = []

    if side in {"양측", "양쪽"}:
        for item, values in findings.items():
            left = values[0] if len(values) > 0 else ""
            right = values[1] if len(values) > 1 else ""

            rows.append(
                [
                    item,
                    special_term_label(left),
                    special_term_label(right),
                ]
            )

        html = _render_simple_table(
            ["검사 항목", "좌측 결과", "우측 결과"],
            rows,
        )
    else:
        for item, values in findings.items():
            lesion_value = _get_value_for_lesion_side(values, side)
            rows.append(
                [
                    item,
                    special_term_label(lesion_value),
                ]
            )

        html = _render_simple_table(
            ["검사 항목", "결과"],
            rows,
        )

    st.markdown(html, unsafe_allow_html=True)


def _render_teaching_result(selected, teaching, diff_dx):
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.markdown('<div class="result-title">✅ 임상 추론 및 통합 해석</div>', unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="case-text-block" style="background:#fff1f2!important; border-left-color:#fecdd3!important;">
            <span class="label-strong text-red">최종 교육용 의심 진단:</span>
            <span class="result-value text-red" style="font-weight:800!important;">
                {html_escape(teaching.get("summary", ""))}
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if teaching.get("ncs_reason"):
        if "눈꺼풀" in selected or "얼굴" in selected:
            label = "얼굴신경/눈깜빡반사 해석 포인트"
        elif "뇌졸중" in selected:
            label = "H-반사 및 경직 평가 해석 포인트"
        else:
            label = "신경전도검사 해석 포인트"

        st.markdown(f'<div class="result-label">{html_escape(label)}</div>', unsafe_allow_html=True)

        for text in teaching.get("ncs_reason", []):
            st.markdown(
                f'<div class="result-text">• {html_escape(text)}</div>',
                unsafe_allow_html=True,
            )

    if teaching.get("emg_reason"):
        is_special_case = (
            "눈꺼풀" in selected
            or "얼굴" in selected
            or "뇌졸중" in selected
        )

        if not is_special_case:
            st.markdown('<div class="result-label">침근전도검사 해석 포인트</div>', unsafe_allow_html=True)

            for text in teaching.get("emg_reason", []):
                text_escaped = html_escape(text.strip())

                if text.strip().startswith(("1)", "2)", "3)", "4)")):
                    st.markdown(
                        f'<div class="result-text label-strong text-blue" style="margin-top:14px;">{text_escaped}</div>',
                        unsafe_allow_html=True,
                    )
                elif text.strip().endswith(":"):
                    st.markdown(
                        f'<div class="result-text label-strong" style="margin-top:14px; color:#b45309!important;">{text_escaped}</div>',
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown(
                        f'<div class="result-text">• {text_escaped}</div>',
                        unsafe_allow_html=True,
                    )

    if teaching.get("integration"):
        st.markdown('<div class="result-label">검사 결과 통합 해석</div>', unsafe_allow_html=True)

        for text in teaching.get("integration", []):
            st.markdown(
                f'<div class="result-text">• {html_escape(text)}</div>',
                unsafe_allow_html=True,
            )

    st.markdown("</div>", unsafe_allow_html=True)

    if diff_dx:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="case-section-label">🧭 감별진단 포인트</div>', unsafe_allow_html=True)

        for idx, item in enumerate(diff_dx):
            st.markdown(
                f'<div class="finding-highlight">{html_escape(item.get("name", ""))}</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                f"""
                <div class="case-bullet">
                    <span class="label-strong">왜 고려하나:</span>
                    <span class="result-value"> {html_escape(item.get("why_consider", ""))}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.markdown(
                f"""
                <div class="case-bullet">
                    <span class="label-strong">어떻게 구분하나:</span>
                    <span class="result-value"> {html_escape(item.get("how_to_differentiate", ""))}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.markdown(
                f"""
                <div class="case-bullet">
                    <span class="label-strong text-green">실전 팁:</span>
                    <span class="result-value"> {html_escape(item.get("practical_tip", ""))}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

            if idx < len(diff_dx) - 1:
                st.markdown('<hr class="item-divider">', unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)


def render_case_list():
    st.markdown('<div class="main-title">사례 학습 모드</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="subtle">
            환자의 증상, 이학적 검사, 간략화된 근전도 소견을 종합하여
            구체적 질환과 손상 위치를 추론하는 임상 사고 훈련 모드입니다.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">📋 학습할 가상 사례 선택</div>', unsafe_allow_html=True)

    case_names = ["선택 안 함"] + list(CASE_LIBRARY.keys())

    if "case_reset_counter" not in st.session_state:
        st.session_state["case_reset_counter"] = 0

    dynamic_radio_key = f"case_radio_selector_{st.session_state['case_reset_counter']}"

    selected = st.radio(
        "학습할 임상 증상 선택",
        case_names,
        key=dynamic_radio_key,
        label_visibility="collapsed",
    )

    st.markdown("</div>", unsafe_allow_html=True)

    if selected != "선택 안 함":
        case = CASE_LIBRARY[selected]
        patient = case.get("patient", {})
        findings = case.get("findings", {})
        teaching = case.get("teaching_diagnosis", {})
        diff_dx = case.get("differential_diagnosis", [])

        raw_side = patient.get("side", "-")
        side = _patient_side_to_display(raw_side)

        _render_patient_card(selected, patient)
        _render_symptoms(patient)
        _render_physical_exam(patient)
        _render_learning_frame(selected)

        grouped = split_findings_by_domain(findings, ANATOMY)

        abnormal_summary = summarize_abnormal_findings(findings, lesion_side=raw_side)

        st.markdown(
            f"""
            <div class="info-card">
                <div class="finding-highlight">🔎 병변 위치 추론을 위한 소견 요약</div>
                <div class="case-bullet">
                    병변측 중심으로 확인되는 이상 항목은 총
                    <span class="text-red" style="font-weight:900;">{abnormal_summary.get("count", 0)}개</span>입니다.
                    단순 개수보다 중요한 것은 <b>어떤 신경, 어떤 근육, 어떤 분절이 함께 침범되는지</b>입니다.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if grouped["sensory"]:
            _render_ncs_block("감각신경전도검사: 병변측 핵심 변화", grouped["sensory"], side)

        if grouped["motor"]:
            _render_ncs_block("운동신경전도검사: 병변측 핵심 변화", grouped["motor"], side)

        if grouped["muscle"] and "눈꺼풀" not in selected and "뇌졸중" not in selected:
            _render_emg_block("침근전도검사: 병변측 핵심 변화", grouped["muscle"], side)

        if grouped["reflex"] or grouped["other"]:
            merged = {**grouped["reflex"], **grouped["other"]}

            if "뇌졸중" in selected:
                title = "H-반사 및 경직 정량검사"
            elif "눈꺼풀" in selected or "얼굴" in selected:
                title = "얼굴신경/눈깜빡반사 관련 검사"
            else:
                title = "반사 및 후기반응 검사"

            _render_reflex_block(title, merged, side)

        _render_teaching_result(selected, teaching, diff_dx)

        st.markdown('<div class="start-button-wrap">', unsafe_allow_html=True)
        if st.button("🔄 다른 사례 분석", type="secondary", use_container_width=True, key="reset_case_radio_btn"):
            st.session_state["case_reset_counter"] += 1
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    render_bottom_navigation()


def render_case_detail():
    """
    현재 앱은 별도 상세 화면 대신 case_list에서 선택 즉시 상세 내용을 보여줍니다.
    라우터 호환을 위해 유지합니다.
    """
    st.session_state["screen"] = "case_list"
    st.rerun()
