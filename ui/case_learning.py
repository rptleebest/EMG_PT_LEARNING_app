# ui/case_learning.py

import re
import streamlit as st
from data.cases import CASE_LIBRARY
from ui.navigation import render_bottom_navigation

# 🚨 에러 원인 해결을 위해 직접 함수 내재화 (other 키 누락 방지)
def split_findings_by_domain(findings):
    grouped = {"sensory": {}, "motor": {}, "muscle": {}, "reflex": {}, "other": {}}
    for item, vals in findings.items():
        name = item.lower()
        if "snap" in name or "감각" in name: grouped["sensory"][item] = vals
        elif "cmap" in name or "운동" in name: grouped["motor"][item] = vals
        elif "반사" in name or "f파" in name or "r1" in name or "r2" in name or "h/m" in name or "blink" in name: grouped["reflex"][item] = vals
        else: grouped["muscle"][item] = vals
    return grouped

def format_title_box(kor, eng):
    return f"<div class='title-box'><div class='title-kor'>{kor}</div><div class='title-eng'>{eng.lower()}</div></div>"

def format_result_label(kor, eng):
    return f"<div class='result-label-box'><div class='title-kor'>{kor}</div><div class='title-eng'>{eng.lower()}</div></div>"

def format_inline_term(text):
    """문장 내 괄호 영어를 소문자(약어 대문자) 띄어쓰기로 깔끔하게 변환"""
    if not text: return ""
    text = str(text)
    text = re.sub(r'\s+\(', '(', text) # 괄호 앞 공백 제거
    def repl(m):
        content = m.group(1)
        if not re.search('[a-zA-Z]', content): return f"({content})"
        words = content.split()
        res = []
        acronyms = {"SNAP", "CMAP", "MUAP", "MUAPS", "NCS", "EMG", "MAS", "DRT", "UMN", "LMN", "TA", "ECR", "EIP", "ADM", "FDI", "EHL", "PL", "R1", "R2", "F-WAVE", "H-REFLEX", "V1", "C5", "C6", "C7", "C8", "T1", "L4", "L5", "S1", "S2"}
        for w in words:
            clean_w = re.sub(r'[^a-zA-Z0-9-]', '', w).upper()
            if clean_w in acronyms: res.append(w.upper())
            else: res.append(w.lower())
        return f"({' '.join(res)})"
    return re.sub(r'\((.*?)\)', repl, text)

def _get_ncs_row(lbl, val, is_bad=False):
    # 🚨 콤마(,)가 있을 경우 줄바꿈 처리하여 세로로 깔끔하게 나열
    val = str(val).replace(", ", "<br>")
    color = "text-red" if is_bad else ("text-blue" if "정상" in val else "")
    return f'<div class="data-line"><div class="data-lbl">{lbl}</div><div class="data-val {color}">{val}</div></div>'

def _get_ncs_line_text(raw_val):
    if raw_val == "ncs_delayed": return _get_ncs_row("진폭", "정상 범위") + _get_ncs_row("잠복기", "지연", True)
    elif raw_val == "ncs_reduced": return _get_ncs_row("진폭", "감소", True) + _get_ncs_row("잠복기", "정상 범위")
    elif raw_val == "ncs_absent": return _get_ncs_row("진폭", "반응 소실", True) + _get_ncs_row("잠복기", "반응 소실", True)
    else: return _get_ncs_row("진폭", "정상 범위") + _get_ncs_row("잠복기", "정상 범위")

def _get_emg_line_text(raw_val):
    if raw_val in ["emg_active_denervation", "emg_paraspinal_denervation"]:
        vol = "동원 감소(reduced MU recruitment)" if raw_val == "emg_active_denervation" else "통증으로 인해 평가불가"
        return _get_ncs_row("휴식 시", format_inline_term("섬유자발전위(fibrillation potential), 양성예파(positive sharp wave)"), True) + _get_ncs_row("수의적 수축 시", format_inline_term(vol), True)
    elif raw_val == "emg_chronic_reinnervation":
        return _get_ncs_row("휴식 시", format_inline_term("전기적 침묵(silent at rest)")) + _get_ncs_row("수의적 수축 시", format_inline_term("거대 운동단위(giant MUAPs), 동원 감소(reduced MU recruitment)"), True)
    elif raw_val == "emg_active_chronic":
        return _get_ncs_row("휴식 시", format_inline_term("섬유자발전위(fibrillation potential), 양성예파(positive sharp wave)"), True) + _get_ncs_row("수의적 수축 시", format_inline_term("거대 운동단위(giant MUAPs), 동원 감소(reduced MU recruitment)"), True)
    elif raw_val == "emg_fasciculation":
        return _get_ncs_row("휴식 시", format_inline_term("근육다발수축전위(fasciculation potential)"), True) + _get_ncs_row("수의적 수축 시", format_inline_term("동원 감소(reduced MU recruitment)"), True)
    else:
        return _get_ncs_row("휴식 시", format_inline_term("전기적 침묵(silent at rest)")) + _get_ncs_row("수의적 수축 시", format_inline_term("정상 동원(normal MU recruitment)"))

