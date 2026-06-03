# ui/case_learning.py

import re
import streamlit as st
from data.cases import CASE_LIBRARY
from ui.navigation import render_bottom_navigation

def split_findings_by_domain(findings):
    grouped = {"sensory": {}, "motor": {}, "muscle": {}, "reflex": {}}
    for item, vals in findings.items():
        name = item.lower()
        if "snap" in name or "감각" in name: grouped["sensory"][item] = vals
        elif "cmap" in name or "운동" in name: grouped["motor"][item] = vals
        elif "반사" in name or "f파" in name or "r1" in name or "r2" in name or "h/m" in name or "blink" in name: grouped["reflex"][item] = vals
        else: grouped["muscle"][item] = vals
    return grouped

def format_eng_term(text):
    if not text: return ""
    text = str(text).replace(", ", "<br>")
    def repl(m):
        kor = m.group(1).strip()
        eng = m.group(2).strip().lower()
        acronyms = ["snap", "cmap", "muap", "muaps", "ncs", "emg", "mas", "drt", "umn", "lmn", "ta", "ecr", "eip", "adm", "fdi", "ehl", "pl"]
        for ac in acronyms:
            eng = re.sub(rf"\b{ac}\b", ac.upper(), eng)
        return f"{kor}<br><span class='title-eng'>{eng}</span>"
    return re.sub(r"([가-힣a-zA-Z0-9\s/]+)\s*\((.*?)\)", repl, text)

def _get_ncs_row(lbl, val, is_bad=False):
    color = "text-red" if is_bad else "text-blue"
    return f'<div class="result-row"><div class="lbl">{lbl}</div><div class="val {color}">{val}</div></div>'

def _get_ncs_line_text(raw_val):
    if raw_val == "ncs_delayed": return _get_ncs_row("진폭", "정상 범위") + _get_ncs_row("잠복기", "지연", True)
    elif raw_val == "ncs_reduced": return _get_ncs_row("진폭", "감소", True) + _get_ncs_row("잠복기", "정상 범위")
    elif raw_val == "ncs_absent": return _get_ncs_row("진폭", "반응 소실", True) + _get_ncs_row("잠복기", "반응 소실", True)
    else: return _get_ncs_row("진폭", "정상 범위") + _get_ncs_row("잠복기", "정상 범위")

def _get_emg_line_text(raw_val):
    if raw_val in ["emg_active_denervation", "emg_paraspinal_denervation"]:
        vol = "reduced MU recruitment" if raw_val == "emg_active_denervation" else "통증으로 인해 평가불가"
        return _get_ncs_row("휴식 시", format_eng_term("섬유자발전위, 양성예파(fibrillation potential, positive sharp wave)"), True) + _get_ncs_row("수의적 수축 시", format_eng_term(f"동원 감소({vol})"), True)
    elif raw_val == "emg_chronic_reinnervation":
        return _get_ncs_row("휴식 시", format_eng_term("전기적 침묵(silent at rest)")) + _get_ncs_row("수의적 수축 시", format_eng_term("거대 운동단위 출현 및 동원 감소(giant MUAPs, reduced MU recruitment)"), True)
    elif raw_val == "emg_active_chronic":
        return _get_ncs_row("휴식 시", format_eng_term("섬유자발전위, 양성예파(fibrillation potential, positive sharp wave)"), True) + _get_ncs_row("수의적 수축 시", format_eng_term("거대 운동단위 출현 및 동원 감소(giant MUAPs, reduced MU recruitment)"), True)
    elif raw_val == "emg_fasciculation":
        return _get_ncs_row("휴식 시", format_eng_term("근육다발수축전위(fasciculation potential)"), True) + _get_ncs_row("수의적 수축 시", format_eng_term("동원 감소(reduced MU recruitment)"), True)
    else:
        return _get_ncs_row("휴식 시", format_eng_term("전기적 침묵(silent at rest)")) + _get_ncs_row("수의적 수축 시", format_eng_term("정상 동원(normal MU recruitment)"))

def _get_reflex_line_text(raw_val):
    if raw_val == "fwave_delayed_absent": return "지연/부재"
    elif raw_val == "blink_delayed": return "R1/R2 지연"
    elif raw_val == "blink_delayed_absent": return "R2 유발 소실"
    elif raw_val == "h_reflex_hyperactive": return "진폭 항진"
    elif raw_val == "h_m_ratio_increased": return "비율 증가"
    elif raw_val in ["ncs_normal", "정상 범위"]: return "정상 범위"
    return raw_val

