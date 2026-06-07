# ui/input_learning.py

import html
import streamlit as st
from ui.navigation import render_bottom_navigation
from data.report_terms import REPORT_LANG_KO, REPORT_LANG_EN, LANGUAGE_OPTIONS, normalize_report_language, translate_term
from data.virtual_reports import VIRTUAL_REPORTS, get_report_section_name, custom_english_translate

def get_input_learning_report_language() -> str:
    selected = st.radio("언어 모드", options=LANGUAGE_OPTIONS, index=0, horizontal=True, label_visibility="collapsed", key="v_lang")
    return normalize_report_language(selected)

def get_result_color_style(value: str) -> str:
    text = str(value)
    abnormal_words = ["비정상", "감소", "지연", "소실", "탈신경", "측정불가", "차단", "Abnormal", "Reduced", "Absent", "Delayed", "Incomplete", "Active", "drop", "block"]
    normal_words = ["정상", "Normal", "Silent", "WNL"]
    if any(w in text for w in abnormal_words): return "color: #991b1b; font-weight: 700;"
    if any(w in text for w in normal_words): return "color: #15803d; font-weight: 700;"
    return ""

def create_responsive_table(headers: list, rows: list) -> str:
    if not rows: return ""
    css = """<style>table { width: 100%; border-collapse: collapse; margin-bottom: 8px; font-size: 0.9rem; } th { background-color: #f8fafc; padding: 10px; border-bottom: 2px solid #cbd5e1; text-align: left; color: #1e293b; font-weight: 700; } td { padding: 10px; border-bottom: 1px solid #e2e8f0; text-align: left; color: #334155; } td.fst-col { font-weight: 700; color: #1e3a8a; } @media screen and (max-width: 768px) { thead { display: none; } tr { display: block; border: 1px solid #e2e8f0; border-radius: 8px; margin-bottom: 12px; background: #ffffff; padding: 8px; } td { display: flex; justify-content: space-between; align-items: center; gap: 12px; border-bottom: 1px dashed #e2e8f0; padding: 10px 8px; text-align: right; } td:last-child { border-bottom: none; } td::before { content: attr(data-label); font-weight: 700; color: #475569; text-align: left; font-size: 0.85rem; flex: 0 0 38%; } td > span { flex: 1; text-align: right; word-break: keep-all; font-weight: 400; } td.fst-col { justify-content: center; background: #f1f5f9; border-radius: 6px 6px 0 0; text-align: center; padding: 12px; } td.fst-col::before { content: none; } td.fst-col > span { text-align: center; font-weight: 700; color: #1e3a8a; } }</style>"""
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
    return f"{css}<table><thead><tr>{header_html}</tr></thead><tbody>{tr_html}</tbody></table>"

def render_input_learning():
    st.markdown('<div class="main-title">가상 검사결과표 해석 모드</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-desc">실제 임상과 동일한 양측 비교 데이터를 통해 병변 위치를 스스로 추론합니다.</div>', unsafe_allow_html=True)
    st.markdown('<hr style="border-top: 1px dotted #cbd5e1; margin-bottom: 20px;">', unsafe_allow_html=True)

    if "v_reset_counter" not in st.session_state: st.session_state["v_reset_counter"] = 0
    case_names = ["선택 안 함"] + list(VIRTUAL_REPORTS.keys())
    
    st.markdown('<div class="sub-title">📋 학습할 가상 검사결과표 선택</div>', unsafe_allow_html=True)
    selected = st.radio("리스트", case_names, index=0, key=f"v_rad_{st.session_state['v_reset_counter']}", label_visibility="collapsed")

    if selected != "선택 안 함":
        render_virtual_report_inline(selected)
    render_bottom_navigation()

