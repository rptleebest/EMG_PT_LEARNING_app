# ui/case_learning.py

import html
import streamlit as st

from data.cases import CASE_LIBRARY
from ui.navigation import render_bottom_navigation

# 안전한 용어 변환기 (오류 방지용 내장 매퍼)
def _safe_format_code(code: str) -> str:
    code_str = str(code)
    mapping = {
        "ncs_normal": "정상",
        "ncs_delayed": "지연",
        "ncs_reduced": "감소",
        "ncs_absent": "소실",
        "ncs_conduction_block": "전도차단",
        "emg_normal": "정상",
        "emg_active_denervation": "활동성 탈신경",
        "emg_paraspinal_denervation": "탈신경",
        "emg_chronic_reinnervation": "만성 재신경지배",
        "emg_active_chronic": "활동성+만성",
        "blink_delayed": "지연",
        "blink_delayed_absent": "지연/소실",
        "h_reflex_hyperactive": "항진",
        "h_m_ratio_increased": "비율 증가",
        "fwave_delayed_absent": "지연/소실"
    }
    return mapping.get(code_str, code_str)


def _get_result_color_style(value: str) -> str:
    text = str(value)
    abnormal_words = ["비정상", "감소", "지연", "소실", "탈신경", "재신경지배", "차단", "항진", "증가"]
    if any(word in text for word in abnormal_words):
        return "color: #991b1b; font-weight: 600;"
    if "정상" in text:
        return "color: #15803d; font-weight: 600;"
    return ""


def _create_responsive_table(headers: list, rows: list, table_id: str) -> str:
    if not rows:
        return "<p style='font-size:0.85rem; color:#64748b;'>해당 데이터가 없습니다.</p>"

    safe_table_id = html.escape(str(table_id), quote=True)

    css = f"""
    <style>
        #{safe_table_id} {{ width: 100%; border-collapse: collapse; margin-bottom: 16px; font-size: 0.86rem; }}
        #{safe_table_id} th {{ background-color: #f1f5f9; padding: 10px; border-bottom: 2px solid #cbd5e1; text-align: center; color: #1e293b; font-weight: 700; }}
        #{safe_table_id} td {{ padding: 10px; border-bottom: 1px solid #e2e8f0; text-align: center; color: #334155; line-height: 1.5; font-weight: 400; }}
        #{safe_table_id} td.left-align {{ text-align: left; font-weight: 600; color: #1e3a8a; }}
        @media screen and (max-width: 768px) {{
            #{safe_table_id} thead {{ display: none; }}
            #{safe_table_id} tr {{ display: block; border: 1px solid #e2e8f0; border-radius: 8px; margin-bottom: 12px; background: #ffffff; padding: 6px; }}
            #{safe_table_id} td {{ display: flex; justify-content: space-between; align-items: center; gap: 12px; border-bottom: 1px solid #f1f5f9; padding: 8px 10px; text-align: right; }}
            #{safe_table_id} td:last-child {{ border-bottom: none; }}
            #{safe_table_id} td::before {{ content: attr(data-label); font-weight: 600; color: #475569; text-align: left; font-size: 0.8rem; flex: 0 0 35%; }}
            #{safe_table_id} td > span {{ flex: 1; text-align: right; word-break: keep-all; font-weight: 400; }}
            #{safe_table_id} td.left-align {{ justify-content: center; background: #f8fafc; border-radius: 6px 6px 0 0; text-align: center; padding: 10px; }}
            #{safe_table_id} td.left-align::before {{ content: none; }}
            #{safe_table_id} td.left-align > span {{ text-align: center; font-weight: 600; }}
        }}
    </style>
    """

    header_html = "".join([f"<th>{html.escape(h, quote=True)}</th>" for h in headers])

    tr_html = ""
    for row in rows:
        td_html = ""
        for idx, col in enumerate(row):
            val = _safe_format_code(col)
            cls = "left-align" if idx == 0 else ""
            color_style = _get_result_color_style(val) if idx > 0 else ""
            header_label = html.escape(headers[idx], quote=True) if idx < len(headers) else ""
            
            td_html += f"<td data-label='{header_label}' class='{cls}' style='{color_style}'><span>{html.escape(val)}</span></td>"
        tr_html += f"<tr>{td_html}</tr>"

    return f"{css}<table id='{safe_table_id}'><thead><tr>{header_html}</tr></thead><tbody>{tr_html}</tbody></table>"


def render_case_list():
    st.markdown('<div class="main-title">사례 학습 모드</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtle">환자 임상 정보와 전기진단 소견을 분석하여 병변 위치를 추론합니다.</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">📋 학습할 임상 증상 선택</div>', unsafe_allow_html=True)

    case_names = list(CASE_LIBRARY.keys())
    
    if "case_reset_counter" not in st.session_state:
        st.session_state["case_reset_counter"] = 0
        
    radio_key = f"case_list_radio_{st.session_state['case_reset_counter']}"

    selected = st.radio(
        "사례 리스트",
        case_names,
        key=radio_key,
        label_visibility="collapsed"
    )

    st.markdown('<div style="text-align: center; margin-top: 16px;">', unsafe_allow_html=True)
    if st.button("진단 추론 시작 ➡️", type="primary", use_container_width=True):
        st.session_state["selected_case"] = selected
        st.session_state["screen"] = "case_detail"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    render_bottom_navigation()


