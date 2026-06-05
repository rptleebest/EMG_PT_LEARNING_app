# ui/input_learning.py

import streamlit as st
from ui.navigation import render_bottom_navigation
from formatters import html_escape, clean_html
from data.virtual_reports import VIRTUAL_REPORTS, translate_value

def _value_class(value):
    text = str(value)
    abnormal_tokens = [
        "반응 소실", "소실", "지연", "감소", "느림", "전도차단", "증가", 
        "Absent", "Delayed", "Reduced", "No Response", 
        "fibrillation", "positive sharp", "Reduced MU recruitment", "Giant"
    ]
    normal_tokens = ["Silent", "Normal", "정상", "보존", "Normal Range"]

    if any(token in text for token in abnormal_tokens): return "text-red"
    if any(token in text for token in normal_tokens): return "text-blue"
    return "text-normal"

def _render_mobile_table(headers, rows, table_id, to_eng):
    safe_table_id = html_escape(table_id)
    translated_headers = [translate_value(h, to_eng) for h in headers]

    css = f"""
    <style>
        #{safe_table_id} {{ width: 100%; border-collapse: collapse; margin: 0.55rem 0 1rem 0; font-size: 0.84rem; background: #ffffff; }}
        #{safe_table_id} th {{ background-color: #f1f5f9; padding: 0.62rem 0.5rem; border: 1px solid #cbd5e1; text-align: center; color: #0f172a; font-weight: 850; line-height: 1.35; }}
        #{safe_table_id} td {{ padding: 0.58rem 0.5rem; border: 1px solid #e2e8f0; text-align: center; color: #334155; line-height: 1.45; }}
        #{safe_table_id} td.left-align {{ text-align: left; font-weight: 800; color: #1e3a8a; }}
        @media screen and (max-width: 700px) {{
            #{safe_table_id} thead {{ display: none; }}
            #{safe_table_id} tr {{ display: block; border: 1px solid #dbeafe; border-radius: 10px; margin-bottom: 0.8rem; background: #ffffff; overflow: hidden; }}
            #{safe_table_id} td {{ display: flex; justify-content: space-between; align-items: flex-start; gap: 0.75rem; border: none; border-bottom: 1px solid #f1f5f9; padding: 0.55rem 0.65rem; text-align: right; }}
            #{safe_table_id} td:last-child {{ border-bottom: none; }}
            #{safe_table_id} td::before {{ content: attr(data-label); font-weight: 850; color: #475569; text-align: left; font-size: 0.78rem; flex: 0 0 38%; }}
            #{safe_table_id} td > span {{ flex: 1; text-align: right; word-break: keep-all; }}
            #{safe_table_id} td.left-align {{ display: block; background: #eff6ff; text-align: left; padding: 0.7rem 0.75rem; color: #1e3a8a; font-weight: 900; }}
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


def _render_patient_summary(title, report, to_eng):
    meta = report["meta"]
    sex_disp = translate_value(meta.get("sex", "-"), to_eng)
    side_disp = translate_value(meta.get("side", "-"), to_eng)

    st.markdown(
        clean_html(
            f"""
            <div class="info-card">
                <div class="case-title-mobile">👤 {html_escape(title)}</div>
                <div class="case-subtitle-mobile">
                    <span class="label-strong">연령/성별:</span> <span class="result-value">{html_escape(meta.get("age", "-"))} / {html_escape(sex_disp)}</span>
                    &nbsp;|&nbsp; <span class="label-strong">병변측:</span> <span class="result-value">{html_escape(side_disp)}</span>
                </div>
                <div class="case-text-block" style="margin-top:0.8rem;">
                    <div class="case-bullet"><span class="label-strong">주요 임상 정보:</span><span class="result-value"> {html_escape(meta.get("chief", ""))}</span></div>
                    {f'<div class="case-bullet"><span class="label-strong text-blue">판독 힌트:</span><span class="result-value"> {html_escape(meta.get("clinical_hint", ""))}</span></div>' if meta.get("clinical_hint") else ""}
                </div>
            </div>
            """
        ), unsafe_allow_html=True
    )


def _render_reading_guide():
    st.markdown(
        clean_html(
            """
            <div class="warn-card">
                <div class="finding-highlight" style="color:#b45309;">🎓 실제형 결과표 판독 순서</div>
                <div class="case-bullet">1. <b>감각신경전도검사(SNAP)</b>: 정상측 대비 진폭 보존 여부 확인(보존=신경뿌리, 감소=말초신경).</div>
                <div class="case-bullet">2. <b>운동신경전도검사(CMAP)</b>: 원위잠복기 지연, 자극 위치별 국소 전도차단 여부 확인.</div>
                <div class="case-bullet">3. <b>침근전도검사(Needle EMG)</b>: 서로 다른 말초신경이나 동일 척수 분절을 공유하는 근육군의 동시 침범 확인.</div>
            </div>
            """
        ), unsafe_allow_html=True
    )


def _render_tables(report, to_eng):
    if report.get("sensory_ncs"):
        st.markdown('<div class="finding-highlight">⚡ 감각신경전도검사(Sensory NCS, SNAP)</div>', unsafe_allow_html=True)
        rows = [[r.get("nerve", ""), r.get("side", ""), r.get("recording", ""), r.get("stimulation", ""), r.get("amplitude", ""), r.get("latency", ""), r.get("velocity", "")] for r in report["sensory_ncs"]]
        st.markdown(_render_mobile_table(["검사 신경", "측", "기록 위치", "자극 위치", "진폭", "잠복기", "전도속도"], rows, "sensory_table", to_eng), unsafe_allow_html=True)

    if report.get("motor_ncs"):
        st.markdown('<div class="finding-highlight">⚡ 운동신경전도검사(Motor NCS, CMAP)</div>', unsafe_allow_html=True)
        rows = [[r.get("nerve", ""), r.get("side", ""), r.get("recording", ""), r.get("stimulation", ""), r.get("amplitude", ""), r.get("latency", ""), r.get("velocity", "")] for r in report["motor_ncs"]]
        st.markdown(_render_mobile_table(["검사 신경", "측", "기록 근육", "자극 위치", "진폭", "잠복기", "전도속도"], rows, "motor_table", to_eng), unsafe_allow_html=True)

    if report.get("late_response"):
        st.markdown('<div class="finding-highlight">⏱️ 후기반응 / 반사 검사</div>', unsafe_allow_html=True)
        rows = [[r.get("test", ""), r.get("side", ""), r.get("latency", ""), r.get("amplitude", "")] for r in report["late_response"]]
        st.markdown(_render_mobile_table(["검사 항목", "측", "잠복기", "진폭"], rows, "late_table", to_eng), unsafe_allow_html=True)

    if report.get("needle_emg"):
        st.markdown('<div class="finding-highlight">🪡 침근전도검사(Needle EMG)</div>', unsafe_allow_html=True)
        rows = [[r.get("muscle", ""), r.get("root", ""), r.get("nerve", ""), r.get("rest", ""), r.get("volition", "")] for r in report["needle_emg"]]
        st.markdown(_render_mobile_table(["검사 근육", "분절", "말초신경", "휴식 시 반응", "수의수축 시 반응"], rows, "emg_table", to_eng), unsafe_allow_html=True)


def _render_interpretation(report):
    interpretation = report["interpretation"]
    st.markdown('<div class="result-card"><div class="result-title">✅ 검사 결과 통합 해석</div>', unsafe_allow_html=True)
    st.markdown(
        clean_html(
            f"""
            <div class="case-text-block" style="background:#fff1f2!important; border-left-color:#fecdd3!important; margin-bottom: 15px;">
                <div class="case-bullet"><span class="label-strong text-red">최종 의심 진단:</span> <span class="result-value text-red" style="font-weight:800!important;">{html_escape(report.get("diagnosis", ""))}</span></div>
                <div class="case-bullet"><span class="label-strong">추정 손상 위치:</span> <span class="result-value"> {html_escape(report.get("lesion", ""))}</span></div>
            </div>
            """
        ), unsafe_allow_html=True
    )

    sections = [
        ("sensory", "1단계: 감각신경전도 해석", "#3b82f6", "#eff6ff"), ("motor", "2단계: 운동/반사검사 해석", "#0f766e", "#f0fdfa"),
        ("emg", "3단계: 침근전도 해석", "#d97706", "#fffbeb"), ("integration", "4단계: 종합 판독 추정", "#dc2626", "#fff1f2"),
        ("differential", "감별진단 가이드", "#9333ea", "#fdf4ff"), ("additional", "물리치료 교육 포인트", "#15803d", "#f0fdf4"),
    ]

    for key, title, b_color, bg_color in sections:
        items = interpretation.get(key) or interpretation.get(key.replace("differential", "ddx").replace("integration", "integrated").replace("additional", "additional_tests"), [])
        if not items: continue
        st.markdown(f'<div class="result-label" style="border-left-color:{b_color}!important; background:{bg_color}!important;">{title}</div>', unsafe_allow_html=True)
        for item in items: st.markdown(f'<div class="result-text">• {html_escape(item)}</div>', unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

def render_input_learning():
    st.markdown(
        "<style>.case-text-block, .result-text, .case-bullet { text-align: justify !important; text-justify: inter-word !important; line-height: 1.6 !important; }</style>",
        unsafe_allow_html=True
    )
    st.markdown('<div class="main-title">가상 결과표 판독학습</div>', unsafe_allow_html=True)

    if "input_reset_counter" not in st.session_state: st.session_state["input_reset_counter"] = 0
    st.markdown('<div class="section-card"><div class="case-section-label">📋 학습할 가상 결과표 선택</div>', unsafe_allow_html=True)
    selected = st.radio("리스트", ["선택 안 함"] + list(VIRTUAL_REPORTS.keys()), key=f"sel_{st.session_state['input_reset_counter']}", label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)

    if selected == "선택 안 함":
        st.markdown('<div class="info-card"><div class="finding-highlight">안내</div><div class="case-bullet">표를 선택하고 하단의 영문 전환 토글을 활용해 실전 임상 판독을 연습하세요.</div></div>', unsafe_allow_html=True)
        render_bottom_navigation()
        return

    st.markdown('<div class="section-card" style="padding-bottom:5px;"><div class="case-section-label">🌐 표 언어 모드 (한글/영문 토글)</div>', unsafe_allow_html=True)
    to_eng = (st.radio("모드", ["🇰🇷 한글 (기초 학습용)", "🇺🇸 영문 (임상 실전용)"], horizontal=True, label_visibility="collapsed") == "🇺🇸 영문 (임상 실전용)")
    st.markdown("</div>", unsafe_allow_html=True)

    report = VIRTUAL_REPORTS[selected]
    _render_patient_summary(selected, report, to_eng)
    _render_reading_guide()

    st.markdown('<div class="section-card"><div class="case-section-label">📋 실제형 결과표 데이터</div>', unsafe_allow_html=True)
    _render_tables(report, to_eng)
    st.markdown("</div>", unsafe_allow_html=True)

    _render_interpretation(report)

    st.markdown('<div class="start-button-wrap">', unsafe_allow_html=True)
    if st.button("🔄 다른 결과표 분석", type="secondary", use_container_width=True):
        st.session_state["input_reset_counter"] += 1
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    render_bottom_navigation()
