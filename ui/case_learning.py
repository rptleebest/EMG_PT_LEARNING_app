# ui/case_learning.py

import streamlit as st
from data.cases import CASE_LIBRARY
from data.constants import ANATOMY
from engine.inference import normalize_result_text, split_findings_by_domain
from ui.navigation import render_bottom_navigation

def render_case_list():
    st.markdown('<div class="main-title">사례 학습 모드</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtle">환자의 임상 증상과 근전도 병변측 소견을 분석하여 병변 부위를 추론합니다.</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">📋 학습할 가상 사례 선택</div>', unsafe_allow_html=True)

    # 1. 필터 및 기본 첫 항목 자동 체크 방지를 위한 '선택 안 함' 도입
    case_names = ["선택 안 함"] + list(CASE_LIBRARY.keys())
    selected = st.radio("학습할 임상 증상 선택", case_names, label_visibility="collapsed")

    if selected != "선택 안 함":
        case = CASE_LIBRARY[selected]
        patient = case["patient"]
        
        side_korean = patient.get("side", "-")
        if side_korean == "우": side_korean = "오른쪽"
        elif side_korean == "좌": side_korean = "왼쪽"
        elif side_korean == "양측": side_korean = "양쪽"

        st.markdown('<div class="info-card" style="margin-top:15px;">', unsafe_allow_html=True)
        st.markdown(f'<div class="case-title-mobile">👤 {selected}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="case-subtitle-mobile"><span class="label-strong text-blue">연령/성별:</span> <span class="result-value">{patient["age"]}세 / {patient["sex"]}</span> | <span class="label-strong text-blue">병변측:</span> <span class="result-value">{side_korean}</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        if st.button("📚 선택한 사례 상세 학습 시작", type="primary", use_container_width=True):
            st.session_state["selected_case"] = selected
            st.session_state["screen"] = "case_detail"
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
    render_bottom_navigation()


def _render_finding_block(title, findings, side):
    if not findings:
        return

    # 5. 표제어 수정 적용: 근전도 결과표 (NCS & Needle EMG): 병변측
    st.markdown(f'<div class="case-section-label">{title} (병변측: {side})</div>', unsafe_allow_html=True)
    block_parts = []

    items = list(findings.items())
    for idx, (item, values) in enumerate(items):
        left = values[0] if len(values) > 0 else ""
        right = values[1] if len(values) > 1 else ""

        # 정상측 정보는 완전히 노출하지 않고 병변측 정보만 렌더링
        lines = [f'<div class="finding-highlight">{item}</div>']

        if side == "양쪽" or side == "양측":
            lines.append(f'<div class="finding-subtext">1) 좌측: <span class="text-red">{normalize_result_text(left)}</span></div>')
            lines.append(f'<div class="finding-subtext">2) 우측: <span class="text-red">{normalize_result_text(right)}</span></div>')
        else:
            pathological_val = right if (side == "오른쪽" or side == "우") else left
            norm_val = normalize_result_text(pathological_val)

            # 진폭과 잠복기를 분리하여 판독 결과 매핑 및 가이드라인 제시 (Request 3 반영)
            if "SNAP" in item or "CMAP" in item:
                if "지연" in norm_val or "delayed" in norm_val.lower():
                    lines.append(f'<div class="finding-subtext">1) 진폭: <span class="text-blue">정상 범위</span></div>')
                    lines.append(f'<div class="finding-subtext">2) 잠복기: <span class="text-red">비정상 (정상범위: 잠복기 정상 대비 130% 미만)</span></div>')
                elif "감소" in norm_val or "reduced" in norm_val.lower():
                    lines.append(f'<div class="finding-subtext">1) 진폭: <span class="text-red">비정상 (정상범위: 진폭 정상 대비 50% 초과)</span></div>')
                    lines.append(f'<div class="finding-subtext">2) 잠복기: <span class="text-blue">정상 범위</span></div>')
                elif "소실" in norm_val or "absent" in norm_val.lower():
                    lines.append(f'<div class="finding-subtext">1) 진폭: <span class="text-red">반응 소실 (전기 자극에 무반응)</span></div>')
                    lines.append(f'<div class="finding-subtext">2) 잠복기: <span class="text-red">반응 소실 (전기 자극에 무반응)</span></div>')
                else:
                    lines.append(f'<div class="finding-subtext">1) 진폭: <span class="text-blue">정상 범위</span></div>')
                    lines.append(f'<div class="finding-subtext">2) 잠복기: <span class="text-blue">정상 범위</span></div>')
            else:
                # EMG 또는 반사계
                lines.append(f'<div class="finding-subtext">판독 결과: <span class="text-red">{norm_val}</span></div>')

        block_parts.append(f'<div class="compact-item">{"".join(lines)}</div>')
        if idx < len(items) - 1:
            block_parts.append('<hr class="item-divider">')

    st.markdown(f'<div class="case-text-block">{"".join(block_parts)}</div>', unsafe_allow_html=True)


def render_case_detail():
    case_name = st.session_state.get("selected_case")
    case = CASE_LIBRARY.get(case_name)

    st.markdown('<div class="main-title">사례 상세 학습</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtle">증상 분포, 근력/반사, 신경전도검사/침근전도검사 패턴을 연결해 해석하는 단계입니다.</div>',
        unsafe_allow_html=True
    )

    if not case:
        st.warning("사례를 찾을 수 없습니다.")
        render_bottom_navigation()
        return

    patient = case.get("patient", {})
    findings = case.get("findings", {})
    teaching = case.get("teaching_diagnosis", {})
    diff_dx = case.get("differential_diagnosis", [])
    
    side = patient.get("side", "-")
    if side == "우": side = "오른쪽"
    elif side == "좌": side = "왼쪽"
    elif side == "양측": side = "양쪽"

    # 5. 학생용 사고 프레임 기준 추가
    st.markdown("""
    <div class="warn-card">
        <div class="finding-highlight" style="color: #b45309; border-bottom-color: #fde68a;">🎓 학생용 사고 프레임 (판독 기준)</div>
        <div class="case-bullet-strong">1. 진폭(Amplitude) 감소: 정상 범위 대비 <b>50% 이하</b>로 감소 시 운동/감각 축삭 손상(Axonal loss)을 의미합니다.</div>
        <div class="case-bullet-strong">2. 잠복기(Latency) 지연: 정상 범위 대비 <b>130% 이상</b> 연장 시 말이집탈락성(Demyelinating) 변화 혹은 국소 포착성 압박을 의미합니다.</div>
        <div class="case-bullet-strong">3. 감각신경전도 보존: 신경근병증(Radiculopathy)은 병변이 뒤뿌리신경절(DRG)보다 근위부에 있으므로 말초 감각신경활동전위(SNAP)가 정상 범위로 보존됩니다.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="case-section-label">🗣️ 주요 증상</div>', unsafe_allow_html=True)
    symptoms_html = "".join([f'<div class="case-bullet">• {s}</div>' for s in patient.get("symptoms", [])])
    st.markdown(f'<div class="case-text-block">{symptoms_html}</div>', unsafe_allow_html=True)

    st.markdown('<div class="case-section-label">🧪 이학적 검사결과</div>', unsafe_allow_html=True)
    exam_html = []
    for sec_name, items in patient.get("physical_exam", {}).items():
        exam_html.append(f'<div class="finding-highlight" style="font-size:1.0rem;">{sec_name}</div>')
        for i in items:
            parts = i.split(":", 1)
            if len(parts) == 2:
                exam_html.append(f'<div class="case-bullet"><span class="label-strong">{parts[0]}:</span> <span class="result-value">{parts[1]}</span></div>')
            else:
                exam_html.append(f'<div class="case-bullet">• {i}</div>')
    st.markdown(f'<div class="case-text-block">{"".join(exam_html)}</div>', unsafe_allow_html=True)

    grouped = split_findings_by_domain(findings, ANATOMY)

    # 5. 표제어 수정 적용: 근전도 결과표 (NCS & Needle EMG): 병변측
    if grouped["sensory"]:
        _render_finding_block("근전도 결과표 (NCS & Needle EMG): 병변측 감각신경전도 소견", grouped["sensory"], side)
    if grouped["motor"]:
        _render_finding_block("근전도 결과표 (NCS & Needle EMG): 병변측 운동신경전도 소견", grouped["motor"], side)
    if grouped["muscle"]:
        _render_finding_block("근전도 결과표 (NCS & Needle EMG): 병변측 침근전도 소견", grouped["muscle"], side)
    if grouped["reflex"] or grouped["other"]:
        merged = {}
        merged.update(grouped["reflex"])
        merged.update(grouped["other"])
        _render_finding_block("근전도 결과표 (NCS & Needle EMG): 병변측 반사 및 후기반응 소견", merged, side)

    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.markdown('<div class="result-title">✅ 교육용 진단 요약</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="result-text"><span class="label-strong text-blue">요약:</span> <span class="result-value">{teaching.get("summary","")}</span></div>', unsafe_allow_html=True)

    if teaching.get("ncs_reason"):
        st.markdown('<div class="result-label">신경전도 해석 포인트</div>', unsafe_allow_html=True)
        for x in teaching["ncs_reason"]:
            st.markdown(f'<div class="result-text">• {x}</div>', unsafe_allow_html=True)

    if teaching.get("emg_reason"):
        st.markdown('<div class="result-label">침근전도 해석 포인트</div>', unsafe_allow_html=True)
        for x in teaching["emg_reason"]:
            st.markdown(f'<div class="result-text">• {x}</div>', unsafe_allow_html=True)

    if teaching.get("integration"):
        st.markdown('<div class="result-label">통합 해석</div>', unsafe_allow_html=True)
        for x in teaching["integration"]:
            st.markdown(f'<div class="result-text">• {x}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    if diff_dx:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="case-section-label">🧭 감별진단 포인트</div>', unsafe_allow_html=True)
        for idx, d in enumerate(diff_dx):
            st.markdown(f'<div class="finding-highlight">{d.get("name","")}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="case-bullet"><span class="label-strong text-blue">왜 고려하나:</span> <span class="result-value">{d.get("why_consider","")}</span></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="case-bullet"><span class="label-strong text-blue">어떻게 구분하나:</span> <span class="result-value">{d.get("how_to_differentiate","")}</span></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="case-bullet"><span class="label-strong text-green">실전 팁:</span> <span class="result-value">{d.get("practical_tip","")}</span></div>', unsafe_allow_html=True)
            if idx < len(diff_dx) - 1:
                st.markdown('<hr class="item-divider">', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # 4 & 6. 다른 케이스 선택 버튼 배치 (뒤로가기가 홈으로 가지 않고 초기화 회귀)
    st.markdown('<div style="text-align: center; margin-top: 20px; margin-bottom: 20px;">', unsafe_allow_html=True)
    if st.button("🔄 다른 임상 케이스 분석하기", key="back_to_case_list_btn"):
        st.session_state["screen"] = "case_list"
        st.session_state["selected_case"] = None
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    render_bottom_navigation()
