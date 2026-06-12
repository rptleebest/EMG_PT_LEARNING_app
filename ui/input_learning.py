# ui/input_learning.py

import html
import re
import streamlit as st
from ui.navigation import render_bottom_navigation
from data.report_terms import REPORT_LANG_KO, REPORT_LANG_EN, LANGUAGE_OPTIONS, normalize_report_language, translate_term
from data.virtual_reports import VIRTUAL_REPORTS, get_report_section_name, custom_english_translate

def get_input_learning_report_language() -> str:
    selected = st.radio("언어 모드", options=LANGUAGE_OPTIONS, index=0, horizontal=True, label_visibility="collapsed", key="v_lang")
    return normalize_report_language(selected)

def get_result_color_style(value: str) -> str:
    text = str(value)
    abnormal_words = ["비정상", "감소", "지연", "소실", "탈신경", "측정불가", "차단", "항진", "초과", "증가", "Abnormal", "Reduced", "Absent", "Delayed", "Incomplete", "Active", "drop", "block"]
    normal_words = ["정상", "Normal", "Silent", "WNL", "침묵", "동원"]
    if any(w in text for w in abnormal_words): return "color: #991b1b; font-weight: 800;"
    if any(w in text for w in normal_words): return "color: #15803d; font-weight: 800;"
    return ""

def _format_reason_text(text: str) -> str:
    text = str(text).strip()
    if re.match(r"^(\d+\))", text) or text.endswith(":"):
        return f'<div style="color:#1e40af; font-weight:700; margin-top:14px; margin-bottom:6px;">{html.escape(text)}</div>'
    return f'<div style="color:#334155; margin-bottom:8px; line-height:1.6; padding-left:14px; text-indent:-14px;">• {html.escape(text)}</div>'

def custom_korean_translate(text: str) -> str:
    raw = str(text)
    code_str = raw.lower().strip()
    
    code_mapping = {
        "ncs_normal": "정상 범위", 
        "ncs_delayed": "잠복기 지연", 
        "ncs_reduced": "진폭 감소", 
        "ncs_absent": "반응 소실", 
        "ncs_conduction_block": "진폭 급감",
        "emg_normal": "정상 범위", 
        "emg_active_denervation": "활동성 탈신경", 
        "emg_paraspinal_denervation": "활동성 탈신경", 
        "emg_chronic_reinnervation": "만성 재신경지배", 
        "emg_active_chronic": "활동성+만성", 
        "blink_delayed": "잠복기 지연", 
        "blink_absent": "반응 소실",
        "blink_delayed_absent": "지연 및 소실",
        "fwave_delayed_absent": "지연 및 소실",
        "h_reflex_hyperactive": "진폭 과항진",
        "h_m_ratio_increased": "비율 증가"
    }
    if code_str in code_mapping:
        return code_mapping[code_str]

    replace_map = {
        "Silent": "전기적 침묵",
        "Normal recruitment": "정상 동원",
        "Reduced recruitment": "동원 감소",
        "No recruitment": "동원 불가",
        "Fibrillation/PSW": "섬유자발전위/양성예파",
        "Absent": "반응 소실",
        "Incomplete due to pain": "통증으로 평가 불가"
    }
    for eng, kor in replace_map.items():
        if eng in raw:
            raw = raw.replace(eng, kor)
            
    return raw

