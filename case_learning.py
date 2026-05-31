# ui/case_learning.py

import streamlit as st

from data.cases import CASE_LIBRARY
from data.constants import ANATOMY
from engine.inference import (
    normalize_result_text,
    split_findings_by_domain,
    build_case_report_text,
    summarize_case_metadata,
    match_cases_by_filters,
)
from ui.navigation import render_bottom_navigation


def _summarize_case_badges(case):
    badges = []
    category = case.get("category")
    difficulty = case.get("difficulty")

    if category:
        badges.append(("badge", category))
    if difficulty:
        color = "badge-green" if difficulty in ["초중급", "중급"] else "badge-amber"
        badges.append((color, difficulty))
    return badges


def _build_case_filter_options():
    categories = sorted({v.get("category", "기타") for v in CASE_LIBRARY.values()})
    difficulties = sorted({v.get("difficulty", "기타") for v in CASE_LIBRARY.values()})
    return categories, difficulties


def render_case_list():
    st.markdown('<div class="main-title">사례 학습</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtle">증상, 이학적 검사, 전기진단 소견을 통합해 병변 위치와 감별 포인트를 학습합니다.</div>',
        unsafe_allow_html=True
    )

    categories, difficulties = _build_case_filter_options()

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">📚 사례 선택</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        selected_category = st.selectbox("질환 범주", ["전체"] + categories, index=0)
    with c2:
        selected_difficulty = st.selectbox("난이도", ["전체"] + difficulties, index=0)

    keyword = st.text_input("검색어", placeholder="예: 발처짐, 손저림, C6, 자신경, CIDP")

    filtered = match_cases_by_filters(
        CASE_LIBRARY,
        category=selected_category,
        difficulty=selected_difficulty,
        keyword=keyword
    )

    st.markdown(f'<div class="mobile-note">총 {len(filtered)}개 사례</div>', unsafe_allow_html=True)

    if not filtered:
        st.warning("조건에 맞는 사례가 없습니다.")
        st.markdown('</div>', unsafe_allow_html=True)
        render_bottom_navigation()
        return

    case_names = [name for name, _ in filtered]
    selected = st.radio("사례 목록", case_names, label_visibility="collapsed")

    if selected:
        case = CASE_LIBRARY[selected]
        meta = summarize_case_metadata(selected, case)
        badges = _summarize_case_badges(case)
        badge_html = "".join([f'<span class="badge {cls}">{label}</span>' for cls, label in badges])

        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="case-title-mobile">{meta["case_name"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="badge-row">{badge_html}</div>', unsafe_allow_html=True)
        st.markdown(
            f'<div class="case-subtitle-mobile"><span class="label-strong text-blue">연령:</span> <span class="result-value">{meta["age"]}세</span> | <span class="label-strong text-blue">성별:</span> <span class="result-value">{meta["sex"]}</span> | <span class="label-strong text-blue">병변측:</span> <span class="result-value">{meta["side"]}</span></div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div class="mobile-note"><span class="label-strong text-blue">핵심 증상:</span> <span class="result-value">{meta["chief_summary"]}</span></div>',
            unsafe_allow_html=True
        )
        st.markdown('</div>', unsafe_allow_html=True)

        if st.button("선택한 사례 학습", type="primary", use_container_width=True):
            st.session_state["selected_case"] = selected
            st.session_state["screen"] = "case_detail"
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
    render_bottom_navigation()


def _render_finding_block(title, findings, side):
    if not findings:
        return

    st.markdown(f'<div class="case-section-label">{title}</div>', unsafe_allow_html=True)
    block_parts = []

    items = list(findings.items())
    for idx, (item, values) in enumerate(items):
        # [주의] values[0]은 좌측 데이터, values[1]은 우측 데이터로 매핑됩니다.
        left = values[0] if len(values) > 0 else ""
        right = values[1] if len(values) > 1 else ""

        lines = [f'<div class="finding-highlight">{item}</div>']

        if side == "양측":
            lines.append(f'<div class="finding-subtext">• <span class="label-strong text-blue">좌측:</span> <span class="result-value">{normalize_result_text(left)}</span></div>')
            lines.append(f'<div class="finding-subtext">• <span class="label-strong text-blue">우측:</span> <span class="result-value">{normalize_result_text(right)}</span></div>')
        elif str(right).strip() != "":
            if side == "우":
                lines.append(f'<div class="finding-subtext">• <span class="label-strong text-green">좌측(정상측):</span> <span class="result-value">{normalize_result_text(left)}</span></div>')
                lines.append(f'<div class="finding-subtext">• <span class="label-strong text-red">우측(병변측):</span> <span class="result-value">{normalize_result_text(right)}</span></div>')
            elif side == "좌":
                lines.append(f'<div class="finding-subtext">• <span class="label-strong text-red">좌측(병변측):</span> <span class="result-value">{normalize_result_text(left)}</span></div>')
                lines.append(f'<div class="finding-subtext">• <span class="label-strong text-green">우측(정상측):</span> <span class="result-value">{normalize_result_text(right)}</span></div>')
            else:
                lines.append(f'<div class="finding-subtext">• <span class="label-strong text-blue">좌측:</span> <span class="result-value">{normalize_result_text(left)}</span></div>')
                lines.append(f'<div class="finding-subtext">• <span class="label-strong text-blue">우측:</span> <span class="result-value">{normalize_result_text(right)}</span></div>')
        else:
            lines.append(f'<div class="finding-subtext">• <span class="label-strong text-blue">결과:</span> <span class="result-value">{normalize_result_text(left)}</span></div>')

        block_parts.append(f'<div class="compact-item">{"".join(lines)}</div>')
        if idx < len(items) - 1:
            block_parts.append('<hr class="item-divider">')

    st.markdown(f'<div class="case-text-block">{"".join(block_parts)}</div>', unsafe_allow_html=True)


def render_case_detail():
    case_name = st.session_state.get("selected_case")
    case = CASE_LIBRARY.get(case_name)

    st.markdown('<div class="main-title">사례 상세 학습</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtle">증상 분포, 근력/반사, 신경전도검사/침근전도검사 패턴을 연결해 해석하는 단계입니다.</div>',
        unsafe_allow_html=True
    )

    if not case:
        st.warning("사례를 찾을 수 없습니다.")
        render_bottom_navigation()
        return

    patient = case.get("patient", {})
    findings = case.get("findings", {})
    teaching = case.get("teaching_diagnosis", {})
    diff_dx = case.get("differential_diagnosis", [])
    side = patient.get("side", "-")

    badges = _summarize_case_badges(case)
    badge_html = "".join([f'<span class="badge {cls}">{label}</span>' for cls, label in badges])

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="case-title-mobile">📘 {case_name}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="badge-row">{badge_html}</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="case-subtitle-mobile"><span class="label-strong text-blue">연령:</span> <span class="result-value">{patient.get("age","-")}세</span> | <span class="label-strong text-blue">성별:</span> <span class="result-value">{patient.get("sex","-")}</span> | <span class="label-strong text-blue">병변측:</span> <span class="result-value">{patient.get("side","-")}</span></div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="warn-card">
        <div class="finding-highlight" style="color: #b45309; border-bottom-color: #fde68a; border-bottom-width:1px;">학생용 사고 프레임</div>
        <div class="case-bullet-strong">• 증상이 피부분절 분포인지, 말초신경 분포인지 먼저 구분합니다.</div>
        <div class="case-bullet-strong">• 감각신경전도가 보존되는지 감소하는지에 따라 신경뿌리병증과 말초신경병변 가능성이 달라집니다.</div>
        <div class="case-bullet-strong">• 어떤 근육들이 함께 침범되는지 보면 공통 분절 또는 공통 신경을 추론할 수 있습니다.</div>
        <div class="case-bullet-strong">• 반사 변화와 기능적 보행/손기능 저하를 함께 연결해 해석합니다.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="case-section-label">🗣️ 주요 증상</div>', unsafe_allow_html=True)
    symptoms_html = "".join([f'<div class="case-bullet">• {s}</div>' for s in patient.get("symptoms", [])])
    st.markdown(f'<div class="case-text-block">{symptoms_html}</div>', unsafe_allow_html=True)

    st.markdown('<div class="case-section-label">🧪 이학적 검사결과</div>', unsafe_allow_html=True)
    exam_html = []
    for sec_name, items in patient.get("physical_exam", {}).items():
        exam_html.append(f'<div class="finding-highlight" style="font-size:1.0rem;">{sec_name}</div>')
        for i in items:
            parts = i.split(":", 1)
            if len(parts) == 2:
                exam_html.append(f'<div class="case-bullet"><span class="label-strong">{parts[0]}:</span> <span class="result-value">{parts[1]}</span></div>')
            else:
                exam_html.append(f'<div class="case-bullet">• {i}</div>')
    st.markdown(f'<div class="case-text-block">{"".join(exam_html)}</div>', unsafe_allow_html=True)

    grouped = split_findings_by_domain(findings, ANATOMY)

    if grouped["sensory"]:
        _render_finding_block("⚡ 감각신경전도검사 소견", grouped["sensory"], side)
    if grouped["motor"]:
        _render_finding_block("⚡ 운동신경전도검사 소견", grouped["motor"], side)
    if grouped["muscle"]:
        _render_finding_block("🪡 침근전도검사 소견", grouped["muscle"], side)
    if grouped["reflex"] or grouped["other"]:
        merged = {}
        merged.update(grouped["reflex"])
        merged.update(grouped["other"])
        _render_finding_block("🔁 반사/후기반응 소견", merged, side)

    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.markdown('<div class="result-title">✅ 교육용 진단 요약</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="result-text"><span class="label-strong text-blue">요약:</span> <span class="result-value">{teaching.get("summary","")}</span></div>', unsafe_allow_html=True)

    if teaching.get("ncs_reason"):
        st.markdown('<div class="result-label">신경전도 해석 포인트</div>', unsafe_allow_html=True)
        for x in teaching["ncs_reason"]:
            st.markdown(f'<div class="result-text">• {x}</div>', unsafe_allow_html=True)

    if teaching.get("emg_reason"):
        st.markdown('<div class="result-label">침근전도 해석 포인트</div>', unsafe_allow_html=True)
        for x in teaching["emg_reason"]:
            st.markdown(f'<div class="result-text">• {x}</div>', unsafe_allow_html=True)

    if teaching.get("integration"):
        st.markdown('<div class="result-label">통합 해석</div>', unsafe_allow_html=True)
        for x in teaching["integration"]:
            st.markdown(f'<div class="result-text">• {x}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    if diff_dx:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="case-section-label">🧭 감별진단 포인트</div>', unsafe_allow_html=True)
        for idx, d in enumerate(diff_dx):
            st.markdown(f'<div class="finding-highlight">{d.get("name","")}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="case-bullet"><span class="label-strong text-blue">왜 고려하나:</span> <span class="result-value">{d.get("why_consider","")}</span></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="case-bullet"><span class="label-strong text-blue">어떻게 구분하나:</span> <span class="result-value">{d.get("how_to_differentiate","")}</span></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="case-bullet"><span class="label-strong text-green">실전 팁:</span> <span class="result-value">{d.get("practical_tip","")}</span></div>', unsafe_allow_html=True)
            if idx < len(diff_dx) - 1:
                st.markdown('<hr class="item-divider">', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    report_text = build_case_report_text(case_name, case)
    st.download_button(
        "📄 사례 요약 텍스트 다운로드",
        report_text,
        file_name=f"{case_name}_교육용요약.txt",
        mime="text/plain",
        use_container_width=True
    )

    render_bottom_navigation()