def _get_reflex_line_text(raw_val):
    if raw_val == "fwave_delayed_absent": return "지연/부재"
    elif raw_val == "blink_delayed": return "R1/R2 지연"
    elif raw_val == "blink_delayed_absent": return "R2 유발 소실"
    elif raw_val == "h_reflex_hyperactive": return "진폭 항진"
    elif raw_val == "h_m_ratio_increased": return "비율 증가"
    elif raw_val in ["ncs_normal", "정상 범위"]: return "정상 범위"
    return raw_val

def _render_finding_block(title_kor, title_eng, findings, side):
    if not findings: return
    st.markdown(format_title_box(title_kor, title_eng), unsafe_allow_html=True)
    
    block_parts = []
    items = list(findings.items())
    for idx, (item, values) in enumerate(items):
        left = values[0] if len(values) > 0 else ""
        right = values[1] if len(values) > 1 else ""
        
        # 신경 이름 분리 (예: 정중신경 감각신경활동전위 (Median SNAP))
        m = re.match(r'^(.*?)\s*\((.*?)\)$', item)
        if m:
            i_kor, i_eng = m.group(1).strip(), m.group(2).strip().lower()
            for ac in ["snap", "cmap"]: i_eng = i_eng.replace(ac, ac.upper())
            head = f"<div class='finding-highlight-kor'>{i_kor}</div><div class='finding-highlight-eng'>{i_eng}</div>"
        else:
            head = f"<div class='finding-highlight-kor'>{item}</div><div class='finding-highlight-eng' style='color:transparent;'>-</div>"
            
        lines = [head]
        pathological_val = right if side in ["오른쪽", "우"] else left
        raw_val = str(pathological_val).strip()

        if side in ["양쪽", "양측"]:
            raw_left, raw_right = str(left).strip(), str(right).strip()
            if "감각" in title_kor or "운동" in title_kor:
                l_txt, r_txt = _get_ncs_line_text(raw_left), _get_ncs_line_text(raw_right)
            elif "침근전도" in title_kor:
                l_txt, r_txt = _get_emg_line_text(raw_left), _get_emg_line_text(raw_right)
            else:
                l_txt, r_txt = _get_ncs_row("판독", _get_reflex_line_text(raw_left)), _get_ncs_row("판독", _get_reflex_line_text(raw_right))
            lines.append(f'<div style="background:#f8fafc; padding:8px; border-radius:6px; margin-bottom:4px;"><div class="data-lbl">좌측:</div>{l_txt}</div>')
            lines.append(f'<div style="background:#f8fafc; padding:8px; border-radius:6px;"><div class="data-lbl">우측:</div>{r_txt}</div>')
        else:
            if "감각" in title_kor or "운동" in title_kor:
                lines.append(_get_ncs_line_text(raw_val))
            elif "침근전도" in title_kor:
                lines.append(_get_emg_line_text(raw_val))
            else:
                norm_val = _get_reflex_line_text(raw_val)
                lines.append(_get_ncs_row("판독 결과", norm_val, norm_val != "정상 범위"))
                if right and right not in ["ncs_normal", "NCS_NORMAL"]:
                    lines.append(_get_ncs_row("측정 데이터", right))

        block_parts.append(f'<div style="margin-bottom: 16px;">{"".join(lines)}</div>')
    if block_parts: st.markdown(f'<div class="section-card">{"".join(block_parts)}</div>', unsafe_allow_html=True)

