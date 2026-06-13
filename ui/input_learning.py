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
    abnormal_words = ["비정상", "감소", "지연", "소실", "탈신경", "측정불가", "차단", "항진", "초과", "증가", "저하", "급감", "Abnormal", "Reduced", "Absent", "Delayed", "Incomplete", "Active", "drop", "block", "Slowed", "Hyper"]
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
        "Incomplete due to pain": "통증으로 평가 불가",
        "Giant MUAPs": "거대운동단위"
    }
    for eng, kor in replace_map.items():
        if eng in raw:
            raw = raw.replace(eng, kor)
            
    return raw

# --- [핵심 수정] PC는 깔끔한 표, 모바일은 직관적인 카드로 변신하도록 로직 정비 ---
def pivot_to_grouped_table(headers: list, rows: list, lesion_side: str, is_eng: bool) -> tuple:
    if "측정측" not in headers and "Side" not in headers:
        return headers, rows

    side_idx = headers.index("Side") if is_eng else headers.index("측정측")
    interp_idx = headers.index("Interpretation") if is_eng else headers.index("판독")

    base_headers = headers[:side_idx]
    val_headers = headers[side_idx+1:interp_idx]

    # 신경/자극위치를 기준으로 데이터 병합
    grouped = {}
    for row in rows:
        if len(row) <= interp_idx: continue
        base_key = tuple(row[:side_idx])
        side_val = str(row[side_idx]).strip()
        vals = row[side_idx+1:interp_idx]
        interp = row[interp_idx]

        if base_key not in grouped:
            grouped[base_key] = {"Rt": None, "Lt": None, "Bil": None}

        if side_val in ["오른쪽", "Rt", "우측"]:
            grouped[base_key]["Rt"] = {"vals": vals, "interp": interp}
        elif side_val in ["왼쪽", "Lt", "좌측"]:
            grouped[base_key]["Lt"] = {"vals": vals, "interp": interp}
        else:
            grouped[base_key]["Bil"] = {"vals": vals, "interp": interp}

    # 환자 병변 호소측을 기준으로 정상/병변측 타이틀 생성
    if "오른쪽" in lesion_side or "Rt" in lesion_side:
        aff_key, nor_key = "Rt", "Lt"
        aff_label = "병변측 (우)" if not is_eng else "Affected (Rt)"
        nor_label = "정상측 (좌)" if not is_eng else "Normal (Lt)"
    elif "왼쪽" in lesion_side or "Lt" in lesion_side:
        aff_key, nor_key = "Lt", "Rt"
        aff_label = "병변측 (좌)" if not is_eng else "Affected (Lt)"
        nor_label = "정상측 (우)" if not is_eng else "Normal (Rt)"
    else:
        aff_key, nor_key = "Bil", None
        aff_label = "검사 결과 (양측)" if not is_eng else "Result (Bilateral)"
        nor_label = ""

    new_headers = base_headers.copy()
    if nor_key: new_headers.append(nor_label)
    new_headers.append(aff_label)
    new_headers.append("병변측 판독" if not is_eng else "Interpretation")

    new_rows = []
    for base_key, data in grouped.items():
        new_row = list(base_key)

        def format_vals(val_list):
            if not val_list: return "-"
            out = []
            for h, v in zip(val_headers, val_list):
                if v != "-":
                    out.append(f"{h}: {v}")
            return " / ".join(out) if out else "-"

        # 정상측 수치 삽입
        if nor_key:
            nor_data = data[nor_key]
            new_row.append(format_vals(nor_data["vals"]) if nor_data else "-")

        # 병변측 수치 및 판독 삽입
        aff_data = data[aff_key] if data[aff_key] else data.get("Bil")
        if aff_data:
            new_row.append(format_vals(aff_data["vals"]))
            new_row.append(aff_data["interp"])
        else:
            if data[nor_key]: # 병변측 검사가 없고 정상측만 있는 경우
                new_row.append("-")
                new_row.append(data[nor_key]["interp"])
            else:
                new_row.append("-")
                new_row.append("-")

        new_rows.append(new_row)

    return new_headers, new_rows

