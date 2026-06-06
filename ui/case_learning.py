# ui/case_learning.py

import html as html_lib
import re
import streamlit as st
from data.cases import CASE_LIBRARY
from data.constants import ANATOMY
from data.terms import ncs_amplitude_latency, emg_case_label, special_term_label
from engine.inference import split_findings_by_domain
from ui.navigation import render_bottom_navigation
from helpers import side_to_korean, lesion_side_index
from formatters import html_escape, clean_html

def _is_bilateral_side(side):
    return str(side).strip().lower() in {"양측", "양쪽", "both", "bilateral"}

def _get_value_for_lesion_side(values, side):
    idx = lesion_side_index(side)
    if idx is None: return None
    if len(values) > idx: return values[idx]
    return values[0] if values else ""

def _color_class_for_text(text):
    text = str(text)
    abnormals = ["반응 소실", "소실", "지연", "감소", "느림", "전도차단", "증가", "비정상적 증가", "Absent", "Delayed", "Reduced", "No Response", "fibrillation", "positive sharp", "Reduced MU recruitment", "Giant"]
    normals = ["Silent", "Normal", "정상", "보존", "Normal Range", "통증 및 환자 협조 부족으로 검사 제한"]
    if any(a in text for a in abnormals): return "text-red"
    if any(n in text for n in normals): return "text-blue"
    return "text-normal"

def _has_abnormality(parsed_data):
    """딕셔너리인지 문자열인지 판별하여 유연하게 에러 없이 색상을 검사합니다."""
    if isinstance(parsed_data, dict):
        return any(_color_class_for_text(v) == "text-red" for v in parsed_data.values() if v)
    return _color_class_for_text(parsed_data) == "text-red"

def _count_abnormalities(findings, side, parser_func):
    count = 0
    for item, values in findings.items():
        if _is_bilateral_side(side):
            left = parser_func(values[0] if len(values) > 0 else "")
            right = parser_func(values[1] if len(values) > 1 else "")
            if _has_abnormality(left) or _has_abnormality(right): 
                count += 1
        else:
            lesion_val = parser_func(_get_value_for_lesion_side(values, side))
            if _has_abnormality(lesion_val): 
                count += 1
    return count

