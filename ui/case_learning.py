# ui/case_learning.py

import streamlit as st
from data.cases import CASE_LIBRARY
from data.constants import ANATOMY
from engine.inference import normalize_result_text, split_findings_by_domain
from ui.navigation import render_bottom_navigation

def _get_ncs_line_text(raw_val):
    if raw_val == "ncs_delayed":
        return "진폭 정상 / <span class='text-red' style='font-weight:700;'>잠복기 지연 (정상측 대비 130% 이상)</span>"
    elif raw_val == "ncs_reduced":
        return "<span class='text-red' style='font-weight:700;'>진폭 감소 (정상측 대비 50% 이하)</span> / 잠복기 정상"
    elif raw_val == "ncs_absent":
        return "<span class='text-red' style='font-weight:700;'>반응 소실 (전기 자극에 무반응)</span>"
    else:
        return "정상 범위 (within normal limits)"

def _get_emg_line_text(raw_val):
    if raw_val in ["emg_active_denervation", "emg_paraspinal_denervation"]:
        rest = "fibrillation potential, positive sharp wave"
        vol = "Reduced MU recruitment" if raw_val == "emg_active_denervation" else "통증으로 인해 평가불가"
        return f"휴식 시: <span class='text-red' style='font-weight:700;'>{rest}</span> / 수의수축 시: <span class='text-red' style='font-weight:700;'>{vol}</span>"
    elif raw_val == "emg_chronic_reinnervation":
        return "휴식 시: <span class='text-blue' style='font-weight:700;'>Silent at rest</span> / 수의수축 시: <span class='text-red' style='font-weight:700;'>Giant MUAPs 출현 및 Reduced MU recruitment</span>"
    elif raw_val == "emg_active_chronic":
        return "휴식 시: <span class='text-red' style='font-weight:700;'>fibrillation potential, positive sharp wave</span> / 수의수축 시: <span class='text-red' style='font-weight:700;'>Giant MUAPs 출현 및 Reduced MU recruitment</span>"
    elif raw_val == "emg_fasciculation":
        return "휴식 시: <span class='text-red' style='font-weight:700;'>fasciculation potential</span> / 수의수축 시: <span class='text-red' style='font-weight:700;'>Reduced MU recruitment</span>"
    else: # emg_normal
        return "휴식 시: <span class='text-blue' style='font-weight:700;'>Silent at rest</span> / 수의수축 시: <span class='text-blue' style='font-weight:700;'>Normal MU recruitment</span>"

