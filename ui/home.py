# ui/home.py

import streamlit as st

def render_home():
    st.markdown('<div style="margin-bottom:24px; text-align:center;"><div style="font-size:1.3rem; font-weight:800; color:#0f172a;">교육용 근전도 판독 보조 앱</div><div style="font-size:0.9rem; color:#64748b; margin-top:4px;">물리치료학과 학생을 위한 실전 임상 판독 시뮬레이터</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">학습 가이드</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.9rem; margin-bottom:10px;"><span style="font-weight:700; color:#2563eb;">1. 사례 학습 모드:</span> 환자의 주호소와 신체 검진 결과를 바탕으로 전체적인 신경 병변의 패턴(Pattern)을 추론하는 능력을 기릅니다.</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.9rem; margin-bottom:10px;"><span style="font-weight:700; color:#2563eb;">2. 가상 결과표 판독학습:</span> 실제 임상 결과지와 유사한 수치 데이터를 분석하여 정상 범위와 대조하고 생리학적 소견을 판독하는 기술을 익힙니다.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">진행할 학습 모드 선택</div>', unsafe_allow_html=True)

    mode = st.radio("모드 선택", ["사례 학습 모드", "가상 결과표 판독학습"], label_visibility="collapsed")

    if "사례" in mode:
        st.markdown('<div class="info-card" style="margin-top:10px;"><b>진행 순서</b>: 임상 증상 파악 → 이학적 검사 확인 → 근전도 패턴 분석 → 통합 해석 및 최종 진단</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="info-card" style="margin-top:10px;"><b>진행 순서</b>: 가상 결과지 수치 판독 → 정상 범위 대조 → 생리학적 소견 정리 → 의심 추정질환 도출</div>', unsafe_allow_html=True)

    st.markdown('<div class="center-btn-container">', unsafe_allow_html=True)
    if st.button("학습 시작", type="primary"):
        st.session_state["screen"] = "case_list" if "사례" in mode else "input_learning"
        st.rerun()
    st.markdown('</div></div>', unsafe_allow_html=True)
