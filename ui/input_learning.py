# ui/input_learning.py

import html
import streamlit as st
from ui.navigation import render_bottom_navigation
from data.report_terms import REPORT_LANG_KO, REPORT_LANG_EN, LANGUAGE_OPTIONS, normalize_report_language, translate_term
from data.virtual_reports import VIRTUAL_REPORTS, get_report_section_name

def get_input_learning_report_language() -> str:
    """언어 모드 선택용 라디오 버튼을 렌더링합니다."""
    selected = st.radio(
        "언어 모드", 
        options=LANGUAGE_OPTIONS, 
        index=0, 
        horizontal=True, 
        label_visibility="collapsed", 
        key="v_lang"
    )
    return normalize_report_language(selected)

def get_result_color_style(value: str) -> str:
    """결과에 따른 폰트 색상을 반환합니다."""
    text = str(value)
    abnormal_words = ["비정상", "감소", "지연", "소실", "탈신경", "측정불가", "차단", "Abnormal", "Reduced", "Absent", "Delayed", "Incomplete", "Active"]
    normal_words = ["정상", "Normal", "Silent"]
    
    if any(w in text for w in abnormal_words): 
        return "color: #991b1b; font-weight: 800;"
    if any(w in text for w in normal_words): 
        return "color: #15803d; font-weight: 800;"
    return ""

def create_responsive_table(headers: list, rows: list, table_id: str) -> str:
    """PC/모바일에 최적화된 반응형 테이블을 렌더링합니다."""
    if not rows: 
        return ""
        
    safe_id = html.escape(str(table_id))
    
    css = f"""
    <style>
        #{safe_id} {{ width: 100%; border-collapse: collapse; margin-bottom: 16px; font-size: 0.9rem; }} 
        #{safe_id} th {{ background-color: #f8fafc; padding: 10px; border-bottom: 2px solid #cbd5e1; text-align: left; color: #1e293b; font-weight: 800; }} 
        #{safe_id} td {{ padding: 10px; border-bottom: 1px solid #e2e8f0; text-align: left; color: #334155; }} 
        #{safe_id} td.fst-col {{ font-weight: 800; color: #1e3a8a; }} 
        
        @media screen and (max-width: 768px) {{ 
            #{safe_id} thead {{ display: none; }} 
            #{safe_id} tr {{ display: block; border: 1px solid #e2e8f0; border-radius: 8px; margin-bottom: 12px; background: #ffffff; padding: 8px; }} 
            #{safe_id} td {{ display: flex; justify-content: space-between; align-items: center; gap: 12px; border-bottom: 1px dashed #e2e8f0; padding: 10px 8px; text-align: right; }} 
            #{safe_id} td:last-child {{ border-bottom: none; }} 
            #{safe_id} td::before {{ content: attr(data-label); font-weight: 800; color: #475569; text-align: left; font-size: 0.85rem; flex: 0 0 38%; }} 
            #{safe_id} td > span {{ flex: 1; text-align: right; word-break: keep-all; font-weight: 400; }} 
            #{safe_id} td.fst-col {{ justify-content: center; background: #f1f5f9; border-radius: 6px 6px 0 0; text-align: center; padding: 12px; }} 
            #{safe_id} td.fst-col::before {{ content: none; }} 
            #{safe_id} td.fst-col > span {{ text-align: center; font-weight: 800; color: #1e3a8a; }} 
        }}
    </style>
    """
    
    header_html = "".join([f"<th>{html.escape(h)}</th>" for h in headers])
    
    tr_html = ""
    for row in rows:
        td_html = ""
        for idx, col in enumerate(row):
            cls = "fst-col" if idx == 0 else ""
            color_style = get_result_color_style(str(col)) if idx == len(row)-1 else ""
            h_lbl = html.escape(headers[idx]) if idx < len(headers) else ""
            td_html += f"<td data-label='{h_lbl}' class='{cls}' style='{color_style}'><span>{html.escape(str(col))}</span></td>"
        tr_html += f"<tr>{td_html}</tr>"
        
    return f"{css}<table id='{safe_id}'><thead><tr>{header_html}</tr></thead><tbody>{tr_html}</tbody></table>"


