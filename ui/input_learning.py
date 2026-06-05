# ui/input_learning.py

import streamlit as st
from ui.navigation import render_bottom_navigation
from formatters import html_escape, clean_html
from data.virtual_reports import VIRTUAL_REPORTS, translate_value

def _value_class(value):
    text = str(value)
    abnormal_tokens = ["반응 소실", "소실", "지연", "감소", "느림", "전도차단", "증가", "Absent", "Delayed", "Reduced", "No Response", "fibrillation", "positive sharp", "Reduced MU recruitment", "Giant"]
    normal_tokens = ["Silent", "Normal", "정상", "보존", "Normal Range"]
    if any(token in text for token in abnormal_tokens): return "text-red"
    if any(token in text for token in normal_tokens): return "text-blue"
    return "text-normal"

def _count_abnormalities(rows, to_eng):
    count = 0
    for row in rows:
        for cell in row[1:]:
            val = translate_value("" if cell is None else str(cell), to_eng)
            if _value_class(val) == "text-red":
                count += 1
                break
    return count

def _render_mobile_table(headers, rows, table_id, to_eng):
    safe_table_id = html_escape(table_id)
    translated_headers = [translate_value(h, to_eng) for h in headers]

    css = f"""
    <style>
        #{safe_table_id} {{ width: 100%; border-collapse: collapse; margin: 0.55rem 0 1rem 0; font-size: 0.84rem; background: #ffffff; }}
        #{safe_table_id} th {{ background-color: #f8fafc; padding: 0.62rem 0.5rem; border: 1px solid #e2e8f0; text-align: center; color: #334155; font-weight: 700; line-height: 1.35; }}
        #{safe_table_id} td {{ padding: 0.58rem 0.5rem; border: 1px solid #e2e8f0; text-align: center; color: #475569; line-height: 1.45; }}
        #{safe_table_id} td.left-align {{ text-align: left; font-weight: 700; color: #0f172a; background-color: #f0fdfa; }}
        .text-red {{ color: #dc2626 !important; font-weight: 600; background-color: #fef2f2; border-radius: 4px; padding: 2px 4px; }}
        .text-blue {{ color: #2563eb !important; font-weight: 600; background-color: #eff6ff; border-radius: 4px; padding: 2px 4px; }}
        @media screen and (max-width: 700px) {{
            #{safe_table_id} thead {{ display: none; }}
            #{safe_table_id} tr {{ display: block; border: 1px solid #e2e8f0; border-radius: 8px; margin-bottom: 0.8rem; background: #ffffff; box-shadow: 0 1px 2px rgba(0,0,0,0.05); }}
            #{safe_table_id} td {{ display: flex; justify-content: space-between; align-items: flex-start; gap: 0.75rem; border: none; border-bottom: 1px solid #f8fafc; padding: 0.6rem 0.7rem; text-align: right; }}
            #{safe_table_id} td:last-child {{ border-bottom: none; }}
            #{safe_table_id} td::before {{ content: attr(data-label); font-weight: 600; color: #64748b; text-align: left; font-size: 0.78rem; flex: 0 0 38%; }}
            #{safe_table_id} td > span {{ flex: 1; text-align: right; word-break: keep-all; }}
            #{safe_table_id} td.left-align {{ display: block; background: #f0fdfa; text-align: left; padding: 0.7rem; color: #0f172a; font-weight: 800; border-radius: 8px 8px 0 0; }}
            #{safe_table_id} td.left-align::before {{ content: none; }}
            #{safe_table_id} td.left-align > span {{ display: block; text-align: left; }}
        }}
    </style>
    """
    header_html = "".join([f"<th>{html_escape(h)}</th>" for h in translated_headers])
    body_html = ""
    for row in rows:
        cell_html = ""
        for idx, cell in enumerate(row):
            translated_cell = translate_value("" if cell is None else str(cell), to_eng)
            left_class = "left-align" if idx == 0 else ""
            color_class = _value_class(translated_cell) if idx > 0 else ""
            label = translated_headers[idx] if idx < len(translated_headers) else ""
            display_text = html_escape(translated_cell).replace(" / ", "<br/>")
            cell_html += f'<td data-label="{html_escape(label)}" class="{left_class} {color_class}"><span>{display_text}</span></td>'
        body_html += f"<tr>{cell_html}</tr>"
    return clean_html(css + f'<table id="{safe_table_id}"><thead><tr>{header_html}</tr></thead><tbody>{body_html}</tbody></table>')