def _render_finding_block(title, findings, side):
    if not findings: return
    st.markdown(f'<div class="case-section-label">{format_eng_term(title)}</div>', unsafe_allow_html=True)
    block_parts = []
    items = list(findings.items())
    for idx, (item, values) in enumerate(items):
        left = values[0] if len(values) > 0 else ""
        right = values[1] if len(values) > 1 else ""
        lines = [f'<div class="finding-highlight">{format_eng_term(item)}</div>']
        pathological_val = right if side in ["오른쪽", "우"] else left
        raw_val = str(pathological_val).strip()

        if side in ["양쪽", "양측"]:
            raw_left, raw_right = str(left).strip(), str(right).strip()
            if "감각" in title or "운동" in title:
                left_text, right_text = _get_ncs_line_text(raw_left), _get_ncs_line_text(raw_right)
            elif "침근전도" in title:
                left_text, right_text = _get_emg_line_text(raw_left), _get_emg_line_text(raw_right)
            else:
                left_text, right_text = _get_ncs_row("판독", _get_reflex_line_text(raw_left)), _get_ncs_row("판독", _get_reflex_line_text(raw_right))
            lines.append(f'<div style="background:#f8fafc; padding:8px; border-radius:6px; margin-bottom:4px;"><div class="lbl">좌측:</div>{left_text}</div>')
            lines.append(f'<div style="background:#f8fafc; padding:8px; border-radius:6px;"><div class="lbl">우측:</div>{right_text}</div>')
        else:
            if "감각" in title or "운동" in title:
                lines.append(_get_ncs_line_text(raw_val))
            elif "침근전도" in title:
                lines.append(_get_emg_line_text(raw_val))
            else:
                norm_val = _get_reflex_line_text(raw_val)
                is_bad = norm_val != "정상 범위"
                lines.append(_get_ncs_row("판독 결과", norm_val, is_bad))
                if right and right not in ["ncs_normal", "NCS_NORMAL"]:
                    lines.append(_get_ncs_row("측정 데이터", right))

        block_parts.append(f'<div style="margin-bottom: 16px;">{"".join(lines)}</div>')
        if idx < len(items) - 1: block_parts.append('<hr style="border:none; border-top:1px dashed #e2e8f0; margin:12px 0;">')
    if block_parts: st.markdown(f'<div class="case-text-block">{"".join(block_parts)}</div>', unsafe_allow_html=True)

