# ui/case_learning.py

import html
import re
import streamlit as st
from data.cases import CASE_LIBRARY
from ui.navigation import render_bottom_navigation

def _safe_format_code(code: str) -> str:
    raw = str(code)
    code_str = raw.lower().strip()
    
    mapping = {
        "ncs_normal": "정상 범위", "ncs_delayed": "비정상 (잠복기 지연)", "ncs_reduced": "비정상 (진폭 감소)", 
        "ncs_absent": "비정상 (반응 소실)", "ncs_conduction_block": "비정상 (진폭 급감)",
        "emg_normal": "정상 범위", "emg_active_denervation": "비정상 (활동성 탈신경)", 
        "emg_paraspinal_denervation": "비정상 (활동성 탈신경)", "emg_chronic_reinnervation": "비정상 (만성 재신경지배)", 
        "emg_active_chronic": "비정상 (활동성+만성)", "blink_delayed": "비정상 (잠복기 지연)", 
        "blink_absent": "비정상 (반응 소실)", "blink_delayed_absent": "비정상 (지연 및 소실)",
        "fwave_delayed_absent": "비정상 (반응 소실)", "h_reflex_hyperactive": "비정상 (과항진)",
        "h_m_ratio_increased": "비정상 (비율 증가)"
    }
    
    if code_str in mapping: return mapping[code_str]
        
    replace_map = {
        "Silent": "전기적 침묵", "Normal recruitment": "정상 동원", "Reduced recruitment": "동원 감소",
        "Giant MUAPs": "거대운동단위", "No recruitment": "동원 불가", "Fibrillation/PSW": "섬유자발전위/양성예파",
        "Absent": "반응 소실", "Incomplete due to pain": "통증으로 평가 불가"
    }
    for eng, kor in replace_map.items():
        if eng in raw: raw = raw.replace(eng, kor)
    return raw

def _get_result_color_style(value: str, is_normal_side: bool = False) -> str:
    # 해당 줄(Row) 전체가 '정상측' 데이터인 경우 색상 강조를 완전히 배제합니다.
    if is_normal_side:
        return ""

    text = str(value)
    if any(x in text for x in ["정상측", "병변측", "Normal (", "Affected ("]):
        return ""

    abnormal_words = ["비정상", "감소", "지연", "소실", "탈신경", "재신경지배", "차단", "항진", "초과", "증가", "저하", "급감"]
    normal_words = ["정상", "Normal", "Silent", "WNL", "침묵", "동원"]
    
    # 눈이 편안하도록 채도/명도를 낮춘 벽돌색 톤(#b91c1c)과 굵기(700) 적용
    if any(w in text for w in abnormal_words): return "color: #b91c1c; font-weight: 700;"
    if any(w in text for w in normal_words): return "color: #15803d; font-weight: 700;"
    return ""

def _format_reason_text(text: str) -> str:
    text = str(text).strip()
    if re.match(r"^(\d+\))", text) or text.endswith(":"):
        return f'<div style="color:#1e40af; font-weight:700; margin-top:14px; margin-bottom:6px;">{html.escape(text)}</div>'
    return f'<div style="color:#334155; margin-bottom:8px; line-height:1.6; padding-left:14px; text-indent:-14px;">• {html.escape(text)}</div>'

