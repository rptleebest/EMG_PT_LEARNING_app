# ui/case_learning.py

import re
import streamlit as st
from data.cases import CASE_LIBRARY
from ui.navigation import render_bottom_navigation

def format_nerve_eng_below(text):
    if not text: return ""
    m = re.match(r'^(.*?)\s*\((.*?)\)$', str(text))
    if m:
        kor, eng = m.group(1).strip(), m.group(2).strip()
        # 약어 전용 대문자 변환 정규식
        eng_formatted = ' '.join([w.upper() if re.sub(r'[^a-zA-Z]', '', w).upper() in {"SNAP", "CMAP", "MUAP", "MUAPS", "NCS", "EMG", "MU", "MMT"} else w.lower() for w in eng.split()])
        return f"<div style='font-size:0.92rem; font-weight:800; color:#1e293b;'>🔹 {kor}</div><div style='font-size:0.78rem; color:#64748b; margin-left:22px; margin-bottom:6px; line-height:1.1;'>{eng_formatted}</div>"
    return f"<div style='font-size:0.92rem; font-weight:800; color:#1e293b; margin-bottom:6px;'>🔹 {text}</div>"

def _get_data_row(lbl, val, is_bad=False):
    color = "txt-red" if is_bad else ("txt-green" if "정상" in val else "txt-normal")
    return f'<div class="data-row" style="margin-left:22px;"><div class="data-label">{lbl}</div><div class="data-value {color}">{val}</div></div>'

def _get_ncs_pattern(raw_val):
    if raw_val == "ncs_delayed": 
        return _get_data_row("진폭", "정상 범위") + _get_data_row("잠복기", "지연(정상측 대비 130%↑)", True) + _get_data_row("판단", "진폭 정상 / 잠복기 지연", True)
    if raw_val == "ncs_reduced": 
        return _get_data_row("진폭", "감소(정상측 대비 50%↓)", True) + _get_data_row("잠복기", "정상 범위") + _get_data_row("판단", "진폭 감소 / 잠복기 정상", True)
    if raw_val == "ncs_absent": 
        return _get_data_row("진폭", "반응 소실", True) + _get_data_row("잠복기", "반응 소실", True) + _get_data_row("판단", "반응 소실(축삭 사멸)", True)
    return _get_data_row("진폭", "정상 범위") + _get_data_row("잠복기", "정상 범위") + _get_data_row("판단", "진폭 정상 / 잠복기 정상")

def _get_emg_pattern(raw_val):
    if raw_val in ["emg_active_denervation", "emg_paraspinal_denervation"]:
        return _get_data_row("휴식 시", "비정상 자발전위(Fibrillation, Positive sharp wave)", True) + _get_data_row("수의적 수축 시", "Reduced MUAPs", True) + _get_data_row("판단", "비정상 반응(활동성 탈신경)", True)
    if raw_val == "emg_chronic_reinnervation":
        return _get_data_row("휴식 시", "전기적 침묵(Silent)") + _get_data_row("수의적 수축 시", "Giant MUAPs, Reduced MUAPs", True) + _get_data_row("판단", "비정상 반응(만성 재신경지배)", True)
    return _get_data_row("휴식 시", "전기적 침묵(Silent)") + _get_data_row("수의적 수축 시", "Normal MUAPs") + _get_data_row("판단", "정상 반응")

def render_case_list():
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">가상 사례 선택</div>', unsafe_allow_html=True)
    case_name = st.selectbox("리스트", ["선택 안 함"] + list(CASE_LIBRARY.keys()), label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

    if case_name != "선택 안 함":
        case = CASE_LIBRARY[case_name]
        patient, findings, teaching = case["patient"], case["findings"], case["teaching_diagnosis"]
        side = patient.get("side", "오른쪽")

        st.markdown(f'<div class="info-card">👤 <b>환자 정보</b>: {patient["age"]}세 / {patient["sex"]} / 병변측: {side}</div>', unsafe_allow_html=True)

        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">💡 판독 기준 팁 (정상측 대비)</div>', unsafe_allow_html=True)
        st.markdown('<div style="font-size:0.85rem; color:#475569;">- 진폭 감소: 50% 이하 시 비정상 (축삭 손상)<br>- 잠복기 지연: 130% 이상 시 비정상 (말이집탈락)<br>- 사례 학습에서는 정상측 수치는 생략하고 결과 패턴만 제시합니다.</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="sub-title">🖐️ 감각 및 ⚡ 운동신경전도검사 (병변측)</div>', unsafe_allow_html=True)
        for item, vals in findings.items():
            if "SNAP" in item or "CMAP" in item:
                st.markdown(format_nerve_eng_below(item), unsafe_allow_html=True)
                st.markdown(_get_ncs_pattern(vals[0] if side == "왼쪽" else vals[1]), unsafe_allow_html=True)
                st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)
        
        st.markdown(f'<div class="sub-title">🪡 침근전도검사 (병변측)</div>', unsafe_allow_html=True)
        for item, vals in findings.items():
            if "SNAP" not in item and "CMAP" not in item and "F파" not in item and "H" not in item:
                st.markdown(format_nerve_eng_below(item), unsafe_allow_html=True)
                st.markdown(_get_emg_pattern(vals[0] if side == "왼쪽" else vals[1]), unsafe_allow_html=True)
                st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">🧠 검사 결과 통합 해석</div>', unsafe_allow_html=True)
        for x in teaching.get("integration", []):
            st.markdown(f'<div style="font-size:0.9rem; color:#334155; margin-bottom:8px;">• {re.sub(r"\(.*?\)", "", x)}</div>', unsafe_allow_html=True)
        
        # 🚨 진단명을 통합해석 아래로 이동
        diag_name = teaching.get("summary", "").replace(" 패턴입니다.", "").replace("입니다.", "")
        st.markdown(f"""
        <div class="diagnosis-box">
            <span style="font-size:0.9rem; font-weight:700; color:#475569;">🩺 의심 추정질환:</span> 
            <span style="font-size:0.95rem; font-weight:800; color:#b91c1c; margin-left:4px;">{diag_name}</span>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="center-btn-container">', unsafe_allow_html=True)
        if st.button("다른 사례 분석", key="reset_case"): st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    render_bottom_navigation()
