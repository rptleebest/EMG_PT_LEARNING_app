# ui/input_learning.py

import streamlit as st
import pandas as pd
from ui.navigation import render_bottom_navigation

# =====================================================================
# 가상의 실제 수치 데이터 세팅 (방대하게 확장된 대표 임상 케이스 6종)
# =====================================================================
VIRTUAL_REPORTS = {
    "1. 좌측 목/어깨 통증 및 팔 저림 (C6 신경뿌리병증 의심)": {
        "info": {"age": 45, "sex": "남성", "symptom": "좌측 목 통증, 엄지/검지 저림, 위팔두갈래근(Biceps) 근력 약화", "side": "좌측"},
        "diagnosis": "좌측 C6 신경뿌리병증 (C6 Radiculopathy)",
        "ncs_sensory": [
            ["정중신경(Median)", "손목(Wrist)", "2.8", "25", "정상 (정상범위: 잠복기 <3.5, 진폭 >20)"],
            ["자신경(Ulnar)", "손목(Wrist)", "2.5", "22", "정상 (정상범위: 잠복기 <3.1, 진폭 >15)"]
        ],
        "ncs_motor": [
            ["정중신경(Median)", "손목(Wrist)", "3.5", "8.5", "정상 (정상범위: 잠복기 <4.2, 진폭 >4.0)"],
            ["정중신경(Median)", "팔꿈치(Elbow)", "7.8", "8.1", "정상 (정상범위: 근위부 진폭 >4.0)"]
        ],
        "emg": [
            ["위팔두갈래근(Biceps)", "근육피부신경 / C5-C6", "Fibrillation potential(+), Positive sharp wave(+)", "운동단위 동원감소(Reduced recruitment)", "신경뿌리병증 의심(활동성)"],
            ["노쪽손목폄근(ECR)", "노신경 / C6-C7", "Fibrillation potential(+), Positive sharp wave(+)", "거대 운동단위전위 출현(Giant MUAP)", "신경뿌리병증 의심(만성)"],
            ["짧은엄지벌림근(APB)", "정중신경 / C8-T1", "전기적 침묵(electrical silence)", "정상 운동단위 동원패턴(normal recruitment)", "정상"],
            ["목 척추주위근(Cervical Paraspinal)", "척수신경후지 / C6", "Fibrillation potential(+), Positive sharp wave(+)", "평가불가(통증/해부학적 한계)", "신경뿌리병증 의심"]
        ],
        "interpretation": [
            "감각신경전도검사(SNAP)가 모두 정상입니다. 이는 병변이 뒤뿌리신경절(DRG)보다 몸쪽(근위부)인 신경뿌리(Root)에 있음을 강하게 시사합니다.",
            "침근전도에서 위팔두갈래근, 노쪽손목폄근 및 목 척추주위근에 자발전위(비정상)가 보입니다.",
            "위 근육들은 서로 다른 말초신경의 지배를 받지만, 공통적으로 C6 신경뿌리의 지배를 받으므로 C6 신경뿌리병증이 확실시됩니다."
        ],
        "emg_meaning": [
            "Fibrillation potential / Positive sharp wave: 축삭 손상으로 인해 근육이 탈신경화(denervation)되어 나타나는 급성/활동성 자발전위입니다.",
            "운동단위 동원감소(Reduced recruitment): 신경 손상으로 동원될 수 있는 운동단위(Motor unit)의 절대적인 숫자가 감소했음을 의미합니다.",
            "거대 운동단위전위 출현(Giant MUAP): 만성적인 손상 후, 살아남은 인접 신경이 가지치기(collateral sprouting)를 통해 재신경지배(reinnervation)를 이룬 상태를 의미합니다."
        ],
        "ddx": "디스크 탈출증(Herniated Nucleus Pulposus)이나 척추관 협착증 확인을 위해 경추 MRI 검사가 강력히 권장됩니다."
    },

    "2. 우측 1~3번째 손가락 저림 및 야간통 (손목굴증후군 의심)": {
        "info": {"age": 52, "sex": "여성", "symptom": "우측 1,2,3번째 손가락 저림, 밤에 통증 심해짐, 물건을 자주 놓침", "side": "우측"},
        "diagnosis": "우측 중증 손목굴증후군 (Severe Carpal Tunnel Syndrome)",
        "ncs_sensory": [
            ["정중신경(Median)", "손목(Wrist)", "4.8", "8", "비정상 (정상범위: 잠복기 <3.5, 진폭 >20)"],
            ["자신경(Ulnar)", "손목(Wrist)", "2.6", "25", "정상 (정상범위: 잠복기 <3.1, 진폭 >15)"]
        ],
        "ncs_motor": [
            ["정중신경(Median)", "손목(Wrist)", "5.5", "3.1", "비정상 (정상범위: 잠복기 <4.2, 진폭 >4.0)"],
            ["정중신경(Median)", "팔꿈치(Elbow)", "9.8", "2.9", "비정상 (정상범위: 진폭 >4.0)"]
        ],
        "emg": [
            ["짧은엄지벌림근(APB)", "정중신경 / C8-T1", "Positive sharp wave(+)", "거대 운동단위전위 출현(Giant MUAP)", "국소 신경병증(만성 축삭손상)"],
            ["첫째등쪽뼈사이근(FDI)", "자신경 / C8-T1", "전기적 침묵(electrical silence)", "정상 운동단위 동원패턴", "정상"],
            ["목 척추주위근(Paraspinal)", "척수신경후지 / C8-T1", "전기적 침묵(electrical silence)", "평가불가", "정상"]
        ],
        "interpretation": [
            "정중신경에서만 감각신경 잠복기 지연(말이집탈락성) 및 진폭 감소(축삭 손상)가 혼재되어 나타납니다. 자신경은 정상입니다.",
            "목 척추주위근이 정상이므로 C8-T1 신경뿌리병증을 배제할 수 있으며, 손목 부위에서의 국소적인 포착성 신경병증(Entrapment neuropathy)입니다."
        ],
        "emg_meaning": [
            "말초 포착 신경병증에서 진폭 감소: 초기의 단순 말이집탈락성(demyelination) 단계를 넘어, 신경 안쪽의 축삭(axon)까지 구조적 손상이 진행되었음을 의미합니다.",
            "거대 운동단위전위 출현(Giant MUAP): 포착이 오랜 기간 지속되어 만성적인 재신경지배가 일어났음을 나타냅니다."
        ],
        "ddx": "당뇨병성 다발신경병증 등 전신성 대사질환 동반 여부 확인이 필요합니다."
    },

    "3. 좌측 허리 통증 및 엄지발가락 올림 약화 (L5 신경뿌리병증 의심)": {
        "info": {"age": 58, "sex": "여성", "symptom": "좌측 엉덩이부터 종아리 가쪽으로 뻗치는 통증, 발처짐(Foot drop) 증상", "side": "좌측"},
        "diagnosis": "좌측 L5 신경뿌리병증 (L5 Radiculopathy)",
        "ncs_sensory": [
            ["얕은종아리신경(S.Peroneal)", "발목(Ankle)", "2.9", "12", "정상 (정상범위: 잠복기 <3.5, 진폭 >10)"],
            ["장딴지신경(Sural)", "발목(Ankle)", "3.1", "15", "정상 (정상범위: 잠복기 <3.6, 진폭 >10)"]
        ],
        "ncs_motor": [
            ["종아리신경(Peroneal)", "발목(Ankle)", "4.5", "3.5", "정상 (정상범위: 잠복기 <6.0, 진폭 >2.0)"],
            ["종아리신경(Peroneal)", "오금(Fibular head)", "11.2", "3.3", "정상"]
        ],
        "emg": [
            ["앞정강근(Tibialis Anterior)", "깊은종아리신경 / L4-L5", "Fibrillation potential(+), Positive sharp wave(+)", "운동단위 동원 감소", "신경뿌리병증 의심"],
            ["긴종아리근(Peroneus Longus)", "얕은종아리신경 / L5-S1", "Positive sharp wave(+)", "거대 운동단위전위 출현", "신경뿌리병증 의심"],
            ["가자미근(Soleus)", "정강신경 / S1-S2", "전기적 침묵(electrical silence)", "정상 운동단위 동원패턴", "정상"],
            ["허리 척추주위근(Lumbar Paraspinal)", "척수신경후지 / L5", "Fibrillation potential(+)", "평가불가", "신경뿌리병증 의심"]
        ],
        "interpretation": [
            "다리의 감각신경전도검사가 완전히 정상입니다. 이는 병변이 말초신경이 아닌 요추 신경뿌리(Root)에 있음을 확인해 줍니다.",
            "앞정강근(L4-L5)과 긴종아리근(L5-S1) 모두에서 비정상 자발전위가 나타났으며, 허리 척추주위근에서도 이상이 확인되어 L5 신경뿌리 병변으로 결론지을 수 있습니다."
        ],
        "emg_meaning": [
            "감각신경 보존의 원리: 신경뿌리병증은 대개 뒤뿌리신경절(DRG)보다 근위부(척수 쪽)에서 발생하므로, DRG 세포체로부터 뻗어나온 말초 감각신경(SNAP)은 전기생리학적으로 온전하게 유지됩니다."
        ],
        "ddx": "L4-L5 추간판 탈출증 또는 요추관 협착증 확인을 위해 요추 MRI 검사가 필요합니다."
    },

    "4. 우측 발처짐 및 종아리 가쪽 감각 저하 (종아리신경 마비 의심)": {
        "info": {"age": 32, "sex": "남성", "symptom": "다리를 꼬고 잔 후 발생한 우측 발처짐(Foot drop), 허리 통증은 없음", "side": "우측"},
        "diagnosis": "우측 온종아리신경 마비 (Common Peroneal Neuropathy at Fibular head)",
        "ncs_sensory": [
            ["얕은종아리신경(S.Peroneal)", "발목(Ankle)", "3.8", "4", "비정상 (정상범위: 잠복기 <3.5, 진폭 >10)"],
            ["장딴지신경(Sural)", "발목(Ankle)", "3.0", "16", "정상 (정상범위: 잠복기 <3.6, 진폭 >10)"]
        ],
        "ncs_motor": [
            ["종아리신경(Peroneal)", "발목(Ankle)", "4.8", "4.5", "정상 (정상범위: 잠복기 <6.0, 진폭 >2.0)"],
            ["종아리신경(Peroneal)", "종아리뼈머리 아래(Below FH)", "11.5", "4.2", "정상"],
            ["종아리신경(Peroneal)", "종아리뼈머리 위(Above FH)", "14.2", "1.1", "비정상 (진폭 50% 이상 급감 - 전도차단)"]
        ],
        "emg": [
            ["앞정강근(Tibialis Anterior)", "깊은종아리신경 / L4-L5", "전기적 침묵(electrical silence)", "무반응(No MUAP recruitment)", "비정상(운동단위 동원소실)"],
            ["긴종아리근(Peroneus Longus)", "얕은종아리신경 / L5-S1", "전기적 침묵(electrical silence)", "운동단위 동원 극히 감소", "비정상"],
            ["가자미근(Soleus)", "정강신경 / S1-S2", "전기적 침묵(electrical silence)", "정상 운동단위 동원패턴", "정상"],
            ["허리 척추주위근(Lumbar Paraspinal)", "척수신경후지 / L5", "전기적 침묵(electrical silence)", "평가불가", "정상"]
        ],
        "interpretation": [
            "종아리뼈머리(Fibular head) 부위를 가로질러 자극했을 때 운동신경 진폭이 급격히 떨어지는 '전도차단(Conduction block)'이 관찰됩니다.",
            "얕은종아리신경(감각)의 진폭이 감소하였고, 척추주위근은 정상이므로 요추 신경뿌리병증(L5)을 명확히 배제할 수 있습니다."
        ],
        "emg_meaning": [
            "전도차단(Conduction block): 축삭은 살아있으나 국소적인 말이집(Myelin) 압박/손상으로 인해 전기 신호가 그 지점을 통과하지 못하는 현상입니다.",
            "무반응(No MUAP recruitment): 수의적인 운동 신호가 차단 부위에 막혀 근육으로 전달되지 않아, 바늘근전도 상 동원되는 운동단위가 전혀 없는 상태입니다."
        ],
        "ddx": "급성 압박성 신경병증(Saturday night palsy). 다리 꼬는 습관 교정 및 발목 보조기(AFO) 착용 여부 평가가 필요합니다."
    },

    "5. 양측 발끝 저림 및 감각 저하 (당뇨병성 다발신경병증 의심)": {
        "info": {"age": 68, "sex": "남성", "symptom": "양쪽 발바닥이 화끈거리고 감각이 무뎌짐 (장갑-양말 분포), 15년 전 당뇨 진단", "side": "양측"},
        "diagnosis": "길이의존성 감각운동 다발신경병증 (Length-dependent Sensorimotor Polyneuropathy)",
        "ncs_sensory": [
            ["장딴지신경(Sural) 우측", "발목(Ankle)", "-", "무반응", "비정상 (반응 소실)"],
            ["장딴지신경(Sural) 좌측", "발목(Ankle)", "-", "무반응", "비정상 (반응 소실)"],
            ["정중신경(Median) 우측", "손목(Wrist)", "3.4", "18", "경미한 이상 (정상범위 경계)"]
        ],
        "ncs_motor": [
            ["정강신경(Tibial) 우측", "발목(Ankle)", "6.2", "1.5", "비정상 (정상범위: 잠복기 <6.0, 진폭 >4.0)"],
            ["종아리신경(Peroneal) 우측", "발목(Ankle)", "6.5", "0.8", "비정상 (정상범위: 잠복기 <6.0, 진폭 >2.0)"],
            ["정중신경(Median) 우측", "손목(Wrist)", "4.0", "4.2", "정상"]
        ],
        "emg": [
            ["앞정강근(Tibialis Anterior)", "깊은종아리신경 / L4-L5", "Positive sharp wave(+)", "운동단위 동원 약간 감소", "비정상(만성 진행성)"],
            ["위팔두갈래근(Biceps)", "근육피부신경 / C5-C6", "전기적 침묵(electrical silence)", "정상 운동단위 동원패턴", "정상"]
        ],
        "interpretation": [
            "가장 긴 신경인 하지 감각신경(장딴지신경)에서 반응 소실이 먼저 나타나며, 상지 신경은 상대적으로 보존되는 전형적인 '길이 의존성(Length-dependent)' 패턴입니다.",
            "감각신경과 운동신경이 대칭적으로 침범되었으며, 진폭 감소가 두드러지는 축삭 손상(Axonal loss) 우세형 다발신경병증입니다."
        ],
        "emg_meaning": [
            "길이의존성 다발신경병증: 대사성/독성 원인(당뇨 등)에 의해 세포체에서 가장 멀리 떨어져 영양공급이 취약한 긴 신경의 끝부분부터 서서히 손상(Dying back)되는 병태생리를 반영합니다."
        ],
        "ddx": "당뇨 합병증 외에 비타민 B12 결핍, 알코올성 신경병증 등의 배제가 필요합니다. 발 상처(당뇨발) 주의 교육 필수."
    },

    "6. 상하지 대칭성 근력 저하 (급성 길랭-바레 증후군 의심)": {
        "info": {"age": 41, "sex": "여성", "symptom": "2주 전 장염 앓은 후, 며칠 전부터 다리에서 시작되어 팔로 올라오는 양측 대칭성 근력 약화", "side": "양측"},
        "diagnosis": "급성 염증성 말이집탈락성 다발신경병증 (AIDP / Guillain-Barre Syndrome)",
        "ncs_sensory": [
            ["정중신경(Median)", "손목(Wrist)", "3.8", "22", "비정상 (정상범위: 잠복기 <3.5)"],
            ["장딴지신경(Sural)", "발목(Ankle)", "3.4", "12", "정상 (Sural sparing pattern)"]
        ],
        "ncs_motor": [
            ["종아리신경(Peroneal)", "발목(Ankle)", "8.5", "3.0", "비정상 (정상범위: 잠복기 <6.0)"],
            ["종아리신경(Peroneal)", "오금(Fibular head)", "20.1", "1.2", "비정상 (전도속도 심한 저하 및 시간분산)"],
            ["정중신경(Median)", "손목(Wrist)", "6.8", "4.5", "비정상 (정상범위: 잠복기 <4.2)"]
        ],
        "emg": [
            ["앞정강근(Tibialis Anterior)", "깊은종아리신경 / L4-L5", "전기적 침묵(electrical silence)", "운동단위 동원 심한 감소", "비정상(초기)"],
            ["허리 척추주위근(Lumbar Paraspinal)", "척수신경후지", "전기적 침묵(electrical silence)", "평가불가", "정상"]
        ],
        "interpretation": [
            "상/하지의 여러 운동신경에서 심한 잠복기 지연과 전도속도 저하가 나타나는 명확한 '말이집탈락성(Demyelinating)' 다발신경병증 소견입니다.",
            "상지 감각신경은 이상이 있으나, 하지 장딴지신경(Sural)은 정상으로 보존되는 AIDP의 특징적인 'Sural sparing pattern'이 관찰됩니다."
        ],
        "emg_meaning": [
            "시간분산(Temporal dispersion): 말이집(Myelin)이 불규칙하게 벗겨져 신경섬유 간의 전도 속도가 제각각이 되면서, 파형이 넓게 퍼지고 진폭이 흩어지는 현상입니다.",
            "초기 침근전도 정상: 신경 축삭 자체는 끊어지지 않았기 때문에 발병 초기(2~3주 이내)에는 Fibrillation 같은 탈신경 전위가 나타나지 않을 수 있습니다."
        ],
        "ddx": "뇌척수액 검사(단백세포 해리 확인) 및 면역글로불린(IVIG) 치료 고려. 호흡근 마비 모니터링 필수."
    }
}