def _create_responsive_table(headers: list, rows: list) -> str:
    if not rows: return ""
    css = """<style>
    /* PC 환경 기본 스타일 (깔끔한 Row-by-Row) */
    .sl-table { width: 100%; border-collapse: collapse; margin-bottom: 16px; font-size: 0.95rem; }
    .sl-table th { background-color: #f8fafc; padding: 12px 10px; border-bottom: 2px solid #cbd5e1; text-align: center !important; color: #1e293b; font-weight: 800; white-space: nowrap; }
    .sl-table th:first-child { text-align: left !important; padding-left: 16px; }
    .sl-table th:last-child { text-align: left !important; padding-left: 16px; }
    .sl-table td { padding: 10px 12px; border-bottom: 1px solid #e2e8f0; text-align: center !important; color: #334155; vertical-align: middle; }
    .sl-table td.fst-col { font-weight: 800; color: #1e3a8a; text-align: left !important; padding-left: 16px; }
    .sl-table td:last-child { text-align: left !important; padding-left: 16px; line-height: 1.4; font-weight: 600;}
    
    /* 모바일 환경: 독립된 카드 UI로 완벽 분리 및 판독 결과 강조 */
    @media screen and (max-width: 768px) {
        .sl-table, .sl-table thead, .sl-table tbody, .sl-table th, .sl-table td, .sl-table tr { display: block; }
        .sl-table thead { display: none; }
        
        .sl-table tr { 
            margin-bottom: 16px; border: 1px solid #cbd5e1; border-radius: 10px; background: #ffffff; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.05); 
        }
        .sl-table td { 
            display: flex; justify-content: space-between; align-items: center; gap: 12px; border-bottom: 1px dashed #e2e8f0; padding: 12px 16px; text-align: right !important; 
        }
        .sl-table td::before { 
            content: attr(data-label); font-weight: 700; color: #64748b; text-align: left !important; font-size: 0.85rem; flex: 0 0 40%; margin-top: 2px; 
        }
        .sl-table td > span { flex: 1; text-align: left !important; word-break: keep-all; font-weight: 500; color: #334155; line-height: 1.4; }
        
        /* 카드 제목 (검사 신경 이름) */
        .sl-table td.fst-col { 
            background: #eff6ff; padding: 14px 16px; border-bottom: 2px solid #bfdbfe; justify-content: flex-start; 
        }
        .sl-table td.fst-col::before { display: none; }
        .sl-table td.fst-col > span { text-align: left !important; font-weight: 800; color: #1d4ed8; font-size: 1.05rem; }
        .sl-table td.fst-col > span::before { content: "🔹 "; }
        
        /* 판독 결과 (맨 아래 넓게 배치) */
        .sl-table td:last-child { 
            flex-direction: column; align-items: flex-start; background-color: #f8fafc; border-bottom: none; padding-top: 14px; padding-bottom: 14px;
        }
        .sl-table td:last-child::before { 
            margin-bottom: 6px; color: #1e3a8a; font-size: 0.95rem; content: "📝 " attr(data-label); width: 100%;
        }
        .sl-table td:last-child > span { 
            text-align: left !important; width: 100%; font-size: 0.95rem; 
        }
    }
    </style>"""
    
    header_html = "".join([f"<th>{html.escape(h)}</th>" for h in headers])
    tr_html = ""
    for row in rows:
        # 해당 줄(Row)에 '정상측' 또는 영문 번역본 'Normal (' 이 포함되어 있는지 확인
        is_normal_side = any("정상측" in str(c) or "Normal (" in str(c) for c in row)
        
        td_html = ""
        for idx, col in enumerate(row):
            val = _safe_format_code(col)
            cls = "fst-col" if idx == 0 else ""
            color_style = _get_result_color_style(val, is_normal_side) if idx > 0 else ""
            header_label = html.escape(headers[idx]) if idx < len(headers) else ""
            td_html += f"<td data-label='{header_label}' class='{cls}' style='{color_style}'><span>{html.escape(val)}</span></td>"
        tr_html += f"<tr>{td_html}</tr>"
    return f"{css}<table class='sl-table'><thead><tr>{header_html}</tr></thead><tbody>{tr_html}</tbody></table>"

