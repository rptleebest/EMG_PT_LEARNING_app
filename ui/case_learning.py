# ui/case_learning.py

import re
import streamlit as st
from data.cases import CASE_LIBRARY
from ui.navigation import render_bottom_navigation

def split_findings_by_domain(findings):
    grouped = {"sensory": {}, "motor": {}, "muscle": {}, "reflex": {}, "other": {}}
    for item, vals in findings.items():
        name = item.lower()
        if "snap" in name or "감각" in name: grouped["sensory"][item] = vals
        elif "cmap" in name or "운동" in name: grouped["motor"][item] = vals
        elif "반사" in name or "f파" in name or "r1" in name or "r2" in name or "h/m" in name or "blink" in name: grouped["reflex"][item] = vals
        else: grouped["muscle"][item] = vals
    return grouped

def format_title_box(kor, icon=""):
    icon_html = f"<span style='margin-right:6px;'>{icon}</span>" if icon else ""
    return f"<div class='title-box'><div class='title-kor'>{icon_html}{kor}</div></div>"

def format_inline_eng(text):
    """영문을 인라인 괄호로 표기하며 띄어쓰기 교정. 약어는 대문자, 나머지는 소문자화"""
    if not text: return ""
    text = str(text)
    text = re.sub(r'\s+\(', '(', text) # 공백 완벽 제거
    def repl(m):
        content = m.group(1)
        if not re.search('[a-zA-Z]', content): return f"({content})"
        words = content.split()
        res = []
        acronyms = {"SNAP", "CMAP", "MUAP", "MUAPS", "NCS", "EMG", "MAS", "DRT", "UMN", "LMN", "TA", "ECR", "EIP", "ADM", "FDI", "EHL", "PL", "R1", "R2", "H", "F", "MU", "MMT"}
        for w in words:
            clean_w = re.sub(r'[^a-zA-Z]', '', w).upper()
            if clean_w in acronyms: res.append(w.upper())
            else: res.append(w.lower())
        return f"({' '.join(res)})"
    return re.sub(r'\((.*?)\)', repl, text)

def remove_english_parens(text):
    """해석 텍스트에서 불필요한 영문 괄호를 완전히 제거하여 가독성을 높임"""
    if not text: return ""
    return re.sub(r'\([a-zA-Z\s\-]+\)', '', str(text)).replace("  ", " ").strip()

def _get_data_row(lbl, val, is_bad=False):
    color = "txt-red" if is_bad else ("txt-green" if "정상" in val else "txt-normal")
    return f'<div class="data-row"><div class="data-label">{lbl}</div><div class="data-value {color}">{val}</div></div>'

def _get_ncs_line_text(raw_val):
    if raw_val == "ncs_delayed": return _get_data_row("진폭", "정상 반응") + _get_data_row("잠복기", "지연", True)
    elif raw_val == "ncs_reduced": return _get_data_row("진폭", "감소", True) + _get_data_row("잠복기", "정상 반응")
    elif raw_val == "ncs_absent": return _get_data_row("진폭", "반응 소실", True) + _get_data_row("잠복기", "반응 소실", True)
    else: return _get_data_row("진폭", "정상 반응") + _get_data_row("잠복기", "정상 반응")

def _get_emg_line_text(raw_val):
    if raw_val in ["emg_active_denervation", "emg_paraspinal_denervation"]:
        vol = "동원 감소" if raw_val == "emg_active_denervation" else "통증으로 인해 평가불가"
        return _get_data_row("휴식 시", "비정상 반응(섬유자발전위, 양성예파)", True) + _get_data_row("수의적 수축 시", vol, True) + _get_data_row("판단", "비정상 반응(활동성 탈신경)", True)
    elif raw_val == "emg_chronic_reinnervation":
        return _get_data_row("휴식 시", "전기적 침묵") + _get_data_row("수의적 수축 시", "거대 운동단위 출현, 동원 감소", True) + _get_data_row("판단", "비정상 반응(만성 재신경지배)", True)
    elif raw_val == "emg_active_chronic":
        return _get_data_row("휴식 시", "비정상 반응(섬유자발전위, 양성예파)", True) + _get_data_row("수의적 수축 시", "거대 운동단위 출현, 동원 감소", True) + _get_data_row("판단", "비정상 반응(활동성 및 만성 탈신경)", True)
    elif raw_val == "emg_fasciculation":
        return _get_data_row("휴식 시", "비정상 반응(근육다발수축전위)", True) + _get_data_row("수의적 수축 시", "동원 감소", True) + _get_data_row("판단", "비정상 반응(전각세포 손상 시사)", True)
    else:
        return _get_data_row("휴식 시", "전기적 침묵") + _get_data_row("수의적 수축 시", "정상 동원") + _get_data_row("판단", "정상 반응")

