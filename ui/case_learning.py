# ui/case_learning.py

import re
import streamlit as st
from data.cases import CASE_LIBRARY
from ui.navigation import render_bottom_navigation

# KeyError 방지 로직 보강
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

def format_inline_eng(text):
    """본문 내 영어를 소문자로 변환하여 인라인으로 삽입 (약어는 대문자 유지)"""
    if not text: return ""
    text = str(text)
    # 괄호 앞 공백 제거
    text = re.sub(r'\s+\(', '(', text)
    def repl(m):
        content = m.group(1)
        if not re.search('[a-zA-Z]', content): return f"({content})"
        words = content.split()
        res = []
        acronyms = {"SNAP", "CMAP", "MUAP", "MUAPS", "NCS", "EMG", "MAS", "DRT", "UMN", "LMN", "TA", "ECR", "EIP", "ADM", "FDI", "EHL", "PL", "R1", "R2"}
        for w in words:
            clean_w = re.sub(r'[^a-zA-Z0-9-]', '', w).upper()
            if clean_w in acronyms: res.append(w.upper())
            else: res.append(w.lower())
        return f"({' '.join(res)})"
    return re.sub(r'\((.*?)\)', repl, text)

def _get_data_row(lbl, val, is_bad=False):
    color = "txt-red" if is_bad else "txt-normal"
    # 콤마(,)가 있으면 줄바꿈으로 변경하여 가독성 증대
    val_formatted = str(val).replace(", ", "<br>")
    return f'<div class="data-row"><div class="data-label">{lbl}</div><div class="data-value {color}">{format_inline_eng(val_formatted)}</div></div>'

def _get_ncs_line_text(raw_val):
    if raw_val == "ncs_delayed": return _get_data_row("진폭", "정상 범위") + _get_data_row("잠복기", "지연", True)
    elif raw_val == "ncs_reduced": return _get_data_row("진폭", "감소", True) + _get_data_row("잠복기", "정상 범위")
    elif raw_val == "ncs_absent": return _get_data_row("진폭", "반응 소실", True) + _get_data_row("잠복기", "반응 소실", True)
    else: return _get_data_row("진폭", "정상 범위") + _get_data_row("잠복기", "정상 범위")

def _get_emg_line_text(raw_val):
    if raw_val in ["emg_active_denervation", "emg_paraspinal_denervation"]:
        vol = "동원 감소(reduced MU recruitment)" if raw_val == "emg_active_denervation" else "통증으로 인해 평가불가"
        return _get_data_row("휴식 시", "섬유자발전위(fibrillation potential), 양성예파(positive sharp wave)", True) + _get_data_row("수의적 수축 시", vol, True)
    elif raw_val == "emg_chronic_reinnervation":
        return _get_data_row("휴식 시", "전기적 침묵(silent at rest)") + _get_data_row("수의적 수축 시", "거대 운동단위(giant MUAPs) 출현, 동원 감소(reduced MU recruitment)", True)
    elif raw_val == "emg_active_chronic":
        return _get_data_row("휴식 시", "섬유자발전위(fibrillation potential), 양성예파(positive sharp wave)", True) + _get_data_row("수의적 수축 시", "거대 운동단위(giant MUAPs) 출현, 동원 감소(reduced MU recruitment)", True)
    elif raw_val == "emg_fasciculation":
        return _get_data_row("휴식 시", "근육다발수축전위(fasciculation potential)", True) + _get_data_row("수의적 수축 시", "동원 감소(reduced MU recruitment)", True)
    else:
        return _get_data_row("휴식 시", "전기적 침묵(silent at rest)") + _get_data_row("수의적 수축 시", "정상 동원(normal MU recruitment)")

def _get_reflex_line_text(raw_val):
    mapping = {"fwave_delayed_absent": "지연/부재", "blink_delayed": "R1/R2 지연", "blink_delayed_absent": "R2 유발 소실", "h_reflex_hyperactive": "진폭 항진", "h_m_ratio_increased": "비율 증가", "ncs_normal": "정상 범위"}
    return mapping.get(raw_val, raw_val)