def render_case_list():
    st.markdown('<div class="main-title" style="text-align:left;">사례 학습 모드</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-desc" style="text-align:left;">원하는 임상 증상을 선택하면 즉시 상세 분석 결과가 아래에 표시됩니다.</div>', unsafe_allow_html=True)
    st.markdown('<hr style="border-top: 1px dotted #cbd5e1; margin-bottom: 20px;">', unsafe_allow_html=True)

    if "case_reset_counter" not in st.session_state: st.session_state["case_reset_counter"] = 0
    case_names = ["선택 안 함"] + list(CASE_LIBRARY.keys())
    
    st.markdown('<div class="sub-title">📋 학습할 임상 증상 선택</div>', unsafe_allow_html=True)
    selected = st.radio("사례 리스트", case_names, index=0, key=f"c_rad_{st.session_state['case_reset_counter']}", label_visibility="collapsed")

    if selected != "선택 안 함":
        render_case_detail_inline(selected)
    render_bottom_navigation()

def render_case_detail_inline(case_name: str):
    data = CASE_LIBRARY[case_name]
    patient = data.get("patient", {})
    findings = data.get("findings", {})
    teaching = data.get("teaching_diagnosis", {})

    st.markdown('<hr style="border-top: 2px solid #94a3b8; margin: 2rem 0;">', unsafe_allow_html=True)
    
    st.markdown('<div class="section-label">👤 환자 기본 정보</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="info-row"><div class="info-label">연령/성별</div><div class="info-value">{patient.get("age")}세 / {patient.get("sex")}</div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="info-row"><div class="info-label">병변 호소측</div><div class="info-value">{patient.get("side")}</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="info-row" style="border:none;"><div class="info-label">주요 증상</div><div class="info-value"></div></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="left-border-box">', unsafe_allow_html=True)
    for sym in patient.get("symptoms", []):
        st.markdown(f'<div style="margin-bottom:4px;">• {sym}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    phys_exam = patient.get("physical_exam", {})
    if phys_exam:
        st.markdown('<div class="section-label" style="margin-top:24px;">🩺 이학적 검사 (신경학적 진찰)</div>', unsafe_allow_html=True)
        
        st.markdown('''
        <style>
        .pe-item { margin-bottom: 6px; color: #334155; line-height: 1.5; font-weight: 500;}
        .pe-main { font-weight: 700; color: #1e293b; }
        .pe-nerve { color: #64748b; font-weight: 500; }
        .pc-dash { display: inline; }
        .mob-arrow { display: none; }
        
        @media screen and (max-width: 768px) {
            .pe-item.mmt { display: flex; flex-direction: column; margin-bottom: 10px; }
            .pc-dash { display: none; }
            .mob-arrow { display: inline; margin-left: 14px; }
            .pe-nerve { font-size: 0.9rem; margin-top: 2px; }
        }
        </style>
        ''', unsafe_allow_html=True)
        
        for cat, items in phys_exam.items():
            icon = "🖐" if "감각" in cat else "💪" if "근력" in cat else "🔨"
            st.markdown(f'<div class="exam-box"><div class="exam-title">{icon} {cat}</div>', unsafe_allow_html=True)
            for item in items:
                if " | " in item:
                    main_part, nerve_part = item.split(" | ", 1)
                    st.markdown(f'''
                    <div class="pe-item mmt">
                        <span class="pe-main">• {main_part}</span>
                        <span class="pe-nerve"><span class="pc-dash"> - 지배 신경: </span><span class="mob-arrow">↳ 지배 신경: </span>{nerve_part}</span>
                    </div>
                    ''', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="pe-item">• {item}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    sensory_rows, motor_rows, emg_rows, blink_rows = [], [], [], []
    for test_name, result_tuple in findings.items():
        if not isinstance(result_tuple, tuple): continue
        
        if len(result_tuple) == 2:
            row = [test_name, result_tuple[0], result_tuple[1], ""]
        else:
            row = [test_name] + list(result_tuple)
            
        test_name_upper = test_name.upper()
        if any(kw in test_name_upper for kw in ["눈깜박", "BLINK", "R1", "R2", "H-반사", "H/M", "F파", "F-WAVE"]): 
            blink_rows.append(row)
        elif "SNAP" in test_name_upper or "감각" in test_name: 
            sensory_rows.append(row)
        elif "CMAP" in test_name_upper or "운동" in test_name: 
            motor_rows.append(row)
        else: 
            emg_rows.append(row)

    if sensory_rows or motor_rows or emg_rows:
        st.markdown("""
        <div style="background-color: #f0fdf4; border-left: 4px solid #16a34a; padding: 12px 16px; margin-top: 32px; border-radius: 4px; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">
            <span style="font-weight: 800; color: #16a34a; font-size: 1.05rem;">💡 검사 결과 표기 안내</span><br>
            <span style="color: #15803d; font-size: 0.95rem; line-height: 1.6;">아래 제시된 신경전도 및 침근전도 수치는 환자의 주요 증상을 반영하는 <b>병변 호소측(Affected side)</b>의 대표 검사 결과입니다.</span>
        </div>
        """, unsafe_allow_html=True)

    if sensory_rows:
        st.markdown('<div class="section-label" style="margin-top:24px;">⚡ 감각신경전도검사 (Sensory NCS)</div>', unsafe_allow_html=True)
        st.markdown(_create_responsive_table(["검사 신경", "진폭", "잠복기", "판독"], sensory_rows), unsafe_allow_html=True)

    if motor_rows:
        st.markdown('<div class="section-label" style="margin-top:32px;">⚡ 운동신경전도검사 (Motor NCS)</div>', unsafe_allow_html=True)
        st.markdown(_create_responsive_table(["검사 신경", "진폭", "잠복기", "판독"], motor_rows), unsafe_allow_html=True)

    if (sensory_rows or motor_rows) and "ncs_reason" in teaching:
        with st.expander("🔍 신경전도검사 결과 해석"):
            for r in teaching["ncs_reason"]:
                st.markdown(_format_reason_text(r), unsafe_allow_html=True)

    if blink_rows:
        st.markdown('<div class="section-label" style="margin-top:32px;">⚡ 특수 및 후기반응 검사 (Special & Late Responses)</div>', unsafe_allow_html=True)
        st.markdown(_create_responsive_table(["검사 항목", "결과", "상세 수치", "판독"], blink_rows), unsafe_allow_html=True)
        if "emg_reason" in teaching and not emg_rows: 
            with st.expander("🔍 특수 검사 소견 해석"):
                for r in teaching["emg_reason"]: 
                    st.markdown(_format_reason_text(r), unsafe_allow_html=True)

    if emg_rows:
        st.markdown('<div class="section-label" style="margin-top:32px;">🪡 침근전도검사 (Needle EMG)</div>', unsafe_allow_html=True)
        st.markdown(_create_responsive_table(["검사 근육", "휴식 시", "수의수축 시", "판독"], emg_rows), unsafe_allow_html=True)
        
        if "emg_reason" in teaching:
            with st.expander("🔍 침근전도검사 결과 해석"):
                st.markdown("""
                <div style="background:#f1f5f9; padding:12px; margin-bottom:12px; border-radius:4px; border-left:4px solid #cbd5e1;">
                    <div style="font-size:0.95rem; margin-bottom:6px;"><span style="color:#1e3a8a; font-weight:800;">• 활동성 탈신경 (Active Denervation):</span> 현재 신경 손상이 활발히 진행 중인 상태 (자발전위 관찰)</div>
                    <div style="font-size:0.95rem; margin-bottom:6px;"><span style="color:#1e3a8a; font-weight:800;">• 만성 재신경지배 (Chronic Reinnervation):</span> 신경 손상 후 회복을 시도하는 만성기 (거대운동단위 관찰)</div>
                    <div style="font-size:0.95rem;"><span style="color:#1e3a8a; font-weight:800;">• 수의수축 시 동원 감소 또는 소실 (Reduced Recruitment or Absent):</span> 신경 손상으로 인해 부분 탈신경으로 근력 저하 또는 완전 탈신경으로 완전 마비된 상태</div>
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
        f'</div>', 
        unsafe_allow_html=True
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
    if st.button("👆 다른 사례 선택하기", type="primary"):
        st.session_state["case_reset_counter"] += 1
        st.rerun()

def render_case_detail(): pass
