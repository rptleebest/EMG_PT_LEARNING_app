# ui/case_learning.py

import streamlit as st
from data.cases import CASE_LIBRARY
from data.constants import ANATOMY
from engine.inference import normalize_result_text, split_findings_by_domain
from ui.navigation import render_bottom_navigation

def _get_ncs_line_text(raw_val):
    if raw_val == "ncs_delayed":
        return "진폭: 정상 범위 / <span class='text-red' style='font-weight:700;'>잠복기: 지연</span>"
    elif raw_val == "ncs_reduced":
        return "<span class='text-red' style='font-weight:700;'>진폭: 감소</span> / 잠복기: 정상 범위"
    elif raw_val == "ncs_absent":
        return "<span class='text-red' style='font-weight:700;'>반응 소실</span>"
    else:
        return "정상 범위"

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
    else: 
        return "휴식 시: <span class='text-blue' style='font-weight:700;'>Silent at rest</span> / 수의수축 시: <span class='text-blue' style='font-weight:700;'>Normal MU recruitment</span>"

# F파 및 반사 검사 결과를 한글 표준 용어로 번역하는 공용 헬퍼 함수
def _get_reflex_line_text(raw_val):
    if raw_val == "fwave_delayed_absent":
        return "F파: 지연/부재"
    elif raw_val == "blink_delayed":
        return "비정상 (눈깜빡반사 R1/R2 지연)"
    elif raw_val == "blink_delayed_absent":
        return "비정상 (눈깜빡반사 R2 유발 소실)"
    elif raw_val == "h_reflex_hyperactive":
        return "비정상 (H-반사 최대 진폭 항진)"
    elif raw_val == "h_m_ratio_increased":
        return "비정상 (H/M ratio 증가)"
    elif raw_val in ["ncs_normal", "정상 범위"]:
        return "정상 범위"
    return raw_val