def render_virtual_report_inline(case_name: str):
    data = VIRTUAL_REPORTS[case_name]

    st.markdown('<hr style="border-top: 2px solid #94a3b8; margin: 2rem 0;">', unsafe_allow_html=True)
    
    # 1. 환자 정보 (- 기호 -> • 기호)
    info = data.get("info", {})
    st.markdown('<div class="section-label">👤 환자 기본 정보</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="info-row"><div class="info-label">연령/성별</div><div class="info-value">{info.get("age")}세 / {info.get("sex")}</div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="info-row"><div class="info-label">병변 호소측</div><div class="info-value">{info.get("side")}</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="info-row" style="border:none;"><div class="info-label">주요 증상</div><div class="info-value"></div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="left-border-box">• {info.get("symptom")}</div>', unsafe_allow_html=True)
    
    st.markdown('<hr style="border-top: 1px dashed #cbd5e1; margin: 1.5rem 0;">', unsafe_allow_html=True)

    # ⚙️ 언어 모드 변경
    st.markdown(
        '<div style="font-weight:700; color:#0f172a; margin-bottom:12px; font-size:1.05rem;">⚙️ 검사결과표 언어 모드 변경</div>', 
        unsafe_allow_html=True
    )
    selected_language = get_input_learning_report_language()
    
    lang = normalize_report_language(selected_language)
    is_eng = lang == REPORT_LANG_EN

    sen_hdrs = ["Nerve", "Side", "Amplitude", "Latency", "Interpretation"] if is_eng else ["검사 신경", "측정측", "진폭", "잠복기", "판독"]
    mot_hdrs = ["Nerve", "Stim Site", "Side", "Amplitude", "Latency", "Interpretation"] if is_eng else ["검사 신경", "자극 위치", "측정측", "진폭", "잠복기", "판독"]
    emg_hdrs = ["Muscle", "Segment", "Side", "Rest", "Volition", "Interpretation"] if is_eng else ["검사 근육", "분절", "측정측", "휴식 시", "수의수축", "판독"]

    def _tr(mat): 
        return [[custom_english_translate(str(c)) for c in row] for row in mat] if is_eng else mat

    teaching = data.get("teaching_diagnosis", {})

    # [감각신경]
    if data.get("ncs_sensory"):
        st.markdown(f'<div class="section-label" style="margin-top:32px;">⚡ {get_report_section_name("sensory", lang)}</div>', unsafe_allow_html=True)
        st.markdown(create_responsive_table(sen_hdrs, _tr(data.get("ncs_sensory", []))), unsafe_allow_html=True)
        if "ncs_reason" in teaching:
            with st.expander("🔍 감각신경전도 결과 해석"):
                st.markdown(f'<div style="color:#334155; margin-bottom:8px;"><span style="color:#1e3a8a; font-weight:700; margin-right:4px;">1.</span>{teaching["ncs_reason"][0]}</div>', unsafe_allow_html=True)

    # [운동신경]
    if data.get("ncs_motor"):
        st.markdown(f'<div class="section-label" style="margin-top:32px;">⚡ {get_report_section_name("motor", lang)}</div>', unsafe_allow_html=True)
        st.markdown(create_responsive_table(mot_hdrs, _tr(data.get("ncs_motor", []))), unsafe_allow_html=True)
        if "ncs_reason" in teaching and len(teaching["ncs_reason"]) > 1:
            with st.expander("🔍 운동신경전도 결과 해석"):
                for idx, r in enumerate(teaching["ncs_reason"][1:]):
                    st.markdown(f'<div style="color:#334155; margin-bottom:8px;"><span style="color:#1e3a8a; font-weight:700; margin-right:4px;">{idx+1}.</span>{r}</div>', unsafe_allow_html=True)

    # [침근전도]
    if data.get("emg"):
        st.markdown(f'<div class="section-label" style="margin-top:32px;">🪡 {get_report_section_name("emg", lang)}</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="background:#f1f5f9; padding:12px; border-left:4px solid #94a3b8; margin-bottom:12px; border-radius:4px;">
            <div style="font-weight:700; color:#1e293b; font-size:1.05rem; margin-bottom:8px;">💡 학생용 침근전도(Needle EMG) 용어 가이드</div>
            <div style="font-size:0.95rem; margin-bottom:6px;"><span style="color:#b91c1c; font-weight:700;">활동성 탈신경 (Active Denervation):</span> 현재 신경 손상이 <b>활발히 진행 중</b>인 상태 (자발전위 관찰)</div>
            <div style="font-size:0.95rem; margin-bottom:6px;"><span style="color:#c2410c; font-weight:700;">만성 재신경지배 (Chronic Reinnervation):</span> 신경 손상 후 회복을 시도하는 <b>만성기</b> (거대운동단위 관찰)</div>
            <div style="font-size:0.95rem;"><span style="color:#0f766e; font-weight:700;">동원 감소 (Reduced Recruitment):</span> 신경 손상으로 인해 근력이 저하되거나 <b>마비된 결과적 상태</b></div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(create_responsive_table(emg_hdrs, _tr(data.get("emg", []))), unsafe_allow_html=True)
        if "emg_reason" in teaching:
            with st.expander("🔍 침근전도 결과 해석"):
                for idx, r in enumerate(teaching["emg_reason"]): 
                    st.markdown(f'<div style="color:#334155; margin-bottom:8px;"><span style="color:#1e3a8a; font-weight:700; margin-right:4px;">{idx+1}.</span>{r}</div>', unsafe_allow_html=True)

    # 4. 통합 결론
    st.markdown('<hr style="border-top: 2px dashed #cbd5e1; margin: 2.5rem 0 1.5rem 0;">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">✅ 임상적 추정진단 및 감별진단</div>', unsafe_allow_html=True)
    if "integration" in teaching:
        st.markdown('<div class="sub-title">🔹 통합 결론 도출</div>', unsafe_allow_html=True)
        st.markdown('<div class="left-border-box">', unsafe_allow_html=True)
        for r in teaching["integration"]: 
            st.markdown(f'<div style="margin-bottom:8px;">{r}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
            
    st.markdown(
        f'<div class="left-border-box success">'
        f'<span style="font-size:1.1rem; color:#15803d; font-weight:700;">임상적 추정진단(Rule out, R/O) : </span>'
        f'<span style="font-size:1.1rem; color:#166534; font-weight:700;">{teaching.get("summary")}</span>'
        f'</div>', unsafe_allow_html=True
    )

    if "differential_diagnosis" in data:
        st.markdown('<div class="sub-title" style="margin-top:24px;">🧭 유사 질환과의 감별진단</div>', unsafe_allow_html=True)
        for ddx in data["differential_diagnosis"]:
            st.markdown(f"""
            <div class="ddx-box">
                <div style="font-size:1.05rem; font-weight:700; color:#4f46e5; margin-bottom:8px;">{ddx.get('name')}</div>
                <div style="color:#334155; line-height:1.6;">
                    증상이 유사하여 혼동될 수 있으나, 본 환자의 검사결과와 비교할 때 {ddx.get('how_to_differentiate')}
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div style="height: 32px;"></div>', unsafe_allow_html=True)
    if st.button("👆 다른 검사결과표 선택하기 (초기화 및 위로 이동)", type="primary"):
        st.session_state["v_reset_counter"] += 1
        st.rerun()

def app(): pass
