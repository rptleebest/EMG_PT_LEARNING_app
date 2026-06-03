# ui/home.py

import streamlit as st
from data.constants import MODE_CASE, MODE_DIRECT


def render_home():
    # 1. 상단 타이틀 및 설명 (전역 CSS 클래스 사용으로 반응형 적용)
    st.markdown('<div class="main-title">교육용 근전도 판독 보조 앱</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtle">모바일 환경 우선으로 최적화된 물리치료학과 학생 및 고급 교육용 EMG/NCS 학습 앱입니다.</div>',
        unsafe_allow_html=True
    )

    # 2. 학습 안내 섹션 (인라인 스타일 제거 및 가독성 개선)
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="big-section-title">📖 학습 안내</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="case-bullet"><span class="label-strong text-blue">• 사례 학습 모드:</span> 임상 증상, 이학적 검사, 전기진단 소견을 통합하여 병변 위치를 입체적으로 추론합니다.</div>', unsafe_allow_html=True)
    st.markdown('<div class="case-bullet"><span class="label-strong text-blue">• 가상 결과표 판독학습:</span> 정교하게 구축된 수치 데이터를 기반으로 결과표 해석 논리를 다각도로 훈련합니다.</div>', unsafe_allow_html=True)
    st.markdown('<div class="case-bullet"><span class="label-strong text-blue">• 고급 교육 포인트:</span> 신경뿌리(Nerve root), 신경얼기(Plexus), 말초신경(Peripheral nerve), 다발신경병증(Polyneuropathy), 반사경로(Reflex pathway)에서의 병변 위치를 학습합니다.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 3. 경고 문구 분리 (시각적 피로도가 적은 딥 브릭 레드 적용)
    st.markdown("""
    <div class="warn-card">
        <div class="case-bullet-strong text-red">⚠️ 본 앱은 교육용 시뮬레이터이며 실제 의학적 임상 진단을 대체할 수 없습니다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 4. 모드 선택 섹션
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">📋 진행할 학습 모드 선택</div>', unsafe_allow_html=True)

    display_modes = {
        MODE_CASE: "사례 학습 모드",
        MODE_DIRECT: "가상 결과표 판독학습"
    }

    selected_display = st.radio(
        "모드 선택",
        options=list(display_modes.values()),
        label_visibility="collapsed",
        key="home_mode_selector"
    )

    mode = [k for k, v in display_modes.items() if v == selected_display][0]

    # 선택된 모드에 따른 힌트 설명 (가독성을 위한 info-card 적용)
    if mode == MODE_CASE:
        st.markdown("""
        <div class="info-card" style="margin-top: 12px;">
            <div class="case-bullet-strong text-blue">사례 학습 모드 (Case Study)</div>
            <div class="case-bullet">10가지 다채로운 증례별 임상 증상 분포, 이학적 검사, 신경전도검사(NCS) 및 침근전도검사(Needle EMG)의 구체 소견과 감별진단 포인트를 통합적으로 분석하여 판독 논리를 정립합니다.</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="info-card" style="margin-top: 12px;">
            <div class="case-bullet-strong text-blue">가상 결과표 판독학습 (Report Analysis)</div>
            <div class="case-bullet">실제 임상 계측 수치 기반 가상 결과표를 통해 목(Cervical)/허리(Lumbar) 신경뿌리병증(Radiculopathy), 단일신경병증(Mononeuropathy), 신경얼기병증(Plexopathy), 다발신경병증(Polyneuropathy)을 원스톱으로 비교 진단합니다.</div>
        </div>
        """, unsafe_allow_html=True)

    # 5. 학습 시작 버튼 (중앙 정렬 및 여백 확보)
    st.markdown('<div style="text-align: center; margin-top: 24px; margin-bottom: 8px;">', unsafe_allow_html=True)
    
    # app.py의 CSS가 이 버튼을 최대 너비(280px)와 입체감 있는 파란색으로 자동 렌더링합니다.
    if st.button("🚀 학습 시작", type="primary", use_container_width=True):
        st.session_state["mode"] = mode
        if mode == MODE_CASE:
            st.session_state["screen"] = "case_list"
        else:
            st.session_state["screen"] = "input_learning"
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