def _render_tables(report, to_eng):
    if report.get("sensory_ncs"):
        abnormal_cnt = _count_abnormalities([list(r.values()) for r in report["sensory_ncs"]], to_eng)
        st.markdown(f'<div style="font-weight: 700; color: #0f766e; margin-top: 15px;">감각신경전도검사 (SNAP) <span style="color:#ef4444; font-size:0.85em; background:#fef2f2; padding:2px 6px; border-radius:10px; margin-left:5px;">이상 소견: {abnormal_cnt}개 신경</span></div>', unsafe_allow_html=True)
        rows = [[r.get("nerve", ""), r.get("side", ""), r.get("recording", ""), r.get("stimulation", ""), r.get("amplitude", ""), r.get("latency", ""), r.get("velocity", "")] for r in report["sensory_ncs"]]
        st.markdown(_render_mobile_table(["검사 신경", "측", "기록 위치", "자극 위치", "진폭", "잠복기", "전도속도"], rows, "sensory_table", to_eng), unsafe_allow_html=True)

    if report.get("motor_ncs"):
        abnormal_cnt = _count_abnormalities([list(r.values()) for r in report["motor_ncs"]], to_eng)
        st.markdown(f'<div style="font-weight: 700; color: #0f766e; margin-top: 15px;">운동신경전도검사 (CMAP) <span style="color:#ef4444; font-size:0.85em; background:#fef2f2; padding:2px 6px; border-radius:10px; margin-left:5px;">이상 소견: {abnormal_cnt}개 신경</span></div>', unsafe_allow_html=True)
        rows = [[r.get("nerve", ""), r.get("side", ""), r.get("recording", ""), r.get("stimulation", ""), r.get("amplitude", ""), r.get("latency", ""), r.get("velocity", "")] for r in report["motor_ncs"]]
        st.markdown(_render_mobile_table(["검사 신경", "측", "기록 근육", "자극 위치", "진폭", "잠복기", "전도속도"], rows, "motor_table", to_eng), unsafe_allow_html=True)

    if report.get("late_response"):
        st.markdown('<div style="font-weight: 700; color: #0f766e; margin-top: 15px;">후기반응 / 반사 검사</div>', unsafe_allow_html=True)
        rows = [[r.get("test", ""), r.get("side", ""), r.get("latency", ""), r.get("amplitude", "")] for r in report["late_response"]]
        st.markdown(_render_mobile_table(["검사 항목", "측", "잠복기", "진폭"], rows, "late_table", to_eng), unsafe_allow_html=True)

    if report.get("needle_emg"):
        abnormal_cnt = _count_abnormalities([list(r.values()) for r in report["needle_emg"]], to_eng)
        st.markdown(f'<div style="font-weight: 700; color: #b45309; margin-top: 15px;">침근전도검사 (Needle EMG) <span style="color:#ef4444; font-size:0.85em; background:#fef2f2; padding:2px 6px; border-radius:10px; margin-left:5px;">이상 소견: {abnormal_cnt}개 근육</span></div>', unsafe_allow_html=True)
        rows = [[r.get("muscle", ""), r.get("root", ""), r.get("nerve", ""), r.get("rest", ""), r.get("volition", "")] for r in report["needle_emg"]]
        st.markdown(_render_mobile_table(["검사 근육", "분절", "말초신경", "휴식 시 반응", "수의수축 시 반응"], rows, "emg_table", to_eng), unsafe_allow_html=True)