def render_input_learning():
    """메인 화면 및 가상결과표 선택 메뉴 렌더링"""
    st.markdown('<div class="main-title">가상 검사결과표 해석 모드</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtle">실제 임상과 동일한 양측 비교 데이터를 통해 병변 위치를 스스로 추론합니다.</div>', unsafe_allow_html=True)
    
    st.markdown('<hr style="border-top: 1px dotted #cbd5e1; margin-bottom: 20px;">', unsafe_allow_html=True)

    if "v_reset_counter" not in st.session_state: 
        st.session_state["v_reset_counter"] = 0
        
    case_names = ["선택 안 함"] + list(VIRTUAL_REPORTS.keys())
    
    st.markdown('<div class="item-title">📋 학습할 가상 검사결과표 선택</div>', unsafe_allow_html=True)
    selected = st.radio(
        "리스트", 
        case_names, 
        index=0, 
        key=f"v_rad_{st.session_state['v_reset_counter']}", 
        label_visibility="collapsed"
    )

    if selected != "선택 안 함":
        render_virtual_report_inline(selected)

    render_bottom_navigation()


def render_virtual_report_inline(case_name: str):
    """선택된 가상 검사결과표 렌더링"""
    data = VIRTUAL_REPORTS[case_name]

    st.markdown('<hr style="margin: 1.5rem 0; border-top: 2px dashed #cbd5e1;">', unsafe_allow_html=True)
    
    # ==========================================
    # 1. 환자 기본 정보
    # ==========================================
    info = data.get("info", {})
    st.markdown('<div class="section-label">환자 기본 정보</div>', unsafe_allow_html=True)
    st.markdown(f'<div><span class="inline-label">연령/성별:</span><span class="inline-content">{info.get("age")}세 / {info.get("sex")}</span></div>', unsafe_allow_html=True)
    st.markdown(f'<div><span class="inline-label">병변 호소측:</span><span class="inline-content">{info.get("side")}</span></div>', unsafe_allow_html=True)
    st.markdown(f'<div style="margin-top:8px;"><span class="inline-label">주요 증상:</span><span class="inline-content">{info.get("symptom")}</span></div>', unsafe_allow_html=True)
    
    st.markdown('<hr style="margin: 1.5rem 0; border-top: 1px solid #cbd5e1;">', unsafe_allow_html=True)

    # ==========================================
    # ⚙️ 표 직전에 언어 모드 선택 배치
    # ==========================================
    st.markdown(
        '<div style="font-weight:800; color:#0f172a; margin-bottom:12px; font-size:1.05rem;">'
        '⚙️ 검사결과표 언어 모드 변경'
        '</div>', 
        unsafe_allow_html=True
    )
    selected_language = get_input_learning_report_language()
    
    lang = normalize_report_language(selected_language)
    is_eng = lang == REPORT_LANG_EN

    # ==========================================
    # 2. 결과표 렌더링 (양측 비교 데이터)
    # ==========================================
    sen_hdrs = ["Nerve", "Side", "Amplitude", "Latency", "Interpretation"] if is_eng else ["검사 신경", "측정측", "진폭", "잠복기", "판독"]
    mot_hdrs = ["Nerve", "Stim Site", "Side", "Amplitude", "Latency", "Interpretation"] if is_eng else ["검사 신경", "자극 위치", "측정측", "진폭", "잠복기", "판독"]
    emg_hdrs = ["Muscle", "Segment", "Side", "Rest", "Volition", "Interpretation"] if is_eng else ["검사 근육", "분절", "측정측", "휴식 시", "수의수축", "판독"]

    def _tr(mat): 
        return [[translate_term(c, lang) for c in row] for row in mat] if is_eng else mat

    st.markdown('<div class="section-label" style="margin-top:24px;">⚡ 전기진단검사 결과표 (양측 비교)</div>', unsafe_allow_html=True)
    
    st.markdown(f'<div class="item-title">{get_report_section_name("sensory", lang)}</div>', unsafe_allow_html=True)
    st.markdown(create_responsive_table(sen_hdrs, _tr(data.get("ncs_sensory", [])), "v_sen"), unsafe_allow_html=True)
    
    st.markdown(f'<div class="item-title">{get_report_section_name("motor", lang)}</div>', unsafe_allow_html=True)
    st.markdown(create_responsive_table(mot_hdrs, _tr(data.get("ncs_motor", [])), "v_mot"), unsafe_allow_html=True)

    # 침근전도 직전 용어 가이드
    st.markdown("""
    <div style="background:#f8fafc; padding:12px; border-left:4px solid #94a3b8; margin-top:20px; margin-bottom:12px; border-radius:4px;">
        <div style="font-weight:800; color:#334155; font-size:0.95rem; margin-bottom:6px;">💡 학생용 침근전도 용어 가이드</div>
        <div style="font-size:0.9rem; line-height:1.5; margin-bottom:4px;"><span style="color:#b91c1c; font-weight:800;">활동성 탈신경 (Active Denervation):</span> 현재 신경 손상이 <b>활발히 진행 중</b>인 상태 (자발전위 관찰)</div>
        <div style="font-size:0.9rem; line-height:1.5; margin-bottom:4px;"><span style="color:#c2410c; font-weight:800;">만성 재신경지배 (Chronic Reinnervation):</span> 신경 손상 후 회복을 시도하는 <b>만성기</b> (거대운동단위 관찰)</div>
        <div style="font-size:0.9rem; line-height:1.5;"><span style="color:#0f766e; font-weight:800;">동원 감소 (Reduced Recruitment):</span> 신경 손상으로 인해 부분 탈신경으로 근력 저하 또는 완전 탈신경으로 <b>마비된 상태</b></div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f'<div class="item-title">{get_report_section_name("emg", lang)}</div>', unsafe_allow_html=True)
    st.markdown(create_responsive_table(emg_hdrs, _tr(data.get("emg", [])), "v_emg"), unsafe_allow_html=True)


    # ==========================================
    # 3. 통합 임상 추론 및 해석
    # ==========================================
    teaching = data.get("teaching_diagnosis", {})
    
    st.markdown('<hr style="margin: 1.5rem 0; border-top: 1px dotted #cbd5e1;">', unsafe_allow_html=True)
    st.markdown('<div class="section-label" style="color:#1e3a8a;">임상 추론 및 통합 해석</div>', unsafe_allow_html=True)
    
    if "ncs_reason" in teaching:
        st.markdown('<div class="inline-label" style="display:block; margin-top:12px; margin-bottom:6px; color:#16a34a;">1. 신경전도검사(NCS) 수치 해석</div>', unsafe_allow_html=True)
        for r in teaching["ncs_reason"]: 
            st.markdown(f'<div class="inline-content" style="margin-bottom:6px;">{r}</div>', unsafe_allow_html=True)
            
    if "emg_reason" in teaching:
        st.markdown('<div class="inline-label" style="display:block; margin-top:16px; margin-bottom:6px; color:#16a34a;">2. 침근전도검사(EMG) 소견 해석</div>', unsafe_allow_html=True)
        for r in teaching["emg_reason"]: 
            st.markdown(f'<div class="inline-content" style="margin-bottom:6px;">{r}</div>', unsafe_allow_html=True)

    if "integration" in teaching:
        st.markdown('<div class="inline-label" style="display:block; margin-top:16px; margin-bottom:6px; color:#1e3a8a;">3. 통합 결론 도출</div>', unsafe_allow_html=True)
        for r in teaching["integration"]: 
            st.markdown(f'<div class="inline-content" style="margin-bottom:12px;">{r}</div>', unsafe_allow_html=True)
            
    st.markdown(
        f'<div style="background:#fff1f2; padding:12px; margin-top:12px; border-radius:6px; border:1px solid #fecdd3;">'
        f'<span class="inline-label" style="color:#991b1b; font-size:1.05rem;">임상적 추정 진단 (Impression):</span><br>'
        f'<span class="inline-content" style="font-weight:800; color:#991b1b; font-size:1.05rem;">R/O {teaching.get("summary")}</span>'
        f'</div>', 
        unsafe_allow_html=True
    )

    # ==========================================
    # 4. 감별 진단 (설명 통합)
    # ==========================================
    if "differential_diagnosis" in data:
        st.markdown('<div class="section-label" style="color:#7e22ce; margin-top:24px;">유사 질환과의 감별 진단</div>', unsafe_allow_html=True)
        
        for ddx in data["differential_diagnosis"]:
            st.markdown(f"""
            <div class="ddx-box">
                <div class="ddx-title">R/O {ddx.get('name')}</div>
                <div class="ddx-content" style="line-height:1.6;">
                    증상이 유사하여 혼동될 수 있으나, 본 데이터의 소견과 비교할 때 {ddx.get('how_to_differentiate')}
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ==========================================
    # 5. 위로 가기 버튼
    # ==========================================
    st.markdown('<div style="height: 24px;"></div>', unsafe_allow_html=True)
    
    if st.button("👆 다른 검사결과표 선택하기 (초기화 및 위로 이동)", type="primary"):
        st.session_state["v_reset_counter"] += 1
        st.rerun()

def app(): 
    pass