def _render_finding_block(title_kor, title_eng, findings, side):
    if not findings: return
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown(format_title_box(title_kor, title_eng), unsafe_allow_html=True)
    
    items = list(findings.items())
    for idx, (item, values) in enumerate(items):
        left, right = (values[0] if len(values) > 0 else ""), (values[1] if len(values) > 1 else "")
        
        # 근육/신경 이름 처리
        m = re.match(r'^(.*?)\s*\((.*?)\)$', item)
        if m:
            item_html = f"<div style='margin-bottom:8px;'><span style='font-size:0.95rem; font-weight:800; color:#1e293b;'>{m.group(1)}</span> <span style='font-size:0.8rem; color:#64748b;'>{m.group(2).lower()}</span></div>"
        else:
            item_html = f"<div style='margin-bottom:8px; font-size:0.95rem; font-weight:800; color:#1e293b;'>{item}</div>"
            
        st.markdown(item_html, unsafe_allow_html=True)
        pathological_val = right if side in ["오른쪽", "우"] else left
        raw_val = str(pathological_val).strip()

        if side in ["양쪽", "양측"]:
            raw_left, raw_right = str(left).strip(), str(right).strip()
            if "감각" in title_kor or "운동" in title_kor: l_txt, r_txt = _get_ncs_line_text(raw_left), _get_ncs_line_text(raw_right)
            elif "침근전도" in title_kor: l_txt, r_txt = _get_emg_line_text(raw_left), _get_emg_line_text(raw_right)
            else: l_txt, r_txt = _get_data_row("판독", _get_reflex_line_text(raw_left)), _get_data_row("판독", _get_reflex_line_text(raw_right))
            st.markdown(f'<div style="background:#f8fafc; padding:8px; border-radius:6px; margin-bottom:4px;"><div style="font-size:0.85rem; font-weight:700; color:#475569; margin-bottom:4px;">좌측:</div>{l_txt}</div>', unsafe_allow_html=True)
            st.markdown(f'<div style="background:#f8fafc; padding:8px; border-radius:6px;"><div style="font-size:0.85rem; font-weight:700; color:#475569; margin-bottom:4px;">우측:</div>{r_txt}</div>', unsafe_allow_html=True)
        else:
            if "감각" in title_kor or "운동" in title_kor: st.markdown(_get_ncs_line_text(raw_val), unsafe_allow_html=True)
            elif "침근전도" in title_kor: st.markdown(_get_emg_line_text(raw_val), unsafe_allow_html=True)
            else:
                norm_val = _get_reflex_line_text(raw_val)
                st.markdown(_get_data_row("판독 결과", norm_val, norm_val != "정상 범위"), unsafe_allow_html=True)
                if right and right not in ["ncs_normal", "NCS_NORMAL"]: st.markdown(_get_data_row("측정 데이터", right), unsafe_allow_html=True)
        if idx < len(items) - 1: st.markdown('<div style="height:1px; background:#e2e8f0; margin:16px 0;"></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def render_interpretation_text(lines):
    for x in lines:
        if ":" in x:
            parts = x.split(":", 1)
            # 콜론 앞은 굵고 파란색, 뒤는 일반 텍스트
            st.markdown(f'<div style="font-size:0.9rem; line-height:1.6; margin-bottom:6px;"><span style="font-weight:700; color:#1d4ed8;">{format_inline_eng(parts[0])}:</span> <span style="color:#334155;">{format_inline_eng(parts[1])}</span></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div style="font-size:0.9rem; color:#334155; line-height:1.6; margin-bottom:6px;">• {format_inline_eng(x)}</div>', unsafe_allow_html=True)

def render_case_list():
    st.markdown('<div style="margin-bottom:16px;"><div style="font-size:1.3rem; font-weight:800; color:#0f172a;">사례 학습 모드</div><div style="font-size:0.85rem; color:#64748b;">case study mode</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown(format_title_box("학습할 가상 사례 선택", "case selection"), unsafe_allow_html=True)

    case_names = ["선택 안 함"] + list(CASE_LIBRARY.keys())
    if "case_reset_counter" not in st.session_state: st.session_state["case_reset_counter"] = 0
    selected = st.radio("사례 선택", case_names, key=f"case_radio_{st.session_state['case_reset_counter']}", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

    if selected != "선택 안 함":
        case = CASE_LIBRARY[selected]
        patient, findings, teaching, diff_dx = case["patient"], case["findings"], case["teaching_diagnosis"], case["differential_diagnosis"]
        side = patient.get("side", "-").replace("우", "오른쪽").replace("좌", "왼쪽").replace("양측", "양쪽")

        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.markdown(f'<div style="font-weight:800; color:#0f172a; margin-bottom:6px;">👤 환자 사례: {selected}</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="font-size:0.9rem; color:#475569;">연령/성별: {patient["age"]}세 / {patient["sex"]} &nbsp;|&nbsp; 병변측: {side}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown(format_title_box("주요 증상", "chief complaint"), unsafe_allow_html=True)
        for s in patient.get("symptoms", []): st.markdown(f'<div style="font-size:0.9rem; color:#334155; margin-bottom:6px;">• {format_inline_eng(s)}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown(format_title_box("이학적 검사결과", "physical examination"), unsafe_allow_html=True)
        for sec_name, items in patient.get("physical_exam", {}).items():
            st.markdown(f'<div style="font-weight:800; color:#0f172a; margin-top:12px; margin-bottom:6px;">[{format_inline_eng(sec_name)}]</div>', unsafe_allow_html=True)
            for i in items:
                parts = i.split(":", 1)
                if len(parts) == 2: st.markdown(_get_data_row(format_inline_eng(parts[0]), format_inline_eng(parts[1])), unsafe_allow_html=True)
                else: st.markdown(f'<div style="font-size:0.9rem; color:#334155;">• {format_inline_eng(i)}</div>', unsafe_allow_html=True)
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

        # 🚨 진단명 카드 (좌측 정렬 및 포맷 적용)
        diag_name = f"{side} {case.get('category', '')}" if "뇌졸중" not in selected else "위운동신경세포(UMN) 중증 경직 소견"
        st.markdown(f"""
        <div class="diagnosis-box">
            <div class="diagnosis-label">의심질환 추정 진단명:</div>
            <div class="diagnosis-name">{format_inline_eng(diag_name)}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        if teaching.get("ncs_reason"):
            label = "눈깜박반사 해석 포인트" if ("눈꺼풀" in selected or "얼굴" in selected) else "H-반사 유발 해석 포인트" if "뇌졸중" in selected else "신경전도 해석 포인트"
            st.markdown(format_title_box(label, "ncs interpretation"), unsafe_allow_html=True)
            render_interpretation_text(teaching["ncs_reason"])
            st.markdown('<div style="height:16px;"></div>', unsafe_allow_html=True)
            
        if teaching.get("emg_reason"):
            if not ("Blink Reflex" in str(teaching["emg_reason"][0]) or "H-reflex" in str(teaching["emg_reason"][0]) or "눈꺼풀" in selected or "뇌졸중" in selected):
                st.markdown(format_title_box("침근전도 해석 포인트", "emg interpretation"), unsafe_allow_html=True)
                render_interpretation_text(teaching["emg_reason"])
                st.markdown('<div style="height:16px;"></div>', unsafe_allow_html=True)
                
        if teaching.get("integration"):
            st.markdown(format_title_box("통합 해석", "integrated interpretation"), unsafe_allow_html=True)
            render_interpretation_text(teaching["integration"])
        st.markdown('</div>', unsafe_allow_html=True)

        if diff_dx:
            st.markdown('<div class="content-card">', unsafe_allow_html=True)
            st.markdown(format_title_box("감별진단 포인트", "differential diagnosis"), unsafe_allow_html=True)
            for idx, d in enumerate(diff_dx):
                st.markdown(f'<div style="font-weight:800; font-size:0.95rem; color:#0f172a; margin-top:8px; margin-bottom:8px;">{format_inline_eng(d.get("name",""))}</div>', unsafe_allow_html=True)
                st.markdown(_get_data_row("왜 고려하나", format_inline_eng(d.get("why_consider",""))), unsafe_allow_html=True)
                st.markdown(_get_data_row("어떻게 구분하나", format_inline_eng(d.get("how_to_differentiate",""))), unsafe_allow_html=True)
                st.markdown(_get_data_row("실전 팁", f"<span style='color:#15803d; font-weight:600;'>{format_inline_eng(d.get('practical_tip',''))}</span>"), unsafe_allow_html=True)
                if idx < len(diff_dx) - 1: st.markdown('<div style="height:1px; background:#e2e8f0; margin:16px 0;"></div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="center-btn" style="margin-top: 24px; margin-bottom: 12px;">', unsafe_allow_html=True)
        if st.button("다른 사례 분석", type="primary", key="reset_case_btn"):
            st.session_state["case_reset_counter"] += 1
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    render_bottom_navigation()
