# ui/input_learning.py

import html
import streamlit as st
from ui.navigation import render_bottom_navigation
from data.report_terms import REPORT_LANG_KO, REPORT_LANG_EN, LANGUAGE_OPTIONS, normalize_report_language, translate_term
from data.virtual_reports import VIRTUAL_REPORTS, get_report_section_name

def get_input_learning_report_language() -> str:
    selected = st.radio(
        "검사결과표 출력 모드",
        options=LANGUAGE_OPTIONS,
        index=0,
        horizontal=True,
        label_visibility="collapsed",
        key="input_learning_lang"
    )
    return normalize_report_language(selected)

def get_result_color_style(value: str) -> str:
    text = str(value)
    abnormal_words = ["비정상", "감소", "지연", "소실", "탈신경", "측정불가", "Abnormal", "Reduced", "Absent", "Delayed", "전도차단"]
    normal_words = ["정상", "Normal", "Silent"]
    
    if any(w in text for w in abnormal_words):
        return "color: #991b1b; font-weight: 700;"
    if any(w in text for w in normal_words):
        return "color: #15803d; font-weight: 700;"
    return ""

def create_responsive_table(headers: list, rows: list, table_id: str) -> str:
    if not rows: return ""
    safe_table_id = html.escape(str(table_id), quote=True)
    css = f"""
    <style>
        #{safe_table_id} {{ width: 100%; border-collapse: collapse; margin-bottom: 16px; font-size: 0.9rem; }}
        #{safe_table_id} th {{ background-color: #f8fafc; padding: 10px; border-bottom: 2px solid #cbd5e1; text-align: left; color: #1e293b; font-weight: 700; }}
        #{safe_table_id} td {{ padding: 10px; border-bottom: 1px solid #e2e8f0; text-align: left; color: #334155; }}
        #{safe_table_id} td.fst-col {{ font-weight: 700; color: #1e40af; }}
        @media screen and (max-width: 768px) {{
            #{safe_table_id} thead {{ display: none; }}
            #{safe_table_id} tr {{ display: block; border: 1px solid #e2e8f0; border-radius: 8px; margin-bottom: 12px; background: #ffffff; padding: 6px; }}
            #{safe_table_id} td {{ display: flex; justify-content: space-between; align-items: center; gap: 12px; border-bottom: 1px solid #f1f5f9; padding: 8px 10px; text-align: right; }}
            #{safe_table_id} td:last-child {{ border-bottom: none; }}
            #{safe_table_id} td::before {{ content: attr(data-label); font-weight: 700; color: #475569; text-align: left; font-size: 0.8rem; flex: 0 0 35%; }}
            #{safe_table_id} td > span {{ flex: 1; text-align: right; word-break: keep-all; font-weight: 400; }}
            #{safe_table_id} td.fst-col {{ justify-content: center; background: #f8fafc; border-radius: 6px 6px 0 0; text-align: center; padding: 10px; }}
            #{safe_table_id} td.fst-col::before {{ content: none; }}
            #{safe_table_id} td.fst-col > span {{ text-align: center; font-weight: 700; }}
        }}
    </style>
    """
    header_html = "".join([f"<th>{html.escape(h)}</th>" for h in headers])
    tr_html = ""
    for row in rows:
        td_html = ""
        for idx, col in enumerate(row):
            raw_col = str(col)
            cls = "fst-col" if idx == 0 else ""
            color_style = get_result_color_style(raw_col) if idx == len(row) - 1 else ""
            header_label = html.escape(headers[idx]) if idx < len(headers) else ""
            td_html += f"<td data-label='{header_label}' class='{cls}' style='{color_style}'><span>{html.escape(raw_col)}</span></td>"
        tr_html += f"<tr>{td_html}</tr>"
    return f"{css}<table id='{safe_table_id}'><thead><tr>{header_html}</tr></thead><tbody>{tr_html}</tbody></table>"

