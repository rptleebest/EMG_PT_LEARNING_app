# ui/case_learning.py

import streamlit as st
from data.cases import CASE_LIBRARY
from ui.navigation import render_bottom_navigation

def render_case_list():
    st.markdown('<div class="main-title">사례 학습 모드</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtle">환자의 임상 증상과 근전도 병변측 소견을 분석하여 병변 부위를 추론합니다.</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">📚 가상 사례 선택</div>', unsafe_allow_html=True)

    # 1. 필터 삭제 및 라디오 버튼 즉시 노출
    case_names = list(CASE_LIBRARY.keys())
    selected = st.radio("학습할 임상 증상 선택", case_names, label_visibility="collapsed")

    if selected:
        case = CASE_LIBRARY[selected]
        patient = case["patient"]
        
        st.markdown('<div class="info-card" style="margin-top:15px;">', unsafe_allow_html=True)
        st.markdown(f'<div class="case-title-mobile">👤 {selected}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="case-subtitle-mobile"><span class="label-strong text-blue">연령/성별:</span> <span class="result-value">{patient["age"]}세 / {patient["sex"]}</span> | <span class="label-strong text-blue">병변측:</span> <span class="result-value">{patient["side"]}</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        if st.button("📚 선택한 사례 상세 학습 시작", type="primary", use_container_width=True):
            st.session_state["selected_case"] = selected
            st.session_state["screen"] = "case_detail"
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
    render_bottom_navigation()

def render_case_detail():
    case_name = st.session_state.get("selected_case")
    case = CASE_LIBRARY.get(case_name)
    if not case: return

    patient = case["patient"]
    side = patient["side"]

    st.markdown(f'<div class="main-title">📘 {case_name}</div>', unsafe_allow_html=True)
    
    # 5. 학생용 사고 프레임에 % 수치 기준 명확화
    st.markdown("""
    <div class="warn-card">
        <div class="finding-highlight" style="color: #b45309; border-bottom-color: #fde68a;">🎓 학생용 사고 프레임 (판독 기준)</div>
        <div class="case-bullet-strong">1. 진폭(Amplitude) 감소: 정상치 대비 <b>50% 이하</b>로 급감 시 '축삭 손상(Axonal loss)'을 의미합니다.</div>
        <div class="case-bullet-strong">2. 잠복기(Latency) 지연: 정상치 대비 <b>130% 이상</b> 길어질 때 국소 포착 또는 '말이집탈락성(Demyelinating)' 병변을 시사합니다.</div>
        <div class="case-bullet-strong">3. 감각신경 보존: 통증/저림이 심한데 감각신경이 정상이라면 병변은 '신경뿌리(Root)' 위치입니다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 이학적 검사 렌더링
    st.markdown('<div class="case-section-label">🗣️ 임상 및 이학적 검사결과</div>', unsafe_allow_html=True)
    exam_html = ""
    for k, v in patient["physical_exam"].items():
        exam_html += f'<div class="label-strong" style="margin-top:8px;">{k}</div>'
        for item in v: exam_html += f'<div class="case-bullet">• {item}</div>'
    st.markdown(f'<div class="case-text-block">{exam_html}</div>', unsafe_allow_html=True)

    # 2 & 3. 병변측 전용 블록 렌더링 함수
    def render_ncs_sensory(data, title):
        if not data: return
        st.markdown(f'<div class="case-section-label">{title} (병변측: {side})</div>', unsafe_allow_html=True)
        for nerve, result in data.items():
            st.markdown(f'<div class="finding-highlight" style="font-size:1rem;">⚡ {nerve}</div>', unsafe_allow_html=True)
            amp_color = "text-red" if "감소" in result["진폭"] or "침묵" in result["진폭"] else "text-blue"
            lat_color = "text-red" if "지연" in result["잠복기"] or "무반응" in result["잠복기"] else "text-blue"
            st.markdown(f'<div class="finding-subtext">1) 진폭: <span class="{amp_color}">{result["진폭"]}</span></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="finding-subtext">2) 잠복기: <span class="{lat_color}">{result["잠복기"]}</span></div>', unsafe_allow_html=True)
            st.markdown('<hr class="item-divider">', unsafe_allow_html=True)

    def render_ncs_motor(data, title):
        if not data: return
        st.markdown(f'<div class="case-section-label">{title} (병변측: {side})</div>', unsafe_allow_html=True)
        for nerve, result in data.items():
            st.markdown(f'<div class="finding-highlight" style="font-size:1rem;">⚡ {nerve}</div>', unsafe_allow_html=True)
            
            d_amp_col = "text-red" if "감소" in result["원위부 진폭"] or "침묵" in result["원위부 진폭"] else "text-blue"
            d_lat_col = "text-red" if "지연" in result["원위부 잠복기"] or "무반응" in result["원위부 잠복기"] else "text-blue"
            p_amp_col = "text-red" if "감소" in result["근위부 진폭"] or "침묵" in result["근위부 진폭"] else "text-blue"
            p_lat_col = "text-red" if "지연" in result["근위부 잠복기"] or "무반응" in result["근위부 잠복기"] else "text-blue"
            
            st.markdown(f'<div class="finding-subtext"><b>[원위부 자극]</b> 진폭: <span class="{d_amp_col}">{result["원위부 진폭"]}</span> | 잠복기: <span class="{d_lat_col}">{result["원위부 잠복기"]}</span></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="finding-subtext"><b>[근위부 자극]</b> 진폭: <span class="{p_amp_col}">{result["근위부 진폭"]}</span> | 잠복기: <span class="{p_lat_col}">{result["근위부 잠복기"]}</span></div>', unsafe_allow_html=True)
            st.markdown('<hr class="item-divider">', unsafe_allow_html=True)

    def render_emg(data, title):
        if not data: return
        st.markdown(f'<div class="case-section-label">{title} (병변측: {side})</div>', unsafe_allow_html=True)
        for muscle, result in data.items():
            st.markdown(f'<div class="finding-highlight" style="font-size:1rem;">🪡 {muscle}</div>', unsafe_allow_html=True)
            rest_col = "text-red" if "출현" in result["휴식 시"] else "text-blue"
            vol_col = "text-red" if "감소" in result["근수축 시"] or "무반응" in result["근수축 시"] or "거대" in result["근수축 시"] or "불가" in result["근수축 시"] else "text-blue"
            st.markdown(f'<div class="finding-subtext">1) 휴식 시 반응: <span class="{rest_col}">{result["휴식 시"]}</span></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="finding-subtext">2) 근수축 시 반응: <span class="{vol_col}">{result["근수축 시"]}</span></div>', unsafe_allow_html=True)
            st.markdown('<hr class="item-divider">', unsafe_allow_html=True)

    render_ncs_sensory(case.get("ncs_sensory"), "감각신경전도검사 소견")
    render_ncs_motor(case.get("ncs_motor"), "운동신경전도검사 소견")
    render_emg(case.get("emg"), "침근전도검사 소견")

    # 결과 및 해석 렌더링
    td = case["teaching_diagnosis"]
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.markdown('<div class="result-title">✅ 근전도 결과 세부 해석</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="result-text"><span class="label-strong text-red">최종 요약:</span> <b>{td["summary"]}</b></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="result-label">신경전도 해석 포인트</div>', unsafe_allow_html=True)
    for r in td["ncs_reason"]: st.markdown(f'<div class="result-text">• {r}</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="result-label">침근전도 해석 포인트</div>', unsafe_allow_html=True)
    for r in td["emg_reason"]: st.markdown(f'<div class="result-text">• {r}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 감별진단
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">🧭 감별진단 포인트</div>', unsafe_allow_html=True)
    for d in case["differential_diagnosis"]:
        st.markdown(f'<div class="finding-highlight">{d["name"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="case-bullet"><span class="label-strong text-blue">왜 고려하나:</span> {d["why_consider"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="case-bullet"><span class="label-strong text-blue">어떻게 구분하나:</span> {d["how_to_differentiate"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="case-bullet"><span class="label-strong text-green">실전 팁:</span> {d["practical_tip"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    render_bottom_navigation()
