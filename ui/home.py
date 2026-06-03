# ui/home.py

import streamlit as st

def format_title_box(kor):
    return f"<div class='title-box'><div class='title-kor'>{kor}</div></div>"

def render_home():
    st.markdown('<div style="margin-bottom:20px;"><div style="font-size:1.25rem; font-weight:800; color:#0f172a; line-height:1.2;">교육용 근전도 판독 보조 앱</div></div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.9rem; color:#334155; margin-bottom:20px; word-break:keep-all;">물리치료학과 학생 및 고급 교육용 근전도(EMG) 및 신경전도(NCS) 학습 앱입니다.</div>', unsafe_allow_html=True)

    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown(format_title_box("학습 안내"), unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.9rem; margin-bottom:6px;"><span style="font-weight:700; color:#1e293b;">• 사례 학습 모드:</span> 임상 증상, 이학적 검사, 전기진단 소견을 통합하여 병변 위치 추론</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.9rem; margin-bottom:6px;"><span style="font-weight:700; color:#1e293b;">• 가상 결과표 판독:</span> 수치 데이터를 기반으로 결과표 해석 논리 훈련</div>', unsafe_allow_html=True)
    
    st.markdown('<div style="font-size:0.9rem; font-weight:700; color:#1e293b; margin-top:12px;">• 고급 교육 포인트:</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.85rem; color:#475569; margin-left:14px; line-height:1.6;">- 신경뿌리(nerve root)<br>- 신경얼기(plexus)<br>- 말초신경(peripheral nerve)<br>- 다발신경병증(polyneuropathy)<br>- 반사경로(reflex pathway)</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div style="background:#fff1f2; border:1px solid #fecdd3; padding:12px; border-radius:6px; margin-bottom:16px; font-size:0.85rem; font-weight:600; color:#b91c1c;">⚠️ 본 앱은 교육용 시뮬레이터이며 실제 의학적 임상 진단을 대체할 수 없습니다.</div>', unsafe_allow_html=True)

    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown(format_title_box("진행할 학습 모드 선택"), unsafe_allow_html=True)

    mode_options = {"case": "사례 학습 모드", "direct": "가상 결과표 판독학습"}
    selected = st.radio("모드 선택", options=list(mode_options.values()), label_visibility="collapsed", key="home_mode")
    mode = [k for k, v in mode_options.items() if v == selected][0]

    if mode == "case":
        st.markdown("""
        <div style="background:#f0f9ff; border:1px solid #bae6fd; padding:12px; border-radius:6px; margin-top:10px;">
            <div style="font-weight:700; color:#1e3a8a; margin-bottom:4px;">사례 학습 모드</div>
            <div style="font-size:0.85rem; color:#334155; word-break:keep-all;">다채로운 증례별 임상 증상, 이학적 검사, 신경전도/침근전도 소견을 통합적으로 분석하여 판독 논리를 정립합니다.</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="background:#f0f9ff; border:1px solid #bae6fd; padding:12px; border-radius:6px; margin-top:10px;">
            <div style="font-weight:700; color:#1e3a8a; margin-bottom:4px;">가상 결과표 판독학습</div>
            <div style="font-size:0.85rem; color:#334155; word-break:keep-all;">실제 임상 계측 수치 기반 가상 결과표를 통해 신경뿌리, 말초신경, 다발신경병증 등을 원스톱으로 비교 진단합니다.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div style="text-align:center; margin-top: 24px;">', unsafe_allow_html=True)
    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        if st.button("학습 시작", type="primary", use_container_width=True):
            st.session_state["mode"] = mode
            st.session_state["screen"] = "case_list" if mode == "case" else "input_learning"
            st.rerun()
    st.markdown('</div></div>', unsafe_allow_html=True)
