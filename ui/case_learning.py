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
    abnormals = ["반응 소실", "소실", "지연", "감소", "느림", "전도차단", "증가", "Absent", "Delayed", "Reduced", "No Response", "fibrillation", "positive sharp", "Reduced MU recruitment", "Giant"]
    normals = ["Silent", "Normal", "정상", "보존", "Normal Range"]
    if any(a in text for a in abnormals): return "text-red"
    if any(n in text for n in normals): return "text-blue"
    return "text-normal"

def _count_abnormalities(findings, side, parser_func):
    count = 0
    for item, values in findings.items():
        if _is_bilateral_side(side):
            left = parser_func(values[0] if len(values) > 0 else "")
            right = parser_func(values[1] if len(values) > 1 else "")
            if any(_color_class_for_text(v) == "text-red" for v in list(left.values()) + list(right.values())):
                count += 1
        else:
            lesion_val = parser_func(_get_value_for_lesion_side(values, side))
            if any(_color_class_for_text(v) == "text-red" for v in lesion_val.values()):
                count += 1
    return count

def _inject_css():
    st.markdown(
        """
        <style>
            .case-text-block, .result-text, .case-bullet { text-align: justify !important; text-justify: inter-word !important; line-height: 1.6 !important; }
            .exam-header-sensory { color: #1e3a8a !important; background-color: #eff6ff !important; font-weight: 800 !important; font-size: 0.95rem !important; padding: 6px 12px !important; border-left: 5px solid #3b82f6 !important; border-radius: 4px !important; margin-top: 14px !important; margin-bottom: 8px !important; }
            .exam-header-motor { color: #14532d !important; background-color: #f0fdf4 !important; font-weight: 800 !important; font-size: 0.95rem !important; padding: 6px 12px !important; border-left: 5px solid #10b981 !important; border-radius: 4px !important; margin-top: 14px !important; margin-bottom: 8px !important; }
            .exam-header-reflex { color: #7f1d1d !important; background-color: #fef2f2 !important; font-weight: 800 !important; font-size: 0.95rem !important; padding: 6px 12px !important; border-left: 5px solid #ef4444 !important; border-radius: 4px !important; margin-top: 14px !important; margin-bottom: 8px !important; }
            .exam-header-default { color: #0f172a !important; background-color: #f8fafc !important; font-weight: 800 !important; font-size: 0.95rem !important; padding: 6px 12px !important; border-left: 5px solid #9ca3af !important; border-radius: 4px !important; margin-top: 14px !important; margin-bottom: 8px !important; }
            .edu-table th { background-color: #f8fafc !important; color: #334155 !important; border: 1px solid #e2e8f0 !important; }
            .edu-table td { border: 1px solid #e2e8f0 !important; color: #475569; }
            .edu-table td.left { font-weight: 700 !important; color: #0f172a !important; background-color: #f0fdfa !important; }
            .text-red { color: #dc2626 !important; font-weight: 600; background-color: #fef2f2; border-radius: 4px; padding: 2px 4px; }
            .text-blue { color: #2563eb !important; font-weight: 600; background-color: #eff6ff; border-radius: 4px; padding: 2px 4px; }
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
    st.markdown('<div style="font-size: 1.1rem; font-weight: 800; color: #1e293b; margin-top: 20px; border-bottom: 2px solid #e2e8f0; padding-bottom: 5px;">🧪 이학적 검사결과</div>', unsafe_allow_html=True)
    pe = patient.get("physical_exam", {})
    if not pe: return
    html = []
    for section_name, items in pe.items():
        sn = _clean_exam_text(section_name) or "검사"
        h_class = "exam-header-sensory" if "감각" in sn else "exam-header-motor" if ("MMT" in sn or "근력" in sn) else "exam-header-reflex" if "반사" in sn else "exam-header-default"
        html.append(f'<div class="{h_class}">[{html_escape(sn)}]</div>')
        for line in items:
            parts = line.split(":", 1)
            if len(parts) == 2: html.append(f'<div class="case-bullet"><span style="font-weight:700; color:#334155;">{html_escape(parts[0].strip())}:</span> {html_escape(parts[1].strip())}</div>')
            else: html.append(f'<div class="case-bullet">• {html_escape(line)}</div>')
    st.markdown(f'<div class="case-text-block">{"".join(html)}</div>', unsafe_allow_html=True)

def _render_simple_table(headers, rows):
    th = "".join([f"<th>{html_escape(h)}</th>" for h in headers])
    tr = "".join([f"<tr>{''.join([f'<td class=\"left\"' if i==0 else f'<td class=\"{_color_class_for_text(col)}\"' for i, col in enumerate(row)])}>{html_escape(str(col))}</td>" for row in rows])
    return clean_html(f'<div class="edu-table-wrap"><table class="edu-table"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>')

def _render_teaching_result(teaching, diff_dx):
    st.markdown('<div style="margin-top: 25px; padding-top: 15px; border-top: 2px dashed #e2e8f0;"><div style="font-size: 1.2rem; font-weight: 800; color: #1e293b; margin-bottom: 15px;">검사 결과 단계별 통합 해석</div>', unsafe_allow_html=True)
    
    for key, label, c1, c2 in [("ncs_reason", "신경전도검사(NCS) 해석", "#3b82f6", "#eff6ff"), ("emg_reason", "침근전도검사(Needle EMG) 해석", "#10b981", "#ecfdf5")]:
        items = teaching.get(key, [])
        if items:
            st.markdown(f'<div style="border-left: 4px solid {c1}; background-color: {c2}; padding: 8px 12px; font-weight: 700; color: #1e293b; margin-bottom: 8px;">{label}</div>', unsafe_allow_html=True)
            for t in items: st.markdown(f'<div style="color: #334155; font-size: 0.95rem; margin-bottom: 6px; padding-left: 10px;">• {html_escape(t)}</div>', unsafe_allow_html=True)

    st.markdown('<div style="border-left: 4px solid #dc2626; background-color: #fef2f2; padding: 8px 12px; font-weight: 700; color: #991b1b; margin-bottom: 12px;">검사결과 추정 질환</div>', unsafe_allow_html=True)
    for t in teaching.get("integration", []):
        t_clean = t.replace("[추정 질환]", "추정 질환:").strip()
        st.markdown(f'<div style="color: #1e293b; font-size: 0.95rem; line-height: 1.6; margin-bottom: 8px; padding-left: 10px;">{html_escape(t_clean)}</div>', unsafe_allow_html=True)
    
    if diff_dx:
        st.markdown('<div style="border-left: 4px solid #9333ea; background-color: #faf5ff; padding: 8px 12px; font-weight: 700; color: #6b21a8; margin-bottom: 8px;">감별진단 가이드</div>', unsafe_allow_html=True)
        for item in diff_dx:
            st.markdown(f'<div style="color: #4c1d95; font-weight:700; font-size: 0.9rem; padding-left: 10px;">{html_escape(item.get("name"))}</div><div style="color: #334155; font-size: 0.9rem; margin-bottom: 6px; padding-left: 20px;">- 감별점: {html_escape(item.get("how_to_differentiate"))}</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

def render_case_list():
    _inject_css()
    st.markdown('<div style="font-size: 1.5rem; font-weight: 800; color: #1e293b; margin-bottom: 1rem;">사례 학습 모드</div>', unsafe_allow_html=True)
    
    if "case_reset_counter" not in st.session_state: st.session_state["case_reset_counter"] = 0
    selected = st.radio("학습할 임상 증상 선택", ["선택 안 함"] + list(CASE_LIBRARY.keys()), key=f"sel_{st.session_state['case_reset_counter']}", label_visibility="collapsed")
    
    if selected != "선택 안 함":
        case = CASE_LIBRARY[selected]
        pat = case["patient"]
        raw_side = pat.get("side", "-")
        st.markdown(f'<div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 15px; margin-bottom: 15px;"><div style="font-size: 1.1rem; font-weight: 800; color: #1e293b; margin-bottom: 8px;">환자 기본 정보</div><div style="font-size: 0.9rem; color: #475569;"><b>연령/성별:</b> {pat.get("age")} / {pat.get("sex")} &nbsp;|&nbsp; <b>병변측:</b> {raw_side}</div><div style="font-size: 0.9rem; color: #334155; margin-top:5px;"><b>주요 증상:</b> {", ".join(pat.get("symptoms", []))}</div></div>', unsafe_allow_html=True)
        _render_physical_exam(pat)

        findings = case.get("findings", {})
        grouped = split_findings_by_domain(findings, ANATOMY)

        st.markdown('<div style="margin-top: 25px; padding-top: 15px; border-top: 2px dashed #e2e8f0;">', unsafe_allow_html=True)
        
        if grouped["sensory"]:
            cnt = _count_abnormalities(grouped["sensory"], raw_side, ncs_amplitude_latency)
            st.markdown(f'<div style="font-weight: 700; color: #0f766e; margin-top: 15px;">감각신경전도검사 (SNAP) <span style="color:#ef4444; font-size:0.85em; background:#fef2f2; padding:2px 6px; border-radius:10px;">이상 소견: {cnt}개 신경</span></div>', unsafe_allow_html=True)
            rows = [[k, ncs_amplitude_latency(_get_value_for_lesion_side(v, raw_side)).get("amplitude"), ncs_amplitude_latency(_get_value_for_lesion_side(v, raw_side)).get("latency")] for k, v in grouped["sensory"].items()]
            st.markdown(_render_simple_table(["검사 신경", "진폭", "잠복기"], rows), unsafe_allow_html=True)

        if grouped["motor"]:
            cnt = _count_abnormalities(grouped["motor"], raw_side, ncs_amplitude_latency)
            st.markdown(f'<div style="font-weight: 700; color: #0f766e; margin-top: 15px;">운동신경전도검사 (CMAP) <span style="color:#ef4444; font-size:0.85em; background:#fef2f2; padding:2px 6px; border-radius:10px;">이상 소견: {cnt}개 신경</span></div>', unsafe_allow_html=True)
            rows = [[k, ncs_amplitude_latency(_get_value_for_lesion_side(v, raw_side)).get("amplitude"), ncs_amplitude_latency(_get_value_for_lesion_side(v, raw_side)).get("latency")] for k, v in grouped["motor"].items()]
            st.markdown(_render_simple_table(["검사 신경", "진폭", "잠복기"], rows), unsafe_allow_html=True)

        if grouped["muscle"]:
            cnt = _count_abnormalities(grouped["muscle"], raw_side, emg_case_label)
            st.markdown(f'<div style="font-weight: 700; color: #b45309; margin-top: 15px;">침근전도검사 (Needle EMG) <span style="color:#ef4444; font-size:0.85em; background:#fef2f2; padding:2px 6px; border-radius:10px;">이상 소견: {cnt}개 근육</span></div>', unsafe_allow_html=True)
            rows = [[k, emg_case_label(_get_value_for_lesion_side(v, raw_side)).get("rest"), emg_case_label(_get_value_for_lesion_side(v, raw_side)).get("volition")] for k, v in grouped["muscle"].items()]
            st.markdown(_render_simple_table(["검사 근육", "휴식 시", "수의수축 시"], rows), unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)
        _render_teaching_result(case.get("teaching_diagnosis", {}), case.get("differential_diagnosis", []))

        st.markdown('<div style="margin-top:30px;">', unsafe_allow_html=True)
        if st.button("다른 사례 분석", type="secondary", use_container_width=True):
            st.session_state["case_reset_counter"] += 1
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    render_bottom_navigation()

# === 누락되었던 필수 라우팅 함수 복원 ===
def render_case_detail():
    """router.py에서 호출하는 상세 페이지 렌더링 함수"""
    st.session_state["screen"] = "case_list"
    st.rerun()