def _render_interpretation(report):
    interp = report["interpretation"]
    st.markdown('<div style="margin-top: 25px; padding-top: 15px; border-top: 2px dashed #e2e8f0;"><div style="font-size: 1.2rem; font-weight: 800; color: #1e293b; margin-bottom: 15px;">검사 결과 단계별 통합 해석</div>', unsafe_allow_html=True)

    sections = [
        ("sensory", "1단계: 감각신경전도검사 해석", "#3b82f6", "#eff6ff"), 
        ("motor", "2단계: 운동신경전도검사 해석", "#0f766e", "#f0fdfa"),
        ("emg", "3단계: 침근전도검사 해석", "#d97706", "#fffbeb")
    ]
    for key, title, b_color, bg_color in sections:
        items = interp.get(key, [])
        if not items: continue
        st.markdown(f'<div style="border-left: 4px solid {b_color}; background-color: {bg_color}; padding: 8px 12px; font-weight: 700; color: #1e293b; margin-bottom: 8px; border-radius: 0 4px 4px 0;">{html_escape(title)}</div>', unsafe_allow_html=True)
        for item in items: 
            st.markdown(f'<div style="color: #334155; font-size: 0.95rem; margin-bottom: 6px; padding-left: 10px;">• {html_escape(item)}</div>', unsafe_allow_html=True)
        st.markdown("<br/>", unsafe_allow_html=True)

    # 4단계 (결론을 뒤에 배치)
    st.markdown('<div style="border-left: 4px solid #dc2626; background-color: #fef2f2; padding: 8px 12px; font-weight: 700; color: #991b1b; margin-bottom: 12px; border-radius: 0 4px 4px 0;">4단계: 검사결과 추정 질환</div>', unsafe_allow_html=True)
    for item in interp.get("integration", []):
        st.markdown(f'<div style="color: #1e293b; font-size: 0.95rem; line-height: 1.6; margin-bottom: 8px; padding-left: 10px;">{html_escape(item)}</div>', unsafe_allow_html=True)
    st.markdown("<br/>", unsafe_allow_html=True)

    if interp.get("differential"):
        st.markdown('<div style="border-left: 4px solid #9333ea; background-color: #faf5ff; padding: 8px 12px; font-weight: 700; color: #6b21a8; margin-bottom: 8px; border-radius: 0 4px 4px 0;">감별진단 가이드</div>', unsafe_allow_html=True)
        for item in interp.get("differential"):
            st.markdown(f'<div style="color: #4c1d95; font-size: 0.9rem; margin-bottom: 6px; padding-left: 10px;">• {html_escape(item)}</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

def render_input_learning():
    st.markdown("<style> .main-title { font-size: 1.5rem; font-weight: 800; color: #1e293b; margin-bottom: 1rem; } </style>", unsafe_allow_html=True)
    st.markdown('<div class="main-title">가상 결과표 판독 학습</div>', unsafe_allow_html=True)

    if "input_reset_counter" not in st.session_state: st.session_state["input_reset_counter"] = 0
    selected = st.radio("학습할 가상 결과표 선택", ["선택 안 함"] + list(VIRTUAL_REPORTS.keys()), key=f"sel_{st.session_state['input_reset_counter']}")

    if selected == "선택 안 함":
        st.info("결과표를 선택하고 하단의 영문 전환 토글을 활용해 실전 임상 판독을 연습하세요.")
        render_bottom_navigation()
        return

    st.markdown('<div style="margin-top:15px; margin-bottom: 10px; font-weight: 700;">결과표 언어 모드 선택</div>', unsafe_allow_html=True)
    to_eng = (st.radio("모드", ["한글 (기초 개념학습용)", "영문 (임상 실전용)"], horizontal=True, label_visibility="collapsed") == "영문 (임상 실전용)")

    report = VIRTUAL_REPORTS[selected]
    meta = report["meta"]
    
    st.markdown(
        clean_html(
            f"""
            <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 15px; margin-bottom: 15px;">
                <div style="font-size: 1.1rem; font-weight: 800; color: #1e293b; margin-bottom: 8px;">환자 기본 정보</div>
                <div style="font-size: 0.9rem; color: #475569; margin-bottom: 8px;">
                    <b>연령/성별:</b> {html_escape(str(meta.get("age", "-")))} / {html_escape(translate_value(meta.get("sex", "-"), to_eng))} &nbsp;|&nbsp; 
                    <b>병변측:</b> {html_escape(translate_value(meta.get("side", "-"), to_eng))}
                </div>
                <div style="font-size: 0.9rem; color: #334155; line-height: 1.5;"><b>주요 임상 증상:</b> {html_escape(meta.get("chief", ""))}</div>
            </div>
            """
        ), unsafe_allow_html=True
    )

    st.markdown('<div style="margin-top: 25px; padding-top: 15px; border-top: 2px dashed #e2e8f0;">', unsafe_allow_html=True)
    _render_tables(report, to_eng)
    st.markdown('</div>', unsafe_allow_html=True)

    # 항상 한글로 해석 출력 (to_eng 안 넘김)
    _render_interpretation(report)

    st.markdown('<div style="margin-top:30px;">', unsafe_allow_html=True)
    if st.button("다른 결과표 분석", type="secondary", use_container_width=True):
        st.session_state["input_reset_counter"] += 1
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    render_bottom_navigation()