def render_input_learning():
    st.markdown('<div class="main-title">가상 근전도 결과표 판독 학습</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtle">실제 임상 현장과 유사한 근전도 수치 표(Raw Data)를 분석하여 병변의 부위와 생리학적 상태를 추론하는 시뮬레이터입니다.</div>', unsafe_allow_html=True)

    # ---------------------------
    # 가상 사례 리스트 (라디오 버튼 방식)
    # ---------------------------
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">1️⃣ 학습할 임상 케이스 선택</div>', unsafe_allow_html=True)
    
    # 드롭다운 대신 라디오 버튼으로 전체 질환명을 노출하여 학습자가 한눈에 파악하도록 함
    selected_case = st.radio(
        "환자의 증상 및 의심 질환 리스트", 
        list(VIRTUAL_REPORTS.keys()),
        label_visibility="collapsed"
    )
    st.markdown('</div>', unsafe_allow_html=True)

    if selected_case:
        data = VIRTUAL_REPORTS[selected_case]
        
        # ---------------------------
        # 환자 정보 요약
        # ---------------------------
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="case-title-mobile">👤 환자 정보 요약</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="case-subtitle-mobile"><span class="label-strong text-blue">연령/성별:</span> <span class="result-value">{data["info"]["age"]}세 / {data["info"]["sex"]}</span> | <span class="label-strong text-blue">병변측:</span> <span class="result-value">{data["info"]["side"]}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="mobile-note"><span class="label-strong text-blue">주요 증상:</span> <span class="result-value">{data["info"]["symptom"]}</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # ---------------------------
        # 근전도 데이터 테이블 직접 렌더링 (CSS 커스텀 표 디자인 - 제목 중앙 정렬 및 굵기 구분)
        # ---------------------------
        st.markdown('<div class="section-card" style="padding-bottom: 25px;">', unsafe_allow_html=True)
        st.markdown('<div class="case-section-label">2️⃣ 근전도 결과표 (Raw Data Table)</div>', unsafe_allow_html=True)
        
        # 표 생성을 위한 HTML/CSS 템플릿 헬퍼
        def create_html_table(headers, rows):
            # 헤더: 중앙 정렬, 굵은 글씨, 배경색 명확히
            th_html = "".join([f"<th style='background-color: #f1f5f9; padding: 10px; text-align: center; font-weight: 800; border-bottom: 2px solid #94a3b8; color: #1e293b; font-size: 0.92rem;'>{h}</th>" for h in headers])
            tr_html = ""
            for row in rows:
                td_html = ""
                for idx, col in enumerate(row):
                    align = "left" if idx == 0 else "center"
                    color = "#0f172a"
                    font_weight = "500"
                    # 결과 열(마지막) 색상 처리
                    if idx == len(row) - 1:
                        if "정상" in col: color = "#16a34a" # Green
                        elif "비정상" in col or "의심" in col: color = "#dc2626"; font_weight = "800" # Red
                    td_html += f"<td style='padding: 8px 10px; border-bottom: 1px solid #e2e8f0; text-align: {align}; color: {color}; font-weight: {font_weight}; font-size: 0.88rem;'>{col}</td>"
                tr_html += f"<tr>{td_html}</tr>"
            
            return f"""
            <div style="overflow-x: auto;">
                <table style="width: 100%; border-collapse: collapse; margin-bottom: 18px; font-family: sans-serif; box-shadow: 0 1px 3px 0 rgba(0,0,0,0.1);">
                    <thead><tr>{th_html}</tr></thead>
                    <tbody>{tr_html}</tbody>
                </table>
            </div>
            """

        # 감각신경전도검사 표
        st.markdown('<div class="finding-highlight">⚡ 감각신경전도검사 (Sensory NCS)</div>', unsafe_allow_html=True)
        ncs_s_headers = ["검사 신경 (Nerve)", "자극 부위", "잠복기(ms)", "진폭(μV)", "결과 판독"]
        st.markdown(create_html_table(ncs_s_headers, data["ncs_sensory"]), unsafe_allow_html=True)
        
        # 운동신경전도검사 표
        st.markdown('<div class="finding-highlight">⚡ 운동신경전도검사 (Motor NCS)</div>', unsafe_allow_html=True)
        ncs_m_headers = ["검사 신경 (Nerve)", "자극 부위", "잠복기(ms)", "진폭(mV)", "결과 판독"]
        st.markdown(create_html_table(ncs_m_headers, data["ncs_motor"]), unsafe_allow_html=True)

        # 침근전도검사 표
        st.markdown('<div class="finding-highlight">🪡 침근전도검사 (Needle EMG)</div>', unsafe_allow_html=True)
        emg_headers = ["검사 근육 (Muscle)", "지배신경 및 분절", "휴식 시 (Rest)", "수의수축 시 (Voluntary)", "결과 판독"]
        st.markdown(create_html_table(emg_headers, data["emg"]), unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

        # ---------------------------
        # 해석 버튼
        # ---------------------------
        if st.button("🔍 근전도 결과 세부 해석 및 감별 진단", type="primary", use_container_width=True):
            st.markdown('<div class="result-card" style="margin-top:20px;">', unsafe_allow_html=True)
            st.markdown('<div class="result-title">✅ 임상 추론 및 생리학적 해석 결과</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="result-text"><span class="label-strong text-red" style="font-size:1.1rem;">최종 의심 진단명:</span> <span style="font-weight:800; color:#1e293b; font-size:1.1rem; margin-left:8px;">{data["diagnosis"]}</span></div>', unsafe_allow_html=True)
            st.markdown('<hr class="item-divider">', unsafe_allow_html=True)
            
            st.markdown('<div class="result-label">🧠 데이터 해석 논리 (Clinical Reasoning)</div>', unsafe_allow_html=True)
            for i in data["interpretation"]:
                st.markdown(f'<div class="finding-subtext">• {i}</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="result-label" style="border-left-color: #d97706; background: #fffbeb;">🔬 근전도 소견의 생리학적 의미 (Physiological Meaning)</div>', unsafe_allow_html=True)
            for m in data["emg_meaning"]:
                # 키워드 강조 처리
                parts = m.split(":", 1)
                if len(parts) == 2:
                    st.markdown(f'<div class="finding-subtext"><span class="label-strong text-blue">{parts[0]}:</span> {parts[1]}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="finding-subtext">• {m}</div>', unsafe_allow_html=True)

            st.markdown('<div class="result-label" style="border-left-color: #9333ea; background: #fdf4ff;">🧭 추가 감별 진단 (Differential Dx)</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="finding-subtext">• {data["ddx"]}</div>', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)

    render_bottom_navigation()