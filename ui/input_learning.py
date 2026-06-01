# ui/input_learning.py

import streamlit as st
from ui.navigation import render_bottom_navigation

# =====================================================================
# 가상의 실제 수치 데이터 세팅 (방대하게 확장된 대표 임상 케이스 6종)
# 실제 병원 판독지(표 7-4, 7-5)의 포맷과 용어(Silent at rest 등)를 완벽히 반영
# =====================================================================
VIRTUAL_REPORTS = {
    "1. 좌측 목/어깨 통증 및 팔 저림 (C6 신경뿌리병증 의심)": {
        "info": {"age": 45, "sex": "남성", "symptom": "좌측 목 통증, 엄지/검지 저림, 위팔두갈래근 근력 약화", "side": "좌측"},
        "diagnosis": "좌측 C6 신경뿌리병증 (C6 Radiculopathy)",
        "ncs_sensory": [
            ["정중신경(Median)", "손목(Wrist)", "2.8", "25", "정상"],
            ["자신경(Ulnar)", "손목(Wrist)", "2.5", "22", "정상"]
        ],
        "ncs_motor": [
            ["정중신경(Median)", "손목(Wrist)", "3.5", "8.5", "정상"],
            ["정중신경(Median)", "팔꿈치(Elbow)", "7.8", "8.1", "정상"]
        ],
        "emg": [
            ["위팔두갈래근(Biceps)", "C5-C6", "Fibrillation(+), Positive sharp wave(+)", "Reduced recruitment", "신경뿌리병증"],
            ["노쪽손목폄근(ECR)", "C6-C7", "Fibrillation(+), Positive sharp wave(+)", "Giant MUAPs", "만성 손상"],
            ["짧은엄지벌림근(APB)", "C8-T1", "Silent at rest", "Normal recruitment", "정상"],
            ["목 척추주위근(Paraspinal)", "C6 Root", "Fibrillation(+), Positive sharp wave(+)", "평가불가", "병변 확진"]
        ],
        "interpretation": [
            "감각신경전도검사(SNAP)가 모두 정상입니다. 이는 병변이 뒤뿌리신경절(DRG)보다 몸쪽(근위부)인 신경뿌리(Root)에 있음을 의미합니다.",
            "침근전도에서 위팔두갈래근, 노쪽손목폄근 및 목 척추주위근에 자발전위(비정상)가 보입니다.",
            "이 근육들은 서로 다른 말초신경의 지배를 받지만, 공통적으로 C6 신경뿌리의 지배를 받으므로 C6 신경뿌리병증으로 확진합니다."
        ],
        "emg_meaning": [
            "Fibrillation / Positive sharp wave: 축삭 손상으로 근육이 신경 지배를 잃었을 때(탈신경화) 나타나는 급성 활동성 자발전위입니다.",
            "Silent at rest: 휴식 시 비정상적인 전기 신호가 없는 '건강한 정상 상태'를 의미합니다."
        ],
        "ddx": "디스크 탈출증이나 척추관 협착증 확인을 위해 경추 MRI 검사가 필요합니다."
    },

    "2. 우측 1~3번째 손가락 저림 및 야간통 (손목굴증후군 의심)": {
        "info": {"age": 52, "sex": "여성", "symptom": "우측 1,2,3번째 손가락 저림, 밤에 통증 심해짐, 쥐기 약화", "side": "우측"},
        "diagnosis": "우측 중증 손목굴증후군 (Severe Carpal Tunnel Syndrome)",
        "ncs_sensory": [
            ["정중신경(Median)", "손목(Wrist)", "4.8", "8", "비정상 (지연/감소)"],
            ["자신경(Ulnar)", "손목(Wrist)", "2.6", "25", "정상"]
        ],
        "ncs_motor": [
            ["정중신경(Median)", "손목(Wrist)", "5.5", "3.1", "비정상 (지연/감소)"],
            ["정중신경(Median)", "팔꿈치(Elbow)", "9.8", "2.9", "비정상 (감소)"]
        ],
        "emg": [
            ["짧은엄지벌림근(APB)", "C8-T1", "Positive sharp wave(+)", "Giant MUAPs", "만성 축삭손상"],
            ["첫째등쪽뼈사이근(FDI)", "C8-T1", "Silent at rest", "Normal recruitment", "정상"],
            ["목 척추주위근(Paraspinal)", "C8-T1", "Silent at rest", "평가불가", "정상"]
        ],
        "interpretation": [
            "정중신경에서만 감각/운동신경 잠복기 지연(말이집탈락성) 및 진폭 감소(축삭 손상)가 혼재되어 나타납니다.",
            "목 척추주위근이 정상이므로 경추 신경뿌리병증을 배제할 수 있으며, 손목 부위에서의 국소적인 포착성 신경병증입니다."
        ],
        "emg_meaning": [
            "진폭 감소 및 Giant MUAPs: 단순 압박을 넘어, 신경 내부의 축삭(axon)까지 구조적 손상이 진행되었으며 만성적인 재신경지배가 일어났음을 의미합니다."
        ],
        "ddx": "당뇨병성 다발신경병증 등 전신성 대사질환 동반 여부 확인이 필요합니다."
    },

    "3. 좌측 허리 통증 및 엄지발가락 올림 약화 (L5 신경뿌리병증 의심)": {
        "info": {"age": 58, "sex": "여성", "symptom": "좌측 엉덩이부터 종아리 가쪽으로 뻗치는 통증, 발처짐 증상", "side": "좌측"},
        "diagnosis": "좌측 L5 신경뿌리병증 (L5 Radiculopathy)",
        "ncs_sensory": [
            ["얕은종아리신경(SPN)", "발목(Ankle)", "2.9", "12", "정상"],
            ["장딴지신경(Sural)", "발목(Ankle)", "3.1", "15", "정상"]
        ],
        "ncs_motor": [
            ["종아리신경(Peroneal)", "발목(Ankle)", "4.5", "3.5", "정상"],
            ["종아리신경(Peroneal)", "오금(Fibular head)", "11.2", "3.3", "정상"]
        ],
        "emg": [
            ["앞정강근(TA)", "L4-L5", "Fibrillation(+), Positive sharp wave(+)", "Reduced recruitment", "신경뿌리병증"],
            ["긴종아리근(PL)", "L5-S1", "Positive sharp wave(+)", "Giant MUAPs", "신경뿌리병증"],
            ["가자미근(Soleus)", "S1-S2", "Silent at rest", "Normal recruitment", "정상"],
            ["허리 척추주위근(L.Para)", "L5 Root", "Fibrillation(+)", "평가불가", "병변 확진"]
        ],
        "interpretation": [
            "다리의 감각신경전도검사(SNAP)가 완전히 정상입니다. 이는 병변이 말초신경이 아닌 요추 신경뿌리(Root)에 있음을 확인해 줍니다.",
            "앞정강근과 긴종아리근, 그리고 허리 척추주위근 모두에서 비정상 자발전위가 나타나 L5 신경뿌리 병변으로 결론짓습니다."
        ],
        "emg_meaning": [
            "감각신경 보존의 원리: 신경뿌리병증은 대개 뒤뿌리신경절(DRG)보다 근위부(척수 쪽)에서 발생하므로, 말초 쪽으로 뻗어나온 감각신경은 온전하게 유지됩니다."
        ],
        "ddx": "L4-L5 추간판 탈출증 또는 요추관 협착증 확인을 위해 요추 MRI 검사가 필요합니다."
    },

    "4. 우측 발처짐 및 종아리 가쪽 감각 저하 (종아리신경 마비 의심)": {
        "info": {"age": 32, "sex": "남성", "symptom": "다리를 꼬고 잔 후 발생한 우측 발처짐, 허리 통증은 없음", "side": "우측"},
        "diagnosis": "우측 온종아리신경 마비 (Common Peroneal Neuropathy)",
        "ncs_sensory": [
            ["얕은종아리신경(SPN)", "발목(Ankle)", "3.8", "4", "비정상 (감소)"],
            ["장딴지신경(Sural)", "발목(Ankle)", "3.0", "16", "정상"]
        ],
        "ncs_motor": [
            ["종아리신경(Peroneal)", "발목(Ankle)", "4.8", "4.5", "정상 (원위부 보존)"],
            ["종아리신경(Peroneal)", "비골두(Fibular head)", "-", "1.1", "비정상 (전도차단)"]
        ],
        "emg": [
            ["앞정강근(TA)", "L4-L5", "Silent at rest", "No MUAPs on volition", "완전 마비"],
            ["긴종아리근(PL)", "L5-S1", "Silent at rest", "Severely reduced", "비정상"],
            ["가자미근(Soleus)", "S1-S2", "Silent at rest", "Normal recruitment", "정상"],
            ["허리 척추주위근(L.Para)", "L5 Root", "Silent at rest", "평가불가", "정상"]
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
            ["장딴지신경(Sural)", "발목(Ankle)", "-", "No response", "비정상 (소실)"],
            ["정중신경(Median)", "손목(Wrist)", "3.4", "18", "경미한 감소"]
        ],
        "ncs_motor": [
            ["정강신경(Tibial)", "발목(Ankle)", "6.2", "1.5", "비정상 (진폭 감소)"],
            ["정강신경(Tibial)", "오금(Popliteal)", "15.2", "1.2", "비정상 (진폭 감소)"]
        ],
        "emg": [
            ["앞정강근(TA)", "L4-L5", "Positive sharp wave(+)", "Reduced recruitment", "만성 진행성"],
            ["위팔두갈래근(Biceps)", "C5-C6", "Silent at rest", "Normal recruitment", "정상"]
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
            ["정중신경(Median)", "손목(Wrist)", "3.8", "22", "비정상 (지연)"],
            ["장딴지신경(Sural)", "발목(Ankle)", "3.4", "12", "정상 (Sparing)"]
        ],
        "ncs_motor": [
            ["종아리신경(Peroneal)", "발목(Ankle)", "8.5", "3.0", "비정상 (심한 지연)"],
            ["종아리신경(Peroneal)", "비골두(Fibular head)", "20.1", "1.2", "비정상 (시간분산)"]
        ],
        "emg": [
            ["앞정강근(TA)", "L4-L5", "Silent at rest", "Severely reduced", "초기 비정상"],
            ["허리 척추주위근(L.Para)", "Lumbar Root", "Silent at rest", "평가불가", "정상"]
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
    st.markdown('<div class="main-title">가상 근전도 결과표 판독 학습</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtle">실제 병원 결과지 형식의 수치를 분석하여 병변 부위를 추론합니다. 모바일에서는 카드로 변환됩니다.</div>', unsafe_allow_html=True)

    # 1. 학습할 케이스 즉시 선택 영역 (버튼 제거)
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">1️⃣ 학습할 임상 케이스 선택</div>', unsafe_allow_html=True)
    
    selected_case = st.radio(
        "환자의 증상 및 의심 질환 리스트", 
        list(VIRTUAL_REPORTS.keys()),
        label_visibility="collapsed"
    )
    st.markdown('</div>', unsafe_allow_html=True)

    if selected_case:
        data = VIRTUAL_REPORTS[selected_case]
        
        # 환자 정보 요약
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.markdown('<div class="case-title-mobile">👤 환자 정보 요약</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="case-subtitle-mobile"><span class="label-strong text-blue">연령/성별:</span> <span class="result-value">{data["info"]["age"]}세 / {data["info"]["sex"]}</span> | <span class="label-strong text-blue">병변측:</span> <span class="result-value">{data["info"]["side"]}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="mobile-note"><span class="label-strong text-blue">주요 증상:</span> <span class="result-value">{data["info"]["symptom"]}</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # ---------------------------
        # 모바일 반응형 HTML/CSS 테이블 생성기 (가장 중요한 부분)
        # ---------------------------
        def create_responsive_table(headers, rows, table_id):
            css = f"""
            <style>
                #{table_id} {{ width: 100%; border-collapse: collapse; margin-bottom: 15px; font-size: 0.88rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
                #{table_id} th {{ background-color: #f1f5f9; padding: 10px; border-bottom: 2px solid #cbd5e1; text-align: center; color: #1e293b; font-weight: 800; }}
                #{table_id} td {{ padding: 10px; border-bottom: 1px solid #e2e8f0; text-align: center; color: #334155; line-height: 1.5; }}
                #{table_id} td.left-align {{ text-align: left; font-weight: 700; color: #1e40af; }}
                
                @media screen and (max-width: 768px) {{
                    #{table_id} thead {{ display: none; }}
                    #{table_id} tr {{ display: block; border: 1px solid #cbd5e1; border-radius: 8px; margin-bottom: 12px; background: #fff; padding: 5px; }}
                    #{table_id} td {{ display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #f1f5f9; padding: 8px 10px; text-align: right; }}
                    #{table_id} td:last-child {{ border-bottom: none; }}
                    #{table_id} td::before {{ content: attr(data-label); font-weight: 800; color: #64748b; text-align: left; padding-right: 10px; flex-shrink: 0; }}
                    #{table_id} td.left-align {{ justify-content: center; background: #f8fafc; border-radius: 6px 6px 0 0; text-align: center; padding: 10px; border-bottom: 2px solid #e2e8f0; }}
                    #{table_id} td.left-align::before {{ content: none; }}
                    
                    /* 긴 텍스트 우측 정렬 유지 보완 */
                    #{table_id} td span {{ text-align: right; word-break: keep-all; }}
                }}
            </style>
            """
            
            tr_html = ""
            for row in rows:
                td_html = ""
                for idx, col in enumerate(row):
                    cls = "left-align" if idx == 0 else ""
                    color_style = ""
                    font_weight = ""
                    
                    # 결과 열(마지막 열) 색상 처리
                    if idx == len(row) - 1:
                        if "정상" in col:
                            color_style = "color: #16a34a;" # Green
                        elif "비정상" in col or "의심" in col or "확진" in col or "마비" in col:
                            color_style = "color: #dc2626;" # Red
                            font_weight = "font-weight: 800;"
                    
                    # 휴식 시 반응 쉼표(,) 줄바꿈 처리 (두 줄 표기 로직)
                    formatted_col = col.replace("), ", ")<br/>") if ("휴식" in headers[idx] or "Rest" in headers[idx]) else col
                    
                    td_html += f"<td data-label='{headers[idx]}' class='{cls}' style='{color_style} {font_weight}'><span>{formatted_col}</span></td>"
                tr_html += f"<tr>{td_html}</tr>"

            th_html = "".join([f"<th>{h}</th>" for h in headers])
            
            return f"""
            {css}
            <table id="{table_id}">
                <thead><tr>{th_html}</tr></thead>
                <tbody>{tr_html}</tbody>
            </table>
            """

        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="case-section-label">2️⃣ 근전도 결과표 (NCS & EMG)</div>', unsafe_allow_html=True)
        
        # 감각신경 표
        st.markdown('<div class="finding-highlight">⚡ 감각신경전도검사 (Sensory NCS)</div>', unsafe_allow_html=True)
        st.markdown(create_responsive_table(["검사 신경", "자극 부위", "잠복기(ms)", "진폭(μV)", "판독 결과"], data["ncs_sensory"], "table_sensory"), unsafe_allow_html=True)
        
        # 운동신경 표 (원위부/근위부 각각 행으로 표현됨)
        st.markdown('<div class="finding-highlight">⚡ 운동신경전도검사 (Motor NCS)</div>', unsafe_allow_html=True)
        st.markdown(create_responsive_table(["검사 신경", "자극 부위", "잠복기(ms)", "진폭(mV)", "판독 결과"], data["ncs_motor"], "table_motor"), unsafe_allow_html=True)

        # 침근전도 표
        st.markdown('<div class="finding-highlight">🪡 침근전도검사 (Needle EMG)</div>', unsafe_allow_html=True)
        st.markdown(create_responsive_table(["검사 근육", "신경/분절(Root)", "휴식 시 (Rest)", "수축 시 (Volition)", "판독 결과"], data["emg"], "table_emg"), unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

        # ---------------------------
        # 즉시 나타나는 해석 블록
        # ---------------------------
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

    render_bottom_navigation()
