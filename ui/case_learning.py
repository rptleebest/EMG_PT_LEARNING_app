# ui/case_learning.py

import html as html_lib
import re
import streamlit as st
from data.cases import CASE_LIBRARY
from data.terms import ncs_amplitude_latency, emg_case_label, special_term_label
from ui.navigation import render_bottom_navigation
from helpers import lesion_side_index
from formatters import html_escape, clean_html

def _categorize_findings(findings):
    """데이터 내 키워드를 분석하여 검사 종류를 자동 분류합니다."""
    grouped = {"sensory": {}, "motor": {}, "muscle": {}, "reflex": {}}
    for k, v in findings.items():
        k_up = k.upper()
        if "SNAP" in k_up or "감각" in k: grouped["sensory"][k] = v
        elif "CMAP" in k_up or "운동" in k: grouped["motor"][k] = v
        elif any(x in k for x in ["반사", "F파", "H/M", "비율", "눈깜빡"]): grouped["reflex"][k] = v
        else: grouped["muscle"][k] = v
    return grouped

def _get_value_for_lesion_side(values, side):
    idx = lesion_side_index(side)
    if idx is None: return None
    if len(values) > idx: return values[idx]
    return values[0] if values else ""

def _color_class_for_text(text):
    text = str(text)
    if any(a in text for a in ["비정상적", "감소", "지연", "소실", "증가된"]): return "text-red"
    if any(n in text for n in ["정상", "침묵", "보존"]): return "text-blue"
    return "text-normal"

def _inject_css():
    st.markdown(
        """
        <style>
            /* 텍스트 가독성 최적화: 제목은 700, 설명문은 400(가는 글씨) */
            .case-text-block, .result-text, .case-bullet { text-align: left !important; word-break: keep-all !important; line-height: 1.6 !important; font-weight: 400; color: #444; }
            .header-label { font-weight: 700 !important; font-size: 1.05rem !important; color: #222 !important; margin-bottom: 8px; }
            
            /* 표 헤더 색상 농도 조절 */
            .edu-table th { background-color: #f1f5f9 !important; color: #475569 !important; border: 1px solid #cbd5e1 !important; padding: 10px; text-align: center; font-weight: 700; }
            .edu-table td { border: 1px solid #e2e8f0 !important; color: #334155; padding: 10px; text-align: center; font-weight: 400; }
            .edu-table td.left { font-weight: 700 !important; color: #1e293b !important; background-color: #f8fafc !important; text-align: left; }
            
            /* 강조색 채도 하향 조절 (눈 보호) */
            .text-red { color: #c2410c !important; font-weight: 600; background-color: #fff7ed; padding: 2px 4px; border-radius: 4px; }
            .text-blue { color: #1d4ed8 !important; font-weight: 600; background-color: #eff6ff; padding: 2px 4px; border-radius: 4px; }
            
            div[role="radiogroup"] > label { width: 100% !important; background-color: #f8fafc !important; border: 1px solid #e2e8f0 !important; border-radius: 8px; padding: 10px 15px !important; margin-bottom: 8px !important; display: flex; font-weight: 400; }
        </style>
        """, unsafe_allow_html=True
    )

def _render_simple_table(headers, rows):
    th = "".join([f"<th>{html_escape(h)}</th>" for h in headers])
    tr = "".join([f"<tr>{''.join([f'<td class=\"left\" data-label=\"{headers[i]}\"><span>{str(col)}</span></td>' if i==0 else f'<td class=\"{_color_class_for_text(col)}\" data-label=\"{headers[i]}\"><span>{str(col)}</span></td>' for i, col in enumerate(row)])}</tr>" for row in rows])
    return clean_html(f'<div style="overflow-x:auto; margin-bottom:1rem;"><table class="edu-table" style="width:100%; border-collapse:collapse;"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>')

