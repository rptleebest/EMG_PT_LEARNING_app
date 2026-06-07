# ui/case_learning.py

import html
import streamlit as st

from data.cases import CASE_LIBRARY
from ui.navigation import render_bottom_navigation

def _safe_format_code(code: str) -> str:
    """내부 코드를 화면 표시용 한글로 변환합니다."""
    mapping = {
        "ncs_normal": "정상 범위", 
        "ncs_delayed": "잠복기 지연", 
        "ncs_reduced": "진폭 감소", 
        "ncs_absent": "반응 소실", 
        "ncs_conduction_block": "진폭 급감 (국소 전도차단)",
        "emg_normal": "정상 범위", 
        "emg_active_denervation": "활동성 탈신경", 
        "emg_paraspinal_denervation": "활동성 탈신경",
        "emg_chronic_reinnervation": "만성 재신경지배", 
        "emg_active_chronic": "활동성+만성"
    }
    return mapping.get(str(code), str(code))

def _get_result_color_style(value: str) -> str:
    """결과에 따른 폰트 색상을 반환합니다."""
    text = str(value)
    abnormal_words = ["비정상", "감소", "지연", "소실", "탈신경", "재신경지배", "차단"]
    if any(w in text for w in abnormal_words): 
        return "color: #991b1b; font-weight: 700;"
    if "정상" in text: 
        return "color: #15803d; font-weight: 700;"
    return ""

def _create_responsive_table(headers: list, rows: list, table_id: str) -> str:
    if not rows: 
        return ""
        
    safe_table_id = html.escape(str(table_id), quote=True)
    
    css = f"""
    <style>
        #{safe_table_id} {{ width: 100%; border-collapse: collapse; margin-bottom: 12px; font-size: 0.9rem; }} 
        #{safe_table_id} th {{ background-color: #f8fafc; padding: 10px; border-bottom: 2px solid #cbd5e1; text-align: left; color: #1e293b; font-weight: 800; }} 
        #{safe_table_id} td {{ padding: 10px; border-bottom: 1px solid #e2e8f0; text-align: left; color: #334155; }} 
        #{safe_table_id} td.fst-col {{ font-weight: 800; color: #1e3a8a; }} 
        
        @media screen and (max-width: 768px) {{ 
            #{safe_table_id} thead {{ display: none; }} 
            #{safe_table_id} tr {{ display: block; border: 1px solid #e2e8f0; border-radius: 8px; margin-bottom: 12px; background: #ffffff; padding: 8px; }} 
            #{safe_table_id} td {{ display: flex; justify-content: space-between; align-items: center; gap: 12px; border-bottom: 1px dashed #e2e8f0; padding: 10px 8px; text-align: right; }} 
            #{safe_table_id} td:last-child {{ border-bottom: none; }} 
            #{safe_table_id} td::before {{ content: attr(data-label); font-weight: 800; color: #475569; text-align: left; font-size: 0.85rem; flex: 0 0 35%; }} 
            #{safe_table_id} td > span {{ flex: 1; text-align: right; word-break: keep-all; font-weight: 400; }} 
            #{safe_table_id} td.fst-col {{ justify-content: center; background: #f1f5f9; border-radius: 6px 6px 0 0; text-align: center; padding: 12px; }} 
            #{safe_table_id} td.fst-col::before {{ content: none; }} 
            #{safe_table_id} td.fst-col > span {{ text-align: center; font-weight: 800; color: #1e3a8a; }} 
        }}
    </style>
    """
    
    header_html = "".join([f"<th>{html.escape(h)}</th>" for h in headers])
    
    tr_html = ""
    for row in rows:
        td_html = ""
        for idx, col in enumerate(row):
            val = _safe_format_code(col)
            cls = "fst-col" if idx == 0 else ""
            color_style = _get_result_color_style(val) if idx > 0 else ""
            header_label = html.escape(headers[idx]) if idx < len(headers) else ""
            
            td_html += f"<td data-label='{header_label}' class='{cls}' style='{color_style}'><span>{html.escape(val)}</span></td>"
        tr_html += f"<tr>{td_html}</tr>"
        
    return f"{css}<table id='{safe_table_id}'><thead><tr>{header_html}</tr></thead><tbody>{tr_html}</tbody></table>"