def render_case_detail():
    case_name = st.session_state.get("selected_case")
    if not case_name or case_name not in CASE_LIBRARY:
        st.session_state["screen"] = "case_list"
        st.rerun()

    data = CASE_LIBRARY[case_name]
    patient = data.get("patient", {})
    findings = data.get("findings", {})
    teaching = data.get("teaching_diagnosis", {})

    st.markdown('<div class="main-title">사례 상세 분석</div>', unsafe_allow_html=True)
    
    # 1. 환자 기본 정보
    st.markdown('<div class="info-card">', unsafe_allow_html=True)
    st.markdown('<div class="case-title-mobile">👤 환자 기본 정보</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="case-subtitle-mobile"><span class="label-strong">연령/성별:</span> {patient.get("age")}세 / {patient.get("sex")} &nbsp;|&nbsp; <span class="label-strong">병변측:</span> {patient.get("side")}</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="case-text-block" style="margin-top:10px;"><span class="label-strong">주요 증상:</span><br/>' + 
        "<br/>".join([f"• {s}" for s in patient.get("symptoms", [])]) + 
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # 2. 이학적 검사 (신경학적 진찰)
    phys_exam = patient.get("physical_exam", {})
    if phys_exam:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="case-section-label">🩺 이학적 검사 (신경학적 진찰)</div>', unsafe_allow_html=True)
        for category, items in phys_exam.items():
            st.markdown(f'<div class="finding-highlight">{category}</div>', unsafe_allow_html=True)
            for item in items:
                st.markdown(f'<div class="case-bullet">• {item}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # 3. 전기진단검사 결과 분류 및 표 렌더링
    st.markdown(
        '<div class="warn-card"><div class="case-bullet-strong text-blue">💡 학습 팁: 아래 표는 병변부의 검사 결과를 요약한 것입니다.</div></div>', 
        unsafe_allow_html=True
    )

    sensory_rows, motor_rows, emg_rows = [], [], []

    for test_name, result_tuple in findings.items():
        name_lower = test_name.lower()
        if not isinstance(result_tuple, tuple):
            continue
            
        row = [test_name] + list(result_tuple)
        
        if "snap" in name_lower or "감각" in test_name:
            sensory_rows.append(row)
        elif "cmap" in name_lower or "운동" in test_name:
            motor_rows.append(row)
        else:
            emg_rows.append(row)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">⚡ 전기진단검사 결과 (NCS / EMG)</div>', unsafe_allow_html=True)
    
    if sensory_rows:
        st.markdown('<div class="finding-highlight">감각신경전도검사 (Sensory NCS)</div>', unsafe_allow_html=True)
        st.markdown(_create_responsive_table(["검사 신경", "진폭(Amplitude)", "잠복기(Latency)"], sensory_rows, "tbl_sensory"), unsafe_allow_html=True)
    
    if motor_rows:
        st.markdown('<div class="finding-highlight">운동신경전도검사 (Motor NCS)</div>', unsafe_allow_html=True)
        st.markdown(_create_responsive_table(["검사 신경", "진폭(Amplitude)", "잠복기(Latency)"], motor_rows, "tbl_motor"), unsafe_allow_html=True)
        
    if emg_rows:
        st.markdown('<div class="finding-highlight">침근전도검사 (Needle EMG)</div>', unsafe_allow_html=True)
        st.markdown(_create_responsive_table(["검사 근육", "휴식 시(Rest)", "수의수축(Volition)"], emg_rows, "tbl_emg"), unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)

    # 4. 임상 추론 및 생리학적 해석 결과
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.markdown('<div class="result-title">✅ 교육용 진단 및 생리학적 해석</div>', unsafe_allow_html=True)
    
    st.markdown(
        f'<div class="case-text-block" style="background:#fff1f2!important; border-left-color:#fecdd3!important;"><span class="label-strong text-red">최종 추론 진단:</span> <span class="result-value text-red" style="font-weight:700!important;">{teaching.get("summary", "진단 요약 없음")}</span></div>',
        unsafe_allow_html=True
    )
    
    if "ncs_reason" in teaching:
        st.markdown('<div class="result-label">🧠 NCS 해석 논리</div>', unsafe_allow_html=True)
        for r in teaching["ncs_reason"]:
            st.markdown(f'<div class="finding-subtext">• {r}</div>', unsafe_allow_html=True)

    if "emg_reason" in teaching:
        st.markdown('<div class="result-label" style="border-left-color:#d97706!important; background:#fffbeb!important;">🔬 EMG 해석 논리</div>', unsafe_allow_html=True)
        for r in teaching["emg_reason"]:
            st.markdown(f'<div class="finding-subtext">• {r}</div>', unsafe_allow_html=True)
            
    st.markdown('</div>', unsafe_allow_html=True)

    render_bottom_navigation()
