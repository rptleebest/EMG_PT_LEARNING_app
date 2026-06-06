# ui/case_learning.py

import re
import streamlit as st
from data.cases import CASE_LIBRARY
from data.terms import ncs_amplitude_latency, emg_case_label, special_term_label
# 에러 원인이었던 외부 의존성을 제거하고 아래에 내부 함수로 내장했습니다.
from ui.navigation import render_bottom_navigation
from helpers import lesion_side_index
from formatters import html_escape, clean_html

def _categorize_findings(findings):
    """외부 모듈 의존성 에러 방지를 위해 파일 내부에 엔진을 내장합니다."""
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
    if any(a in text for a in ["비정상적", "감소", "지연", "소실"]): return "text-red"
    if any(n in text for n in ["정상", "침묵", "보존"]): return "text-blue"
    return "text-normal"

def _inject_css():
    st.markdown(
        """
        <style>
            /* 시각적 피로도를 낮춘 본문 400 굵기와 부드러운 텍스트 색상 */
            .case-text-block, .case-bullet { text-align: left !important; word-break: keep-all !important; line-height: 1.65 !important; font-weight: 400; color: #334155; font-size: 0.95rem; }
            .header-label { font-weight: 700 !important; font-size: 1.05rem !important; color: #1e293b !important; margin-bottom: 8px; }
            
            /* 표 헤더 색상 연화 및 테두리 */
            .edu-table th { background-color: #f8fafc !important; color: #475569 !important; border: 1px solid #e2e8f0 !important; padding: 10px; text-align: center; font-weight: 700; }
            .edu-table td { border: 1px solid #e2e8f0 !important; color: #334155 !important; padding: 10px; text-align: center; font-weight: 400; font-size: 0.9rem; }
            .edu-table td.left { font-weight: 700 !important; color: #0f172a !important; background-color: #f8fafc !important; text-align: left; }
            
            /* 파스텔 톤 배지(Badge) 형태 강조 */
            .text-red { color: #c2410c !important; font-weight: 600; background-color: #fff7ed; padding: 2px 6px; border-radius: 4px; }
            .text-blue { color: #1d4ed8 !important; font-weight: 600; background-color: #eff6ff; padding: 2px 6px; border-radius: 4px; }
            
            div[role="radiogroup"] > label { width: 100% !important; background-color: #ffffff; border: 1px solid #e2e8f0 !important; border-radius: 8px; padding: 12px; margin-bottom: 8px; display: flex; font-weight: 400; box-shadow: 0 1px 2px rgba(0,0,0,0.05); cursor: pointer; }
            div[role="radiogroup"] > label:hover { background-color: #f8fafc !important; }
        </style>
        """, unsafe_allow_html=True
    )

def _render_simple_table(headers, rows):
    th = "".join([f"<th>{html_escape(h)}</th>" for h in headers])
    tr = "".join([f"<tr>{''.join([f'<td class=\"left\" data-label=\"{headers[i]}\"><span>{str(col)}</span></td>' if i==0 else f'<td class=\"{_color_class_for_text(col)}\" data-label=\"{headers[i]}\"><span>{str(col)}</span></td>' for i, col in enumerate(row)])}</tr>" for row in rows])
    return clean_html(f'<div style="overflow-x:auto; margin-bottom:1.5rem;"><table class="edu-table" style="width:100%; border-collapse:collapse;"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>')