def _get_reflex_line_text(raw_val):
    mapping = {"fwave_delayed_absent": "지연/부재", "blink_delayed": "R1/R2 지연", "blink_delayed_absent": "R2 유발 소실", "h_reflex_hyperactive": "진폭 항진", "h_m_ratio_increased": "비율 증가", "ncs_normal": "정상 반응"}
    return mapping.get(raw_val, raw_val)

def _render_finding_block(title_kor, findings, side):
    if not findings: return
    st.markdown(format_title_box(title_kor), unsafe_allow_html=True)
    
    items = list(findings.items())
    for item, values in items:
        left, right = (values[0] if len(values) > 0 else ""), (values[1] if len(values) > 1 else "")
        
        # 박스 제거, 깔끔한 구분선 사용
        st.markdown(f"<div style='font-size:0.95rem; font-weight:800; color:#1e293b; margin-top:12px; margin-bottom:6px;'>{format_inline_eng(item)}</div>", unsafe_allow_html=True)
            
        pathological_val = right if side in ["오른쪽", "우"] else left
        raw_val = str(pathological_val).strip()

        if side in ["양쪽", "양측"]:
            raw_left, raw_right = str(left).strip(), str(right).strip()
            if "감각" in title_kor or "운동" in title_kor: l_txt, r_txt = _get_ncs_line_text(raw_left), _get_ncs_line_text(raw_right)
            elif "침근전도" in title_kor: l_txt, r_txt = _get_emg_line_text(raw_left), _get_emg_line_text(raw_right)
            else: l_txt, r_txt = _get_data_row("판독", _get_reflex_line_text(raw_left)), _get_data_row("판독", _get_reflex_line_text(raw_right))
            st.markdown(f'<div style="margin-bottom:4px;"><span style="font-weight:700; color:#475569;">좌측:</span></div>{l_txt}', unsafe_allow_html=True)
            st.markdown(f'<div style="margin-top:8px; margin-bottom:4px;"><span style="font-weight:700; color:#475569;">우측:</span></div>{r_txt}', unsafe_allow_html=True)
        else:
            if "감각" in title_kor or "운동" in title_kor: st.markdown(_get_ncs_line_text(raw_val), unsafe_allow_html=True)
            elif "침근전도" in title_kor: st.markdown(_get_emg_line_text(raw_val), unsafe_allow_html=True)
            else:
                norm_val = _get_reflex_line_text(raw_val)
                st.markdown(_get_data_row("판독 결과", norm_val, norm_val != "정상 반응"), unsafe_allow_html=True)
                if right and right not in ["ncs_normal", "NCS_NORMAL"]: st.markdown(_get_data_row("측정 데이터", right), unsafe_allow_html=True)
        
        st.markdown('<div style="height:1px; background:#e2e8f0; margin:12px 0;"></div>', unsafe_allow_html=True)

def render_interpretation_text(lines):
    for x in lines:
        clean_text = remove_english_parens(x)
        if ":" in clean_text:
            parts = clean_text.split(":", 1)
            st.markdown(f'<div style="font-size:0.9rem; margin-bottom:8px;"><span style="font-weight:800; color:#1d4ed8;">{parts[0]}:</span> <span style="color:#334155;">{parts[1]}</span></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div style="font-size:0.9rem; color:#334155; margin-bottom:8px;">• {clean_text}</div>', unsafe_allow_html=True)

