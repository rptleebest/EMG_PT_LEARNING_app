# ui/home.py

import streamlit as st
from data.constants import MODE_CASE, MODE_DIRECT


def render_home():
    st.markdown('<div class="main-title">교육용 근전도 판독 보조 앱</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtle" style="font-size:0.84rem; line-height:1.45; word-break:keep-all;">'
        '모바일 환경 우선으로 최적화된 물리치료학과 학생 및 고급 교육용 EMG/NCS 학습 앱입니다.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="warn-card" style="padding: 10px 8px; margin-bottom: 12px;">', unsafe_allow_html=True)
    st.markdown("### 📌 학습 안내", style="font-size: 0.95rem; margin-bottom: 6px;")
    st.markdown('<div class="case-bullet" style="font-size:0.82rem; margin-bottom:4px;">• <b>사례 학습 모드</b>: 임상 증상, 이학적 검사, 전기진단 소견을 통합하여 병변 위치를 입체적으로 추론합니다.</div>', unsafe_allow_html=True)
    st.markdown('<div class="case-bullet" style="font-size:0.82rem; margin-bottom:4px;">• <b>가상 결과표 판독학습</b>: 정교하게 구축된 수치 데이터를 기반으로 결과표 해석 논리를 다각도로 훈련합니다.</div>', unsafe_allow_html=True)
    st.markdown('<div class="case-bullet" style="font-size:0.82rem; margin-bottom:4px;">• <b>고급 교육 포인트</b>: 신경뿌리(Nerve root), 신경얼기(Plexus), 말초신경(Peripheral nerve), 다발신경병증(Polyneuropathy), 반사경로(Reflex pathway)를 완벽하게 비교 학습합니다.</div>', unsafe_allow_html=True)
    st.markdown('<div class="case-bullet" style="font-size:0.82rem; color: #dc2626; font-weight:700;">• 본 앱은 교육용 시뮬레이터이며 실제 의학적 임상 진단을 대체할 수 없습니다.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-card" style="padding: 10px 8px;">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label" style="font-size:0.92rem; margin-bottom: 8px;">📋 진행할 학습 모드 선택</div>', unsafe_allow_html=True)

    # 상수 데이터 결합 방지를 위한 화면 표시 매핑 매트릭스 설계
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

    # 역방향 바인딩을 통해 내부 상수 상태 매핑 무결성 유지
    mode = [k for k, v in display_modes.items() if v == selected_display][0]

    if mode == MODE_CASE:
        st.markdown("""
        <div class="section-hint" style="padding: 8px; margin-top: 8px; margin-bottom: 12px; font-size:0.82rem; line-height:1.45;">
        <b>사례 학습 모드 (Case Study)</b><br>
        10가지 다채로운 증례별 임상 증상 분포, 이학적 검사, 신경전도검사(NCS) 및 침근전도검사(Needle EMG)의 구체 소견과 감별진단 포인트를 통합적으로 분석하여 판독 논리를 정립합니다.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="section-hint" style="padding: 8px; margin-top: 8px; margin-bottom: 12px; font-size:0.82rem; line-height:1.45;">
        <b>가상 결과표 판독학습 (Report Analysis)</b><br>
        실제 임상 계측 수치 기반 가상 결과표를 통해 목(Cervical)/허리(Lumbar) 신경뿌리병증(Radiculopathy), 단일신경병증(Mononeuropathy), 신경얼기병증(Plexopathy), 다발신경병증(Polyneuropathy)을 원스톱으로 비교 진단합니다.
        </div>
        """, unsafe_allow_html=True)

    if st.button("🚀 학습 시작", type="primary", use_container_width=True):
        st.session_state["mode"] = mode
        if mode == MODE_CASE:
            st.session_state["screen"] = "case_list"
        else:
            st.session_state["screen"] = "input_learning"
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