def _render_finding_block(title, findings, side):
    if not findings:
        return

    st.markdown(f'<div class="case-section-label" style="font-size:0.92rem; padding: 6px 8px;">{title}</div>', unsafe_allow_html=True)
    block_parts = []

    items = list(findings.items())
    for idx, (item, values) in enumerate(items):
        left = values[0] if len(values) > 0 else ""
        right = values[1] if len(values) > 1 else ""

        lines = [f'<div class="finding-highlight" style="font-size:0.88rem; margin-top:4px; padding-bottom:2px;">{item}</div>']
        
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
                # [버그 수정] 양측 F파 및 반사 검사의 원시 코드를 한글 맵핑 텍스트로 치환 적용
                left_text = _get_reflex_line_text(raw_left)
                right_text = _get_reflex_line_text(raw_right)

            st.markdown(f"""
            <div style="padding-left: 6px; margin-bottom: 6px; border-bottom: 1px solid #f1f5f9; padding-bottom: 6px;">
                <div class="finding-highlight" style="font-size:0.88rem; border-bottom:none; margin-top:2px;">{item}</div>
                <div class="finding-subtext" style="margin-bottom: 1px; font-size:0.8rem; line-height:1.4;">• 좌측: {left_text}</div>
                <div class="finding-subtext" style="margin-bottom: 1px; font-size:0.8rem; line-height:1.4;">• 우측: {right_text}</div>
            </div>
            """, unsafe_allow_html=True)
            continue
        else:
            if "감각" in title or "운동" in title:
                if raw_val == "ncs_delayed":
                    lines.append(f'<div class="finding-subtext" style="font-size:0.82rem; margin-bottom:2px;">진폭: <span class="text-blue">정상 범위</span></div>')
                    lines.append(f'<div class="finding-subtext" style="font-size:0.82rem; margin-bottom:2px;">잠복기: <span class="text-red" style="font-weight:800;">지연</span></div>')
                elif raw_val == "ncs_reduced":
                    lines.append(f'<div class="finding-subtext" style="font-size:0.82rem; margin-bottom:2px;">진폭: <span class="text-red" style="font-weight:800;">감소</span></div>')
                    lines.append(f'<div class="finding-subtext" style="font-size:0.82rem; margin-bottom:2px;">잠복기: <span class="text-blue">정상 범위</span></div>')
                elif raw_val == "ncs_absent":
                    lines.append(f'<div class="finding-subtext" style="font-size:0.82rem; margin-bottom:2px;">진폭: <span class="text-red" style="font-weight:800;">반응 소실</span></div>')
                    lines.append(f'<div class="finding-subtext" style="font-size:0.82rem; margin-bottom:2px;">잠복기: <span class="text-red" style="font-weight:800;">반응 소실</span></div>')
                else: 
                    lines.append(f'<div class="finding-subtext" style="font-size:0.82rem; margin-bottom:2px;">진폭: <span class="text-blue">정상 범위</span></div>')
                    lines.append(f'<div class="finding-subtext" style="font-size:0.82rem; margin-bottom:2px;">잠복기: <span class="text-blue">정상 범위</span></div>')
                    
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
                <div style="padding-left: 6px; margin-bottom: 6px; border-bottom: 1px solid #f1f5f9; padding-bottom: 6px;">
                    <div class="finding-highlight" style="font-size:0.88rem; border-bottom:none; margin-top:2px;">{item}</div>
                    <div class="finding-subtext" style="margin-bottom: 1px; font-size:0.82rem;">• 휴식 시: <span class="{rest_color}" style="font-weight: 700;">{rest_val}</span></div>
                    <div class="finding-subtext" style="margin-bottom: 1px; font-size:0.82rem;">• 수의수축 시: <span class="{vol_color}" style="font-weight: 700;">{vol_val}</span></div>
                </div>
                """, unsafe_allow_html=True)
                continue
            else:
                norm_val = _get_reflex_line_text(raw_val)
                
                lines.append(f'<div class="finding-subtext" style="font-size:0.82rem;">판독 결과: <span class="text-red" style="font-weight:700;">{norm_val}</span></div>')
                if right and right not in ["ncs_normal", "NCS_NORMAL"]:
                    lines.append(f'<div class="finding-subtext" style="font-size:0.82rem;">측정 데이터: <span class="text-blue">{right}</span></div>')

        block_parts.append(f'<div class="compact-item" style="padding: 2px 0;">{"".join(lines)}</div>')
        if idx < len(items) - 1:
            block_parts.append('<hr class="item-divider" style="margin: 4px 0;">')

    if block_parts:
        st.markdown(f'<div class="case-text-block" style="padding: 6px 8px;">{"".join(block_parts)}</div>', unsafe_allow_html=True)


def render_case_list():
    st.markdown('<div class="main-title">사례 학습 모드</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtle" style="font-size:0.84rem; line-height:1.45; word-break:keep-all;">환자의 임상 증상과 근전도 소견을 실시간 비교 분석하여 임상적 판단력을 기릅니다.</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-card" style="padding: 10px 8px;">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label" style="font-size:0.92rem;">📋 학습할 가상 사례 선택 (비교 분석형)</div>', unsafe_allow_html=True)

    case_names = ["선택 안 함"] + list(CASE_LIBRARY.keys())
    
    if "case_reset_counter" not in st.session_state:
        st.session_state["case_reset_counter"] = 0

    dynamic_radio_key = f"case_radio_selector_{st.session_state['case_reset_counter']}"

    selected = st.radio(
        "학습할 임상 증상 선택", 
        case_names, 
        key=dynamic_radio_key,
        label_visibility="collapsed"
    )

    st.markdown('</div>', unsafe_allow_html=True)

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

        # 상단 카드에서 정답 스포일러 방지를 위해 "최종 교육용 진단" 행을 완전히 영구 삭제
        st.markdown(f'<div class="info-card" style="padding: 10px 8px;">', unsafe_allow_html=True)
        st.markdown(f'<div class="case-title-mobile" style="font-size:0.94rem;">👤 환자 사례: {selected}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="case-subtitle-mobile" style="font-size:0.82rem; margin-top:2px;"><span class="label-strong text-blue">연령/성별:</span> <span class="result-value">{patient["age"]}세 / {patient["sex"]}</span> | <span class="label-strong text-blue">병변측:</span> <span class="result-value">{side}</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # 주요 증상(Chief Complaints)
        st.markdown('<div class="case-section-label" style="font-size:0.92rem;">🗣️ 주요 증상</div>', unsafe_allow_html=True)
        symptoms_html = "".join([f'<div class="case-bullet" style="font-size:0.82rem; margin-bottom:4px;">• {s}</div>' for s in patient.get("symptoms", [])])
        st.markdown(f'<div class="case-text-block" style="padding: 8px 10px;">{symptoms_html}</div>', unsafe_allow_html=True)

        # 이학적 검사 결과
        st.markdown('<div class="case-section-label" style="font-size:0.92rem;">🧪 이학적 검사결과</div>', unsafe_allow_html=True)
        exam_html = []
        for sec_name, items in patient.get("physical_exam", {}).items():
            exam_html.append(f'<div class="finding-highlight" style="font-size:0.86rem; margin-top:4px; padding-bottom:1px; border-bottom:none; color:#475569;">[{sec_name}]</div>')
            for i in items:
                parts = i.split(":", 1)
                if len(parts) == 2:
                    exam_html.append(f'<div class="case-bullet" style="font-size:0.82rem; margin-bottom:3px;"><span class="label-strong" style="font-size:0.82rem;">{parts[0]}:</span> <span class="result-value" style="font-size:0.82rem;">{parts[1]}</span></div>')
                else:
                    exam_html.append(f'<div class="case-bullet" style="font-size:0.82rem; margin-bottom:3px;">• {i}</div>')
        st.markdown(f'<div class="case-text-block" style="padding: 8px 10px;">{"".join(exam_html)}</div>', unsafe_allow_html=True)

        # 학생용 사고 프레임 가이드
        if "뇌졸중" in selected:
            st.markdown("""
            <div class="warn-card" style="padding: 8px 8px; margin-bottom:10px; border-left-color: #9333ea; background: #faf5ff;">
                <div class="finding-highlight" style="color: #7c3aed; border-bottom-color: #f3e8ff; font-size:0.85rem; padding-bottom:2px; margin-top:2px;">🎓 학생용 사고 프레임 (UMN H-reflex 판독 기준)</div>
                <div class="case-bullet-strong" style="font-size:0.8rem; margin-bottom:3px; color:#5b21b6;">1. H-반사(H-reflex) 특성: 일반 신경전도(NCS)나 침근전도(Needle EMG)를 적용하지 않으며, 단일시냅스 척수 반사(Spinal reflex)를 직접 평가합니다.</div>
                <div class="case-bullet-strong" style="font-size:0.8rem; margin-bottom:3px; color:#5b21b6;">2. 중추성 위운동신경세포(UMN) 병변: 하행성 억제 소실로 인해 알파운동신경세포의 과흥분성으로 <b>H-반사 최대 진폭 항진</b> 및 <b>H/M ratio 비율 대폭 증가(> 40%)</b> 됩니다.</div>
                <div class="case-bullet-strong" style="font-size:0.8rem; margin-bottom:2px; color:#5b21b6;">3. 치료 완화 정량화: 물리치료 중재 적용 후 H/M ratio 수치의 유의미한 감소 여부로 경직(Spasticity) 완화도를 정량적으로 평가합니다.</div>
            </div>
            """, unsafe_allow_html=True)
        elif "눈꺼풀" in selected:
            st.markdown("""
            <div class="warn-card" style="padding: 8px 8px; margin-bottom:10px; border-left-color: #0d9488; background: #f0fdfa;">
                <div class="finding-highlight" style="color: #0d9488; border-bottom-color: #ccfbf1; font-size:0.85rem; padding-bottom:2px; margin-top:2px;">🎓 학생용 사고 프레임 (눈깜빡반사 Blink Reflex 판독 기준)</div>
                <div class="case-bullet-strong" style="font-size:0.8rem; margin-bottom:3px; color:#115e59;">1. 들신경(Afferent) 삼차신경 장애: 병변측 전기자극 시 양측 수축 반응 R1, R2가 동시에 지연 및 부재하며, 정상측 자극 시에는 양측 반응 모두 대칭성 정상을 나타냅니다.</div>
                <div class="case-bullet-strong" style="font-size:0.8rem; margin-bottom:3px; color:#115e59;">2. 날신경(Efferent) 얼굴신경 장애: 자극 방향에 상관없이 항상 병변측 근수축 반응 R1, R2가 모두 손상 및 소실됩니다.</div>
                <div class="case-bullet-strong" style="font-size:0.8rem; margin-bottom:2px; color:#115e59;">3. 뇌간 반사 회로 평가: 얼굴 표정근 마비 변성과 관계없이 반사궁 회로의 무결성만을 측정하므로 일반 침근전도는 배제됩니다.</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="warn-card" style="padding: 8px 8px; margin-bottom:10px;">
                <div class="finding-highlight" style="color: #b45309; border-bottom-color: #fde68a; font-size:0.85rem; padding-bottom:2px; margin-top:2px;">🎓 학생용 사고 프레임 (NCS / EMG 판독 기준)</div>
                <div class="case-bullet-strong" style="font-size:0.8rem; margin-bottom:3px;">1. 진폭(Amplitude) 감소: 정상측 대비 <b>50% 이하</b> 시 축삭 손상(Axonal loss) 지시</div>
                <div class="case-bullet-strong" style="font-size:0.8rem; margin-bottom:3px;">2. 잠복기(Latency) 지연: 정상측 대비 <b>130% 이상</b> 시 말이집털락 변화(Demyelinating) 또는 포착 지시</div>
                <div class="case-bullet-strong" style="font-size:0.8rem; margin-bottom:2px;">3. 감각 전도 보존: 신경근병증(Radiculopathy)은 뒤뿌리신경절(DRG) 몸쪽 병변이므로 감각신경활동전위(SNAP)가 정상 범위로 온전하게 보존됨</div>
            </div>
            """, unsafe_allow_html=True)

        grouped = split_findings_by_domain(findings, ANATOMY)

        # 전기진단 소견 분류 렌더링
        if grouped["sensory"]:
            _render_finding_block("감각신경전도검사: 병변측", grouped["sensory"], side)
        if grouped["motor"]:
            _render_finding_block("운동신경전도검사: 병변측", grouped["motor"], side)
            
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
                _render_finding_block("눈깜빡반사 회로 분석: 병변측", merged, side)
            else:
                _render_finding_block("반사 및 후기반응 소견: 병변측", merged, side)

        # 최하단 리포트 요약 헤더를 "최종 교육용 진단"으로 고착화하여 렌더링
        st.markdown('<div class="result-card" style="padding: 10px 8px;">', unsafe_allow_html=True)
        st.markdown('<div class="result-title" style="font-size:0.92rem;">✅ 임상 추론 및 해석 결과</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="result-text" style="font-size:0.84rem; background: #fff1f2; border: 1px solid #fecdd3; padding: 8px; border-radius:6px;"><span class="label-strong text-red" style="font-size:0.85rem; font-weight:800;">최종 교육용 진단:</span> <span class="result-value" style="font-weight: 800; font-size:0.88rem; color: #9f1239; margin-left: 4px;">{teaching.get("summary","")}</span></div>', unsafe_allow_html=True)
        st.markdown('<div style="height: 10px;"></div>', unsafe_allow_html=True)

        if teaching.get("ncs_reason"):
            st.markdown('<div class="result-label" style="font-size:0.85rem; padding: 4px 6px;">신경전도 및 후기반응 해석 포인트</div>', unsafe_allow_html=True)
            for x in teaching["ncs_reason"]:
                st.markdown(f'<div class="result-text" style="font-size:0.8rem; line-height:1.45;">• {x}</div>', unsafe_allow_html=True)

        if teaching.get("emg_reason"):
            is_emg_skipped = "Blink Reflex" in str(teaching["emg_reason"][0]) or "H-reflex" in str(teaching["emg_reason"][0]) or "H-반사" in str(teaching["emg_reason"][0]) or "눈꺼풀" in selected or "뇌졸중" in selected
            
            if not is_emg_skipped:
                st.markdown('<div class="result-label" style="font-size:0.85rem; padding: 4px 6px;">침근전도 해석 포인트</div>', unsafe_allow_html=True)
                for x in teaching["emg_reason"]:
                    x_strip = x.strip()
                    if x_strip.startswith(("1)", "2)", "3)", "4)", "5)")):
                        st.markdown(
                            f'<div class="result-text" style="padding-left: 8px; margin-top: 8px; margin-bottom: 4px; line-height:1.4; font-weight: 800; color: #1e3a8a; font-size: 0.84rem;">{x_strip}</div>', 
                            unsafe_allow_html=True
                        )
                    elif x_strip.endswith(":"):
                        st.markdown(
                            f'<div class="result-text" style="font-weight: 800; color: #b45309; margin-top: 10px; margin-bottom: 4px; font-size:0.82rem;">{x_strip}</div>', 
                            unsafe_allow_html=True
                        )
                    else:
                        st.markdown(
                            f'<div class="result-text" style="line-height:1.45; margin-bottom:3px; padding-left: 6px; color: #334155; font-size:0.8rem;">• {x_strip}</div>', 
                            unsafe_allow_html=True
                        )

        if teaching.get("integration"):
            st.markdown('<div class="result-label" style="font-size:0.85rem; padding: 4px 6px;">통합 해석</div>', unsafe_allow_html=True)
            for x in teaching["integration"]:
                st.markdown(f'<div class="result-text" style="font-size:0.8rem; line-height:1.45;">• {x}</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

        if diff_dx:
            st.markdown('<div class="section-card" style="padding: 10px 8px;">', unsafe_allow_html=True)
            st.markdown('<div class="case-section-label" style="font-size:0.92rem;">🧭 감별진단 포인트</div>', unsafe_allow_html=True)
            for idx, d in enumerate(diff_dx):
                st.markdown(f'<div class="finding-highlight" style="font-size:0.86rem; margin-top:2px;">{d.get("name","")}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="case-bullet" style="font-size:0.8rem; margin-bottom:3px;"><span class="label-strong text-blue" style="font-size:0.8rem;">왜 고려하나:</span> <span class="result-value" style="font-size:0.8rem;">{d.get("why_consider","")}</span></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="case-bullet" style="font-size:0.8rem; margin-bottom:3px;"><span class="label-strong text-blue" style="font-size:0.8rem;">어떻게 구분하나:</span> <span class="result-value" style="font-size:0.8rem;">{d.get("how_to_differentiate","")}</span></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="case-bullet" style="font-size:0.8rem; margin-bottom:3px;"><span class="label-strong text-green" style="font-size:0.8rem;">실전 팁:</span> <span class="result-value" style="font-size:0.8rem;">{d.get("practical_tip","")}</span></div>', unsafe_allow_html=True)
                if idx < len(diff_dx) - 1:
                    st.markdown('<hr class="item-divider" style="margin: 6px 0;">')
            st.markdown('</div>', unsafe_allow_html=True)

        # 다른 임상케이스 분석하기 버튼 동적 키 로테이션 리셋 바인딩
        st.markdown('<div style="text-align: center; margin-top: 15px; margin-bottom: 15px;">', unsafe_allow_html=True)
        if st.button("🔄 다른 임상 케이스 분석하기", key="reset_case_radio_btn"):
            st.session_state["case_reset_counter"] += 1
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    render_bottom_navigation()


def render_case_detail():
    st.session_state["screen"] = "case_list"
    st.rerun()
