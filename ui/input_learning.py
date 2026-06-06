# ui/input_learning.py

import streamlit as st
import re
from ui.navigation import render_bottom_navigation
from formatters import html_escape, clean_html
from data.virtual_reports import VIRTUAL_REPORTS, translate_value

def _value_class(value):
    text = str(value)
    if any(a in text for a in ["소실", "지연", "감소", "비정상적"]): return "text-red"
    if any(n in text for n in ["정상", "침묵", "보존"]): return "text-blue"
    return "text-normal"

def _render_mobile_table(headers, rows, table_id, to_eng):
    translated_headers = [translate_value(h, to_eng) for h in headers]
    css = f"""
    <style>
        #{table_id} {{ width: 100%; border-collapse: collapse; margin-bottom: 1rem; font-size: 0.85rem; }}
        #{table_id} th {{ background-color: #f8fafc; padding: 10px; border: 1px solid #e2e8f0; color: #475569; font-weight: 700; }}
        #{table_id} td {{ padding: 10px; border: 1px solid #e2e8f0; text-align: center; word-break: keep-all; font-weight: 400; }}
        .text-red {{ color: #b91c1c !important; font-weight: 600; background-color: #fef2f2; border-radius: 4px; padding: 2px 4px; }}
        .text-blue {{ color: #1d4ed8 !important; font-weight: 600; background-color: #eff6ff; border-radius: 4px; padding: 2px 4px; }}
        @media screen and (max-width: 700px) {{
            #{table_id} thead {{ display: none; }}
            #{table_id} tr {{ display: block; border: 1px solid #e2e8f0; border-radius: 8px; margin-bottom: 10px; padding: 5px; }}
            #{table_id} td {{ display: flex; justify-content: space-between; border: none; padding: 5px 10px; text-align: right; }}
            #{table_id} td::before {{ content: attr(data-label); font-weight: 700; color: #64748b; flex: 1; text-align: left; }}
        }}
    </style>
    """
    body = ""
    for row in rows:
        cells = "".join([f'<td data-label="{translated_headers[i]}" class="{_value_class(translate_value(c, to_eng))}"><span>{html_escape(translate_value(c, to_eng))}</span></td>' for i, c in enumerate(row)])
        body += f"<tr>{cells}</tr>"
    return clean_html(css + f'<table id="{table_id}"><thead><tr>{"".join([f"<th>{h}</th>" for h in translated_headers])}</tr></thead><tbody>{body}</tbody></table>')

def _render_interpretation(report):
    interp = report["interpretation"]
    st.markdown('<div style="margin-top: 35px; padding-top: 20px; border-top: 2px dashed #e2e8f0;"><div style="font-weight: 700; font-size: 1.1rem; margin-bottom: 15px;">🔍 검사 결과 단계별 통합 해석</div>', unsafe_allow_html=True)
    
    for key, label, c1, c2 in [
        ("sensory", "1단계: 감각신경전도검사(SNAP) 해석", "#3b82f6", "#eff6ff"),
        ("motor", "2단계: 운동신경전도검사(CMAP) 해석", "#10b981", "#ecfdf5"),
        ("emg", "3단계: 침근전도검사(Needle EMG) 해석", "#f59e0b", "#fffbeb"),
        ("reflex", "특수 및 반사검사 해석", "#8b5cf6", "#faf5ff")
    ]:
        items = interp.get(key, [])
        if items:
            st.markdown(f'<div style="border-left: 5px solid {c1}; background-color: {c2}; padding: 10px 14px; font-weight: 700; font-size: 1rem; color: #1e293b; margin-bottom: 10px;">{label}</div>', unsafe_allow_html=True)
            for t in items:
                st.markdown(f'<div style="color: #334155; font-size: 0.95rem; line-height: 1.6; margin-bottom: 6px; padding-left: 10px; word-break: keep-all;">• {html_escape(t)}</div>', unsafe_allow_html=True)
            st.markdown("<br/>", unsafe_allow_html=True)

    st.markdown('<div style="border-left: 5px solid #dc2626; background-color: #fef2f2; padding: 10px 14px; font-weight: 700; font-size: 1rem; color: #991b1b; margin-bottom: 12px;">최종 검사결과 추정 질환</div>', unsafe_allow_html=True)
    for t in interp.get("integration", []):
        st.markdown(f'<div style="color: #1e293b; font-size: 0.95rem; line-height: 1.6; margin-bottom: 8px; word-break: keep-all;">{html_escape(t)}</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

def render_input_learning():
    st.markdown('<div style="font-size: 1.5rem; font-weight: 700; color: #0f172a; margin-bottom: 1.2rem;">📊 가상 결과표 판독 학습</div>', unsafe_allow_html=True)
    if "input_reset_counter" not in st.session_state: st.session_state["input_reset_counter"] = 0
    selected = st.radio("가상 결과표 선택", ["선택 안 함"] + list(VIRTUAL_REPORTS.keys()), key=f"inp_{st.session_state['input_reset_counter']}")
    
    if selected != "선택 안 함":
        report = VIRTUAL_REPORTS[selected]
        to_eng = (st.radio("언어 모드", ["🇰🇷 한글", "🇺🇸 영문"], horizontal=True) == "🇺🇸 영문")
        
        meta = report["meta"]
        st.markdown(f'<div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px; margin-top: 15px;"><b>주요 증상:</b><br/>{html_escape(meta.get("chief", ""))}</div>', unsafe_allow_html=True)

        if report.get("sensory_ncs"):
            st.markdown('<div style="font-weight: 700; margin-top: 25px; margin-bottom: 8px;">⚡ 감각신경전도검사 (SNAP)</div>', unsafe_allow_html=True)
            rows = [[r["nerve"], r["side"], r["recording"], r["stimulation"], r["amplitude"], r["latency"], r["velocity"]] for r in report["sensory_ncs"]]
            st.markdown(_render_mobile_table(["검사 신경", "측", "기록 위치", "자극 위치", "진폭", "잠복기", "전도속도"], rows, "snc", to_eng), unsafe_allow_html=True)

        if report.get("motor_ncs"):
            st.markdown('<div style="font-weight: 700; margin-top: 25px; margin-bottom: 8px;">⚡ 운동신경전도검사 (CMAP)</div>', unsafe_allow_html=True)
            rows = [[r["nerve"], r["side"], r["recording"], r["stimulation"], r["amplitude"], r["latency"], r["velocity"]] for r in report["motor_ncs"]]
            st.markdown(_render_mobile_table(["검사 신경", "측", "기록 근육", "자극 위치", "진폭", "잠복기", "전도속도"], rows, "mnc", to_eng), unsafe_allow_html=True)

        if report.get("needle_emg"):
            st.markdown('<div style="font-weight: 700; margin-top: 25px; margin-bottom: 8px;">🪡 침근전도검사 (Needle EMG)</div>', unsafe_allow_html=True)
            rows = [[r["muscle"], r["root"], r["nerve"], r["rest"], r["volition"]] for r in report["needle_emg"]]
            st.markdown(_render_mobile_table(["검사 근육", "분절", "말초신경", "휴식 시 반응", "자발적 근수축 시 반응"], rows, "emg", to_eng), unsafe_allow_html=True)

        _render_interpretation(report)
        if st.button("🔄 처음으로 돌아가기", type="primary", use_container_width=True):
            st.session_state["input_reset_counter"] += 1
            st.rerun()
    else:
        render_bottom_navigation()
