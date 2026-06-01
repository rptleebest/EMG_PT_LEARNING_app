# ui/input_learning.py

import streamlit as st
from ui.navigation import render_bottom_navigation

# =====================================================================
# 가상의 실제 수치 데이터 세팅 (방대하게 확장된 대표 임상 케이스 6종 완벽 복원)
# =====================================================================
VIRTUAL_REPORTS = {
    "1. 좌측 목/어깨 통증 및 팔 저림 (C6 신경뿌리병증 의심)": {
        "info": {"age": 45, "sex": "남성", "symptom": "좌측 목 통증, 엄지/검지 저림, 위팔두갈래근 근력 약화", "side": "좌측"},
        "diagnosis": "좌측 C6 신경뿌리병증 (C6 Radiculopathy)",
        "ncs_sensory": [
            ["정중신경 (Median SNAP)", "정상 범위", "정상 범위", "정상 (정상범위: 잠복기 < 3.5ms, 진폭 > 20μV)"],
            ["자신경 (Ulnar SNAP)", "정상 범위", "정상 범위", "정상 (정상범위: 잠복기 < 3.1ms, 진폭 > 15μV)"]
        ],
        "ncs_motor": [
            ["정중신경 (Median CMAP)", "원위부 자극 (손목)", "정상 범위", "정상 범위", "정상 (정상범위: 잠복기 < 4.2ms, 진폭 > 4.0mV)"],
            ["정중신경 (Median CMAP)", "근위부 자극 (팔꿈치)", "정상 범위", "정상 범위", "정상 (정상범위: 잠복기 < 4.2ms, 진폭 > 4.0mV)"]
        ],
        "emg": [
            ["위팔두갈래근 (Biceps brachii)", "근육피부신경(C5-C6) [C5 우세]", "Fibrillation potentials 및<br/>Positive sharp waves 출현", "Reduced MU recruitment", "비정상 (활동성 탈신경 상태)"],
            ["노쪽손목폄근 (ECRL)", "노신경(C6-C7) [C6 우세]", "Fibrillation potentials 및<br/>Positive sharp waves 출현", "Giant MUAPs 출현 및<br/>Reduced MU recruitment", "비정상 (만성 재신경지배 상태)"],
            ["짧은엄지벌림근 (Abductor Pollicis APB)", "정중신경(C8-T1) [T1 우세]", "Silent at rest (전기적 침묵)", "Normal MU recruitment", "정상"],
            ["목 척추주위근 (Cervical Paraspinal)", "척수신경후지 (C6 Root)", "Fibrillation potentials 및<br/>Positive sharp waves 출현", "통증으로 인해 동원 제한", "비정상 (활동성 탈신경 상태)"]
        ],
        "interpretation": [
            "감각신경전도검사(SNAP)가 모두 정상입니다. 이는 병변이 뒤뿌리신경절(DRG)보다 몸쪽(근위부)인 신경뿌리(Root)에 있음을 의미합니다.",
            "침근전도에서 위팔두갈래근, 노쪽손목폄근 및 목 척추주위근에 비정상 자발전위가 대거 관찰됩니다.",
            "이 근육들은 서로 다른 말초신경의 지배를 받지만, 공통적으로 C6 신경뿌리의 지배를 받으므로 C6 신경뿌리병증으로 확진합니다."
        ],
        "emg_meaning": [
            "Fibrillation / Positive sharp wave: 축삭 사멸로 인해 지배력을 잃은 근섬유가 자발적으로 미세 유발하는 급성 활동성 전위입니다.",
            "Silent at rest: 휴식 시 어떠한 비정상 전기 활동도 관찰되지 않는 완벽한 전기적 침묵 상태입니다.",
            "Normal MU recruitment: 근수축 요구도에 따라 정량적인 운동단위(Motor Unit) 결합 동원이 원활한 정상 상태입니다."
        ],
        "ddx": "디스크 탈출증이나 척추관 협착증 확인을 위해 경추 MRI 검사 시행이 권장됩니다."
    },

    "2. 우측 1~3번째 손가락 저림 및 야간통 (손목굴증후군 의심)": {
        "info": {"age": 52, "sex": "여성", "symptom": "우측 1,2,3번째 손가락 저림, 밤에 통증 심해짐, 쥐기 약화", "side": "우측"},
        "diagnosis": "우측 중증 손목굴증후군 (Severe Carpal Tunnel Syndrome)",
        "ncs_sensory": [
            ["정중신경 (Median SNAP)", "진폭 감소", "잠복기 지연", "비정상 (정상범위: 잠복기 < 3.5ms, 진폭 > 20μV)"],
            ["자신경 (Ulnar SNAP)", "정상 범위", "정상 범위", "정상 (정상범위: 잠복기 < 3.1ms, 진폭 > 15μV)"]
        ],
        "ncs_motor": [
            ["정중신경 (Median CMAP)", "원위부 자극 (손목)", "진폭 감소", "잠복기 지연", "비정상 (정상범위: 잠복기 < 4.2ms, 진폭 > 4.0mV)"],
            ["정중신경 (Median CMAP)", "근위부 자극 (팔꿈치)", "정상 범위", "정상 범위", "정상 (정상범위: 잠복기 < 4.2ms, 진폭 > 4.0mV)"]
        ],
        "emg": [
            ["짧은엄지벌림근 (Abductor Pollicis APB)", "정중신경(C8-T1) [T1 우세]", "Positive sharp waves 출현", "Giant MUAPs 출현 및<br/>Reduced MU recruitment", "비정상 (만성 재신경지배 상태)"],
            ["첫째등쪽뼈사이근 (First Dorsal FDI)", "자신경(C8-T1) [T1 우세]", "Silent at rest (전기적 침묵)", "Normal MU recruitment", "정상"]
        ],
        "interpretation": [
            "정중신경에서만 말이집탈락성을 의미하는 국소 전도 잠복기 지연 및 진폭 감소가 확인됩니다.",
            "목 척추주위근이 완전히 정상이므로 C8-T1 신경뿌리병증을 원천 배제할 수 있으며, 손목 부위에 한정된 국소 포착성 단일신경병증입니다."
        ],
        "emg_meaning": [
            "진폭 감소 및 Giant MUAPs: 단순 수초 손상 단계를 지나 신경 내부 축삭(axon) 사멸과 그에 따른 우회로 만성 측부 재지배가 일어났음을 나타냅니다."
        ],
        "ddx": "동일 수근관 부위 포착을 악화시키는 당뇨 및 갑상선 질환 등 전신 대사질환 배제가 병행되어야 합니다."
    },

    "3. 좌측 허리 통증 및 엄지발가락 올림 약화 (L5 신경뿌리병증 의심)": {
        "info": {"age": 58, "sex": "여성", "symptom": "좌측 엉덩이부터 종아리 가쪽으로 방사통, 발처짐 증상", "side": "좌측"},
        "diagnosis": "좌측 L5 신경뿌리병증 (L5 Radiculopathy)",
        "ncs_sensory": [
            ["얕은종아리신경 (Superficial Peroneal SNAP)", "정상 범위", "정상 범위", "정상 (정상범위: 잠복기 < 3.5ms, 진폭 > 10μV)"],
            ["장딴지신경 (Sural SNAP)", "정상 범위", "정상 범위", "정상 (정상범위: 잠복기 < 3.6ms, 진폭 > 10μV)"]
        ],
        "ncs_motor": [
            ["종아리신경 (Peroneal CMAP)", "원위부 자극 (발목)", "정상 범위", "정상 범위", "정상 (정상범위: 잠복기 < 6.0ms, 진폭 > 2.0mV)"],
            ["종아리신경 (Peroneal CMAP)", "근위부 자극 (오금)", "정상 범위", "정상 범위", "정상 (정상범위: 잠복기 < 6.0ms, 진폭 > 2.0mV)"]
        ],
        "emg": [
            ["앞정강근 (Tibialis Anterior)", "깊은종아리신경(L4-L5) [L4-L5 우세]", "Fibrillation potentials 및<br/>Positive sharp waves 출현", "Reduced MU recruitment", "비정상 (활동성 탈신경 상태)"],
            ["긴종아리근 (Peroneus Longus)", "얕은종아리신경(L5-S1) [L5 우세]", "Positive sharp waves 출현", "Giant MUAPs 출현 및<br/>Reduced MU recruitment", "비정상 (만성 재신경지배 상태)"],
            ["가자미근 (Soleus)", "정강신경(S1-S2) [S1 우세]", "Silent at rest (전기적 침묵)", "Normal MU recruitment", "정상"],
            ["허리 척추주위근 (Lumbar Paraspinal)", "척수신경후지 (L5 Root)", "Fibrillation potentials 출현", "평가불가", "비정상 (활동성 탈신경 상태)"]
        ],
        "interpretation": [
            "다리의 감각신경전도검사(SNAP)가 완전히 정상입니다. 이는 병변이 말초신경이 아닌 요추 신경뿌리(Root)에 있음을 확인해 줍니다.",
            "앞정강근(L4-L5)과 긴종아리근(L5-S1) 모두에서 비정상 자발전위가 나타났으며, 허리 척추주위근에서도 이상이 확인되어 L5 신경뿌리 병변으로 결론짓습니다."
        ],
        "emg_meaning": [
            "감각신경 보존의 원리: 신경뿌리병증은 대개 뒤뿌리신경절(DRG)보다 근위부(척수 쪽)에서 발생하므로, 말초 쪽으로 뻗어나온 감각신경은 온전하게 유지됩니다."
        ],
        "ddx": "L4-L5 추간판 탈출증 또는 요추관 협착증 확인을 위해 요추 MRI 검사가 필요합니다."
    },

    "4. 우측 발처짐 및 종아리 가쪽 감각 저하 (종아리신경 마비 의심)": {
        "info": {"age": 32, "sex": "남성", "symptom": "다리를 꼬고 잔 후 발생한 우측 발처짐, 허리 통증 없음", "side": "우측"},
        "diagnosis": "우측 온종아리신경 마비 (Common Peroneal Neuropathy)",
        "ncs_sensory": [
            ["얕은종아리신경 (Superficial Peroneal SNAP)", "진폭 감소", "잠복기 지연", "비정상 (정상범위: 잠복기 < 3.5ms, 진폭 > 10μV)"],
            ["장딴지신경 (Sural SNAP)", "정상 범위", "정상 범위", "정상 (정상범위: 잠복기 < 3.6ms, 진폭 > 10μV)"]
        ],
        "ncs_motor": [
            ["종아리신경 (Peroneal CMAP)", "원위부 자극 (발목)", "정상 범위", "정상 범위", "정상 (정상범위: 잠복기 < 6.0ms, 진폭 > 2.0mV)"],
            ["종아리신경 (Peroneal CMAP)", "근위부 자극 (비골두 위)", "진폭 감소", "잠복기 지연", "비정상 (전도차단 부위)"]
        ],
        "emg": [
            ["앞정강근 (Tibialis Anterior)", "깊은종아리신경(L4-L5) [L4-L5 우세]", "Silent at rest (전기적 침묵)", "No MUAPs on volition", "비정상 (완전 동원 소실 상태)"],
            ["긴종아리근 (Peroneus Longus)", "얕은종아리신경(L5-S1) [L5 우세]", "Silent at rest (전기적 침묵)", "Severely reduced MU recruitment", "비정상 (불완전 동원 감소 상태)"],
            ["가자미근 (Soleus)", "정강신경(S1-S2) [S1 우세]", "Silent at rest", "Normal MU recruitment", "정상"],
            ["허리 척추주위근 (Lumbar Paraspinal)", "척수신경후지 (L5 Root)", "Silent at rest", "평가불가", "정상"]
        ],
        "interpretation": [
            "종아리뼈머리(Fibular head) 부위를 가로질러 근위부 자극 시 운동신경 진폭이 급격히 떨어지는 '전도차단(Conduction block)'이 관찰됩니다.",
            "얕은종아리신경(감각)의 진폭이 감소하였고, 척추주위근은 정상이므로 요추 신경뿌리병증(L5)을 명확히 배제할 수 있습니다."
        ],
        "emg_meaning": [
            "전도차단(Conduction block): 국소적인 말이집 압박으로 전기 신호가 그 지점을 통과하지 못하는 기능적 마비 상태입니다.",
            "No MUAPs on volition: 수의적인 운동 신호가 차단 부위에 막혀 바늘근전도 상 운동단위가 전혀 동원되지 않는 완전 마비 상태입니다."
        ],
        "ddx": "급성 압박성 신경병증. 다리 꼬는 습관 교정 및 발목 보조기(AFO) 착용 여부 평가가 필요합니다."
    },

    "5. 양측 발끝 저림 및 감각 저하 (당뇨병성 다발신경병증 의심)": {
        "info": {"age": 68, "sex": "남성", "symptom": "양쪽 발바닥이 화끈거리고 감각 둔화 (장갑-양말 분포), 당뇨", "side": "양측"},
        "diagnosis": "길이의존성 감각운동 다발신경병증 (Polyneuropathy)",
        "ncs_sensory": [
            ["장딴지신경 (Sural SNAP) 우측", "반응 소실", "반응 소실", "비정상 (무반응)"],
            ["정중신경 (Median SNAP) 우측", "경미한 진폭 감소", "정상 범위", "경미한 비정상"]
        ],
        "ncs_motor": [
            ["정강신경 (Tibial CMAP) 우측", "원위부 자극 (발목)", "진폭 감소", "정상 범위", "비정상 (정상범위: 잠복기 < 6.0ms, 진폭 > 4.0mV)"],
            ["정강신경 (Tibial CMAP) 우측", "근위부 자극 (오금)", "진폭 감소", "정상 범위", "비정상 (정상범위: 잠복기 < 6.0ms, 진폭 > 4.0mV)"]
        ],
        "emg": [
            ["앞정강근 (Tibialis Anterior)", "깊은종아리신경(L4-L5)", "Positive sharp waves 출현", "Reduced MU recruitment", "비정상 (활동성 탈신경 상태)"],
            ["위팔두갈래근 (Biceps brachii)", "근육피부신경(C5-C6)", "Silent at rest (전기적 침묵)", "Normal MU recruitment", "정상"]
        ],
        "interpretation": [
            "가장 긴 신경인 하지 감각신경에서 반응 소실(No response)이 먼저 나타나며, 상지 신경은 비교적 보존되는 전형적인 '길이 의존성(Length-dependent)' 패턴입니다.",
            "진폭 감소가 두드러지는 축삭 손상(Axonal loss) 우세형 다발신경병증입니다."
        ],
        "emg_meaning": [
            "길이의존성 병태생리: 대사성/독성 원인에 의해 세포체에서 가장 멀리 떨어져 영양공급이 취약한 긴 신경의 끝부분부터 서서히 손상(Dying back)되는 양상입니다."
        ],
        "ddx": "비타민 B12 결핍, 알코올성 신경병증 감별 및 발 상처(당뇨발) 주의 교육 필수."
    },

    "6. 상하지 대칭성 근력 저하 (급성 길랭-바레 증후군 의심)": {
        "info": {"age": 41, "sex": "여성", "symptom": "2주 전 장염, 다리에서 시작되어 팔로 올라오는 대칭성 근력 약화", "side": "양측"},
        "diagnosis": "급성 염증성 말이집탈락성 다발신경병증 (GBS)",
        "ncs_sensory": [
            ["정중신경 (Median SNAP)", "정상 범위", "잠복기 지연", "비정상 (정상범위: 잠복기 < 3.5ms)"],
            ["장딴지신경 (Sural SNAP)", "정상 범위", "정상 범위", "정상 (Sural sparing pattern)"]
        ],
        "ncs_motor": [
            ["종아리신경 (Peroneal CMAP)", "원위부 자극 (발목)", "정상 범위", "잠복기 지연", "비정상 (정상범위: 잠복기 < 6.0ms)"],
            ["종아리신경 (Peroneal CMAP)", "근위부 자극 (비골두)", "진폭 감소", "잠복기 지연", "비정상 (시간분산 출현)"]
        ],
        "emg": [
            ["앞정강근 (Tibialis Anterior)", "깊은종아리신경(L4-L5)", "Silent at rest (전기적 침묵)", "Severely reduced MU recruitment", "비정상 (운동단위 동원 감소 상태)"],
            ["허리 척추주위근 (Lumbar Paraspinal)", "척수신경후지 (L5 Root)", "Silent at rest", "평가불가", "정상"]
        ],
        "interpretation": [
            "여러 운동신경에서 심한 잠복기 지연과 전도속도 저하가 나타나는 명확한 '말이집탈락성(Demyelinating)' 소견입니다.",
            "상지 감각신경은 이상이 있으나, 하지 감각은 정상으로 보존되는 GBS의 특징적인 'Sural sparing pattern'이 관찰됩니다."
        ],
        "emg_meaning": [
            "시간분산(Temporal dispersion): 근위부 자극 시 말이집이 불규칙하게 벗겨져 전도 속도가 제각각이 되면서, 파형이 넓게 퍼지고 진폭이 흩어지는 현상입니다.",
            "초기 Silent at rest: 발병 초기(2~3주 이내)에는 축삭 자체가 끊어지지 않아 탈신경 전위가 나타나지 않습니다."
        ],
        "ddx": "뇌척수액 검사(단백세포 해리 확인) 및 호흡근 마비 모니터링 필수."
    }
}