def _render_finding_block(title, findings, side):
    if not findings:
        return

    st.markdown(f'<div class="case-section-label">{title}</div>', unsafe_allow_html=True)
    block_parts = []

    items = list(findings.items())
    for idx, (item, values) in enumerate(items):
        left = values[0] if len(values) > 0 else ""
        right = values[1] if len(values) > 1 else ""

        lines = [f'<div class="finding-highlight">{item}</div>']
        
        pathological_val = right if (side == "오른쪽" or side == "우") else left
        raw_val = str(pathological_val).strip()

        if side == "양쪽" or side == "양측":
            raw_left = str(left).strip()
            raw_right = str(right).strip()
            
            if "감각" in title or "운동" in title:
                left_text = _get_ncs_line_text(raw_left)
                right_text = _get_ncs_line_text(raw_right)
            elif "침근전도" in title:
                left_text = _get_emg_line_text(raw_left)
                right_text = _get_emg_line_text(raw_right)
            else:
                left_text = raw_left
                right_text = raw_right

            st.markdown(f"""
            <div style="padding-left: 10px; margin-bottom: 8px;">
                <div class="finding-highlight" style="font-size:1.0rem; border-bottom:none; margin-top:5px;">{item}</div>
                <div class="finding-subtext" style="margin-bottom: 2px;">• 좌측: {left_text}</div>
                <div class="finding-subtext">• 우측: {right_text}</div>
            </div>
            """, unsafe_allow_html=True)
            continue
        else:
            if "감각" in title or "운동" in title:
                if raw_val == "ncs_delayed":
                    lines.append(f'<div class="finding-subtext">진폭: <span class="text-blue">정상 범위</span></div>')
                    lines.append(f'<div class="finding-subtext">잠복기: <span class="text-red" style="font-weight:700;">비정상 [잠복기: 지연 (정상측 대비 130% 이상)]</span></div>')
                elif raw_val == "ncs_reduced":
                    lines.append(f'<div class="finding-subtext">진폭: <span class="text-red" style="font-weight:700;">비정상 [진폭: 감소 (정상측 대비 50% 이하)]</span></div>')
                    lines.append(f'<div class="finding-subtext">잠복기: <span class="text-blue">정상 범위</span></div>')
                elif raw_val == "ncs_absent":
                    lines.append(f'<div class="finding-subtext">진폭: <span class="text-red" style="font-weight:700;">반응 소실 (전기 자극에 무반응)</span></div>')
                    lines.append(f'<div class="finding-subtext">잠복기: <span class="text-red" style="font-weight:700;">반응 소실 (전기 자극에 무반응)</span></div>')
                else: # ncs_normal
                    lines.append(f'<div class="finding-subtext">진폭: <span class="text-blue">정상 범위</span></div>')
                    lines.append(f'<div class="finding-subtext">잠복기: <span class="text-blue">정상 범위</span></div>')
                    
            elif "침근전도" in title:
                rest_val = "Silent at rest"
                vol_val = "Normal MU recruitment"
                
                if raw_val in ["emg_active_denervation", "emg_paraspinal_denervation"]:
                    rest_val = "fibrillation potential, positive sharp wave"
                    vol_val = "Reduced MU recruitment" if raw_val == "emg_active_denervation" else "통증으로 인해 평가불가"
                elif raw_val == "emg_chronic_reinnervation":
                    rest_val = "Silent at rest"
                    vol_val = "Giant MUAPs 출현 및 Reduced MU recruitment"
                elif raw_val == "emg_active_chronic":
                    rest_val = "fibrillation potential, positive sharp wave"
                    vol_val = "Giant MUAPs 출현 및 Reduced MU recruitment"
                elif raw_val == "emg_fasciculation":
                    rest_val = "fasciculation potential"
                    vol_val = "Reduced MU recruitment"

                rest_color = "text-red" if rest_val != "Silent at rest" else "text-blue"
                vol_color = "text-red" if any(k in vol_val for k in ["Reduced", "Giant", "No MUAPs", "평가불가"]) else "text-blue"

                st.markdown(f"""
                <div style="padding-left: 10px; margin-bottom: 8px;">
                    <div class="finding-highlight" style="font-size:1.0rem; border-bottom:none; margin-top:5px;">{item}</div>
                    <div class="finding-subtext" style="margin-bottom: 2px;">• 휴식 시: <span class="{rest_color}" style="font-weight: 700;">{rest_val}</span></div>
                    <div class="finding-subtext">• 수의수축 시: <span class="{vol_color}" style="font-weight: 700;">{vol_val}</span></div>
                </div>
                """, unsafe_allow_html=True)
                continue
            else:
                norm_val = raw_val
                if raw_val == "blink_delayed":
                    norm_val = "비정상 (눈깜빡반사 R1/R2 지연)"
                elif raw_val == "blink_delayed_absent":
                    norm_val = "비정상 (눈깜빡반사 R2 유발 소실)"
                elif raw_val == "h_reflex_hyperactive":
                    norm_val = "비정상 [H-반사 최대 진폭 항진 (S1 위운동신경세포 병변)]"
                elif raw_val == "h_m_ratio_increased":
                    norm_val = "비정상 [H/M ratio 증가 (중추성 가자미근 강직)]"
                elif raw_val == "fwave_delayed_absent":
                    norm_val = "비정상 (F파 최소잠복기 지연 및 유발 소실)"
                elif raw_val == "ncs_normal":
                    norm_val = "정상 범위 (within normal limits)"
                
                lines.append(f'<div class="finding-subtext">판독 결과: <span class="text-red" style="font-weight:700;">{norm_val}</span></div>')
                if right and right not in ["ncs_normal", "NCS_NORMAL"]:
                    lines.append(f'<div class="finding-subtext">측정 데이터: <span class="text-blue">{right}</span></div>')

        block_parts.append(f'<div class="compact-item">{"".join(lines)}</div>')
        if idx < len(items) - 1:
            block_parts.append('<hr class="item-divider">')

    if block_parts:
        st.markdown(f'<div class="case-text-block">{"".join(block_parts)}</div>', unsafe_allow_html=True)


