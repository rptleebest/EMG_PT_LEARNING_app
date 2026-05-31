# ui/home.py

import streamlit as st
from data.constants import MODE_CASE, MODE_DIRECT


def render_home():
    st.markdown('<div class="main-title">교육용 근전도 판독 보조 앱</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtle">모바일 환경 우선으로 최적화된 물리치료학과 학생 및 고급 교육용 EMG/NCS 학습 앱입니다.</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="warn-card">', unsafe_allow_html=True)
    st.markdown("### 📌 학습 안내")
    st.markdown('<div class="case-bullet">• 사례 학습: 증상, 이학적 검사, 전기진단 소견을 통합하여 병변 위치를 추론합니다.</div>', unsafe_allow_html=True)
    st.markdown('<div class="case-bullet">• 입력 학습: 사용자가 직접 검사 이상 소견을 선택해 패턴을 비교 학습합니다.</div>', unsafe_allow_html=True)
    st.markdown('<div class="case-bullet">• 고급 교육 포인트: 신경뿌리, 신경얼기, 말초신경, 다발신경병증, 반사경로를 비교 학습합니다.</div>', unsafe_allow_html=True)
    st.markdown('<div class="case-bullet">• 본 앱은 교육용이며 실제 임상 진단을 대체하지 않습니다.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 진행할 학습 모드 선택")

    mode = st.radio(
        "모드 선택",
        [MODE_CASE, MODE_DIRECT],
        label_visibility="collapsed"
    )

    if mode == MODE_CASE:
        st.markdown("""
        <div class="section-hint">
        <b>사례 학습</b><br>
        사례별 증상 분포, 이학적 검사, 신경전도/침근전도 소견, 감별진단 포인트를 통합적으로 학습합니다.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="section-hint">
        <b>검사 정보 입력 학습</b><br>
        사용자가 직접 이상 소견을 선택해 root lesion, mononeuropathy, plexopathy, polyneuropathy 패턴을 추론해봅니다.
        </div>
        """, unsafe_allow_html=True)

    if st.button("학습 시작", type="primary", use_container_width=True):
        st.session_state["mode"] = mode
        if mode == MODE_CASE:
            st.session_state["screen"] = "case_list"
        else:
            st.session_state["screen"] = "input_learning"
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)