def render_input_learning():
    st.markdown('<div class="main-title">가상 검사결과표 해석 모드</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtle">실제 임상과 유사한 양측 비교 데이터를 통해 정상과 비정상을 감별하고 병변 위치를 추론합니다.</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">🌐 검사표 언어 모드 선택</div>', unsafe_allow_html=True)
    selected_language = get_input_learning_report_language()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">📋 학습할 가상 검사결과표 선택</div>', unsafe_allow_html=True)
    
    if "input_reset_counter" not in st.session_state:
        st.session_state["input_reset_counter"] = 0
        
    case_names = ["선택 안 함"] + list(VIRTUAL_REPORTS.keys())
    selected = st.radio("리스트", case_names, index=0, key=f"v_radio_{st.session_state['input_reset_counter']}", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

    if selected != "선택 안 함":
        render_virtual_report_inline(selected, selected_language)

    render_bottom_navigation()

def render_virtual_report_inline(case_name: str, language: str):
    data = VIRTUAL_REPORTS[case_name]
    lang = normalize_report_language(language)
    is_eng = lang == REPORT_LANG_EN

    st.markdown('<hr style="margin: 2rem 0; border-top: 2px dashed #cbd5e1;">', unsafe_allow_html=True)
    
    # 1. 환자 기본 정보
    info = data.get("info", {})
    st.markdown('<div class="info-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">환자 기본 정보</div>', unsafe_allow_html=True)
    st.markdown(f'<div><span class="item-label">연령/성별:</span><span class="item-content">{info.get("age")}세 / {info.get("sex")}</span></div>', unsafe_allow_html=True)
    st.markdown(f'<div><span class="item-label">병변 호소측:</span><span class="item-content">{translate_term(info.get("side"), lang) if is_eng else info.get("side")}</span></div>', unsafe_allow_html=True)
    st.markdown(f'<div style="margin-top:6px;"><span class="item-label">주요 증상:</span><span class="item-content">{info.get("symptom")}</span></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 2. 결과표 렌더링
    sen_headers = ["Nerve", "Side", "Amplitude", "Latency", "Interpretation"] if is_eng else ["검사 신경", "검사측", "진폭(Amp)", "잠복기(Lat)", "짧은 판독"]
    mot_headers = ["Nerve", "Stim Site", "Side", "Amplitude", "Latency", "Interpretation"] if is_eng else ["검사 신경", "자극 위치", "검사측", "진폭(Amp)", "잠복기(Lat)", "짧은 판독"]
    emg_headers = ["Muscle", "Segment", "Side", "Rest", "Volition", "Interpretation"] if is_eng else ["검사 근육", "해당 분절", "검사측", "휴식 시", "수의수축", "짧은 판독"]

    def _translate_matrix(matrix):
        return [[translate_term(c, lang) for c in row] for row in matrix] if is_eng else matrix

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">⚡ 전기진단검사 결과표 (양측 비교 데이터)</div>', unsafe_allow_html=True)
    
    st.markdown(f'<div class="item-label" style="margin-top:10px;">{get_report_section_name("sensory", lang)}</div>', unsafe_allow_html=True)
    st.markdown(create_responsive_table(sen_headers, _translate_matrix(data.get("ncs_sensory", [])), "v_sen"), unsafe_allow_html=True)

    st.markdown(f'<div class="item-label" style="margin-top:10px;">{get_report_section_name("motor", lang)}</div>', unsafe_allow_html=True)
    st.markdown(create_responsive_table(mot_headers, _translate_matrix(data.get("ncs_motor", [])), "v_mot"), unsafe_allow_html=True)

    st.markdown(f'<div class="item-label" style="margin-top:10px;">{get_report_section_name("emg", lang)}</div>', unsafe_allow_html=True)
    st.markdown(create_responsive_table(emg_headers, _translate_matrix(data.get("emg", [])), "v_emg"), unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 💡 학생용 침근전도 핵심 용어 가이드 (탈신경 vs 활동성 탈신경 명확화)
    st.markdown("""
    <div class="info-card" style="background:#f8fafc; border-left-color:#94a3b8; margin-bottom:1rem;">
        <div class="item-label" style="color:#475569; font-size:1rem; margin-bottom:8px;">💡 학생을 위한 침근전도(EMG) 용어 가이드</div>
        <div style="margin-bottom:6px;"><span class="item-label" style="font-size:0.9rem; color:#475569;">탈신경 (Denervation):</span> <span class="item-content" style="font-size:0.9rem;">신경 지배가 끊어지거나 마비된 상태를 통칭하는 넓은 의미의 단어입니다.</span></div>
        <div style="margin-bottom:6px;"><span class="item-label" style="font-size:0.9rem; color:#b91c1c;">활동성 탈신경 (Active Denervation):</span> <span class="item-content" style="font-size:0.9rem;">최근에 신경이 손상되어, 지배를 잃은 근육 섬유가 불안정해져 스스로 미세하게 떠는 상태(섬유자발전위, 양성예파)입니다. <b>현재 신경 손상이 활발히 진행 중임</b>을 뜻합니다.</span></div>
        <div style="margin-bottom:6px;"><span class="item-label" style="font-size:0.9rem; color:#c2410c;">만성 재신경지배 (Chronic Reinnervation):</span> <span class="item-content" style="font-size:0.9rem;">손상 후 시간이 흘러, 주변 건강한 신경이 가지를 뻗어 도와주는 상태(거대운동단위)입니다. <b>회복을 시도하는 만성기</b>를 뜻합니다.</span></div>
        <div><span class="item-label" style="font-size:0.9rem; color:#0f766e;">동원 감소 (Reduced Recruitment):</span> <span class="item-content" style="font-size:0.9rem;">힘을 줄 때 동원되는 운동단위 숫자가 줄어든 것으로, 신경 지배가 끊어진 <b>최종 결과적 마비 상태</b>를 의미합니다.</span></div>
    </div>
    """, unsafe_allow_html=True)

    # 3. 데이터 해석 논리 (세분화)
    teaching = data.get("teaching_diagnosis", {})
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-label" style="color:#16a34a;">교육용 데이터 해석 및 통합 추론</div>', unsafe_allow_html=True)
    
    st.markdown(f'<div style="background:#fff1f2; padding:10px; border-radius:8px; margin-bottom:12px;"><span class="item-label" style="color:#991b1b;">최종 진단:</span><span style="font-weight:700; color:#991b1b;">{teaching.get("summary")}</span></div>', unsafe_allow_html=True)

    if "ncs_reason" in teaching:
        st.markdown('<div class="item-label">1. 신경전도검사(NCS) 수치 해석</div>', unsafe_allow_html=True)
        for r in teaching["ncs_reason"]:
            st.markdown(f'<div style="margin-left:8px; margin-bottom:6px; color:#334155;">- {r}</div>', unsafe_allow_html=True)

    if "emg_reason" in teaching:
        st.markdown('<div class="item-label" style="margin-top:10px;">2. 침근전도검사(EMG) 소견 해석</div>', unsafe_allow_html=True)
        for r in teaching["emg_reason"]:
            st.markdown(f'<div style="margin-left:8px; margin-bottom:6px; color:#334155;">- {r}</div>', unsafe_allow_html=True)

    if "integration" in teaching:
        st.markdown('<div class="item-label" style="margin-top:10px;">3. 임상 통합 결론</div>', unsafe_allow_html=True)
        for r in teaching["integration"]:
            st.markdown(f'<div style="margin-left:8px; margin-bottom:6px; font-weight:600; color:#1e40af;">👉 {r}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 4. 감별 진단
    if "differential_diagnosis" in data:
        st.markdown('<div class="section-card" style="border-left: 4px solid #7e22ce;">', unsafe_allow_html=True)
        st.markdown('<div class="section-label" style="color:#7e22ce; border-bottom-color:#e9d5ff;">유사 질환과의 감별 진단 (Differential Diagnosis)</div>', unsafe_allow_html=True)
        
        for ddx in data["differential_diagnosis"]:
            st.markdown(f"""
            <div class="ddx-box">
                <div class="ddx-title">질환명: {ddx.get('name')}</div>
                <div style="margin-bottom: 6px;"><span class="item-label" style="color: #581c87;">감별이 필요한 이유:</span><span class="item-content">{ddx.get('why_consider')}</span></div>
                <div><span class="item-label" style="color: #581c87;">데이터 감별 포인트:</span><span class="item-content">{ddx.get('how_to_differentiate')}</span></div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

def app():
    pass