def create_responsive_table(headers: list, rows: list) -> str:
    if not rows: return ""
    css = """<style>
    /* PC 환경 기본 스타일 */
    .res-table { width: 100%; border-collapse: collapse; margin-bottom: 16px; font-size: 0.92rem; }
    .res-table th { background-color: #f8fafc; padding: 12px 10px; border-bottom: 2px solid #cbd5e1; text-align: center !important; color: #1e293b; font-weight: 800; white-space: nowrap; }
    .res-table th:first-child { text-align: left !important; padding-left: 16px; }
    .res-table td { padding: 12px 10px; border-bottom: 1px solid #e2e8f0; text-align: center !important; color: #334155; vertical-align: middle; line-height: 1.5; }
    .res-table td.fst-col { font-weight: 800; color: #1e3a8a; text-align: left !important; padding-left: 16px; }
    .res-table td:last-child { text-align: left !important; padding-left: 16px; }
    
    /* 모바일 환경: 병합된 데이터를 예쁜 독립 카드 UI로 표출 */
    @media screen and (max-width: 768px) {
        .res-table, .res-table thead, .res-table tbody, .res-table th, .res-table td, .res-table tr { display: block; }
        .res-table thead { display: none; }
        
        .res-table tr { 
            margin-bottom: 1rem; 
            border: 1px solid #cbd5e1; 
            border-radius: 10px; 
            background: #ffffff; 
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            overflow: hidden;
        }
        
        .res-table td { 
            display: flex; 
            flex-direction: column; /* 라벨과 수치가 위아래로 깔끔하게 떨어지도록 설정 */
            padding: 12px 16px; 
            border-bottom: 1px dashed #e2e8f0; 
            text-align: left !important; 
        }
        .res-table td:last-child { border-bottom: none; background-color: #f8fafc; }
        
        .res-table td::before { 
            content: attr(data-label); 
            font-weight: 700; 
            color: #64748b; 
            font-size: 0.85rem; 
            margin-bottom: 4px;
        }
        .res-table td > span { font-weight: 500; word-break: keep-all; line-height: 1.4; }
        
        /* 신경 및 자극위치 열은 카드 타이틀 모양으로 강조 */
        .res-table td.fst-col, .res-table td:nth-child(2) { 
            background: #eff6ff; 
            padding: 10px 16px; 
            flex-direction: row; 
            align-items: center; 
        }
        .res-table td.fst-col { border-bottom: none; padding-bottom: 2px; }
        .res-table td:nth-child(2) { border-bottom: 2px solid #bfdbfe; padding-top: 2px; }
        .res-table td.fst-col::before, .res-table td:nth-child(2)::before { display: none; }
        .res-table td.fst-col > span { font-weight: 800; color: #1d4ed8; font-size: 1.05rem; }
        .res-table td.fst-col > span::before { content: "🔹 "; }
        .res-table td:nth-child(2) > span { font-weight: 700; color: #3b82f6; font-size: 0.95rem; margin-left: 20px;}
    }
    </style>"""
    
    header_html = "".join([f"<th>{html.escape(h)}</th>" for h in headers])
    tr_html = ""
    for row in rows:
        td_html = ""
        for idx, col in enumerate(row):
            cls = "fst-col" if idx == 0 else ""
            color_style = get_result_color_style(str(col)) if idx > 0 else ""
            h_lbl = html.escape(str(headers[idx])) if idx < len(headers) else ""
            td_html += f"<td data-label='{h_lbl}' class='{cls}' style='{color_style}'><span>{html.escape(str(col))}</span></td>"
        tr_html += f"<tr>{td_html}</tr>"
    return f"{css}<table class='res-table'><thead><tr>{header_html}</tr></thead><tbody>{tr_html}</tbody></table>"

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
    lesion_side = info.get("side", "")

    sen_hdrs = ["Nerve", "Side", "Amplitude", "Latency", "Interpretation"] if is_eng else ["검사 신경", "측정측", "진폭", "잠복기", "판독"]
    mot_hdrs = ["Nerve", "Stim Site", "Side", "Amplitude", "Latency", "NCV", "Interpretation"] if is_eng else ["검사 신경", "자극 위치", "측정측", "진폭", "잠복기", "전도속도(NCV)", "판독"]
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
        p_headers, p_rows = pivot_table_left_right(sen_hdrs, _tr(data.get("ncs_sensory", [])), lesion_side, is_eng)
        st.markdown(create_responsive_table(p_headers, p_rows), unsafe_allow_html=True)

    if data.get("ncs_motor"):
        st.markdown(f'<div class="section-label" style="margin-top:32px;">⚡ {get_report_section_name("motor", lang)}</div>', unsafe_allow_html=True)
        p_headers, p_rows = pivot_table_left_right(mot_hdrs, _tr(data.get("ncs_motor", [])), lesion_side, is_eng)
        st.markdown(create_responsive_table(p_headers, p_rows), unsafe_allow_html=True)

    if (data.get("ncs_sensory") or data.get("ncs_motor")) and "ncs_reason" in teaching:
        with st.expander("🔍 신경전도검사 결과 해석"):
            st.markdown("""
            <div style="background:#f1f5f9; padding:12px; margin-bottom:12px; border-radius:4px; border-left:4px solid #cbd5e1;">
                <div style="font-size:0.95rem; font-weight:800; color:#1e3a8a; margin-bottom:6px;">💡 [참고] 신경전도속도(NCV) 임상 정상 기준치</div>
                <div style="font-size:0.9rem; margin-bottom:4px; color:#334155;">• <b>상지(팔) 신경:</b> 일반적으로 <b>50 m/s 이상</b> 정상</div>
                <div style="font-size:0.9rem; margin-bottom:4px; color:#334155;">• <b>하지(다리) 신경:</b> 일반적으로 <b>40 m/s 이상</b> 정상</div>
                <div style="font-size:0.85rem; color:#64748b; margin-top:4px;">* 속도가 기준치 미만으로 저하된 경우, 말이집(Myelin) 손상성 지연이나 국소 포착(Entrapment)을 의심할 수 있습니다.</div>
            </div>
            """, unsafe_allow_html=True)
            for r in teaching["ncs_reason"]:
                st.markdown(_format_reason_text(r), unsafe_allow_html=True)

    if data.get("special"):
        spec_title = "Special & Late Responses" if is_eng else "특수 및 후기반응 검사"
        st.markdown(f'<div class="section-label" style="margin-top:32px;">⚡ {spec_title}</div>', unsafe_allow_html=True)
        p_headers, p_rows = pivot_table_left_right(spec_hdrs, _tr(data.get("special", [])), lesion_side, is_eng)
        st.markdown(create_responsive_table(p_headers, p_rows), unsafe_allow_html=True)
        if "emg_reason" in teaching and not data.get("emg"):
            with st.expander("🔍 특수 검사 소견 해석"):
                for r in teaching["emg_reason"]: 
                    st.markdown(_format_reason_text(r), unsafe_allow_html=True)

    if data.get("emg"):
        st.markdown(f'<div class="section-label" style="margin-top:32px;">🪡 {get_report_section_name("emg", lang)}</div>', unsafe_allow_html=True)
        p_headers, p_rows = pivot_table_left_right(emg_hdrs, _tr(data.get("emg", [])), lesion_side, is_eng)
        st.markdown(create_responsive_table(p_headers, p_rows), unsafe_allow_html=True)
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

    if "differential_diagnosis" in data and not is_stroke_case:
        st.markdown('<div class="sub-title" style="margin-top:24px;">🧭 유사 질환과의 감별진단</div>', unsafe_allow_html=True)
        for ddx in data["differential_diagnosis"]:
            name = ddx.get('name', '')
            why = ddx.get('why_consider', '')
            how = ddx.get('how_to_differentiate', '')
            tip = ddx.get('practical_tip', '')
            
            ddx_html = f"<div style='font-size:1.05rem; font-weight:800; color:#4f46e5; margin-bottom:12px;'>{name}</div>"
            if why:
                ddx_html += f"<div style='color:#475569; line-height:1.6; margin-bottom:8px;'><span style='font-weight:700; color:#334155;'>🤔 고려 이유: </span>{why}</div>"
            if how:
                ddx_html += f"<div style='color:#475569; line-height:1.6; margin-bottom:8px;'><span style='font-weight:700; color:#334155;'>🔎 감별 포인트: </span>{how}</div>"
            if tip:
                ddx_html += f"<div style='color:#ea580c; line-height:1.6; margin-top:12px; font-weight:600; background:#fff7ed; padding:8px 12px; border-radius:6px; border-left:3px solid #ea580c;'>💡 임상 꿀팁: {tip}</div>"
            
            st.markdown(f"""
            <div class="ddx-box" style="background:#f8fafc; border:1px solid #e2e8f0; padding:16px; border-radius:8px; margin-bottom:16px; border-left: 4px solid #4f46e5; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">
                {ddx_html}
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div style="height: 32px;"></div>', unsafe_allow_html=True)
    if st.button("👆 다른 검사결과표 선택하기", type="primary"):
        st.session_state["v_reset_counter"] += 1
        st.rerun()

def app(): pass
