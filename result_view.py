# result_view.py

import streamlit as st


def _score_to_badge(score):
    """
    모바일 친화적으로 기술 점수를 높음/중간/낮음으로 변환.
    """
    try:
        score = int(score)
    except (TypeError, ValueError):
        return "참고"

    if score >= 90:
        return "매우 높음"
    if score >= 60:
        return "높음"
    if score >= 40:
        return "중간"
    return "낮음"


def _render_list_block(items, empty_text="해당 내용이 없습니다."):
    if not items:
        st.markdown(f'<div class="result-small">{empty_text}</div>', unsafe_allow_html=True)
        return
    for item in items:
        st.markdown(f'<div class="result-text">• {item}</div>', unsafe_allow_html=True)


def render_result_view(result):
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.markdown('<div class="result-title">✅ 자동 해석 결과</div>', unsafe_allow_html=True)

    final_dx = result.get("final_dx", "")
    lesion_tags = result.get("lesion_tags", [])
    involved_nerves = result.get("involved_nerves", "")
    involved_levels = result.get("involved_levels", "")
    severity = result.get("severity", "")

    st.markdown(
        f'<div class="result-text"><b>가장 가능성이 높은 진단:</b> {final_dx or "-"}</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="result-text"><b>병변 해석 태그:</b> {", ".join(lesion_tags) if lesion_tags else "특이 태그 없음"}</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="result-text"><b>의심 신경:</b> {involved_nerves or "-"}</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="result-text"><b>의심 분절/레벨:</b> {involved_levels or "-"}</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="result-text"><b>추정 중증도:</b> {severity or "-"}</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="result-label">우선 감별해야 할 진단</div>', unsafe_allow_html=True)
    top3 = result.get("top3", [])
    if not top3:
        st.markdown('<div class="result-small">표시할 감별진단이 없습니다.</div>', unsafe_allow_html=True)
    else:
        for idx, (dx, score) in enumerate(top3, 1):
            badge = _score_to_badge(score)
            st.markdown(
                f"""
                <div class="case-text-block">
                    <div class="finding-item-title">{idx}. {dx}</div>
                    <div class="finding-subtext"><b>가능성 수준:</b> {badge}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown('<div class="result-label">감별 포인트</div>', unsafe_allow_html=True)
    top3_details = result.get("top3_details", [])
    if not top3_details:
        st.markdown('<div class="result-small">감별 포인트 정보가 없습니다.</div>', unsafe_allow_html=True)
    else:
        for idx, item in enumerate(top3_details, 1):
            name = item.get("name", "")
            why_consider = item.get("why_consider", "")
            how_to_differentiate = item.get("how_to_differentiate", "")
            practical_tip = item.get("practical_tip", "")

            st.markdown(
                f"""
                <div class="case-text-block">
                    <div class="finding-item-title">{idx}. {name}</div>
                    {f'<div class="finding-subtext"><b>고려 이유:</b> {why_consider}</div>' if why_consider else ''}
                    {f'<div class="finding-subtext"><b>감별 핵심:</b> {how_to_differentiate}</div>' if how_to_differentiate else ''}
                    {f'<div class="finding-subtext" style="color:#0f172a; font-weight:600;"><b>학습 팁:</b> {practical_tip}</div>' if practical_tip else ''}
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown('<div class="result-label">이렇게 판단한 이유</div>', unsafe_allow_html=True)
    _render_list_block(result.get("reasons", []), "판단 근거가 없습니다.")

    st.markdown('<div class="result-label">이상 소견 요약</div>', unsafe_allow_html=True)
    abnormal_items = result.get("abnormal_items", [])
    if not abnormal_items:
        st.markdown('<div class="result-small">뚜렷한 이상 소견이 없습니다.</div>', unsafe_allow_html=True)
    else:
        for item in abnormal_items:
            st.markdown(
                f"""
                <div class="case-text-block">
                    <div class="finding-item-title">{item.get("항목", "")}</div>
                    <div class="finding-subtext"><b>관련 신경:</b> {item.get("신경", "")}</div>
                    <div class="finding-subtext"><b>관련 레벨:</b> {item.get("레벨", "")}</div>
                    <div class="finding-subtext"><b>결과:</b> {item.get("결과", "")}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    suggestions = result.get("suggestions", [])
    if suggestions:
        st.markdown('<div class="result-label">추가 학습 포인트</div>', unsafe_allow_html=True)
        _render_list_block(suggestions, "추가 제안이 없습니다.")

    st.markdown(
        '<div class="result-small">※ 본 결과는 학생 교육용 참고 자료이며 실제 임상 진단을 대체하지 않습니다.</div>',
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)