def render_input_learning():
    if "selected_report_case" not in st.session_state:
        st.session_state["selected_report_case"] = None

    if st.session_state["selected_report_case"] is None:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="case-section-label">📋 학습할 환자 사례 선택 (6가지 전형적 케이스)</div>', unsafe_allow_html=True)
        
        chosen = st.radio(
            "의심 질환 가이드 리스트",
            ["선택 안 함"] + list(VIRTUAL_REPORTS.keys()),
            key="virtual_report_case_selector"
        )
        
        if chosen != "선택 안 함":
            if st.button("🚀 결과지 판독 시작", key="start_report_btn"):
                st.session_state["selected_report_case"] = chosen
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    else:
        case_name = st.session_state["selected_report_case"]
        data = VIRTUAL_REPORTS[case_name]

        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="case-title-mobile">👤 환자 정보: {case_name}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="case-subtitle-mobile">연령/성별: {data["info"]["age"]}세 / {data["info"]["sex"]} | 병변측: {data["info"]["side"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="mobile-note">주요 임상 증상: {data["info"]["symptom"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        def create_responsive_table(headers, rows, table_id):
            css = f"""
            <style>
                #{table_id} {{ width: 100%; border-collapse: collapse; margin-bottom: 15px; font-size: 0.88rem; }}
                #{table_id} th {{ background-color: #f1f5f9; padding: 10px; border-bottom: 2px solid #cbd5e1; text-align: center; color: #1e293b; font-weight: 800; }}
                #{table_id} td {{ padding: 10px; border-bottom: 1px solid #e2e8f0; text-align: center; color: #334155; line-height: 1.5; }}
                #{table_id} td.left-align {{ text-align: left; font-weight: 700; color: #1e40af; }}
                @media screen and (max-width: 768px) {{
                    #{table_id} thead {{ display: none; }}
                    #{table_id} tr {{ display: block; border: 1px solid #cbd5e1; border-radius: 8px; margin-bottom: 12px; background: #fff; padding: 5px; }}
                    #{table_id} td {{ display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #f1f5f9; padding: 8px 10px; }}
                    #{table_id} td:last-child {{ border-bottom: none; }}
                    #{table_id} td::before {{ content: attr(data-label); font-weight: 800; color: #64748b; text-align: left; }}
                    #{table_id} td.left-align {{ justify-content: center; background: #f8fafc; border-radius: 6px 6px 0 0; text-align: center; padding: 10px; }}
                    #{table_id} td.left-align::before {{ content: none; }}
                }}
            </style>
            """
            tr_html = ""
            for row in rows:
                td_html = ""
                for idx, col in enumerate(row):
                    cls = "left-align" if idx == 0 else ""
                    color_style = ""
                    if idx == len(row) - 1:
                        if "정상" in col and "비정상" not in col:
                            color_style = "color: #16a34a; font-weight:700;"
                        elif "비정상" in col or "침범" in col or "확진" in col or "마비" in col or "소실" in col:
                            color_style = "color: #dc2626; font-weight: 800;"
                    
                    formatted_col = col.replace(" / ", "<br/>") if "휴식" in headers[idx] else col
                    td_html += f"<td data-label='{headers[idx]}' class='{cls}' style='{color_style}'><span>{formatted_col}</span></td>"
                tr_html += f"<tr>{td_html}</tr>"
            return f'{css}<table id="{table_id}"><thead><tr>{"".join([f"<th>{h}</th>" for h in headers])}</tr></thead><tbody>{tr_html}</tbody></table>'

        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="case-section-label">📋 근전도 결과표 (NCS & Needle EMG): 병변측 ({data["info"]["side"]})</div>', unsafe_allow_html=True)

        st.markdown('<div class="finding-highlight">⚡ 감각신경전도검사 (Sensory NCS)</div>', unsafe_allow_html=True)
        st.markdown(create_responsive_table(["검사 신경", "진폭 판독", "잠복기 판독", "최종 판정 및 정상 기준"], data["ncs_sensory"], "sensory_tbl"), unsafe_allow_html=True)

        st.markdown('<div class="finding-highlight">⚡ 운동신경전도검사 (Motor NCS)</div>', unsafe_allow_html=True)
        st.markdown(create_responsive_table(["검사 신경", "자극 위치", "진폭 판독", "잠복기 판독", "최종 판정"], data["ncs_motor"], "motor_tbl"), unsafe_allow_html=True)

        st.markdown('<div class="finding-highlight">🪡 침근전도검사 (Needle EMG)</div>', unsafe_allow_html=True)
        st.markdown(create_responsive_table(["검사 근육", "해당 분절 (Root)", "휴식 시 반응 (Rest)", "근수축 시 반응 (Volition - MU recruitment)", "근생리 상태 진단"], data["emg"], "emg_tbl"), unsafe_allow_html=True)

        st.markdown("""
        <div class="info-legend-box" style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:8px; padding:10px; margin-top:15px; font-size:0.83rem; line-height:1.45;">
            ℹ️ <b>결과표 약어 해설 사전:</b><br/>
            • <b>Silent at rest:</b> 휴식 시 생리적 무반응(정상 상태)<br/>
            • <b>Fibrillation potential:</b> 섬유자발전위 (축삭 사멸 시 개별 근섬유의 단독 미세 수축)<br/>
            • <b>Positive sharp wave:</b> 양성예파 (탈신경된 근섬유 침 자극 시 유발되는 비정상 자발활동)<br/>
            • <b>MU recruitment:</b> 운동단위 동원패턴 (근수축 강도에 비례한 운동단위 참여도)<br/>
            • <b>MUAPs:</b> 운동단위활동전위 (Motor Unit Action Potentials)<br/>
            • <b>Giant MUAP:</b> 거대 운동단위전위 (탈신경 후 인접 생존 신경가지의 Sprouting 재지배로 형성된 거대 파형)<br/>
            • <b>No MUAPs on volition:</b> 의지적인 근수축(Volition) 시도에도 불구하고 운동단위 전위가 전혀 동원되지 않는 완전 마비 상태
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown('<div class="result-title">✅ 임상 추론 및 생리학적 해석 결과</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="result-text"><span class="label-strong text-red" style="font-size:1.05rem;">최종 의심 진단명:</span> <span style="font-weight:800; color:#1e293b; font-size:1.05rem; margin-left:8px;">{data["diagnosis"]}</span></div>', unsafe_allow_html=True)
        st.markdown('<hr class="item-divider">', unsafe_allow_html=True)
        
        st.markdown('<div class="result-label">🧠 데이터 해석 논리</div>', unsafe_allow_html=True)
        for i in data["interpretation"]: st.markdown(f'<div class="finding-subtext">• {i}</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="result-label" style="border-left-color: #d97706; background: #fffbeb;">🔬 근전도 소견 생리학적 의미</div>', unsafe_allow_html=True)
        for m in data["emg_meaning"]:
            parts = m.split(":", 1)
            if len(parts) == 2: st.markdown(f'<div class="finding-subtext"><span class="label-strong text-blue">{parts[0]}:</span> {parts[1]}</div>', unsafe_allow_html=True)
            else: st.markdown(f'<div class="finding-subtext">• {m}</div>', unsafe_allow_html=True)

        st.markdown('<div class="result-label" style="border-left-color: #9333ea; background: #fdf4ff;">🧭 감별 진단 및 추가 검사</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="finding-subtext">• {data["ddx"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div style="text-align: center; margin-top: 15px; margin-bottom: 25px;">', unsafe_allow_html=True)
        if st.button("🔄 다른 임상 케이스 분석하기", key="reset_report_case_btn"):
            st.session_state["selected_report_case"] = None
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    render_bottom_navigation()
