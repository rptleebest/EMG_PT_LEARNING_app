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

def format_nerve_name_eng_below(text):
    """한글(영어) 텍스트를 입력받아, 영어를 괄호 없이 아래줄로 배치 (약어 대문자화)"""
    if not text: return ""
    text = str(text)
    m = re.match(r'^(.*?)\s*\((.*?)\)$', text)
    if m:
        kor = m.group(1).strip()
        eng = m.group(2).strip()
        words = eng.split()
        res = []
        acronyms = {"SNAP", "CMAP", "MUAP", "MUAPS", "NCS", "EMG", "MAS", "DRT", "UMN", "LMN", "TA", "ECR", "EIP", "ADM", "FDI", "EHL", "PL", "R1", "R2", "H", "F", "MU"}
        for w in words:
            clean_w = re.sub(r'[^a-zA-Z]', '', w).upper()
            if clean_w in acronyms: res.append(w.upper())
            else: res.append(w.lower())
        eng_formatted = ' '.join(res)
        return f"<div style='font-size:0.95rem; font-weight:800; color:#1e293b; margin-bottom:2px;'>{kor}</div><div style='font-size:0.8rem; font-weight:500; color:#64748b; margin-bottom:6px; line-height:1.1;'>{eng_formatted}</div>"
    else:
        return f"<div style='font-size:0.95rem; font-weight:800; color:#1e293b; margin-bottom:6px;'>{text}</div>"

def _get_data_row(lbl, val, is_bad=False):
    color = "txt-red" if is_bad else ("txt-green" if "정상" in val else "txt-normal")
    return f'<div class="data-row"><div class="data-label">{lbl}</div><div class="data-value {color}">{val}</div></div>'

# 🚨 사례 학습 모드: 교육용 정상/비정상 기준 직접 제시
def _get_ncs_line_text(raw_val):
    if raw_val == "ncs_delayed": 
        return _get_data_row("진폭", "정상 범위") + _get_data_row("잠복기", "지연 (정상측 대비 130% 이상 증가)", True)
    elif raw_val == "ncs_reduced": 
        return _get_data_row("진폭", "감소 (정상측 대비 50% 이상 감소)", True) + _get_data_row("잠복기", "정상 범위")
    elif raw_val == "ncs_absent": 
        return _get_data_row("진폭", "반응 소실", True) + _get_data_row("잠복기", "반응 소실", True)
    else: 
        return _get_data_row("진폭", "정상 범위 (예: 5.0mV 이상)") + _get_data_row("잠복기", "정상 범위 (예: 4.0ms 이하)")

def _get_emg_line_text(raw_val):
    if raw_val in ["emg_active_denervation", "emg_paraspinal_denervation"]:
        vol = "Reduced MUAPs" if raw_val == "emg_active_denervation" else "통증으로 인해 평가불가"
        return _get_data_row("휴식 시", "Fibrillation, Positive sharp wave", True) + _get_data_row("수의적 수축 시", vol, True) + _get_data_row("판단", "비정상 반응 (활동성 탈신경 추정)", True)
    elif raw_val == "emg_chronic_reinnervation":
        return _get_data_row("휴식 시", "Silent") + _get_data_row("수의적 수축 시", "Giant MUAPs, Reduced MUAPs", True) + _get_data_row("판단", "비정상 반응 (만성 재신경지배)", True)
    elif raw_val == "emg_active_chronic":
        return _get_data_row("휴식 시", "Fibrillation, Positive sharp wave", True) + _get_data_row("수의적 수축 시", "Giant MUAPs, Reduced MUAPs", True) + _get_data_row("판단", "비정상 반응 (활동/만성 탈신경 혼재)", True)
    elif raw_val == "emg_fasciculation":
        return _get_data_row("휴식 시", "Fasciculation potential", True) + _get_data_row("수의적 수축 시", "Reduced MUAPs", True) + _get_data_row("판단", "비정상 반응 (전각세포 이상 시사)", True)
    else:
        return _get_data_row("휴식 시", "Silent") + _get_data_row("수의적 수축 시", "Normal MUAPs") + _get_data_row("판단", "정상 반응")

def _get_reflex_line_text(raw_val):
    mapping = {"fwave_delayed_absent": "지연/부재", "blink_delayed": "R1/R2 지연", "blink_delayed_absent": "R2 유발 소실", "h_reflex_hyperactive": "진폭 항진", "h_m_ratio_increased": "비율 증가", "ncs_normal": "정상 범위"}
    return mapping.get(raw_val, raw_val)