def _render_teaching_result(teaching, diff_dx):
    st.markdown('<div style="margin-top: 35px; padding-top: 20px; border-top: 2px dashed #cbd5e1;"><div class="header-label">🔍 검사 결과 단계별 통합 해석</div>', unsafe_allow_html=True)
    
    # 감각 -> 운동 -> 침근전도 -> 특수반사 순서로 이원화 해석 출력
    steps = [
        ("sensory_reason", "1단계: 감각신경전도검사(SNAP) 해석", "#3b82f6", "#eff6ff"),
        ("motor_reason", "2단계: 운동신경전도검사(CMAP) 해석", "#10b981", "#ecfdf5"),
        ("emg_reason", "3단계: 침근전도검사(Needle EMG) 해석", "#f59e0b", "#fffbeb"),
        ("reflex_reason", "4단계: 특수 및 반사검사 해석", "#8b5cf6", "#faf5ff")
    ]
    
    for key, label, c1, c2 in steps:
        items = teaching.get(key, [])
        if items:
            st.markdown(f'<div style="border-left: 5px solid {c1}; background-color: {c2}; padding: 10px 14px; font-weight: 700; font-size: 1rem; color: #1e293b; margin-bottom: 10px; border-radius: 0 6px 6px 0;">{label}</div>', unsafe_allow_html=True)
            for t in items:
                if re.match(r"^\d+[\)\.]", t.strip()):
                    st.markdown(f'<div style="color: #111; font-size: 0.95rem; font-weight: 700; margin-top: 10px; margin-bottom: 4px;">{html_escape(t)}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="case-bullet" style="margin-bottom: 6px; padding-left: 10px;">• {html_escape(t)}</div>', unsafe_allow_html=True)
            st.markdown("<br/>", unsafe_allow_html=True)

    st.markdown('<div style="border-left: 5px solid #dc2626; background-color: #fef2f2; padding: 10px 14px; font-weight: 700; font-size: 1rem; color: #991b1b; margin-bottom: 12px; border-radius: 0 6px 6px 0;">최종 검사결과 추정 질환</div>', unsafe_allow_html=True)
    for t in teaching.get("integration", []):
        if "🎯" in t or "추정" in t:
            st.markdown(f'<div style="color: #dc2626; font-size: 1.1rem; font-weight: 700; margin-bottom: 8px;">{html_escape(t)}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="case-text-block" style="margin-bottom: 8px;">{html_escape(t)}</div>', unsafe_allow_html=True)
    
    if diff_dx:
        st.markdown('<div style="border-left: 5px solid #6366f1; background-color: #f5f3ff; padding: 10px 14px; font-weight: 700; font-size: 1rem; color: #4338ca; margin-top: 20px; border-radius: 0 6px 6px 0;">⚖️ 감별진단 가이드</div>', unsafe_allow_html=True)
        for item in diff_dx:
            st.markdown(f'<div style="color: #4338ca; font-weight: 700; font-size: 0.95rem; margin-top: 10px; padding-left: 5px;">{html_escape(item.get("name", ""))}</div><div class="case-text-block" style="font-size: 0.9rem; padding-left: 15px;">• {html_escape(item.get("how_to_differentiate", ""))}</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

def render_case_list():
    _inject_css()
    st.markdown('<div style="font-size: 1.6rem; font-weight: 700; color: #0f172a; margin-bottom: 1.2rem;">📊 사례 학습 모드</div>', unsafe_allow_html=True)
    
    if "case_reset_counter" not in st.session_state: st.session_state["case_reset_counter"] = 0
    st.markdown('<div class="header-label">학습할 임상 증상 선택</div>', unsafe_allow_html=True)
    selected = st.radio("사례선택", ["선택 안 함"] + list(CASE_LIBRARY.keys()), key=f"sel_{st.session_state['case_reset_counter']}", label_visibility="collapsed")
    
    if selected != "선택 안 함":
        case = CASE_LIBRARY[selected]
        pat = case["patient"]
        raw_side = pat.get("side", "-")
        st.markdown(f'<div style="background-color: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 18px; margin-top: 15px;"><div class="header-label">👤 환자 기본 정보</div><div class="case-text-block"><b>연령/성별:</b> {pat.get("age")} / {pat.get("sex")} | <b>병변측:</b> {raw_side}<br/><b>주요 증상:</b><br/>{"<br/>".join(pat.get("symptoms", []))}</div></div>', unsafe_allow_html=True)
        
        # 팁 박스 위치: 검사 표 바로 위
        st.markdown('<div style="background-color: #fffbeb; border: 1px solid #fde68a; border-radius: 6px; padding: 12px; margin-top: 20px; color: #b45309; font-size: 0.9rem; font-weight: 600;">💡 학습 팁: 아래 표는 병변측의 검사 결과만을 요약한 것이며, 용어는 의협 6.1판 신용어를 따릅니다.</div>', unsafe_allow_html=True)

        grouped = _categorize_findings(case.get("findings", {}))
        
        configs = [
            ("sensory", "⚡ 감각신경전도검사 (SNAP)", ["검사 신경", "진폭", "잠복기"], ncs_amplitude_latency),
            ("motor", "⚡ 운동신경전도검사 (CMAP)", ["검사 신경", "진폭", "잠복기"], ncs_amplitude_latency),
            ("muscle", "🪡 침근전도검사 (Needle EMG)", ["검사 근육", "휴식 시", "자발적 근수축 시"], emg_case_label),
            ("reflex", "⏱️ 특수 및 반사 검사", ["검사 항목", "결과"], special_term_label)
        ]

        for g_key, g_title, g_headers, p_func in configs:
            if grouped[g_key]:
                st.markdown(f'<div style="font-weight: 700; color: #334155; font-size: 1.05rem; margin-top: 25px; margin-bottom: 8px;">{g_title}</div>', unsafe_allow_html=True)
                rows = []
                for k, v in grouped[g_key].items():
                    val = p_func(_get_value_for_lesion_side(v, raw_side))
                    if g_key in ["sensory", "motor"]: rows.append([k, val["amplitude"], val["latency"]])
                    elif g_key == "muscle": rows.append([k, val["rest"], val["volition"]])
                    else: rows.append([k, val])
                st.markdown(_render_simple_table(g_headers, rows), unsafe_allow_html=True)

        _render_teaching_result(case.get("teaching_diagnosis", {}), case.get("differential_diagnosis", []))
        if st.button("🔄 처음으로 돌아가기", type="primary", use_container_width=True):
            st.session_state["case_reset_counter"] += 1
            st.rerun()
    else:
        render_bottom_navigation()

def render_case_detail():
    st.session_state["screen"] = "case_list"
    st.rerun()