def render_case_list():
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown(format_title_box("가상 사례 선택"), unsafe_allow_html=True)

    case_names = ["선택 안 함"] + list(CASE_LIBRARY.keys())
    if "case_reset_counter" not in st.session_state: st.session_state["case_reset_counter"] = 0
    selected = st.radio("사례 선택", case_names, key=f"case_radio_{st.session_state['case_reset_counter']}", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

    if selected != "선택 안 함":
        case = CASE_LIBRARY[selected]
        patient, findings, teaching, diff_dx = case["patient"], case["findings"], case["teaching_diagnosis"], case["differential_diagnosis"]
        side = patient.get("side", "-").replace("우", "오른쪽").replace("좌", "왼쪽").replace("양측", "양쪽")

        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.markdown(f'<div style="font-weight:800; font-size:0.95rem; color:#0f172a; margin-bottom:6px;">👤 환자 사례: {selected}</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="font-size:0.85rem; color:#475569;">연령/성별: {patient["age"]}세 / {patient["sex"]} &nbsp;|&nbsp; 병변측: {side}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown(format_title_box("주요 증상"), unsafe_allow_html=True)
        for s in patient.get("symptoms", []): st.markdown(f'<div style="font-size:0.9rem; color:#334155; margin-bottom:6px;">• {format_inline_eng(s)}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown(format_title_box("이학적 검사결과"), unsafe_allow_html=True)
        for sec_name, items in patient.get("physical_exam", {}).items():
            st.markdown(f'<div style="font-weight:800; color:#1e3a8a; margin-top:12px; margin-bottom:6px;">[{format_inline_eng(sec_name)}]</div>', unsafe_allow_html=True)
            for i in items:
                # 🚨 맨손근력 및 반사 검사 들여쓰기 
                if "맨손근력" in sec_name or "MMT" in sec_name.upper():
                    parts = i.split(" - ", 1)
                    if len(parts) == 2:
                        st.markdown(f'<div style="font-size:0.9rem; margin-bottom:2px;">• <span style="font-weight:700;">{format_inline_eng(parts[0])}</span></div>', unsafe_allow_html=True)
                        st.markdown(f'<div style="font-size:0.8rem; color:#64748b; margin-left:14px; margin-bottom:8px;">└ 지배신경: {format_inline_eng(parts[1])}</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div style="font-size:0.9rem; color:#334155; margin-bottom:8px;">• {format_inline_eng(i)}</div>', unsafe_allow_html=True)
                elif "반사 검사" in sec_name:
                    st.markdown(f'<div style="font-size:0.9rem; color:#334155; margin-bottom:6px;">• {format_inline_eng(i)}</div>', unsafe_allow_html=True)
                else:
                    parts = i.split(":", 1)
                    if len(parts) == 2:
                        st.markdown(f'<div style="font-size:0.9rem; margin-bottom:6px;">• <span style="font-weight:700;">{format_inline_eng(parts[0])}:</span> <span style="color:#334155;">{format_inline_eng(parts[1])}</span></div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div style="font-size:0.9rem; color:#334155; margin-bottom:6px;">• {format_inline_eng(i)}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("""
        <div style="background:#fffbeb; border:1px solid #fde68a; padding:12px; border-radius:6px; margin-bottom:16px;">
            <div style="font-size:0.85rem; font-weight:800; color:#d97706; margin-bottom:4px;">💡 근전도 판독 기준 팁 (정상측 대비)</div>
            <div style="font-size:0.8rem; color:#92400e;">- 진폭 감소: 50% 이하 감소 시 비정상 (축삭 손상 시사)<br>- 잠복기 지연: 130% 이상 증가 시 비정상 (말이집탈락 시사)<br>- 사례 문제에서는 정상측 결과가 정상이므로 <b>병변측 결과만 표기</b>됩니다.</div>
        </div>
        """, unsafe_allow_html=True)

        grouped = split_findings_by_domain(findings)
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown(f"<div style='font-size:1.0rem; font-weight:800; color:#1e40af; margin-bottom:12px;'>근전도 검사 결과 (병변측: {side})</div>", unsafe_allow_html=True)
        if grouped["sensory"]: _render_finding_block("🖐️ 감각신경전도검사", grouped["sensory"], side)
        if grouped["motor"]: _render_finding_block("⚡ 운동신경전도검사", grouped["motor"], side)
        if grouped["muscle"] and "눈꺼풀" not in selected and "뇌졸중" not in selected: _render_finding_block("🪡 침근전도검사 소견", grouped["muscle"], side)
        if grouped["reflex"] or grouped["other"]:
            merged = {**grouped["reflex"], **grouped["other"]}
            if "뇌졸중" in selected: _render_finding_block("🔄 H-반사 유발 검사", merged, side)
            elif "눈꺼풀" in selected: _render_finding_block("👁️ 눈깜빡반사 회로 분석", merged, side)
            else: _render_finding_block("🔄 반사 및 후기반응 소견", merged, side)
        st.markdown('</div>', unsafe_allow_html=True)

        diag_name = f"{side} {case.get('category', '')}" if "뇌졸중" not in selected else "위운동신경세포(UMN) 중증 경직 소견"
        st.markdown(f"""
        <div class="diagnosis-box">
            <div class="diagnosis-label">의심질환 추정 진단명:</div>
            <div class="diagnosis-name">{format_inline_eng(diag_name)}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        if teaching.get("ncs_reason"):
            label = "눈깜박반사 해석 포인트" if ("눈꺼풀" in selected or "얼굴" in selected) else "H-반사 해석 포인트" if "뇌졸중" in selected else "신경전도 해석 포인트"
            st.markdown(format_title_box(label), unsafe_allow_html=True)
            render_interpretation_text(teaching["ncs_reason"])
            st.markdown('<div style="height:16px;"></div>', unsafe_allow_html=True)
            
        if teaching.get("emg_reason"):
            if not ("Blink Reflex" in str(teaching["emg_reason"][0]) or "H-reflex" in str(teaching["emg_reason"][0]) or "눈꺼풀" in selected or "뇌졸중" in selected):
                st.markdown(format_title_box("침근전도 해석 포인트"), unsafe_allow_html=True)
                render_interpretation_text(teaching["emg_reason"])
                st.markdown('<div style="height:16px;"></div>', unsafe_allow_html=True)
                
        if teaching.get("integration"):
            st.markdown(format_title_box("통합 해석"), unsafe_allow_html=True)
            render_interpretation_text(teaching["integration"])
        st.markdown('</div>', unsafe_allow_html=True)

        if diff_dx:
            st.markdown('<div class="content-card">', unsafe_allow_html=True)
            st.markdown(format_title_box("감별진단 포인트"), unsafe_allow_html=True)
            for idx, d in enumerate(diff_dx):
                st.markdown(f'<div style="font-weight:800; font-size:0.95rem; color:#0f172a; margin-top:8px; margin-bottom:8px;">{remove_english_parens(d.get("name",""))}</div>', unsafe_allow_html=True)
                st.markdown(f'<div style="font-size:0.9rem; margin-bottom:6px;"><span style="font-weight:700; color:#1d4ed8;">왜 고려하나?:</span> <span style="color:#334155;">{remove_english_parens(d.get("why_consider",""))}</span></div>', unsafe_allow_html=True)
                st.markdown(f'<div style="font-size:0.9rem; margin-bottom:6px;"><span style="font-weight:700; color:#1d4ed8;">어떻게 구분하나?:</span> <span style="color:#334155;">{remove_english_parens(d.get("how_to_differentiate",""))}</span></div>', unsafe_allow_html=True)
                st.markdown(f'<div style="font-size:0.9rem; margin-bottom:6px;"><span style="font-weight:700; color:#15803d;">실전 팁:</span> <span style="color:#15803d; font-weight:500;">{remove_english_parens(d.get("practical_tip",""))}</span></div>', unsafe_allow_html=True)
                if idx < len(diff_dx) - 1: st.markdown('<div style="height:1px; background:#e2e8f0; margin:16px 0;"></div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="center-btn" style="margin-top: 24px; margin-bottom: 12px;">', unsafe_allow_html=True)
        if st.button("다른 사례 분석", type="primary"):
            st.session_state["case_reset_counter"] += 1
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    render_bottom_navigation()