def _inject_css():
    st.markdown(
        """
        <style>
            /* 텍스트 가독성 최적화: 왼쪽 정렬 및 단어 단위 줄바꿈 유지 */
            .case-text-block, .result-text, .case-bullet { 
                text-align: left !important; 
                word-break: keep-all !important; 
                line-height: 1.6 !important; 
            }
            
            /* 이학적 검사 파스텔톤 부드러운 헤더 */
            .exam-header-sensory { color: #1e3a8a !important; background-color: #eff6ff !important; font-weight: 800 !important; font-size: 0.95rem !important; padding: 6px 12px !important; border-left: 5px solid #3b82f6 !important; border-radius: 4px !important; margin-top: 14px !important; margin-bottom: 8px !important; }
            .exam-header-motor { color: #14532d !important; background-color: #f0fdf4 !important; font-weight: 800 !important; font-size: 0.95rem !important; padding: 6px 12px !important; border-left: 5px solid #10b981 !important; border-radius: 4px !important; margin-top: 14px !important; margin-bottom: 8px !important; }
            .exam-header-reflex { color: #7f1d1d !important; background-color: #fef2f2 !important; font-weight: 800 !important; font-size: 0.95rem !important; padding: 6px 12px !important; border-left: 5px solid #ef4444 !important; border-radius: 4px !important; margin-top: 14px !important; margin-bottom: 8px !important; }
            .exam-header-default { color: #0f172a !important; background-color: #f8fafc !important; font-weight: 800 !important; font-size: 0.95rem !important; padding: 6px 12px !important; border-left: 5px solid #9ca3af !important; border-radius: 4px !important; margin-top: 14px !important; margin-bottom: 8px !important; }
            
            /* 라디오 버튼 100% 폭 맞춤 및 색상 시각적 위계화 */
            div[role="radiogroup"] > label {
                width: 100% !important;
                background-color: #f0fdf4 !important;
                border: 1px solid #bbf7d0 !important;
                border-left: 5px solid #10b981 !important;
                border-radius: 8px !important;
                padding: 10px 15px !important;
                margin-bottom: 8px !important;
                transition: all 0.2s ease;
                display: flex;
            }
            div[role="radiogroup"] > label:first-child {
                background-color: #e2e8f0 !important;
                border: 1px solid #cbd5e1 !important;
                border-left: 5px solid #64748b !important;
            }
            
            /* 반응형 테이블 (파스텔톤) */
            .edu-table th { background-color: #f1f5f9 !important; color: #1e293b !important; border: 1px solid #cbd5e1 !important; padding: 10px; text-align: center; }
            .edu-table td { border: 1px solid #cbd5e1 !important; color: #334155; padding: 10px; text-align: center; vertical-align: middle; }
            .edu-table td.left { font-weight: 800 !important; color: #0f172a !important; background-color: #f8fafc !important; text-align: left; }
            .text-red { color: #b91c1c !important; font-weight: 800; background-color: #fef2f2; border-radius: 4px; padding: 3px 6px; }
            .text-blue { color: #1d4ed8 !important; font-weight: 800; background-color: #eff6ff; border-radius: 4px; padding: 3px 6px; }
            
            @media screen and (max-width: 700px) {
                .edu-table thead { display: none; }
                .edu-table tr { display: block; border: 1px solid #e2e8f0; border-radius: 8px; margin-bottom: 0.8rem; background: #ffffff; box-shadow: 0 1px 2px rgba(0,0,0,0.05); }
                .edu-table td { display: flex; justify-content: space-between; align-items: flex-start; gap: 0.75rem; border: none; border-bottom: 1px solid #f8fafc; padding: 0.6rem 0.7rem; text-align: right; word-break: keep-all; }
                .edu-table td:last-child { border-bottom: none; }
                .edu-table td::before { content: attr(data-label); font-weight: 800; color: #475569; text-align: left; font-size: 0.8rem; flex: 0 0 38%; }
                .edu-table td > span { flex: 1; text-align: right; }
                .edu-table td.left { display: block; background: #f8fafc; text-align: left; padding: 0.7rem; color: #0f172a; font-weight: 800; border-radius: 8px 8px 0 0; }
                .edu-table td.left::before { content: none; }
                .edu-table td.left > span { display: block; text-align: left; }
            }
        </style>
        """, unsafe_allow_html=True
    )

def _clean_exam_text(text):
    if text is None: return ""
    cleaned = str(text)
    for _ in range(5):
        n = html_lib.unescape(cleaned)
        if n == cleaned: break
        cleaned = n
    cleaned = re.sub(r"<[^>]+>", "", cleaned)
    return "\n".join([line.strip() for line in cleaned.splitlines() if line.strip()])

def _render_physical_exam(patient):
    st.markdown('<div style="font-size: 1.1rem; font-weight: 800; color: #1e293b; margin-top: 20px; border-bottom: 2px solid #cbd5e1; padding-bottom: 5px;">🧪 이학적 검사결과</div>', unsafe_allow_html=True)
    pe = patient.get("physical_exam", {})
    if not pe: return
    html = []
    for section_name, items in pe.items():
        sn = _clean_exam_text(section_name) or "검사"
        h_class = "exam-header-sensory" if "감각" in sn else "exam-header-motor" if ("MMT" in sn or "근력" in sn or "표정근" in sn) else "exam-header-reflex" if "반사" in sn else "exam-header-default"
        html.append(f'<div class="{h_class}">[{html_escape(sn)}]</div>')
        for line in items:
            parts = line.split(":", 1)
            if len(parts) == 2: html.append(f'<div class="case-bullet"><span style="font-weight:800; color:#1e293b;">{html_escape(parts[0].strip())}:</span> {html_escape(parts[1].strip())}</div>')
            else: html.append(f'<div class="case-bullet">• {html_escape(line)}</div>')
    st.markdown(f'<div class="case-text-block">{"".join(html)}</div>', unsafe_allow_html=True)