def _render_teaching_result(teaching, diff_dx):
    st.markdown('<div style="margin-top: 35px; padding-top: 20px; border-top: 2px dashed #cbd5e1;"><div class="header-label" style="font-size: 1.15rem !important;">🔍 검사 결과 단계별 통합 해석</div>', unsafe_allow_html=True)
    
    # 4단계 분리형 파스텔 박스 렌더링
    steps = [
        ("sensory_reason", "1단계: 감각신경전도검사(SNAP) 해석", "#3b82f6", "#eff6ff"),
        ("motor_reason", "2단계: 운동신경전도검사(CMAP) 해석", "#10b981", "#f0fdf4"),
        ("emg_reason", "3단계: 침근전도검사(Needle EMG) 해석", "#f59e0b", "#fffbeb"),
        ("reflex_reason", "4단계: 특수 및 반사검사 해석", "#8b5cf6", "#faf5ff")
    ]
    
    for key, label, border_color, bg_color in steps:
        items = teaching.get(key, [])
        if items:
            st.markdown(f'<div style="border-left: 5px solid {border_color}; background-color: {bg_color}; padding: 10px 14px; font-weight: 700; font-size: 1rem; color: #1e293b; margin-bottom: 10px; border-radius: 0 8px 8px 0;">{label}</div>', unsafe_allow_html=True)
            for t in items:
                # 번호가 있는 문장은 살짝 강조, 일반 불릿 문장은 400 굵기 적용
                if re.match(r"^\d+[\)\.]", t.strip()):
                    st.markdown(f'<div style="color: #0f172a; font-size: 0.95rem; font-weight: 600; margin-top: 10px; margin-bottom: 4px; padding-left: 5px;">{html_escape(t)}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="case-bullet" style="margin-bottom: 8px; padding-left: 12px; font-weight: 400; color: #475569;">• {html_escape(t)}</div>', unsafe_allow_html=True)
            st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)

    st.markdown('<div style="border-left: 5px solid #dc2626; background-color: #fef2f2; padding: 10px 14px; font-weight: 700; font-size: 1rem; color: #991b1b; margin-top: 10px; margin-bottom: 12px; border-radius: 0 8px 8px 0;">최종 검사결과 추정 질환</div>', unsafe_allow_html=True)
    for t in teaching.get("integration", []):
        if "🎯" in t or "추정" in t:
            st.markdown(f'<div style="color: #dc2626; font-size: 1.05rem; font-weight: 700; margin-bottom: 8px; padding-left: 5px;">{html_escape(t)}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="case-text-block" style="margin-bottom: 8px; padding-left: 5px; font-weight: 400;">{html_escape(t)}</div>', unsafe_allow_html=True)
    
    if diff_dx:
        st.markdown('<div style="border-left: 5px solid #6366f1; background-color: #f5f3ff; padding: 10px 14px; font-weight: 700; font-size: 1rem; color: #4338ca; margin-top: 25px; border-radius: 0 8px 8px 0;">⚖️ 감별진단 가이드</div>', unsafe_allow_html=True)
        for item in diff_dx:
            st.markdown(f'<div style="color: #4338ca; font-weight: 700; font-size: 0.95rem; margin-top: 10px; padding-left: 5px;">{html_escape(item.get("name", ""))}</div><div class="case-text-block" style="font-size: 0.9rem; padding-left: 15px; font-weight: 400;">• {html_escape(item.get("how_to_differentiate", ""))}</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

def render_case_list():
    _inject_css()
    st.markdown('<div style="font-size: 1.5rem; font-weight: 700; color: #0f172a; margin-bottom: 1.2rem;">📊 사례 학습 모드</div>', unsafe_allow_html=True)
    
    if "case_reset_counter" not in st.session_state: st.session_state["case_reset_counter"] = 0
    st.markdown('<div class="header-label">학습할 임상 증상 선택</div>', unsafe_allow_html=True)
    selected = st.radio("사례선택", ["선택 안 함"] + list(CASE_LIBRARY.keys()), key=f"sel_{st.session_state['case_reset_counter']}", label_visibility="collapsed")
    
    if selected != "선택 안 함":
        case = CASE_LIBRARY[selected]
        pat = case["patient"]
        raw_side = pat.get("side", "-")
        st.markdown(f'<div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px; margin-top: 15px;"><div class="header-label">👤 환자 기본 정보</div><div class="case-text-block"><b>연령/성별:</b> {pat.get("age")} / {pat.get("sex")} &nbsp;|&nbsp; <b>병변측:</b> {raw_side}<br/><br/><b>주요 증상:</b><br/>{"<br/>".join(pat.get("symptoms", []))}</div></div>', unsafe_allow_html=True)
        
        st.markdown('<div style="background-color: #fffbeb; border: 1px solid #fde68a; border-radius: 6px; padding: 12px; margin-top: 20px; color: #b45309; font-size: 0.9rem; font-weight: 600;">💡 학습 팁: 아래 표는 병변측의 검사 결과만을 요약한 것이며, 의협 6.1판 신용어를 따릅니다.</div>', unsafe_allow_html=True)

        # 내장된 엔진 호출로 에러 방지
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
        
        st.markdown("<div style='margin-top:40px;'></div>", unsafe_allow_html=True)
        if st.button("🔄 다른 사례 학습하기", type="primary", use_container_width=True):
            st.session_state["case_reset_counter"] += 1
            st.rerun()
    else:
        render_bottom_navigation()

def render_case_detail():
    st.session_state["screen"] = "case_list"
    st.rerun()
