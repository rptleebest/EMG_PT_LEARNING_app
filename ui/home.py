# ui/home.py

import streamlit as st
from data.constants import MODE_CASE, MODE_DIRECT

def render_home() -> None:
    """
    앱의 첫 진입 화면을 렌더링합니다.
    불필요한 박스를 없애고, 텍스트와 구분선을 활용하여 깔끔하게 구성했습니다.
    """
    st.markdown(
        '<div class="main-title" style="color:#1e3a8a; font-size:1.6rem; text-align:center;">근전도 판독 보조 및 학습 앱</div>', 
        unsafe_allow_html=True
    )
    
    st.markdown(
        '<div class="subtle" style="text-align:center; font-size:1rem; color:#475569;">'
        '물리치료학과 학생을 위한 근전도 결과 해석 학습 및 임상 물리치료사들의 판독 보조를 위한 앱입니다.'
        '</div>',
        unsafe_allow_html=True,
    )
    
    st.markdown('<hr style="border-top: 1px solid #cbd5e1; margin-bottom: 24px;">', unsafe_allow_html=True)

    st.markdown('<div class="item-title" style="font-size:1.1rem;">📚 학습 모드 안내</div>', unsafe_allow_html=True)
    
    st.markdown(
        '<div style="margin-bottom: 12px;"><span class="inline-label">1. 사례 학습 모드:</span>'
        '<span class="inline-content">환자의 주관적 증상, 이학적 검사 결과, 전기진단 소견을 통합하여 임상적 추론(Clinical Reasoning) 과정을 훈련합니다.</span></div>',
        unsafe_allow_html=True,
    )
    
    st.markdown(
        '<div style="margin-bottom: 24px;"><span class="inline-label">2. 가상 검사결과표 해석 모드:</span>'
        '<span class="inline-content">실제 임상과 유사한 수치 기반의 양측 비교 NCS/EMG 결과표를 직접 분석하고, 병변의 위치를 스스로 판별하는 능력을 기릅니다.</span></div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">진행할 학습 모드 선택</div>', unsafe_allow_html=True)

    display_modes = {MODE_CASE: "사례 학습 모드", MODE_DIRECT: "가상 검사결과표 해석 모드"}
    current_mode = st.session_state.get("mode", MODE_CASE)
    
    selected_display = st.radio(
        "모드 선택",
        options=list(display_modes.values()),
        index=0 if current_mode == MODE_CASE else 1,
        label_visibility="collapsed",
    )

    mode = [k for k, v in display_modes.items() if v == selected_display][0]

    st.markdown('<div style="height: 16px;"></div>', unsafe_allow_html=True)
    
    if st.button("🚀 선택한 모드로 학습 시작하기", type="primary"):
        st.session_state["mode"] = mode
        st.session_state["screen"] = "case_list" if mode == MODE_CASE else "input_learning"
        st.rerun()
        
    st.markdown("</div>", unsafe_allow_html=True)
