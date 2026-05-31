# case_view.py

import streamlit as st
from data.cases import CASE_LIBRARY
from data.anatomy import ANATOMY
from core.formatters import normalize_result_text
from utils.helpers import (
    get_case_names_for_selection,
    normalize_case_item_name,
    get_compact_item_label,
)


def _get_side_labels(case):
    """
    모바일 화면에서 더 자연스러운 좌/우 표기 생성
    """
    side = case.get("patient", {}).get("side", "")

    if side == "우":
        return "반대측", "병변측(우)"
    if side == "좌":
        return "병변측(좌)", "반대측"
    if side == "양측":
        return "좌측", "우측"
    return "좌측/정상측", "우측/병변측"


def _render_bullets(items):
    for item in items:
        st.markdown(f'<div class="case-bullet">• {item}</div>', unsafe_allow_html=True)


def _render_exam_section(title, items):
    if not items:
        return
    st.markdown(
        f'<div class="finding-item-title" style="margin-top:12px; color:#2563eb;">■ {title}</div>',
        unsafe_allow_html=True
    )
    html = "".join(
        [f'<div class="case-bullet" style="margin-left: 10px;">• {item}</div>' for item in items]
    )
    st.markdown(f'<div class="case-text-block">{html}</div>', unsafe_allow_html=True)


def render_case_selector_only():
    case_options = get_case_names_for_selection()

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">📖 대표 사례 선택</div>', unsafe_allow_html=True)

    selected_case = st.radio(
        "대표 사례 선택",
        case_options,
        label_visibility="collapsed"
    )

    st.markdown(
        '<div class="result-small" style="margin-top:6px;">관심 있는 대표 사례를 선택한 뒤 학습을 시작하세요.</div>',
        unsafe_allow_html=True
    )

    if st.button("사례 학습 시작", type="primary", use_container_width=True):
        st.session_state["confirmed_case"] = selected_case
        st.session_state["current_screen"] = "case_detail"
        st.session_state["last_result"] = None
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


def render_case_learning_info(case_name):
    case = CASE_LIBRARY.get(case_name)
    if not case:
        st.warning("선택한 사례 정보를 찾을 수 없습니다.")
        return

    patient = case.get("patient", {})
    findings = case.get("findings", {})
    physical_exam = patient.get("physical_exam", {})
    left_label, right_label = _get_side_labels(case)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="case-title-mobile">📘 {case_name}</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="case-subtitle-mobile">연령: {patient.get("age", "-")}세 | 성별: {patient.get("sex", "-")} | 병변측: {patient.get("side", "-")}</div>',
        unsafe_allow_html=True
    )

    category = case.get("category", "")
    difficulty = case.get("difficulty", "")
    st.markdown(
        f'<div class="result-small" style="margin-top:6px;">분류: {category or "-"} | 난이도: {difficulty or "-"}</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="case-section-label">🗣️ 주요 증상</div>', unsafe_allow_html=True)
    _render_bullets(patient.get("symptoms", []))

    st.markdown('<div class="case-section-label">🧪 이학적 검사결과</div>', unsafe_allow_html=True)
    for exam_category, exam_items in physical_exam.items():
        _render_exam_section(exam_category, exam_items)

    st.markdown('<hr class="strong-divider">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">⚡ 주요 검사 소견</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="result-small" style="margin-bottom:8px;">검사 항목은 모바일 화면에 맞게 축약 표기되며, 진단 설명에서는 전체 의미를 함께 해석합니다.</div>',
        unsafe_allow_html=True
    )

    sensory_items, motor_items, needle_items, reflex_items = [], [], [], []

    for item_name, values in findings.items():
        normalized_name = normalize_case_item_name(item_name)
        anatomy = ANATOMY.get(normalized_name, {})
        domain = anatomy.get("domain")

        if domain == "sensory":
            sensory_items.append((normalized_name, values))
        elif domain == "motor":
            motor_items.append((normalized_name, values))
        elif domain == "muscle":
            needle_items.append((normalized_name, values))
        else:
            reflex_items.append((normalized_name, values))

    def render_finding_group(title, items):
        if not items:
            return

        st.markdown(
            f'<div class="finding-item-title" style="margin-top:16px; color:#065f46;">✔ {title}</div>',
            unsafe_allow_html=True
        )

        for name, values in items:
            left_val = values[0] if len(values) > 0 else ""
            right_val = values[1] if len(values) > 1 else ""
            compact_label = get_compact_item_label(name)

            st.markdown(
                f"""
                <div class="case-text-block" style="padding: 8px 11px;">
                    <div style="font-weight: 600; font-size: 0.88rem; color: #0f172a;">{compact_label}</div>
                    <div class="finding-subtext" style="margin-bottom:0;"><b>{left_label}:</b> {normalize_result_text(left_val)}</div>
                    <div class="finding-subtext" style="margin-bottom:0;"><b>{right_label}:</b> {normalize_result_text(right_val)}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    render_finding_group("감각신경전도검사", sensory_items)
    render_finding_group("운동신경전도검사", motor_items)
    render_finding_group("침근전도검사", needle_items)
    render_finding_group("특수 및 반사검사", reflex_items)

    teaching_dx = case.get("teaching_diagnosis", {})
    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">💡 왜 이 진단을 생각하는가?</div>', unsafe_allow_html=True)

    if teaching_dx.get("summary"):
        st.markdown(
            f'<div class="case-bullet" style="font-weight:600; color:#1d4ed8;">• 핵심 요약: {teaching_dx["summary"]}</div>',
            unsafe_allow_html=True
        )

    reason_sections = [
        ("ncs_reason", "신경전도검사 기반 해석"),
        ("emg_reason", "침근전도 및 기타검사 기반 해석"),
        ("integration", "종합 해석"),
    ]

    for key, label in reason_sections:
        if teaching_dx.get(key):
            st.markdown(f'<div class="case-subheading">{label}</div>', unsafe_allow_html=True)
            for line in teaching_dx[key]:
                st.markdown(f'<div class="case-bullet">• {line}</div>', unsafe_allow_html=True)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">🔍 감별진단 가이드</div>', unsafe_allow_html=True)

    differential_list = case.get("differential_diagnosis", [])
    if not differential_list:
        st.markdown('<div class="result-small">등록된 감별진단 정보가 없습니다.</div>', unsafe_allow_html=True)
    else:
        for idx, dx_item in enumerate(differential_list, 1):
            st.markdown(
                f"""
                <div class="case-text-block" style="background:#fffaf3; border-left:4px solid #f59e0b;">
                    <div class="finding-item-title" style="color:#b45309;">{idx}. {dx_item.get("name", "")}</div>
                    <div class="finding-subtext"><b>고려 이유:</b> {dx_item.get("why_consider", "")}</div>
                    <div class="finding-subtext"><b>감별 포인트:</b> {dx_item.get("how_to_differentiate", "")}</div>
                    <div class="finding-subtext" style="color:#0f172a; font-weight:600;"><b>💡 학생 팁:</b> {dx_item.get("practical_tip", "")}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown(
        '<div class="result-small" style="margin-top:14px;">※ 본 사례는 학생 교육용 학습 자료이며, 실제 환자 진단은 병력·진찰·영상·전기생리 소견을 함께 종합해야 합니다.</div>',
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)
