# ui/case_learning.py

import html
import streamlit as st
from data.cases import CASE_LIBRARY
from ui.navigation import render_bottom_navigation

def _safe_format_code(code: str) -> str:
    mapping = {
        "ncs_normal": "정상", "ncs_delayed": "지연", "ncs_reduced": "감소", "ncs_absent": "소실", "ncs_conduction_block": "전도차단",
        "emg_normal": "정상", "emg_active_denervation": "활동성 탈신경", "emg_paraspinal_denervation": "탈신경",
        "emg_chronic_reinnervation": "만성 재신경지배", "emg_active_chronic": "활동성+만성"
    }
    return mapping.get(str(code), str(code))

def _get_result_color_style(value: str) -> str:
    text = str(value)
    if any(w in text for w in ["비정상", "감소", "지연", "소실", "탈신경", "재신경지배", "차단"]): return "color: #991b1b; font-weight: 700;"
    if "정상" in text: return "color: #15803d; font-weight: 700;"
    return ""

def _create_responsive_table(headers: list, rows: list, table_id: str) -> str:
    if not rows: return ""
    safe_table_id = html.escape(str(table_id), quote=True)
    css = f"""<style>#{safe_table_id} {{ width: 100%; border-collapse: collapse; margin-bottom: 12px; font-size: 0.9rem; }} #{safe_table_id} th {{ background-color: #f8fafc; padding: 10px; border-bottom: 2px solid #cbd5e1; text-align: left; color: #1e293b; font-weight: 700; }} #{safe_table_id} td {{ padding: 10px; border-bottom: 1px solid #e2e8f0; text-align: left; color: #334155; }} #{safe_table_id} td.fst-col {{ font-weight: 700; color: #1e40af; }} @media screen and (max-width: 768px) {{ #{safe_table_id} thead {{ display: none; }} #{safe_table_id} tr {{ display: block; border: 1px solid #e2e8f0; border-radius: 8px; margin-bottom: 12px; background: #ffffff; padding: 6px; }} #{safe_table_id} td {{ display: flex; justify-content: space-between; align-items: center; gap: 12px; border-bottom: 1px solid #f1f5f9; padding: 8px 10px; text-align: right; }} #{safe_table_id} td:last-child {{ border-bottom: none; }} #{safe_table_id} td::before {{ content: attr(data-label); font-weight: 700; color: #475569; text-align: left; font-size: 0.8rem; flex: 0 0 35%; }} #{safe_table_id} td > span {{ flex: 1; text-align: right; word-break: keep-all; font-weight: 400; }} #{safe_table_id} td.fst-col {{ justify-content: center; background: #f8fafc; border-radius: 6px 6px 0 0; text-align: center; padding: 10px; }} #{safe_table_id} td.fst-col::before {{ content: none; }} #{safe_table_id} td.fst-col > span {{ text-align: center; font-weight: 700; }} }}</style>"""
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
    st.markdown('<div class="subtle">원하는 임상 증상을 선택하면 즉시 아래에 결과표가 표시됩니다.</div>', unsafe_allow_html=True)

    if "case_reset_counter" not in st.session_state:
        st.session_state["case_reset_counter"] = 0

    case_names = ["선택 안 함"] + list(CASE_LIBRARY.keys())
    selected = st.radio("사례 리스트", case_names, index=0, key=f"c_rad_{st.session_state['case_reset_counter']}", label_visibility="collapsed")

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
    st.markdown('<div class="section-label" style="color:#0f172a;">환자 기본 정보</div>', unsafe_allow_html=True)
    st.markdown(f'<div><span class="inline-label">연령/성별:</span><span class="inline-content">{patient.get("age")}세 / {patient.get("sex")}</span></div>', unsafe_allow_html=True)
    st.markdown(f'<div><span class="inline-label">병변측:</span><span class="inline-content">{patient.get("side")}</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="inline-label" style="margin-top:8px;">주요 증상</div>', unsafe_allow_html=True)
    for sym in patient.get("symptoms", []): st.markdown(f'<div class="inline-content" style="margin-left:8px;">{sym}</div>', unsafe_allow_html=True)
    
    st.markdown('<hr style="margin: 1.2rem 0; border-top: 1px dotted #cbd5e1;">', unsafe_allow_html=True)

    # 2. 이학적 검사
    phys_exam = patient.get("physical_exam", {})
    if phys_exam:
        st.markdown('<div class="section-label" style="color:#0f172a;">이학적 검사 (신경학적 진찰)</div>', unsafe_allow_html=True)
        for cat, items in phys_exam.items():
            st.markdown(f'<div class="item-title">{cat}</div>', unsafe_allow_html=True)
            for item in items: st.markdown(f'<div class="inline-content">{item}</div>', unsafe_allow_html=True)
        st.markdown('<hr style="margin: 1.2rem 0; border-top: 1px dotted #cbd5e1;">', unsafe_allow_html=True)

    # 3. 전기진단검사 표
    sensory_rows, motor_rows, emg_rows = [], [], []
    for test_name, result_tuple in findings.items():
        if not isinstance(result_tuple, tuple): continue
        row = [test_name] + list(result_tuple)
        if "snap" in test_name.lower() or "감각" in test_name: sensory_rows.append(row)
        elif "cmap" in test_name.lower() or "운동" in test_name: motor_rows.append(row)
        else: emg_rows.append(row)

    st.markdown('<div class="section-label" style="color:#0f172a;">전기진단검사 결과 요약</div>', unsafe_allow_html=True)
    if sensory_rows:
        st.markdown('<div class="item-title">감각신경전도검사 (Sensory NCS)</div>', unsafe_allow_html=True)
        st.markdown(_create_responsive_table(["검사 신경", "진폭", "잠복기"], sensory_rows, "tbl_sen"), unsafe_allow_html=True)
    if motor_rows:
        st.markdown('<div class="item-title">운동신경전도검사 (Motor NCS)</div>', unsafe_allow_html=True)
        st.markdown(_create_responsive_table(["검사 신경", "진폭", "잠복기"], motor_rows, "tbl_mot"), unsafe_allow_html=True)

    if emg_rows:
        st.markdown("""
        <div style="background:#f8fafc; padding:10px; border-left:3px solid #94a3b8; margin-top:16px; margin-bottom:8px;">
            <div style="font-weight:700; color:#475569; font-size:0.95rem; margin-bottom:4px;">💡 학생용 침근전도 용어 가이드</div>
            <div style="font-size:0.9rem; line-height:1.4;"><span style="color:#b91c1c; font-weight:700;">활동성 탈신경:</span> <b>현재 진행 중인</b> 신경 손상 (자발전위 관찰)</div>
            <div style="font-size:0.9rem; line-height:1.4;"><span style="color:#c2410c; font-weight:700;">만성 재신경지배:</span> 회복을 시도하는 <b>만성기</b> (거대운동단위 관찰)</div>
            <div style="font-size:0.9rem; line-height:1.4;"><span style="color:#0f766e; font-weight:700;">동원 감소:</span> 신경이 끊어져 <b>마비된 최종 결과</b></div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<div class="item-title">침근전도검사 (Needle EMG)</div>', unsafe_allow_html=True)
        st.markdown(_create_responsive_table(["검사 근육", "휴식 시", "수의수축 시"], emg_rows, "tbl_emg"), unsafe_allow_html=True)

    # 4. 수치 해석 보기 (토글 확장 버튼)
    with st.expander("🔍 검사 수치 해석 및 생리학적 논리 보기"):
        if "ncs_reason" in teaching:
            st.markdown('<div class="item-title" style="color:#16a34a; margin-top:0;">신경전도검사(NCS) 수치 해석</div>', unsafe_allow_html=True)
            for r in teaching["ncs_reason"]: st.markdown(f'<div class="inline-content">{r}</div>', unsafe_allow_html=True)
        
        if "emg_reason" in teaching:
            st.markdown('<div class="item-title" style="color:#16a34a;">침근전도검사(EMG) 소견 해석</div>', unsafe_allow_html=True)
            for r in teaching["emg_reason"]: st.markdown(f'<div class="inline-content">{r}</div>', unsafe_allow_html=True)

    st.markdown('<hr style="margin: 1.2rem 0; border-top: 1px dotted #cbd5e1;">', unsafe_allow_html=True)

    # 5. 최종 통합 추론
    st.markdown('<div class="section-label" style="color:#1e40af;">최종 임상 통합 추론</div>', unsafe_allow_html=True)
    if "integration" in teaching:
        for r in teaching["integration"]: st.markdown(f'<div class="inline-content">{r}</div>', unsafe_allow_html=True)
    st.markdown(f'<div style="background:#fff1f2; padding:10px; margin-top:8px; border-radius:4px;"><span class="inline-label" style="color:#991b1b;">최종 진단명:</span><span class="inline-content" style="font-weight:700; color:#991b1b;">{teaching.get("summary")}</span></div>', unsafe_allow_html=True)

    # 6. 감별 진단
    if "differential_diagnosis" in data:
        st.markdown('<div class="section-label" style="color:#7e22ce; margin-top:24px;">유사 질환과의 감별 진단</div>', unsafe_allow_html=True)
        for ddx in data["differential_diagnosis"]:
            st.markdown(f"""
            <div class="ddx-box">
                <div class="ddx-title">{ddx.get('name')}</div>
                <span class="ddx-label">감별이 필요한 이유:</span>
                <div class="ddx-content">{ddx.get('why_consider')}</div>
                <span class="ddx-label">데이터 감별 포인트:</span>
                <div class="ddx-content">{ddx.get('how_to_differentiate')}</div>
            </div>
            """, unsafe_allow_html=True)

    # 위로 가기 버튼
    st.markdown('<div style="height: 16px;"></div>', unsafe_allow_html=True)
    if st.button("👆 다른 사례 선택하기 (초기화 및 위로 이동)", type="primary"):
        st.session_state["case_reset_counter"] += 1
        st.rerun()

def render_case_detail():
    pass
