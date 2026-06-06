# ui/home.py

import streamlit as st

from data.constants import MODE_CASE, MODE_DIRECT


def render_home():
    st.markdown('<div class="main-title">교육용 근전도 판독 보조 앱</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtle">모바일 환경 우선으로 최적화된 물리치료학과 학생 및 고급 교육용 EMG/NCS 학습 앱입니다.</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="big-section-title">📖 학습 안내</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="case-bullet"><span class="label-strong text-blue">• 사례 학습 모드:</span> 임상 증상, 이학적 검사, 전기진단 소견을 통합하여 병변 위치를 입체적으로 추론합니다.</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="case-bullet"><span class="label-strong text-blue">• 가상 결과표 판독학습:</span> 수치 기반 결과표를 통해 NCS/Needle EMG/특수검사 해석 논리를 훈련합니다.</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="case-bullet"><span class="label-strong text-blue">• 고급 교육 포인트:</span> 신경뿌리, 신경얼기, 말초신경, 다발신경병증, 반사경로에서의 병변 위치 추론을 학습합니다.</div>',
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="warn-card">
            <div class="case-bullet-strong text-red">
                ⚠️ 본 앱은 교육용 시뮬레이터이며 실제 의학적 임상 진단을 대체할 수 없습니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">📋 진행할 학습 모드 선택</div>', unsafe_allow_html=True)

    display_modes = {
        MODE_CASE: "사례 학습 모드",
        MODE_DIRECT: "가상 결과표 판독학습",
    }

    current_mode = st.session_state.get("mode", MODE_CASE)
    default_index = 0 if current_mode == MODE_CASE else 1

    selected_display = st.radio(
        "모드 선택",
        options=list(display_modes.values()),
        index=default_index,
        label_visibility="collapsed",
        key="home_mode_selector",
    )

    mode = [key for key, value in display_modes.items() if value == selected_display][0]

    if mode == MODE_CASE:
        st.markdown(
            """
            <div class="info-card" style="margin-top: 12px;">
                <div class="case-bullet-strong text-blue">사례 학습 모드 (Case Study)</div>
                <div class="case-bullet">
                    임상 증상, 이학적 검사, 신경전도검사 및 침근전도검사 소견을 통합하여 판독 논리를 정립합니다.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="info-card" style="margin-top: 12px;">
                <div class="case-bullet-strong text-blue">가상 결과표 판독학습 (Report Analysis)</div>
                <div class="case-bullet">
                    가상 결과표의 수치와 판정값을 바탕으로 신경뿌리병증, 단일신경병증, 신경얼기병증, 다발신경병증을 비교 학습합니다.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown('<div style="text-align: center; margin-top: 24px; margin-bottom: 8px;">', unsafe_allow_html=True)

    if st.button("🚀 학습 시작", type="primary", use_container_width=True, key="home_start_button"):
        st.session_state["mode"] = mode
        st.session_state["screen"] = "case_list" if mode == MODE_CASE else "input_learning"
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
