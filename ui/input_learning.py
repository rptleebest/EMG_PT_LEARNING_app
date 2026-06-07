# ui/input_learning.py

import html
import streamlit as st
from ui.navigation import render_bottom_navigation
from data.report_terms import REPORT_LANG_KO, REPORT_LANG_EN, LANGUAGE_OPTIONS, normalize_report_language, translate_term
from data.virtual_reports import VIRTUAL_REPORTS, get_report_section_name

def get_input_learning_report_language() -> str:
    selected = st.radio("모드", options=LANGUAGE_OPTIONS, index=0, horizontal=True, label_visibility="collapsed", key="v_lang")
    return normalize_report_language(selected)

def get_result_color_style(value: str) -> str:
    text = str(value)
    if any(w in text for w in ["비정상", "감소", "지연", "소실", "탈신경", "측정불가", "차단", "Abnormal", "Reduced", "Absent", "Delayed"]): return "color: #991b1b; font-weight: 700;"
    if any(w in text for w in ["정상", "Normal", "Silent"]): return "color: #15803d; font-weight: 700;"
    return ""

def create_responsive_table(headers: list, rows: list, table_id: str) -> str:
    if not rows: return ""
    safe_id = html.escape(str(table_id))
    css = f"""<style>#{safe_id} {{ width: 100%; border-collapse: collapse; margin-bottom: 12px; font-size: 0.9rem; }} #{safe_id} th {{ background-color: #f8fafc; padding: 10px; border-bottom: 2px solid #cbd5e1; text-align: left; color: #1e293b; font-weight: 700; }} #{safe_id} td {{ padding: 10px; border-bottom: 1px solid #e2e8f0; text-align: left; color: #334155; }} #{safe_id} td.fst-col {{ font-weight: 700; color: #1e40af; }} @media screen and (max-width: 768px) {{ #{safe_id} thead {{ display: none; }} #{safe_id} tr {{ display: block; border: 1px solid #e2e8f0; border-radius: 8px; margin-bottom: 12px; background: #ffffff; padding: 6px; }} #{safe_id} td {{ display: flex; justify-content: space-between; align-items: center; gap: 12px; border-bottom: 1px solid #f1f5f9; padding: 8px 10px; text-align: right; }} #{safe_id} td:last-child {{ border-bottom: none; }} #{safe_id} td::before {{ content: attr(data-label); font-weight: 700; color: #475569; text-align: left; font-size: 0.8rem; flex: 0 0 35%; }} #{safe_id} td > span {{ flex: 1; text-align: right; word-break: keep-all; font-weight: 400; }} #{safe_id} td.fst-col {{ justify-content: center; background: #f8fafc; border-radius: 6px 6px 0 0; text-align: center; padding: 10px; }} #{safe_id} td.fst-col::before {{ content: none; }} #{safe_id} td.fst-col > span {{ text-align: center; font-weight: 700; }} }}</style>"""
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
    return f"{css}<table id='{safe_id}'><thead><tr>{header_html}</tr></thead><tbody>{tr_html}</tbody></table>"

def render_input_learning():
    st.markdown('<div class="main-title">가상 검사결과표 해석 모드</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtle">실제 양측 비교 데이터를 통해 병변 위치를 추론합니다.</div>', unsafe_allow_html=True)

    if "v_reset_counter" not in st.session_state: st.session_state["v_reset_counter"] = 0
    case_names = ["선택 안 함"] + list(VIRTUAL_REPORTS.keys())
    selected = st.radio("리스트", case_names, index=0, key=f"v_rad_{st.session_state['v_reset_counter']}", label_visibility="collapsed")

    if selected != "선택 안 함":
        # ⚙️ 검사표 직전에 언어 선택 위젯 배치
        st.markdown('<div style="margin-top:20px; margin-bottom:8px; font-weight:700; color:#475569;">⚙️ 검사결과표 언어 모드 변경</div>', unsafe_allow_html=True)
        selected_language = get_input_learning_report_language()
        render_virtual_report_inline(selected, selected_language)

    render_bottom_navigation()