def render_case_list():
    st.markdown('<div class="main-title">사례 학습 모드</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtle">환자의 임상 증상과 근전도 소견을 실시간 비교 분석하여 임상적 판단력을 기릅니다.</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">📋 학습할 가상 사례 선택 (비교 분석형)</div>', unsafe_allow_html=True)

    case_names = ["선택 안 함"] + list(CASE_LIBRARY.keys())
    
    # 1. 세션 상태의 무결성을 담보하는 안전 위젯 상태값 선언
    if "case_radio_selector" not in st.session_state:
        st.session_state["case_radio_selector"] = "선택 안 함"

    # st.radio에 key를 적용하면 session_state["case_radio_selector"]와 직접 동기화되어 desync(디싱크)가 해결됩니다.
    selected = st.radio(
        "학습할 임상 증상 선택", 
        case_names, 
        key="case_radio_selector",
        label_visibility="collapsed"
    )

    st.markdown('</div>', unsafe_allow_html=True)

    # 사례 선택 즉시 실시간 통합 동시 렌더링
    if selected != "선택 안 함":
        case = CASE_LIBRARY[selected]
        patient = case["patient"]
        findings = case["findings"]
        teaching = case["teaching_diagnosis"]
        diff_dx = case["differential_diagnosis"]
        
        side = patient.get("side", "-")
        if side == "우": side = "오른쪽"
        elif side == "좌": side = "왼쪽"
        elif side == "양측": side = "양쪽"

        # 환자 기본 정보 카드
        st.markdown(f'<div class="info-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="case-title-mobile">👤 환자 사례: {selected}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="case-subtitle-mobile"><span class="label-strong text-blue">연령/성별:</span> <span class="result-value">{patient["age"]}세 / {patient["sex"]}</span> | <span class="label-strong text-blue">병변측:</span> <span class="result-value">{side}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="case-subtitle-mobile"><span class="label-strong text-red">최종 교육용 진단:</span> <span class="result-value">{teaching.get("summary","")}</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # 주요 증상(Chief Complaints)
        st.markdown('<div class="case-section-label">🗣️ 주요 증상</div>', unsafe_allow_html=True)
        symptoms_html = "".join([f'<div class="case-bullet">• {s}</div>' for s in patient.get("symptoms", [])])
        st.markdown(f'<div class="case-text-block">{symptoms_html}</div>', unsafe_allow_html=True)

        # 이학적 검사 결과
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

        # 학생용 사고 프레임 가이드 (정량 기준 정렬)
        st.markdown("""
        <div class="warn-card">
            <div class="finding-highlight" style="color: #b45309; border-bottom-color: #fde68a;">🎓 학생용 사고 프레임 (판독 기준)</div>
            <div class="case-bullet-strong">1. 진폭(Amplitude) 감소: 정상 범위 대비 <b>50% 이하 (정상측 대비 50% 이하)</b>로 감소 시 운동/감각 축삭 손상(Axonal loss)을 의미합니다.</div>
            <div class="case-bullet-strong">2. 잠복기(Latency) 지연: 정상 범위 대비 <b>130% 이상 (정상측 대비 130% 이상)</b> 연장 시 말이집탈락성(Demyelinating) 변화 혹은 국소 포착성 압박을 의미합니다.</div>
            <div class="case-bullet-strong">3. 감각신경전도 보존: 신경근병증(Radiculopathy)은 병변이 뒤뿌리신경절(DRG)보다 근위부에 있으므로 말초 감각신경활동전위(SNAP)가 정상 범위로 보존됩니다.</div>
        </div>
        """, unsafe_allow_html=True)

        grouped = split_findings_by_domain(findings, ANATOMY)

        # 전기진단 소견 분류 렌더링
        if grouped["sensory"]:
            _render_finding_block("감각신경전도검사: 병변측", grouped["sensory"], side)
        if grouped["motor"]:
            _render_finding_block("운동신경전도검사: 병변측", grouped["motor"], side)
            
        # 침근전도가 생략된 특수 사례(눈꺼풀 떨림, 뇌졸중 H-반사)는 침근전도 결과표를 완전 숨김 처리
        is_emg_needed = "눈꺼풀" not in selected and "뇌졸중" not in selected
        if grouped["muscle"] and is_emg_needed:
            _render_finding_block("침근전도검사 소견: 병변측", grouped["muscle"], side)
            
        if grouped["reflex"] or grouped["other"]:
            merged = {}
            merged.update(grouped["reflex"])
            merged.update(grouped["other"])
            if "뇌졸중" in selected:
                _render_finding_block("H-반사 유발 및 경직 정량검사: 병변측", merged, side)
            elif "눈꺼풀" in selected:
                _render_finding_block("눈깜빡반사 (Blink Reflex Test) 회로 분석: 병변측", merged, side)
            else:
                _render_finding_block("반사 및 후기반응 소견: 병변측", merged, side)

        # 추론 분석 보고서 영역
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown('<div class="result-title">✅ 교육용 진단 요약</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="result-text"><span class="label-strong text-blue">요약:</span> <span class="result-value">{teaching.get("summary","")}</span></div>', unsafe_allow_html=True)

        if teaching.get("ncs_reason"):
            st.markdown('<div class="result-label">신경전도 및 후기반응 해석 포인트</div>', unsafe_allow_html=True)
            for x in teaching["ncs_reason"]:
                st.markdown(f'<div class="result-text">• {x}</div>', unsafe_allow_html=True)

        if teaching.get("emg_reason"):
            is_emg_skipped = "Blink Reflex" in str(teaching["emg_reason"][0]) or "H-reflex" in str(teaching["emg_reason"][0]) or "H-반사" in str(teaching["emg_reason"][0]) or "눈꺼풀" in selected or "뇌졸중" in selected
            
            if not is_emg_skipped:
                st.markdown('<div class="result-label">침근전도 해석 포인트</div>', unsafe_allow_html=True)
                for x in teaching["emg_reason"]:
                    x_strip = x.strip()
                    if x_strip.startswith(("1)", "2)", "3)", "4)", "5)")):
                        st.markdown(
                            f'<div class="result-text" style="padding-left: 14px; margin-top: 10px; margin-bottom: 5px; line-height:1.6; font-weight: 800; color: #1e3a8a; font-size: 0.94rem;">{x_strip}</div>', 
                            unsafe_allow_html=True
                        )
                    elif x_strip.endswith(":"):
                        st.markdown(
                            f'<div class="result-text" style="font-weight: 800; color: #b45309; margin-top: 14px; margin-bottom: 6px; font-size:0.92rem;">{x_strip}</div>', 
                            unsafe_allow_html=True
                        )
                    else:
                        st.markdown(
                            f'<div class="result-text" style="line-height:1.6; margin-bottom:5px; padding-left: 10px; color: #334155;">• {x_strip}</div>', 
                            unsafe_allow_html=True
                        )

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

        # 2. 다른 임상케이스 분석하기 버튼 동적 바인딩 버그 완전 제어
        st.markdown('<div style="text-align: center; margin-top: 20px; margin-bottom: 20px;">', unsafe_allow_html=True)
        if st.button("🔄 다른 임상 케이스 분석하기", key="reset_case_radio_btn"):
            # 위젯 키 세션을 직접 초기화하여 버퍼 락을 무결하게 파쇄합니다.
            st.session_state["case_radio_selector"] = "선택 안 함"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    render_bottom_navigation()


def render_case_detail():
    st.session_state["screen"] = "case_list"
    st.rerun()
