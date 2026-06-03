# ui/home.py

import streamlit as st

def format_title_box(kor, eng):
    return f"<div class='title-box'><div class='title-kor'>{kor}</div><div class='title-eng'>{eng.lower()}</div></div>"

def render_home():
    st.markdown('<div class="main-title-kor">교육용 근전도 판독 보조 앱</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-title-eng">educational emg reading assistant app</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtle">모바일 환경 우선으로 최적화된 물리치료학과 학생 및 고급 교육용 근전도(EMG) / 신경전도(NCS) 학습 앱입니다.</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown(format_title_box("학습 안내", "learning guide"), unsafe_allow_html=True)
    
    st.markdown('<div class="case-bullet"><span style="font-weight:800;">• 사례 학습 모드:</span> 임상 증상, 이학적 검사, 전기진단 소견을 통합하여 병변 위치를 입체적으로 추론합니다.</div>', unsafe_allow_html=True)
    st.markdown('<div class="case-bullet"><span style="font-weight:800;">• 가상 결과표 판독학습:</span> 정교하게 구축된 수치 데이터를 기반으로 결과표 해석 논리를 다각도로 훈련합니다.</div>', unsafe_allow_html=True)
    
    # 영어 아래로 배치
    edu_points = [
        "신경뿌리<br><span class='title-eng' style='display:inline;'>nerve root</span>",
        "신경얼기<br><span class='title-eng' style='display:inline;'>plexus</span>",
        "말초신경<br><span class='title-eng' style='display:inline;'>peripheral nerve</span>",
        "다발신경병증<br><span class='title-eng' style='display:inline;'>polyneuropathy</span>",
        "반사경로<br><span class='title-eng' style='display:inline;'>reflex pathway</span>"
    ]
    points_html = "<div style='margin-top:6px; margin-bottom:6px;'>".join([f"<div style='margin-left:14px;'>- {p}</div>" for p in edu_points])
    st.markdown(f'<div class="case-bullet"><span style="font-weight:800;">• 고급 교육 포인트:</span><div style="margin-top:4px;">{points_html}</div></div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="warn-card">
        <div style="font-weight:800; color:#dc2626; font-size:0.9rem;">⚠️ 본 앱은 교육용 시뮬레이터이며 실제 의학적 임상 진단을 대체할 수 없습니다.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown(format_title_box("진행할 학습 모드 선택", "select learning mode"), unsafe_allow_html=True)

    # 🚨 상수를 직접 딕셔너리에 넣어 import 에러 원천 차단
    display_modes = {
        "case": "사례 학습 모드",
        "direct": "가상 결과표 판독학습"
    }

    selected_display = st.radio(
        "모드 선택",
        options=list(display_modes.values()),
        label_visibility="collapsed",
        key="home_mode_selector"
    )

    mode = [k for k, v in display_modes.items() if v == selected_display][0]

    if mode == "case":
        st.markdown(f"""
        <div class="info-card">
            <div style="font-weight:800; color:#2563eb; margin-bottom:2px;">사례 학습 모드</div>
            <div class="title-eng" style="margin-bottom:8px;">case study</div>
            <div class="case-bullet">10가지 다채로운 증례별 임상 증상 분포, 이학적 검사, 신경전도검사(NCS) 및 침근전도검사(needle EMG)의 구체 소견과 감별진단 포인트를 통합적으로 분석하여 판독 논리를 정립합니다.</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="info-card">
            <div style="font-weight:800; color:#2563eb; margin-bottom:2px;">가상 결과표 판독학습</div>
            <div class="title-eng" style="margin-bottom:8px;">report analysis</div>
            <div class="case-bullet">실제 임상 계측 수치 기반 가상 결과표를 통해 신경뿌리병증(radiculopathy), 단일신경병증(mononeuropathy), 신경얼기병증(plexopathy), 다발신경병증(polyneuropathy)을 원스톱으로 비교 진단합니다.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="center-btn-wrapper" style="margin-top: 24px; margin-bottom: 8px;">', unsafe_allow_html=True)
    if st.button("🚀 학습 시작", type="primary"):
        st.session_state["mode"] = mode
        if mode == "case":
            st.session_state["screen"] = "case_list"
        else:
            st.session_state["screen"] = "input_learning"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