def render_virtual_report_inline(case_name: str, language: str):
    data = VIRTUAL_REPORTS[case_name]
    lang = normalize_report_language(language)
    is_eng = lang == REPORT_LANG_EN

    st.markdown('<hr style="margin: 1.5rem 0; border-top: 2px dashed #cbd5e1;">', unsafe_allow_html=True)
    
    info = data.get("info", {})
    st.markdown('<div class="section-label" style="color:#0f172a;">환자 기본 정보</div>', unsafe_allow_html=True)
    st.markdown(f'<div><span class="inline-label">연령/성별:</span><span class="inline-content">{info.get("age")}세 / {info.get("sex")}</span></div>', unsafe_allow_html=True)
    side_val = translate_term(info.get("side"), lang) if is_eng else info.get("side")
    st.markdown(f'<div><span class="inline-label">병변 호소측:</span><span class="inline-content">{side_val}</span></div>', unsafe_allow_html=True)
    st.markdown(f'<div style="margin-top:8px;"><span class="inline-label">주요 증상:</span><span class="inline-content">{info.get("symptom")}</span></div>', unsafe_allow_html=True)
    
    st.markdown('<hr style="margin: 1.2rem 0; border-top: 1px dotted #cbd5e1;">', unsafe_allow_html=True)

    sen_hdrs = ["Nerve", "Side", "Amplitude", "Latency", "Interpretation"] if is_eng else ["검사 신경", "검사측", "진폭", "잠복기", "판독"]
    mot_hdrs = ["Nerve", "Stim Site", "Side", "Amplitude", "Latency", "Interpretation"] if is_eng else ["검사 신경", "자극 위치", "검사측", "진폭", "잠복기", "판독"]
    emg_hdrs = ["Muscle", "Segment", "Side", "Rest", "Volition", "Interpretation"] if is_eng else ["검사 근육", "분절", "검사측", "휴식 시", "수의수축", "판독"]

    def _tr(mat): return [[translate_term(c, lang) for c in row] for row in mat] if is_eng else mat

    st.markdown('<div class="section-label" style="color:#0f172a;">⚡ 전기진단검사 결과표 (양측 비교)</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="item-title">{get_report_section_name("sensory", lang)}</div>', unsafe_allow_html=True)
    st.markdown(create_responsive_table(sen_hdrs, _tr(data.get("ncs_sensory", [])), "v_sen"), unsafe_allow_html=True)
    st.markdown(f'<div class="item-title">{get_report_section_name("motor", lang)}</div>', unsafe_allow_html=True)
    st.markdown(create_responsive_table(mot_hdrs, _tr(data.get("ncs_motor", [])), "v_mot"), unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#f8fafc; padding:10px; border-left:3px solid #94a3b8; margin-top:16px; margin-bottom:8px;">
        <div style="font-weight:700; color:#475569; font-size:0.95rem; margin-bottom:4px;">💡 학생용 침근전도 용어 가이드</div>
        <div style="font-size:0.9rem; line-height:1.4;"><span style="color:#b91c1c; font-weight:700;">활동성 탈신경:</span> <b>현재 진행 중인</b> 신경 손상 (자발전위 관찰)</div>
        <div style="font-size:0.9rem; line-height:1.4;"><span style="color:#c2410c; font-weight:700;">만성 재신경지배:</span> 회복을 시도하는 <b>만성기</b> (거대운동단위 관찰)</div>
        <div style="font-size:0.9rem; line-height:1.4;"><span style="color:#0f766e; font-weight:700;">동원 감소:</span> 신경이 끊어져 <b>마비된 최종 결과</b></div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(f'<div class="item-title">{get_report_section_name("emg", lang)}</div>', unsafe_allow_html=True)
    st.markdown(create_responsive_table(emg_hdrs, _tr(data.get("emg", [])), "v_emg"), unsafe_allow_html=True)

    teaching = data.get("teaching_diagnosis", {})
    
    with st.expander("🔍 검사 수치 해석 및 생리학적 논리 보기"):
        if "ncs_reason" in teaching:
            st.markdown('<div class="item-title" style="color:#16a34a; margin-top:0;">신경전도검사(NCS) 수치 해석</div>', unsafe_allow_html=True)
            for r in teaching["ncs_reason"]: st.markdown(f'<div class="inline-content">{r}</div>', unsafe_allow_html=True)
        if "emg_reason" in teaching:
            st.markdown('<div class="item-title" style="color:#16a34a;">침근전도검사(EMG) 소견 해석</div>', unsafe_allow_html=True)
            for r in teaching["emg_reason"]: st.markdown(f'<div class="inline-content">{r}</div>', unsafe_allow_html=True)

    st.markdown('<hr style="margin: 1.2rem 0; border-top: 1px dotted #cbd5e1;">', unsafe_allow_html=True)

    st.markdown('<div class="section-label" style="color:#1e40af;">최종 임상 통합 추론</div>', unsafe_allow_html=True)
    if "integration" in teaching:
        for r in teaching["integration"]: st.markdown(f'<div class="inline-content">{r}</div>', unsafe_allow_html=True)
    st.markdown(f'<div style="background:#fff1f2; padding:10px; margin-top:8px; border-radius:4px;"><span class="inline-label" style="color:#991b1b;">최종 진단명:</span><span class="inline-content" style="font-weight:700; color:#991b1b;">{teaching.get("summary")}</span></div>', unsafe_allow_html=True)

    if "differential_diagnosis" in data:
        st.markdown('<div class="section-label" style="color:#7e22ce; margin-top:24px;">유사 질환과의 감별 진단</div>', unsafe_allow_html=True)
        for ddx in data["differential_diagnosis"]:
            st.markdown(f"""
            <div class="ddx-box">
                <div class="ddx-title">{ddx.get('name')}</div>
                <span class="ddx-label">감별이 필요한 이유:</span>
                <div class="ddx-content">{ddx.get('why_consider')}</div>
                <span class="ddx-label">데이터 감별 포인트:</span>
                <div class="ddx-content">{ddx.get('how_to_differentiate')}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div style="height: 16px;"></div>', unsafe_allow_html=True)
    if st.button("👆 다른 검사결과표 선택하기 (초기화 및 위로 이동)", type="primary"):
        st.session_state["v_reset_counter"] += 1
        st.rerun()

def app(): pass
