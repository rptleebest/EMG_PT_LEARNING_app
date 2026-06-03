# ui/home.py

import streamlit as st

def format_title_box(kor, eng):
    return f"<div class='title-box'><div class='title-kor'>{kor}</div><div class='title-eng'>{eng.lower()}</div></div>"

def render_home():
    st.markdown('<div style="margin-bottom:20px;"><div style="font-size:1.3rem; font-weight:800; color:#0f172a; line-height:1.2;">교육용 근전도 판독 보조 앱</div><div style="font-size:0.85rem; color:#64748b; margin-top:2px;">educational emg reading assistant app</div></div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.9rem; color:#334155; margin-bottom:20px;">모바일 환경 우선으로 최적화된 물리치료학과 학생 및 고급 교육용 근전도(emg) / 신경전도(ncs) 학습 앱입니다.</div>', unsafe_allow_html=True)

    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown(format_title_box("학습 안내", "learning guide"), unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.9rem; margin-bottom:8px;"><span style="font-weight:700; color:#1e293b;">• 사례 학습 모드:</span> 임상 증상, 이학적 검사, 전기진단 소견을 통합하여 병변 위치 추론</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.9rem; margin-bottom:8px;"><span style="font-weight:700; color:#1e293b;">• 가상 결과표 판독:</span> 수치 데이터를 기반으로 결과표 해석 논리 훈련</div>', unsafe_allow_html=True)
    
    st.markdown('<div style="font-size:0.9rem; font-weight:700; color:#1e293b; margin-top:12px;">• 고급 교육 포인트:</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.85rem; color:#475569; margin-left:14px; line-height:1.6;">- 신경뿌리(nerve root)<br>- 신경얼기(plexus)<br>- 말초신경(peripheral nerve)<br>- 다발신경병증(polyneuropathy)<br>- 반사경로(reflex pathway)</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div style="background:#fff1f2; border:1px solid #fecdd3; padding:12px; border-radius:6px; margin-bottom:16px; font-size:0.85rem; font-weight:600; color:#b91c1c;">⚠️ 본 앱은 교육용 시뮬레이터이며 실제 의학적 임상 진단을 대체할 수 없습니다.</div>', unsafe_allow_html=True)

    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown(format_title_box("진행할 학습 모드 선택", "select learning mode"), unsafe_allow_html=True)

    mode_options = {"case": "사례 학습 모드", "direct": "가상 결과표 판독학습"}
    selected = st.radio("모드 선택", options=list(mode_options.values()), label_visibility="collapsed", key="home_mode")
    mode = [k for k, v in mode_options.items() if v == selected][0]

    if mode == "case":
        st.markdown("""
        <div class="info-card">
            <div style="font-weight:700; color:#0f172a; margin-bottom:4px;">사례 학습 모드 (case study)</div>
            <div style="font-size:0.85rem; color:#475569;">10가지 다채로운 증례별 임상 증상, 이학적 검사, 신경전도/침근전도 소견과 감별진단 포인트를 통합적으로 분석하여 판독 논리를 정립합니다.</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="info-card">
            <div style="font-weight:700; color:#0f172a; margin-bottom:4px;">가상 결과표 판독학습 (report analysis)</div>
            <div style="font-size:0.85rem; color:#475569;">실제 임상 계측 수치 기반 가상 결과표를 통해 신경뿌리, 단일신경, 다발신경병증 등을 원스톱으로 비교 진단합니다.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="center-btn" style="margin-top: 24px;">', unsafe_allow_html=True)
    if st.button("학습 시작", type="primary"):
        st.session_state["mode"] = mode
        st.session_state["screen"] = "case_list" if mode == "case" else "input_learning"
        st.rerun()
    st.markdown('</div></div>', unsafe_allow_html=True)