def _render_finding_block(title_kor, findings, side):
    if not findings: return
    st.markdown(f'<div class="sub-title">{title_kor}</div>', unsafe_allow_html=True)
    
    items = list(findings.items())
    for item, values in items:
        left, right = (values[0] if len(values) > 0 else ""), (values[1] if len(values) > 1 else "")
        
        # 🚨 근육/신경 블록 처리 및 영어명 하단 배치
        st.markdown(f'<div style="background:#f8fafc; padding:12px; border-radius:8px; margin-bottom:12px;">{format_nerve_name_eng_below(item)}', unsafe_allow_html=True)
            
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
                st.markdown(_get_data_row("판독 결과", norm_val, norm_val != "정상 범위"), unsafe_allow_html=True)
                if right and right not in ["ncs_normal", "NCS_NORMAL"]: st.markdown(_get_data_row("측정 데이터", right), unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

def render_interpretation_text(lines):
    # 해석 파트에서 영문 완전히 제거
    for x in lines:
        clean_text = re.sub(r'\([a-zA-Z\s\-]+\)', '', str(x)).replace("  ", " ").strip()
        if ":" in clean_text:
            parts = clean_text.split(":", 1)
            st.markdown(f'<div style="font-size:0.9rem; margin-bottom:8px;"><span style="font-weight:800; color:#1d4ed8;">{parts[0]}:</span> <span style="color:#334155;">{parts[1]}</span></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div style="font-size:0.9rem; color:#334155; margin-bottom:8px;">• {clean_text}</div>', unsafe_allow_html=True)

def render_case_list():
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">가상 사례 선택</div>', unsafe_allow_html=True)

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
        st.markdown('<div class="section-title">주요 증상</div>', unsafe_allow_html=True)
        for s in patient.get("symptoms", []): st.markdown(f'<div style="font-size:0.9rem; color:#334155; margin-bottom:6px;">• {re.sub(r"\(.*?\)", "", s)}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">이학적 검사결과</div>', unsafe_allow_html=True)
        for sec_name, items in patient.get("physical_exam", {}).items():
            st.markdown(f'<div style="font-weight:800; color:#1e3a8a; margin-top:12px; margin-bottom:6px;">[{re.sub(r"\(.*?\)", "", sec_name)}]</div>', unsafe_allow_html=True)
            for i in items:
                # 🚨 맨손근력 및 반사 검사 들여쓰기 
                if "맨손근력" in sec_name or "MMT" in sec_name.upper():
                    parts = i.split(" - ", 1)
                    if len(parts) == 2:
                        st.markdown(f'<div style="font-size:0.9rem; margin-bottom:2px;">• <span style="font-weight:700;">{re.sub(r"\(.*?\)", "", parts[0])}</span></div>', unsafe_allow_html=True)
                        st.markdown(f'<div style="font-size:0.8rem; color:#64748b; margin-left:14px; margin-bottom:8px;">└ 지배신경 및 레벨: {parts[1]}</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div style="font-size:0.9rem; color:#334155; margin-bottom:8px;">• {i}</div>', unsafe_allow_html=True)
                elif "반사 검사" in sec_name:
                    st.markdown(f'<div style="font-size:0.9rem; color:#334155; margin-bottom:6px;">• {i}</div>', unsafe_allow_html=True)
                else:
                    parts = i.split(":", 1)
                    if len(parts) == 2:
                        st.markdown(f'<div style="font-size:0.9rem; margin-bottom:6px;">• <span style="font-weight:700;">{re.sub(r"\(.*?\)", "", parts[0])}:</span> <span style="color:#334155;">{parts[1]}</span></div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div style="font-size:0.9rem; color:#334155; margin-bottom:6px;">• {i}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        grouped = split_findings_by_domain(findings)
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="section-title">근전도 검사 결과</div>', unsafe_allow_html=True)
        if grouped["sensory"]: _render_finding_block(f"🖐️ 감각신경전도검사 (병변측: {side})", grouped["sensory"], side)
        if grouped["motor"]: _render_finding_block(f"⚡ 운동신경전도검사 (병변측: {side})", grouped["motor"], side)
        if grouped["muscle"] and "눈꺼풀" not in selected and "뇌졸중" not in selected: _render_finding_block(f"🪡 침근전도검사 (병변측: {side})", grouped["muscle"], side)
        if grouped["reflex"] or grouped["other"]:
            merged = {**grouped["reflex"], **grouped["other"]}
            if "뇌졸중" in selected: _render_finding_block(f"🔄 H-반사 유발 검사 (병변측: {side})", merged, side)
            elif "눈꺼풀" in selected: _render_finding_block(f"👁️ 눈깜빡반사 회로 분석 (병변측: {side})", merged, side)
            else: _render_finding_block(f"🔄 반사 및 후기반응 소견 (병변측: {side})", merged, side)
        st.markdown('</div>', unsafe_allow_html=True)

        # 🚨 진단명 카드 포맷팅 개선
        diag_name = f"{side} {case.get('category', '')}" if "뇌졸중" not in selected else "위운동신경세포(UMN) 중증 경직 소견"
        kor_diag = diag_name.split('(')[0].strip()
        eng_diag = f"({diag_name.split('(')[1]}" if '(' in diag_name else ""
        
        st.markdown(f"""
        <div style="background:#f8fafc; border-left:4px solid #64748b; padding:14px; border-radius:6px; margin-bottom:20px;">
            <span style="font-size:1.0rem; font-weight:800; color:#475569; margin-right:8px;">의심질환 추정 진단명:</span>
            <span style="font-size:1.0rem; font-weight:800; color:#b91c1c;">{kor_diag}</span>
            <span style="font-size:0.85rem; font-weight:500; color:#94a3b8; margin-left:4px;">{eng_diag}</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">검사 결과 통합 해석</div>', unsafe_allow_html=True)
        if teaching.get("ncs_reason"):
            label = "눈깜박반사 해석 포인트" if ("눈꺼풀" in selected or "얼굴" in selected) else "H-반사 해석 포인트" if "뇌졸중" in selected else "신경전도 해석 포인트"
            st.markdown(f'<div class="sub-title">{label}</div>', unsafe_allow_html=True)
            render_interpretation_text(teaching["ncs_reason"])
            
        if teaching.get("emg_reason"):
            if not ("Blink Reflex" in str(teaching["emg_reason"][0]) or "H-reflex" in str(teaching["emg_reason"][0]) or "눈꺼풀" in selected or "뇌졸중" in selected):
                st.markdown('<div class="sub-title">침근전도 해석 포인트</div>', unsafe_allow_html=True)
                render_interpretation_text(teaching["emg_reason"])
                
        if teaching.get("integration"):
            st.markdown('<div class="sub-title">통합 해석</div>', unsafe_allow_html=True)
            render_interpretation_text(teaching["integration"])
        st.markdown('</div>', unsafe_allow_html=True)

        if diff_dx:
            st.markdown('<div class="content-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">감별진단 포인트</div>', unsafe_allow_html=True)
            for idx, d in enumerate(diff_dx):
                st.markdown(f'<div style="font-weight:800; font-size:0.95rem; color:#0f172a; margin-top:8px; margin-bottom:8px;">{re.sub(r"\(.*?\)", "", d.get("name",""))}</div>', unsafe_allow_html=True)
                # 🚨 물음표(?) 및 콜론 형식 적용
                st.markdown(f'<div style="font-size:0.9rem; margin-bottom:6px;"><span style="font-weight:700; color:#1d4ed8;">왜 고려하나?:</span> <span style="color:#334155;">{re.sub(r"\(.*?\)", "", d.get("why_consider",""))}</span></div>', unsafe_allow_html=True)
                st.markdown(f'<div style="font-size:0.9rem; margin-bottom:6px;"><span style="font-weight:700; color:#1d4ed8;">어떻게 구분하나?:</span> <span style="color:#334155;">{re.sub(r"\(.*?\)", "", d.get("how_to_differentiate",""))}</span></div>', unsafe_allow_html=True)
                st.markdown(f'<div style="font-size:0.9rem; margin-bottom:6px;"><span style="font-weight:700; color:#15803d;">실전 팁:</span> <span style="color:#15803d; font-weight:500;">{re.sub(r"\(.*?\)", "", d.get("practical_tip",""))}</span></div>', unsafe_allow_html=True)
                if idx < len(diff_dx) - 1: st.markdown('<div style="height:1px; background:#e2e8f0; margin:16px 0;"></div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="nav-wrapper" style="margin-top: 24px; margin-bottom: 12px;">', unsafe_allow_html=True)
        col_l, col_c, col_r = st.columns([1, 1.5, 1])
        with col_c:
            if st.button("다른 사례 분석", type="primary", use_container_width=True):
                st.session_state["case_reset_counter"] += 1
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    render_bottom_navigation()
