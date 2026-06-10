# ui/case_learning.py

import html
import streamlit as st
from data.cases import CASE_LIBRARY
from ui.navigation import render_bottom_navigation

def _safe_format_code(code: str) -> str:
    mapping = {
        "ncs_normal": "정상 범위", "ncs_delayed": "잠복기 지연", "ncs_reduced": "진폭 감소", 
        "ncs_absent": "반응 소실", "ncs_conduction_block": "진폭 급감 (국소 전도차단 의심)",
        "emg_normal": "정상 범위", "emg_active_denervation": "활동성 탈신경", 
        "emg_paraspinal_denervation": "활동성 탈신경", "emg_chronic_reinnervation": "만성 재신경지배", 
        "emg_active_chronic": "활동성+만성", "blink_delayed": "잠복기 지연", "blink_absent": "반응 소실"
    }
    return mapping.get(str(code), str(code))

def _get_result_color_style(value: str) -> str:
    text = str(value)
    abnormal_words = ["비정상", "감소", "지연", "소실", "탈신경", "재신경지배", "차단"]
    if any(w in text for w in abnormal_words): return "color: #991b1b; font-weight: 800;"
    if "정상" in text: return "color: #15803d; font-weight: 800;"
    return ""

def _create_responsive_table(headers: list, rows: list) -> str:
    if not rows: return ""
    # th 요소의 text-align을 center로 수정하여 제목을 중앙 정렬합니다.
    css = """<style>table { width: 100%; border-collapse: collapse; margin-bottom: 8px; font-size: 0.9rem; } th { background-color: #f8fafc; padding: 10px; border-bottom: 2px solid #cbd5e1; text-align: center; color: #1e293b; font-weight: 800; } td { padding: 10px; border-bottom: 1px solid #e2e8f0; text-align: left; color: #334155; } td.fst-col { font-weight: 800; color: #1e3a8a; } @media screen and (max-width: 768px) { thead { display: none; } tr { display: block; border: 1px solid #e2e8f0; border-radius: 8px; margin-bottom: 12px; background: #ffffff; padding: 8px; } td { display: flex; justify-content: space-between; align-items: center; gap: 12px; border-bottom: 1px dashed #e2e8f0; padding: 10px 8px; text-align: right; } td:last-child { border-bottom: none; } td::before { content: attr(data-label); font-weight: 800; color: #475569; text-align: left; font-size: 0.85rem; flex: 0 0 35%; } td > span { flex: 1; text-align: right; word-break: keep-all; font-weight: 400; } td.fst-col { justify-content: center; background: #f1f5f9; border-radius: 6px 6px 0 0; text-align: center; padding: 12px; } td.fst-col::before { content: none; } td.fst-col > span { text-align: center; font-weight: 800; color: #1e3a8a; } }</style>"""
    header_html = "".join([f"<th>{html.escape(h)}</th>" for h in headers])
    tr_html = ""
    for row in rows:
        td_html = ""
        for idx, col in enumerate(row):
            val = _safe_format_code(col)
            cls = "fst-col" if idx == 0 else ""
            color_style = _get_result_color_style(val) if idx > 0 else ""
            header_label = html.escape(headers[idx]) if idx < len(headers) else ""
            td_html += f"<td data-label='{header_label}' class='{cls}' style='{color_style}'><span>{html.escape(val)}</span></td>"
        tr_html += f"<tr>{td_html}</tr>"
    return f"{css}<table><thead><tr>{header_html}</tr></thead><tbody>{tr_html}</tbody></table>"

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
        for cat, items in phys_exam.items():
            icon = "🖐" if "감각" in cat else "💪" if "근력" in cat else "🔨"
            st.markdown(f'<div class="exam-box"><div class="exam-title">{icon} {cat}</div>', unsafe_allow_html=True)
            for item in items:
                if "(" in item and ")" in item:
                    parts = item.split("(", 1)
                    main_text = parts[0].strip()
                    sub_text = "(" + parts[1].strip()
                    st.markdown(f'<div style="margin-bottom:2px; font-weight:700; color:#334155;">• {main_text}</div>', unsafe_allow_html=True)
                    st.markdown(f'<div style="margin-left:14px; margin-bottom:8px; font-size:0.9rem; color:#64748b;">{sub_text}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div style="margin-bottom:4px; color:#334155;">• {item}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    sensory_rows, motor_rows, emg_rows, blink_rows = [], [], [], []
    for test_name, result_tuple in findings.items():
        if not isinstance(result_tuple, tuple): continue
        row = [test_name] + list(result_tuple)
        if "눈깜박" in test_name or "blink" in test_name.lower(): blink_rows.append(row)
        elif "snap" in test_name.lower() or "감각" in test_name: sensory_rows.append(row)
        elif "cmap" in test_name.lower() or "운동" in test_name: motor_rows.append(row)
        else: emg_rows.append(row)

    if sensory_rows:
        st.markdown('<div class="section-label" style="margin-top:32px;">⚡ 감각신경전도검사 (Sensory NCS)</div>', unsafe_allow_html=True)
        st.markdown(_create_responsive_table(["검사 신경", "진폭", "잠복기"], sensory_rows), unsafe_allow_html=True)

    if motor_rows:
        st.markdown('<div class="section-label" style="margin-top:32px;">⚡ 운동신경전도검사 (Motor NCS)</div>', unsafe_allow_html=True)
        st.markdown(_create_responsive_table(["검사 신경", "진폭", "잠복기"], motor_rows), unsafe_allow_html=True)

    if (sensory_rows or motor_rows) and "ncs_reason" in teaching:
        with st.expander("🔍 신경전도검사 결과 해석"):
            for idx, r in enumerate(teaching["ncs_reason"]):
                st.markdown(f'<div style="color:#334155; margin-bottom:8px;"><span style="color:#1e3a8a; font-weight:800; margin-right:4px;">{idx+1}.</span>{r}</div>', unsafe_allow_html=True)

    if blink_rows:
        st.markdown('<div class="section-label" style="margin-top:32px;">⚡ 특수 및 후기반응 검사 (Special & Late Responses)</div>', unsafe_allow_html=True)
        st.markdown(_create_responsive_table(["검사 신경", "진폭", "잠복기"], blink_rows), unsafe_allow_html=True)
        if "emg_reason" in teaching: 
            with st.expander("🔍 특수 검사 소견 해석"):
                for idx, r in enumerate(teaching["emg_reason"]): 
                    st.markdown(f'<div style="color:#334155; margin-bottom:8px;"><span style="color:#1e3a8a; font-weight:800; margin-right:4px;">{idx+1}.</span>{r}</div>', unsafe_allow_html=True)

    if emg_rows:
        st.markdown('<div class="section-label" style="margin-top:32px;">🪡 침근전도검사 (Needle EMG)</div>', unsafe_allow_html=True)
        st.markdown(_create_responsive_table(["검사 근육", "휴식 시", "수의수축 시"], emg_rows), unsafe_allow_html=True)
        if "emg_reason" in teaching:
            with st.expander("🔍 침근전도검사 결과 해석"):
                st.markdown("""
                <div style="background:#f1f5f9; padding:12px; margin-bottom:12px; border-radius:4px; border-left:4px solid #cbd5e1;">
                    <div style="font-size:0.95rem; margin-bottom:6px;"><span style="color:#1e3a8a; font-weight:800;">• 활동성 탈신경 (Active Denervation):</span> 현재 신경 손상이 활발히 진행 중인 상태 (자발전위 관찰)</div>
                    <div style="font-size:0.95rem; margin-bottom:6px;"><span style="color:#1e3a8a; font-weight:800;">• 만성 재신경지배 (Chronic Reinnervation):</span> 신경 손상 후 회복을 시도하는 만성기 (거대운동단위 관찰)</div>
                    <div style="font-size:0.95rem;"><span style="color:#1e3a8a; font-weight:800;">• 수의수축 시 동원 감소 또는 소실 (Reduced Recruitment or Absent):</span> 신경 손상으로 인해 부분 탈신경으로 근력 저하 또는 완전 탈신경으로 완전 마비된 상태</div>
                </div>
                """, unsafe_allow_html=True)
                if not blink_rows:
                    for idx, r in enumerate(teaching["emg_reason"]): 
                        st.markdown(f'<div style="color:#334155; margin-bottom:8px;"><span style="color:#1e3a8a; font-weight:800; margin-right:4px;">{idx+1}.</span>{r}</div>', unsafe_allow_html=True)

    st.markdown('<hr style="border-top: 2px dashed #cbd5e1; margin: 2.5rem 0 1.5rem 0;">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">✅ 임상적 통합 해석 및 감별진단</div>', unsafe_allow_html=True)
    
    if "integration" in teaching:
        st.markdown('<div class="sub-title">🔹 검사 결과 통합 결론</div>', unsafe_allow_html=True)
        st.markdown('<div class="left-border-box" style="border-left-color:#3b82f6;">', unsafe_allow_html=True)
        for r in teaching["integration"]: 
            st.markdown(f'<div style="margin-bottom:8px;">• {r}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
            
    st.markdown(
        f'<div style="background:#fdf2f8; border:1px solid #fbcfe8; padding:12px 16px; border-radius:8px; margin-top:16px;">'
        f'<span style="font-size:1.05rem; color:#9d174d; font-weight:800;">임상적 추정진단 (R/O) : {teaching.get("summary")}</span>'
        f'</div>', 
        unsafe_allow_html=True
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
    if st.button("👆 다른 사례 선택하기", type="primary"):
        st.session_state["case_reset_counter"] += 1
        st.rerun()

def render_case_detail(): pass