def render_case_list():
    st.markdown('<div class="main-title">사례 학습 모드</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtle">원하는 임상 증상을 선택하면 즉시 상세 분석 결과가 아래에 표시됩니다.</div>', unsafe_allow_html=True)

    if "case_reset_counter" not in st.session_state:
        st.session_state["case_reset_counter"] = 0

    case_names = ["선택 안 함"] + list(CASE_LIBRARY.keys())
    
    selected = st.radio(
        "사례 리스트", 
        case_names, 
        index=0, 
        key=f"c_rad_{st.session_state['case_reset_counter']}", 
        label_visibility="collapsed"
    )

    if selected != "선택 안 함":
        render_case_detail_inline(selected)
    
    render_bottom_navigation()

def render_case_detail_inline(case_name: str):
    data = CASE_LIBRARY[case_name]
    patient = data.get("patient", {})
    findings = data.get("findings", {})
    teaching = data.get("teaching_diagnosis", {})

    st.markdown('<hr style="margin: 1.5rem 0; border-top: 2px dashed #cbd5e1;">', unsafe_allow_html=True)
    
    # 1. 환자 기본 정보
    st.markdown('<div class="section-label">환자 기본 정보</div>', unsafe_allow_html=True)
    st.markdown(f'<div><span class="inline-label">연령/성별:</span><span class="inline-content">{patient.get("age")}세 / {patient.get("sex")}</span></div>', unsafe_allow_html=True)
    st.markdown(f'<div><span class="inline-label">병변측:</span><span class="inline-content">{patient.get("side")}</span></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="inline-label" style="margin-top:12px; display:block;">주요 증상</div>', unsafe_allow_html=True)
    for sym in patient.get("symptoms", []):
        st.markdown(f'<div class="inline-content" style="margin-left:8px; margin-bottom:4px;">{sym}</div>', unsafe_allow_html=True)
    
    st.markdown('<hr style="margin: 1.2rem 0; border-top: 1px dotted #cbd5e1;">', unsafe_allow_html=True)

    # 2. 이학적 검사
    phys_exam = patient.get("physical_exam", {})
    if phys_exam:
        st.markdown('<div class="section-label">이학적 검사 (신경학적 진찰)</div>', unsafe_allow_html=True)
        for cat, items in phys_exam.items():
            st.markdown(f'<div class="item-title">{cat}</div>', unsafe_allow_html=True)
            for item in items: 
                st.markdown(f'<div class="inline-content" style="margin-bottom:6px;">{item}</div>', unsafe_allow_html=True)
        st.markdown('<hr style="margin: 1.2rem 0; border-top: 1px dotted #cbd5e1;">', unsafe_allow_html=True)

    # 3. 표 렌더링
    sensory_rows, motor_rows, emg_rows = [], [], []
    for test_name, result_tuple in findings.items():
        if not isinstance(result_tuple, tuple): continue
        row = [test_name] + list(result_tuple)
        if "snap" in test_name.lower() or "감각" in test_name: sensory_rows.append(row)
        elif "cmap" in test_name.lower() or "운동" in test_name: motor_rows.append(row)
        else: emg_rows.append(row)

    st.markdown('<div class="section-label">전기진단검사 결과 요약</div>', unsafe_allow_html=True)
    
    if sensory_rows:
        st.markdown('<div class="item-title">감각신경전도검사 (Sensory NCS)</div>', unsafe_allow_html=True)
        st.markdown(_create_responsive_table(["검사 신경", "진폭", "잠복기"], sensory_rows, "tbl_sen"), unsafe_allow_html=True)
        
    if motor_rows:
        st.markdown('<div class="item-title">운동신경전도검사 (Motor NCS)</div>', unsafe_allow_html=True)
        st.markdown(_create_responsive_table(["검사 신경", "진폭", "잠복기"], motor_rows, "tbl_mot"), unsafe_allow_html=True)

    if emg_rows:
        st.markdown("""
        <div style="background:#f8fafc; padding:12px; border-left:4px solid #94a3b8; margin-top:20px; margin-bottom:12px; border-radius:4px;">
            <div style="font-weight:800; color:#334155; font-size:0.95rem; margin-bottom:6px;">💡 학생용 침근전도 용어 가이드</div>
            <div style="font-size:0.9rem; line-height:1.5; margin-bottom:4px;"><span style="color:#b91c1c; font-weight:800;">활동성 탈신경 (Active Denervation):</span> 현재 신경 손상이 <b>활발히 진행 중</b>인 상태 (자발전위 관찰)</div>
            <div style="font-size:0.9rem; line-height:1.5; margin-bottom:4px;"><span style="color:#c2410c; font-weight:800;">만성 재신경지배 (Chronic Reinnervation):</span> 신경 손상 후 회복을 시도하는 <b>만성기</b> (거대운동단위 관찰)</div>
            <div style="font-size:0.9rem; line-height:1.5;"><span style="color:#0f766e; font-weight:800;">동원 감소 (Reduced Recruitment):</span> 신경 손상으로 인해 부분 탈신경으로 근력 저하 또는 완전 탈신경으로 <b>마비된 상태</b></div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="item-title">침근전도검사 (Needle EMG)</div>', unsafe_allow_html=True)
        st.markdown(_create_responsive_table(["검사 근육", "휴식 시", "수의수축 시"], emg_rows, "tbl_emg"), unsafe_allow_html=True)

    # 4. 통합 임상 추론
    st.markdown('<hr style="margin: 1.5rem 0; border-top: 1px dotted #cbd5e1;">', unsafe_allow_html=True)
    st.markdown('<div class="section-label" style="color:#1e3a8a;">임상 추론 및 통합 해석</div>', unsafe_allow_html=True)
    
    if "ncs_reason" in teaching:
        st.markdown('<div class="inline-label" style="display:block; margin-top:12px; margin-bottom:6px; color:#16a34a;">1. 신경전도검사(NCS) 수치 해석</div>', unsafe_allow_html=True)
        for r in teaching["ncs_reason"]: 
            st.markdown(f'<div class="inline-content" style="margin-bottom:6px;">{r}</div>', unsafe_allow_html=True)
            
    if "emg_reason" in teaching:
        st.markdown('<div class="inline-label" style="display:block; margin-top:16px; margin-bottom:6px; color:#16a34a;">2. 침근전도검사(EMG) 소견 해석</div>', unsafe_allow_html=True)
        for r in teaching["emg_reason"]: 
            st.markdown(f'<div class="inline-content" style="margin-bottom:6px;">{r}</div>', unsafe_allow_html=True)

    if "integration" in teaching:
        st.markdown('<div class="inline-label" style="display:block; margin-top:16px; margin-bottom:6px; color:#1e3a8a;">3. 통합 결론 도출</div>', unsafe_allow_html=True)
        for r in teaching["integration"]: 
            st.markdown(f'<div class="inline-content" style="margin-bottom:12px;">{r}</div>', unsafe_allow_html=True)
            
    st.markdown(
        f'<div style="background:#fff1f2; padding:12px; margin-top:12px; border-radius:6px; border:1px solid #fecdd3;">'
        f'<span class="inline-label" style="color:#991b1b; font-size:1.05rem;">임상적 추정 진단 (Impression):</span><br>'
        f'<span class="inline-content" style="font-weight:800; color:#991b1b; font-size:1.05rem;">R/O {teaching.get("summary")}</span>'
        f'</div>', 
        unsafe_allow_html=True
    )

    # 5. 감별 진단 (설명 통합)
    if "differential_diagnosis" in data:
        st.markdown('<div class="section-label" style="color:#7e22ce; margin-top:24px;">유사 질환과의 감별 진단</div>', unsafe_allow_html=True)
        
        for ddx in data["differential_diagnosis"]:
            st.markdown(f"""
            <div class="ddx-box">
                <div class="ddx-title">R/O {ddx.get('name')}</div>
                <div class="ddx-content" style="line-height:1.6;">
                    증상이 유사하여 혼동될 수 있으나, 본 데이터의 소견과 비교할 때 {ddx.get('how_to_differentiate')}
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div style="height: 24px;"></div>', unsafe_allow_html=True)
    
    if st.button("👆 다른 사례 선택하기 (초기화 및 위로 이동)", type="primary"):
        st.session_state["case_reset_counter"] += 1
        st.rerun()

def render_case_detail():
    pass
