# ui/home.py

import streamlit as st
from data.constants import MODE_CASE, MODE_DIRECT

def format_eng_title(kor, eng):
    eng_lower = eng.lower()
    return f"{kor}<br><span class='title-eng'>{eng_lower}</span>"

def render_home():
    st.markdown('<div class="main-title">교육용 근전도 판독 보조 앱</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtle">모바일 환경 우선으로 최적화된 물리치료학과 학생 및 고급 교육용 근전도(EMG) / 신경전도(NCS) 학습 앱입니다.</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="case-section-label">{format_eng_title("학습 안내", "learning guide")}</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="case-bullet"><span class="lbl">• 사례 학습 모드:</span> 임상 증상, 이학적 검사, 전기진단 소견을 통합하여 병변 위치를 입체적으로 추론합니다.</div>', unsafe_allow_html=True)
    st.markdown('<div class="case-bullet"><span class="lbl">• 가상 결과표 판독학습:</span> 정교하게 구축된 수치 데이터를 기반으로 결과표 해석 논리를 다각도로 훈련합니다.</div>', unsafe_allow_html=True)
    
    # 콤마 나열을 브레이크로 분리하고 영어 포맷 적용
    edu_points = [
        format_eng_title("신경뿌리", "nerve root"),
        format_eng_title("신경얼기", "plexus"),
        format_eng_title("말초신경", "peripheral nerve"),
        format_eng_title("다발신경병증", "polyneuropathy"),
        format_eng_title("반사경로", "reflex pathway")
    ]
    points_html = "<br>".join([f"&nbsp;&nbsp;- {p}" for p in edu_points])
    st.markdown(f'<div class="case-bullet"><span class="lbl">• 고급 교육 포인트:</span><br>{points_html}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="warn-card">
        <div class="lbl text-red">⚠️ 본 앱은 교육용 시뮬레이터이며 실제 의학적 임상 진단을 대체할 수 없습니다.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="case-section-label">{format_eng_title("진행할 학습 모드 선택", "select learning mode")}</div>', unsafe_allow_html=True)

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

    if mode == MODE_CASE:
        st.markdown(f"""
        <div class="info-card">
            <div class="lbl text-blue" style="margin-bottom:6px;">{format_eng_title("사례 학습 모드", "case study")}</div>
            <div class="case-bullet">10가지 다채로운 증례별 임상 증상 분포, 이학적 검사, 신경전도검사(NCS) 및 침근전도검사(Needle EMG)의 구체 소견과 감별진단 포인트를 통합적으로 분석하여 판독 논리를 정립합니다.</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="info-card">
            <div class="lbl text-blue" style="margin-bottom:6px;">{format_eng_title("가상 결과표 판독학습", "report analysis")}</div>
            <div class="case-bullet">실제 임상 계측 수치 기반 가상 결과표를 통해 신경뿌리병증(radiculopathy), 단일신경병증(mononeuropathy), 신경얼기병증(plexopathy), 다발신경병증(polyneuropathy)을 원스톱으로 비교 진단합니다.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="center-btn-wrapper" style="margin-top: 20px; margin-bottom: 8px;">', unsafe_allow_html=True)
    if st.button("🚀 학습 시작", type="primary"):
        st.session_state["mode"] = mode
        if mode == MODE_CASE:
            st.session_state["screen"] = "case_list"
        else:
            st.session_state["screen"] = "input_learning"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