def render_case_list():
    st.markdown('<div class="main-title-kor">사례 학습 모드</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-title-eng">case study mode</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtle">환자의 임상 증상과 근전도 소견을 실시간 비교 분석하여 임상적 판단력을 기릅니다.</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown(format_title_box("학습할 가상 사례 선택", "case selection"), unsafe_allow_html=True)

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
        st.markdown(f'<div class="data-lbl" style="font-size:1rem; margin-bottom:8px;">👤 환자 사례: {selected}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="data-val">연령/성별: {patient["age"]}세 / {patient["sex"]} &nbsp;|&nbsp; 병변측: {side}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown(format_title_box("주요 증상", "chief complaint"), unsafe_allow_html=True)
        symptoms_html = "".join([f'<div class="case-bullet">• {format_inline_term(s)}</div>' for s in patient.get("symptoms", [])])
        st.markdown(f'<div>{symptoms_html}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown(format_title_box("이학적 검사결과", "physical examination"), unsafe_allow_html=True)
        exam_html = []
        for sec_name, items in patient.get("physical_exam", {}).items():
            exam_html.append(f'<div style="font-weight:800; color:#1e3a8a; margin-top:10px; margin-bottom:4px;">[{sec_name}]</div>')
            for i in items:
                parts = i.split(":", 1)
                if len(parts) == 2: exam_html.append(_get_ncs_row(format_inline_term(parts[0]), format_inline_term(parts[1])))
                else: exam_html.append(f'<div class="case-bullet">• {format_inline_term(i)}</div>')
        st.markdown(f'<div>{"".join(exam_html)}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        grouped = split_findings_by_domain(findings)
        if grouped["sensory"]: _render_finding_block("감각신경전도검사", "sensory NCS", grouped["sensory"], side)
        if grouped["motor"]: _render_finding_block("운동신경전도검사", "motor NCS", grouped["motor"], side)
        if grouped["muscle"] and "눈꺼풀" not in selected and "뇌졸중" not in selected: _render_finding_block("침근전도검사 소견", "needle EMG", grouped["muscle"], side)
        if grouped["reflex"] or grouped["other"]:
            merged = {**grouped["reflex"], **grouped["other"]}
            if "뇌졸중" in selected: _render_finding_block("H-반사 유발 검사", "h-reflex", merged, side)
            elif "눈꺼풀" in selected: _render_finding_block("눈깜빡반사 회로 분석", "blink reflex", merged, side)
            else: _render_finding_block("반사 및 후기반응 소견", "late response", merged, side)

        # 🚨 진단명 카드 (글자 제거, 진단명만, 중앙 정렬)
        diag_name = f"{side} {case.get('category', '')}" if "뇌졸중" not in selected else "위운동신경세포(UMN) 중증 경직 소견"
        st.markdown(f"""
        <div class="diag-box">
            <div class="diag-kor">{diag_name.split('(')[0].strip()}</div>
            <div class="diag-eng">{"(" + diag_name.split('(')[1] if '(' in diag_name else ""}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        if teaching.get("ncs_reason"):
            label = "눈깜박반사 해석 포인트" if ("눈꺼풀" in selected or "얼굴" in selected) else "H-반사 유발 해석 포인트" if "뇌졸중" in selected else "신경전도 해석 포인트"
            st.markdown(format_result_label(label, "ncs interpretation"), unsafe_allow_html=True)
            for x in teaching["ncs_reason"]: st.markdown(f'<div class="case-bullet">• {format_inline_term(x)}</div>', unsafe_allow_html=True)
        
        if teaching.get("emg_reason"):
            if not ("Blink Reflex" in str(teaching["emg_reason"][0]) or "H-reflex" in str(teaching["emg_reason"][0]) or "눈꺼풀" in selected or "뇌졸중" in selected):
                st.markdown(format_result_label("침근전도 해석 포인트", "emg interpretation"), unsafe_allow_html=True)
                for x in teaching["emg_reason"]: st.markdown(f'<div class="case-bullet">• {format_inline_term(x)}</div>', unsafe_allow_html=True)
        
        if teaching.get("integration"):
            st.markdown(format_result_label("통합 해석", "integrated interpretation"), unsafe_allow_html=True)
            for x in teaching["integration"]: st.markdown(f'<div class="case-bullet">• {format_inline_term(x)}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        if diff_dx:
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown(format_title_box("감별진단 포인트", "differential diagnosis"), unsafe_allow_html=True)
            for idx, d in enumerate(diff_dx):
                st.markdown(f'<div style="font-weight:800; font-size:0.95rem; color:#1e3a8a; margin-top:10px; margin-bottom:8px;">{format_inline_term(d.get("name",""))}</div>', unsafe_allow_html=True)
                st.markdown(_get_ncs_row("왜 고려하나", format_inline_term(d.get("why_consider",""))), unsafe_allow_html=True)
                st.markdown(_get_ncs_row("어떻게 구분하나", format_inline_term(d.get("how_to_differentiate",""))), unsafe_allow_html=True)
                st.markdown(_get_ncs_row("실전 팁", f"<span class='text-green'>{format_inline_term(d.get('practical_tip',''))}</span>"), unsafe_allow_html=True)
                if idx < len(diff_dx) - 1: st.markdown('<hr style="border:none; border-top:1px dashed #e2e8f0; margin:12px 0;">', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="center-btn-wrapper" style="margin-top: 24px; margin-bottom: 8px;">', unsafe_allow_html=True)
        if st.button("🔄 다른 사례 분석", type="secondary", key="reset_case_radio_btn"):
            st.session_state["case_reset_counter"] += 1
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    render_bottom_navigation()

def render_case_detail():
    st.session_state["screen"] = "case_list"
    st.rerun()