def _render_simple_table(headers, rows):
    th = "".join([f"<th>{html_escape(h)}</th>" for h in headers])
    tr = "".join([f"<tr>{''.join([f'<td class=\"left\" data-label=\"{html_escape(headers[i])}\"><span>{html_escape(str(col))}</span></td>' if i==0 else f'<td class=\"{_color_class_for_text(col)}\" data-label=\"{html_escape(headers[i])}\"><span>{html_escape(str(col))}</span></td>' for i, col in enumerate(row)])}</tr>" for row in rows])
    return clean_html(f'<div style="overflow-x:auto; margin-bottom:1rem;"><table class="edu-table" style="width:100%; border-collapse:collapse;"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>')

def _render_teaching_result(teaching, diff_dx):
    st.markdown('<div style="margin-top: 35px; padding-top: 15px; border-top: 2px dashed #cbd5e1;"><div style="font-size: 1.2rem; font-weight: 900; color: #0f172a; margin-bottom: 15px;">🔍 검사 결과 단계별 통합 해석</div>', unsafe_allow_html=True)
    
    # 동적 렌더링: 데이터가 있는 검사 항목만 헤더를 생성하여 출력
    sections = [
        ("ncs_reason", "신경전도검사(NCS) 해석", "#3b82f6", "#eff6ff"),
        ("emg_reason", "침근전도검사(Needle EMG) 해석", "#10b981", "#ecfdf5"),
        ("reflex_reason", "특수 및 반사검사 해석", "#9333ea", "#faf5ff")
    ]
    
    for key, label, c1, c2 in sections:
        items = teaching.get(key, [])
        if items:
            st.markdown(f'<div style="border-left: 5px solid {c1}; background-color: {c2}; padding: 10px 14px; font-weight: 800; font-size: 1.05rem; color: #0f172a; margin-bottom: 10px; border-radius: 0 6px 6px 0; word-break: keep-all;">{label}</div>', unsafe_allow_html=True)
            for t in items:
                clean_t = html_escape(t)
                if re.match(r"^\d+[\)\.]", t.strip()):
                    st.markdown(f'<div style="color: #0f172a; font-size: 1.0rem; font-weight: 800; margin-top: 12px; margin-bottom: 4px; padding-left: 5px; word-break: keep-all;">{clean_t}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div style="color: #334155; font-size: 0.95rem; line-height: 1.6; margin-bottom: 8px; padding-left: 15px; word-break: keep-all;">• {clean_t}</div>', unsafe_allow_html=True)
            st.markdown("<br/>", unsafe_allow_html=True)

    st.markdown('<div style="border-left: 5px solid #dc2626; background-color: #fef2f2; padding: 10px 14px; font-weight: 800; font-size: 1.05rem; color: #7f1d1d; margin-top: 5px; margin-bottom: 12px; border-radius: 0 6px 6px 0; word-break: keep-all;">검사결과 추정 질환</div>', unsafe_allow_html=True)
    for t in teaching.get("integration", []):
        t_clean = t.replace("▶", "").strip()
        if t_clean.startswith("추정 질환:") or t_clean.startswith("추정 진단:"):
            name = t_clean.replace("추정 질환:", "").replace("추정 진단:", "").strip()
            st.markdown(f'<div style="color: #dc2626; font-size: 1.15rem; font-weight:900; margin-bottom: 10px; padding-left: 5px; word-break: keep-all;">🎯 {html_escape(name)}</div>', unsafe_allow_html=True)
        elif t_clean.startswith("추정한 이유:") or t_clean.startswith("평가 요약:"):
            reason = t_clean.replace("추정한 이유:", "").replace("평가 요약:", "").strip()
            st.markdown(f'<div style="color: #1e293b; font-size: 0.95rem; line-height: 1.6; margin-bottom: 8px; padding-left: 5px; word-break: keep-all;">💡 <span style="font-weight:800; color:#b45309;">추정한 이유:</span> {html_escape(reason)}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div style="color: #1e293b; font-size: 0.95rem; line-height: 1.6; margin-bottom: 8px; padding-left: 5px; word-break: keep-all;">{html_escape(t_clean)}</div>', unsafe_allow_html=True)
    
    if diff_dx:
        st.markdown('<div style="border-left: 5px solid #9333ea; background-color: #faf5ff; padding: 10px 14px; font-weight: 800; font-size: 1.05rem; color: #581c87; margin-top: 20px; margin-bottom: 10px; border-radius: 0 6px 6px 0; word-break: keep-all;">감별진단 가이드</div>', unsafe_allow_html=True)
        for item in diff_dx:
            name_clean = item.get("name", "").replace("▶", "").replace("⚖️", "").strip()
            st.markdown(f'<div style="color: #7e22ce; font-weight:900; font-size: 1.05rem; padding-left: 5px; margin-top: 5px; margin-bottom: 4px; word-break: keep-all;">⚖️ {html_escape(name_clean)}</div><div style="color: #334155; font-size: 0.95rem; line-height: 1.6; margin-bottom: 10px; padding-left: 25px; word-break: keep-all;">• <span style="font-weight:800; color:#4c1d95;">구분점:</span> {html_escape(item.get("how_to_differentiate"))}</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

def render_case_list():
    _inject_css()
    st.markdown('<div style="font-size: 1.6rem; font-weight: 900; color: #0f172a; margin-bottom: 1rem; word-break: keep-all;">📊 사례 학습 모드</div>', unsafe_allow_html=True)
    
    if "case_reset_counter" not in st.session_state: st.session_state["case_reset_counter"] = 0
    st.markdown('<div style="font-weight: 800; color: #1e293b; margin-bottom: 12px; font-size: 1.05rem;">학습할 임상 증상 선택</div>', unsafe_allow_html=True)
    selected = st.radio("학습할 임상 증상 선택", ["선택 안 함"] + list(CASE_LIBRARY.keys()), key=f"sel_{st.session_state['case_reset_counter']}", label_visibility="collapsed")
    
    if selected != "선택 안 함":
        case = CASE_LIBRARY[selected]
        pat = case["patient"]
        raw_side = pat.get("side", "-")
        st.markdown(f'<div style="background-color: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 18px; margin-bottom: 15px; margin-top: 20px;"><div style="font-size: 1.15rem; font-weight: 900; color: #0f172a; margin-bottom: 12px;">👤 환자 기본 정보</div><div style="font-size: 0.95rem; color: #334155;"><b>연령/성별:</b> {pat.get("age")} / {pat.get("sex")} &nbsp;|&nbsp; <b>병변측:</b> {raw_side}</div><div style="font-size: 0.95rem; color: #1e293b; margin-top:10px; line-height: 1.6; word-break: keep-all;"><b>주요 증상:</b><br/> {"<br/>".join(pat.get("symptoms", []))}</div></div>', unsafe_allow_html=True)
        
        _render_physical_exam(pat)
        
        st.markdown(
            """<div style="background-color: #fffbeb; border: 1px solid #fde68a; border-radius: 8px; padding: 12px; margin-top: 15px; margin-bottom: 10px;">
               <div style="font-size: 0.95rem; color: #b45309; font-weight: 800; line-height: 1.5; word-break: keep-all;">💡 학습 팁: 아래 신경전도 및 침근전도 표는 병변측(증상 발생 위치)의 주요 검사 결과를 요약한 것입니다.</div>
               </div>""", unsafe_allow_html=True)

        findings = case.get("findings", {})
        grouped = split_findings_by_domain(findings, ANATOMY)
        
        if grouped["sensory"]:
            cnt = _count_abnormalities(grouped["sensory"], raw_side, ncs_amplitude_latency)
            st.markdown(f'<div style="font-weight: 900; color: #1e3a8a; font-size: 1.1rem; margin-top: 25px; margin-bottom: 8px;">⚡ 감각신경전도검사 (SNAP) <span style="color:#ef4444; font-size:0.85em; background:#fef2f2; padding:2px 6px; border-radius:10px; font-weight:800;">🚨 이상 소견: {cnt}개 신경</span></div>', unsafe_allow_html=True)
            rows = [[k, ncs_amplitude_latency(_get_value_for_lesion_side(v, raw_side)).get("amplitude"), ncs_amplitude_latency(_get_value_for_lesion_side(v, raw_side)).get("latency")] for k, v in grouped["sensory"].items()]
            st.markdown(_render_simple_table(["검사 신경", "진폭", "잠복기"], rows), unsafe_allow_html=True)

        if grouped["motor"]:
            cnt = _count_abnormalities(grouped["motor"], raw_side, ncs_amplitude_latency)
            st.markdown(f'<div style="font-weight: 900; color: #14532d; font-size: 1.1rem; margin-top: 25px; margin-bottom: 8px;">⚡ 운동신경전도검사 (CMAP) <span style="color:#ef4444; font-size:0.85em; background:#fef2f2; padding:2px 6px; border-radius:10px; font-weight:800;">🚨 이상 소견: {cnt}개 신경</span></div>', unsafe_allow_html=True)
            rows = [[k, ncs_amplitude_latency(_get_value_for_lesion_side(v, raw_side)).get("amplitude"), ncs_amplitude_latency(_get_value_for_lesion_side(v, raw_side)).get("latency")] for k, v in grouped["motor"].items()]
            st.markdown(_render_simple_table(["검사 신경", "진폭", "잠복기"], rows), unsafe_allow_html=True)

        if grouped["muscle"]:
            cnt = _count_abnormalities(grouped["muscle"], raw_side, emg_case_label)
            st.markdown(f'<div style="font-weight: 900; color: #b45309; font-size: 1.1rem; margin-top: 25px; margin-bottom: 8px;">🪡 침근전도검사 (Needle EMG) <span style="color:#ef4444; font-size:0.85em; background:#fef2f2; padding:2px 6px; border-radius:10px; font-weight:800;">🚨 이상 소견: {cnt}개 근육</span></div>', unsafe_allow_html=True)
            rows = [[k, emg_case_label(_get_value_for_lesion_side(v, raw_side)).get("rest"), emg_case_label(_get_value_for_lesion_side(v, raw_side)).get("volition")] for k, v in grouped["muscle"].items()]
            st.markdown(_render_simple_table(["검사 근육", "휴식 시", "자발적 근수축 시"], rows), unsafe_allow_html=True)

        if grouped.get("reflex") or grouped.get("other"):
            merged_reflex = {**grouped.get("reflex", {}), **grouped.get("other", {})}
            if merged_reflex:
                cnt = _count_abnormalities(merged_reflex, raw_side, special_term_label)
                st.markdown(f'<div style="font-weight: 900; color: #6b21a8; font-size: 1.1rem; margin-top: 25px; margin-bottom: 8px;">⏱️ 특수 및 반사 검사 <span style="color:#ef4444; font-size:0.85em; background:#fef2f2; padding:2px 6px; border-radius:10px; font-weight:800;">🚨 이상 소견: {cnt}개 항목</span></div>', unsafe_allow_html=True)
                rows = []
                for k, v in merged_reflex.items():
                    if _is_bilateral_side(raw_side):
                        rows.append([k, special_term_label(v[0] if len(v)>0 else ""), special_term_label(v[1] if len(v)>1 else "")])
                    else:
                        rows.append([k, special_term_label(_get_value_for_lesion_side(v, raw_side))])
                headers = ["검사 항목", "좌측 결과", "우측 결과"] if _is_bilateral_side(raw_side) else ["검사 항목", "결과"]
                st.markdown(_render_simple_table(headers, rows), unsafe_allow_html=True)

        _render_teaching_result(case.get("teaching_diagnosis", {}), case.get("differential_diagnosis", []))

        st.markdown('<div style="margin-top:35px;">', unsafe_allow_html=True)
        if st.button("🔄 처음으로 돌아가기", type="primary", use_container_width=True):
            st.session_state["case_reset_counter"] += 1
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    
    render_bottom_navigation()

def render_case_detail():
    st.session_state["screen"] = "case_list"
    st.rerun()