def create_responsive_table(headers: list, rows: list) -> str:
    if not rows: return ""
    css = """<style>
    table { width: 100%; border-collapse: collapse; margin-bottom: 12px; font-size: 0.95rem; }
    
    /* PC 환경: 헤더와 셀의 기본은 가운데 정렬, 첫번째/마지막(판독) 열은 좌측 정렬 */
    th { background-color: #f8fafc; padding: 12px 10px; border-bottom: 2px solid #cbd5e1; text-align: center !important; color: #1e293b; font-weight: 800; }
    th:first-child { text-align: left !important; padding-left: 16px; }
    th:last-child { text-align: left !important; padding-left: 16px; }
    td { padding: 10px; border-bottom: 1px solid #e2e8f0; text-align: center !important; color: #334155; }
    td.fst-col { font-weight: 800; color: #1e3a8a; text-align: left !important; padding-left: 16px; }
    td:last-child { text-align: left !important; padding-left: 16px; line-height: 1.4; }
    
    /* 모바일 환경: 좌측 정렬 및 들여쓰기 적용 */
    @media screen and (max-width: 768px) {
        thead { display: none; }
        tr { display: block; border: 1px solid #cbd5e1; border-radius: 8px; margin-bottom: 16px; background: #ffffff; overflow: hidden; }
        td { display: flex; align-items: flex-start; gap: 12px; border-bottom: 1px dashed #e2e8f0; padding: 10px 12px 10px 24px; text-align: left !important; }
        td:last-child { border-bottom: none; }
        td::before { content: attr(data-label); font-weight: 800; color: #64748b; text-align: left !important; font-size: 0.85rem; flex: 0 0 38%; margin-top: 2px; }
        td > span { flex: 1; text-align: left !important; word-break: keep-all; font-weight: 400; color: #334155; line-height: 1.4; }
        td.fst-col { display: flex; flex-direction: row; justify-content: flex-start; background: #f1f5f9; text-align: left !important; padding: 12px 16px; border-bottom: 2px solid #cbd5e1; }
        td.fst-col::before { content: attr(data-label) ": "; color: #1e3a8a; font-weight: 800; flex: unset; margin-right: 8px; font-size: 0.95rem; margin-top: 0; text-align: left !important;}
        td.fst-col > span { text-align: left !important; font-weight: 800; color: #1e3a8a; font-size: 0.95rem; }
    }
    </style>"""
    
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
    
    info = data.get("info", {})
    st.markdown('<div class="section-label">👤 환자 기본 정보</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="info-row"><div class="info-label">연령/성별</div><div class="info-value">{info.get("age")}세 / {info.get("sex")}</div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="info-row"><div class="info-label">병변 호소측</div><div class="info-value">{info.get("side")}</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="info-row" style="border:none;"><div class="info-label">주요 증상</div><div class="info-value"></div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="left-border-box">• {info.get("symptom")}</div>', unsafe_allow_html=True)
    
    st.markdown('<hr style="border-top: 1px dashed #cbd5e1; margin: 1.5rem 0;">', unsafe_allow_html=True)

    st.markdown('<div style="font-weight:800; color:#0f172a; margin-bottom:12px; font-size:1.05rem;">⚙️ 검사결과표 언어 모드 변경</div>', unsafe_allow_html=True)
    selected_language = get_input_learning_report_language()
    
    lang = normalize_report_language(selected_language)
    is_eng = lang == REPORT_LANG_EN

    sen_hdrs = ["Nerve", "Side", "Amplitude", "Latency", "Interpretation"] if is_eng else ["검사 신경", "측정측", "진폭", "잠복기", "판독"]
    mot_hdrs = ["Nerve", "Stim Site", "Side", "Amplitude", "Latency", "Interpretation"] if is_eng else ["검사 신경", "자극 위치", "측정측", "진폭", "잠복기", "판독"]
    emg_hdrs = ["Muscle", "Segment", "Side", "Rest", "Volition", "Interpretation"] if is_eng else ["검사 근육", "분절", "측정측", "휴식 시", "수의수축", "판독"]
    spec_hdrs = ["Test", "Condition", "Result", "Interpretation"] if is_eng else ["검사 항목", "조건/측정측", "결과", "상세 수치 및 판독"]

    def _tr(mat): 
        if is_eng:
            return [[custom_english_translate(str(c)) for c in row] for row in mat]
        else:
            return [[custom_korean_translate(str(c)) for c in row] for row in mat]

    teaching = data.get("teaching_diagnosis", {})

    if data.get("ncs_sensory"):
        st.markdown(f'<div class="section-label" style="margin-top:32px;">⚡ {get_report_section_name("sensory", lang)}</div>', unsafe_allow_html=True)
        st.markdown(create_responsive_table(sen_hdrs, _tr(data.get("ncs_sensory", []))), unsafe_allow_html=True)

    if data.get("ncs_motor"):
        st.markdown(f'<div class="section-label" style="margin-top:32px;">⚡ {get_report_section_name("motor", lang)}</div>', unsafe_allow_html=True)
        st.markdown(create_responsive_table(mot_hdrs, _tr(data.get("ncs_motor", []))), unsafe_allow_html=True)

    if (data.get("ncs_sensory") or data.get("ncs_motor")) and "ncs_reason" in teaching:
        with st.expander("🔍 신경전도검사 결과 해석"):
            for r in teaching["ncs_reason"]:
                st.markdown(_format_reason_text(r), unsafe_allow_html=True)

    if data.get("special"):
        spec_title = "Special & Late Responses" if is_eng else "특수 및 후기반응 검사"
        st.markdown(f'<div class="section-label" style="margin-top:32px;">⚡ {spec_title}</div>', unsafe_allow_html=True)
        st.markdown(create_responsive_table(spec_hdrs, _tr(data.get("special", []))), unsafe_allow_html=True)
        if "emg_reason" in teaching and not data.get("emg"):
            with st.expander("🔍 특수 검사 소견 해석"):
                for r in teaching["emg_reason"]: 
                    st.markdown(_format_reason_text(r), unsafe_allow_html=True)

    if data.get("emg"):
        st.markdown(f'<div class="section-label" style="margin-top:32px;">🪡 {get_report_section_name("emg", lang)}</div>', unsafe_allow_html=True)
        st.markdown(create_responsive_table(emg_hdrs, _tr(data.get("emg", []))), unsafe_allow_html=True)
        if "emg_reason" in teaching:
            with st.expander("🔍 침근전도검사 결과 해석"):
                st.markdown("""
                <div style="background:#f1f5f9; padding:12px; margin-bottom:12px; border-radius:4px; border-left:4px solid #cbd5e1;">
                    <div style="font-size:0.95rem; margin-bottom:6px;"><span style="color:#1e3a8a; font-weight:800;">• 활동성 탈신경 (Active Denervation):</span> 현재 신경 손상이 활발히 진행 중인 상태 (자발전위 관찰)</div>
                    <div style="font-size:0.95rem; margin-bottom:6px;"><span style="color:#1e3a8a; font-weight:800;">• 만성 재신경지배 (Chronic Reinnervation):</span> 신경 손상 후 회복을 시도하는 만성기 (거대운동단위 관찰)</div>
                    <div style="font-size:0.95rem;"><span style="color:#1e3a8a; font-weight:800;">• 수의수축 시 동원 감소 또는 소실 (Reduced Recruitment or Absent):</span> 신경 손상으로 인해 부분 탈신경으로 근력 저하 또는 완전 탈신경으로 완전 마비된 상태</div>
                    <div style="font-size:0.95rem;"><span style="color:#1e3a8a; font-weight:800;">• 휴식 시 관찰되는 비정상적인 자발전위 (Rest):</span> 섬유자발전위(fibrillation), 양성예파(positive sharp wave, PSW)</div>
                    <div style="font-size:0.95rem;"><span style="color:#1e3a8a; font-weight:800;">• 휴식 시 정상적인 반응 (Rest):</span> 전기적 침묵(Silent)</div>                    
                </div>
                """, unsafe_allow_html=True)
                for r in teaching["emg_reason"]: 
                    st.markdown(_format_reason_text(r), unsafe_allow_html=True)

    st.markdown('<hr style="border-top: 2px dashed #cbd5e1; margin: 2.5rem 0 1.5rem 0;">', unsafe_allow_html=True)
    
    is_stroke_case = "뇌졸중" in case_name

    section_title = "✅ 임상적 통합 해석" if is_stroke_case else "✅ 임상적 통합 해석 및 감별진단"
    st.markdown(f'<div class="section-label">{section_title}</div>', unsafe_allow_html=True)
    
    if "integration" in teaching:
        st.markdown('<div class="sub-title">🔹 검사 결과 통합 결론</div>', unsafe_allow_html=True)
        st.markdown('<div class="left-border-box" style="border-left-color:#3b82f6;">', unsafe_allow_html=True)
        for r in teaching["integration"]: 
            st.markdown(f'<div style="margin-bottom:8px;">• {r}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
            
    box_label = "경직(spasticity) 평가 : " if is_stroke_case else "임상적 추정진단 (R/O) : "
    st.markdown(
        f'<div style="background:#fdf2f8; border:1px solid #fbcfe8; padding:12px 16px; border-radius:8px; margin-top:16px;">'
        f'<span style="font-size:1.05rem; color:#9d174d; font-weight:700;">{box_label}</span>'
        f'<span style="font-size:1.05rem; color:#9d174d; font-weight:800;">{teaching.get("summary")}</span>'
        f'</div>', unsafe_allow_html=True
    )

    if "differential_diagnosis" in data:
        st.markdown('<div class="sub-title" style="margin-top:24px;">🧭 유사 질환과의 감별진단</div>', unsafe_allow_html=True)
        for ddx in data["differential_diagnosis"]:
            st.markdown(f"""
            <div class="ddx-box">
                <div style="font-size:1.05rem; font-weight:800; color:#4f46e5; margin-bottom:8px;">{ddx.get('name')}</div>
                <div style="color:#475569; line-height:1.6;">
                    {ddx.get('how_to_differentiate')}
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div style="height: 32px;"></div>', unsafe_allow_html=True)
    if st.button("👆 다른 검사결과표 선택하기", type="primary"):
        st.session_state["v_reset_counter"] += 1
        st.rerun()

def app(): pass