def render_case_list():
    st.markdown('<div class="main-title">사례 학습 모드</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtle">환자의 임상 증상과 근전도 소견을 실시간 비교 분석하여 임상적 판단력을 기릅니다.</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="case-section-label">{format_eng_term("학습할 가상 사례 선택(case selection)")}</div>', unsafe_allow_html=True)

    case_names = ["선택 안 함"] + list(CASE_LIBRARY.keys())
    if "case_reset_counter" not in st.session_state: st.session_state["case_reset_counter"] = 0
    dynamic_radio_key = f"case_radio_selector_{st.session_state['case_reset_counter']}"

    selected = st.radio("학습할 임상 증상 선택", case_names, key=dynamic_radio_key, label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

    if selected != "선택 안 함":
        case = CASE_LIBRARY[selected]
        patient, findings, teaching, diff_dx = case["patient"], case["findings"], case["teaching_diagnosis"], case["differential_diagnosis"]
        side = patient.get("side", "-").replace("우", "오른쪽").replace("좌", "왼쪽").replace("양측", "양쪽")

        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="lbl" style="font-size:1rem; margin-bottom:8px;">👤 환자 사례: {selected}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="val">연령/성별: {patient["age"]}세 / {patient["sex"]} &nbsp;|&nbsp; 병변측: {side}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown(f'<div class="case-section-label">{format_eng_term("주요 증상(chief complaint)")}</div>', unsafe_allow_html=True)
        symptoms_html = "".join([f'<div class="case-bullet">• {format_eng_term(s)}</div>' for s in patient.get("symptoms", [])])
        st.markdown(f'<div class="case-text-block">{symptoms_html}</div>', unsafe_allow_html=True)

        st.markdown(f'<div class="case-section-label">{format_eng_term("이학적 검사결과(physical examination)")}</div>', unsafe_allow_html=True)
        exam_html = []
        for sec_name, items in patient.get("physical_exam", {}).items():
            exam_html.append(f'<div class="finding-highlight">{format_eng_term(sec_name)}</div>')
            for i in items:
                parts = i.split(":", 1)
                if len(parts) == 2: exam_html.append(f'<div class="result-row"><div class="lbl">{format_eng_term(parts[0])}</div><div class="val">{format_eng_term(parts[1])}</div></div>')
                else: exam_html.append(f'<div class="case-bullet">• {format_eng_term(i)}</div>')
        st.markdown(f'<div class="case-text-block">{"".join(exam_html)}</div>', unsafe_allow_html=True)

        grouped = split_findings_by_domain(findings)
        if grouped["sensory"]: _render_finding_block("감각신경전도검사(sensory NCS)", grouped["sensory"], side)
        if grouped["motor"]: _render_finding_block("운동신경전도검사(motor NCS)", grouped["motor"], side)
        if grouped["muscle"] and "눈꺼풀" not in selected and "뇌졸중" not in selected: _render_finding_block("침근전도검사 소견(needle EMG)", grouped["muscle"], side)
        if grouped["reflex"] or grouped["other"]:
            merged = {**grouped["reflex"], **grouped["other"]}
            if "뇌졸중" in selected: _render_finding_block("H-반사 유발 및 경직 정량검사(h-reflex)", merged, side)
            elif "눈꺼풀" in selected: _render_finding_block("눈깜빡반사 회로 분석(blink reflex)", merged, side)
            else: _render_finding_block("반사 및 후기반응 소견(late response)", merged, side)

        st.markdown('<div class="diag-box">', unsafe_allow_html=True)
        # 교육용 진단 요약 글자 삭제, 진단명만 노출
        st.markdown(f'<div class="diag-name">{format_eng_term(teaching.get("summary",""))}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        if teaching.get("ncs_reason"):
            label = "눈깜박반사 해석 포인트" if ("눈꺼풀" in selected or "얼굴" in selected) else "H-반사 유발 해석 포인트" if "뇌졸중" in selected else "신경전도 해석 포인트"
            st.markdown(f'<div class="result-label">{label}</div>', unsafe_allow_html=True)
            for x in teaching["ncs_reason"]: st.markdown(f'<div class="case-bullet">• {format_eng_term(x)}</div>', unsafe_allow_html=True)
        if teaching.get("emg_reason"):
            if not ("Blink Reflex" in str(teaching["emg_reason"][0]) or "H-reflex" in str(teaching["emg_reason"][0]) or "눈꺼풀" in selected or "뇌졸중" in selected):
                st.markdown('<div class="result-label">침근전도 해석 포인트</div>', unsafe_allow_html=True)
                for x in teaching["emg_reason"]: st.markdown(f'<div class="case-bullet">• {format_eng_term(x)}</div>', unsafe_allow_html=True)
        if teaching.get("integration"):
            st.markdown('<div class="result-label">통합 해석</div>', unsafe_allow_html=True)
            for x in teaching["integration"]: st.markdown(f'<div class="case-bullet">• {format_eng_term(x)}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        if diff_dx:
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown(f'<div class="case-section-label">{format_eng_term("감별진단 포인트(differential diagnosis)")}</div>', unsafe_allow_html=True)
            for idx, d in enumerate(diff_dx):
                st.markdown(f'<div class="finding-highlight">{format_eng_term(d.get("name",""))}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="result-row"><div class="lbl">왜 고려하나</div><div class="val">{format_eng_term(d.get("why_consider",""))}</div></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="result-row"><div class="lbl">어떻게 구분하나</div><div class="val">{format_eng_term(d.get("how_to_differentiate",""))}</div></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="result-row"><div class="lbl text-green">실전 팁</div><div class="val text-green">{format_eng_term(d.get("practical_tip",""))}</div></div>', unsafe_allow_html=True)
                if idx < len(diff_dx) - 1: st.markdown('<hr style="border:none; border-top:1px dashed #e2e8f0; margin:12px 0;">', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="center-btn-wrapper" style="margin-top: 16px; margin-bottom: 8px;">', unsafe_allow_html=True)
        if st.button("🔄 다른 사례 분석", type="secondary", key="reset_case_radio_btn"):
            st.session_state["case_reset_counter"] += 1
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    render_bottom_navigation()

def render_case_detail():
    st.session_state["screen"] = "case_list"
    st.rerun()
