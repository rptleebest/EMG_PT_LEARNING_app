# ui/input_learning.py

import re
import streamlit as st
from ui.navigation import render_bottom_navigation

# 🚨 원장님 요청 사항: 10개 사례 완벽 복구 및 실제 수치/정상범위 데이터 세팅
VIRTUAL_REPORTS = {
    "1. C6 신경뿌리병증 의심 (목 통증 및 엄지 저림)": {
        "info": {"age": 45, "sex": "남성", "side": "왼쪽", "symptom": "목-어깨 통증, 엄지/검지 끝 저림"},
        "diagnosis": "왼쪽 C6 목 신경뿌리병증 (Cervical radiculopathy)",
        "results": [
            {"type": "🖐️ 감각신경 (Sensory NCS)", "name": "정중신경(Median SNAP)", "amp": "25.2 μV (정상 / 범위: >15)", "lat": "2.8 ms (정상 / 범위: <3.5)", "judge": "진폭 정상 / 잠복기 정상"},
            {"type": "⚡ 운동신경 (Motor NCS)", "name": "정중신경(Median CMAP)", "amp": "8.5 mV (정상 / 범위: >4.0)", "lat": "3.5 ms (정상 / 범위: <4.2)", "judge": "진폭 정상 / 잠복기 정상"},
            {"type": "🪡 침근전도 (Needle EMG)", "name": "위팔두갈래근(Biceps)", "level": "C5-C6", "rest": "비정상(Fibrillation +1)", "vol": "Reduced MUAPs", "judge": "비정상 반응(활동성 탈신경)"}
        ],
        "logic": ["SNAP 보존은 병변이 DRG 몸쪽에 있음을 의미합니다.", "C6 지배 근육의 탈신경은 신경뿌리 압박을 시사합니다."]
    },
    "2. 손목굴증후군 (1-3지 저림 및 야간통)": {
        "info": {"age": 52, "sex": "여성", "side": "오른쪽", "symptom": "오른손 1-3지 저림, 야간 통증 심화"},
        "diagnosis": "오른쪽 손목굴증후군 (Carpal tunnel syndrome)",
        "results": [
            {"type": "🖐️ 감각신경 (Sensory NCS)", "name": "정중신경(Median SNAP)", "amp": "7.5 μV (감소 / 정상측 25)", "lat": "4.8 ms (지연 / 정상측 2.8)", "judge": "진폭 감소 / 잠복기 지연"},
            {"type": "⚡ 운동신경 (Motor NCS)", "name": "정중신경(Median CMAP)", "amp": "3.2 mV (감소 / 정상측 8.5)", "lat": "5.5 ms (지연 / 정상측 3.5)", "judge": "진폭 감소 / 잠복기 지연"}
        ],
        "logic": ["정중신경의 국소적 지연은 정중신경 포착을 확진합니다."]
    },
    "3. L5 신경뿌리병증 (허리 통증 및 발처짐)": {
        "info": {"age": 58, "sex": "여성", "side": "왼쪽", "symptom": "왼쪽 허리 방사통 및 발목 힘 빠짐"},
        "diagnosis": "왼쪽 L5 허리 신경뿌리병증 (Lumbar radiculopathy)",
        "results": [
            {"type": "🖐️ 감각신경 (Sensory NCS)", "name": "얕은종아리신경(Superficial Peroneal SNAP)", "amp": "12.0 μV (정상 / 범위: >6.0)", "lat": "2.9 ms (정상 / 범위: <4.0)", "judge": "진폭 정상 / 잠복기 정상"},
            {"type": "🪡 침근전도 (Needle EMG)", "name": "앞정강근(Tibialis Anterior)", "level": "L4-L5", "rest": "Fibrillation 관찰", "vol": "Reduced MUAPs", "judge": "비정상 반응(활동성 탈신경)"}
        ],
        "logic": ["L5 지배 근육인 앞정강근의 이상은 해당 분절의 신경근병증을 의미합니다."]
    },
    "4. 온종아리신경 마비 (외부 압박 후 발처짐)": {
        "info": {"age": 32, "sex": "남성", "side": "오른쪽", "symptom": "석고 붕대 제거 후 발생한 발처짐"},
        "diagnosis": "오른쪽 온종아리신경 마비 (Common peroneal neuropathy)",
        "results": [
            {"type": "⚡ 운동신경 (Motor NCS)", "name": "종아리신경(Peroneal CMAP) 비골두", "amp": "1.2 mV (감소 / 범위: >2.0)", "lat": "무반응", "judge": "진폭 감소 / 전도 차단"}
        ],
        "logic": ["비골두 부위의 전도 차단(Conduction Block)이 특징적입니다."]
    },
    "5. 척골신경병증 (4-5지 저림 및 손 근력 약화)": {
        "info": {"age": 42, "sex": "남성", "side": "오른쪽", "symptom": "우측 소지 감각 저하 및 젓가락질 힘듦"},
        "diagnosis": "오른쪽 팔꿈치 부위 척골신경병증 (Ulnar neuropathy at elbow)",
        "results": [
            {"type": "🖐️ 감각신경 (Sensory NCS)", "name": "자신경(Ulnar SNAP)", "amp": "4.8 μV (감소 / 범위: >10)", "lat": "4.0 ms (지연 / 범위: <3.1)", "judge": "진폭 감소 / 잠복기 지연"}
        ],
        "logic": ["팔꿈치 부위 주행 경로상의 지연 소견입니다."]
    },
    "6. 당뇨병성 다발신경병증 (양발 끝 저림)": {
        "info": {"age": 68, "sex": "남성", "side": "양측", "symptom": "양발 바닥 화끈거림 및 감각 무딤"},
        "diagnosis": "길이의존성 축삭성 다발신경병증 (Axonal polyneuropathy)",
        "results": [
            {"type": "🖐️ 감각신경 (Sensory NCS)", "name": "장딴지신경(Sural SNAP)", "amp": "무반응 (소실 / 정상측 15)", "lat": "무반응", "judge": "진폭 소실 (비정상)"}
        ],
        "logic": ["긴 신경부터 손상되는 대사성 신경병증의 전형입니다."]
    },
    "7. 급성 기얭-바레 증후군 (GBS)": {
        "info": {"age": 41, "sex": "여성", "side": "양측", "symptom": "하지 근력 약화 후 상행성 마비 진행"},
        "diagnosis": "급성 염증성 탈말이집성 다발신경병증 (GBS)",
        "results": [
            {"type": "⚡ 운동신경 (Motor NCS)", "name": "종아리신경(Peroneal CMAP)", "amp": "2.8 mV", "lat": "8.8 ms (지연 / 범위 <4.5)", "judge": "광범위 잠복기 지연"}
        ],
        "logic": ["운동신경의 다발성 지연 및 Sural sparing 현상이 중요합니다."]
    },
    "8. C7 신경뿌리병증 (중지 저림)": {
        "info": {"age": 49, "sex": "여성", "side": "오른쪽", "symptom": "가운데 손가락 통증 및 삼두근 근력 저하"},
        "diagnosis": "오른쪽 C7 목 신경뿌리병증 (Cervical radiculopathy)",
        "results": [
            {"type": "🪡 침근전도 (Needle EMG)", "name": "위팔세갈래근(Triceps)", "level": "C7-C8", "rest": "Fibrillation 관찰", "vol": "Reduced MUAPs", "judge": "비정상 반응(활동성 탈신경)"}
        ],
        "logic": ["C7 분절 지배 근육의 이상으로 진단합니다."]
    },
    "9. 가슴문증후군 (TOS)": {
        "info": {"age": 38, "sex": "여성", "side": "오른쪽", "symptom": "어깨 통증 및 손 내재근 위축"},
        "diagnosis": "오른쪽 가슴문증후군 (Thoracic outlet syndrome)",
        "results": [
            {"type": "🖐️ 감각신경 (Sensory NCS)", "name": "안쪽아래팔피부신경(MAC)", "amp": "1.8 μV (감소 / 범위 >15)", "lat": "3.8 ms", "judge": "진폭 감소 (비정상)"}
        ],
        "logic": ["하부 신경얼기 포착에 의한 먼쪽 변성 소견입니다."]
    },
    "10. 얼굴신경마비 (Bell's palsy)": {
        "info": {"age": 29, "sex": "남성", "side": "왼쪽", "symptom": "편측 안면 마비 및 눈 감김 불능"},
        "diagnosis": "왼쪽 특발성 얼굴신경마비 (Bell's palsy)",
        "results": [
            {"type": "⚡ 운동신경 (Motor NCS)", "name": "얼굴신경(Facial CMAP)", "amp": "1.0 mV (감소 / 정상측 3.2)", "lat": "4.6 ms", "judge": "진폭 감소 (심한 축삭 손상)"}
        ],
        "logic": ["정상측 대비 50% 이상의 진폭 감소는 불량한 예후를 시사합니다."]
    }
}

def format_nerve_eng_below(text):
    if not text: return ""
    m = re.match(r'^(.*?)\s*\((.*?)\)$', str(text))
    if m:
        kor, eng = m.group(1).strip(), m.group(2).strip()
        eng_formatted = ' '.join([w.upper() if re.sub(r'[^a-zA-Z]', '', w).upper() in {"SNAP", "CMAP", "MUAP", "MUAPS", "NCS", "EMG", "MU", "MMT"} else w.lower() for w in eng.split()])
        return f"<div style='font-size:0.92rem; font-weight:800; color:#1e293b;'>🔹 {kor}</div><div style='font-size:0.78rem; color:#64748b; margin-left:22px; margin-bottom:6px; line-height:1.1;'>{eng_formatted}</div>"
    return f"<div style='font-size:0.92rem; font-weight:800; color:#1e293b; margin-bottom:8px;'>🔹 {text}</div>"

def _get_data_row(lbl, val, is_bad=False):
    color = "txt-red" if is_bad else ("txt-green" if "정상" in val else "txt-normal")
    return f'<div class="data-row" style="margin-left:22px;"><div class="data-label">{lbl}</div><div class="data-value {color}">{val}</div></div>'

def render_input_learning():
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">가상 결과지 선택</div>', unsafe_allow_html=True)
    selected_name = st.selectbox("리스트", list(VIRTUAL_REPORTS.keys()), key=f"sel_{st.session_state['input_reset_counter']}", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

    data = VIRTUAL_REPORTS[selected_name]
    st.markdown(f'<div class="info-card">👤 <b>환자 정보</b>: {data["info"]["age"]}세 / {data["info"]["sex"]} / 병변측: {data["info"]["side"]} / 증상: {data["info"]["symptom"]}</div>', unsafe_allow_html=True)

    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">⚡ 근전도 검사 결과지 (병변측: {data["info"]["side"]})</div>', unsafe_allow_html=True)
    
    current_type = ""
    for res in data["results"]:
        if res["type"] != current_type:
            current_type = res["type"]
            st.markdown(f'<div class="sub-title">{current_type}</div>', unsafe_allow_html=True)
        
        st.markdown(format_nerve_eng_below(res["name"]), unsafe_allow_html=True)
        if "NCS" in res["type"]:
            st.markdown(_get_data_row("진폭", res["amp"]), unsafe_allow_html=True)
            st.markdown(_get_data_row("잠복기", res["lat"]), unsafe_allow_html=True)
            st.markdown(_get_data_row("판단", res["judge"], "비정상" in res["judge"] or "감소" in res["judge"]), unsafe_allow_html=True)
        else:
            st.markdown(_get_data_row("지배 수준", res["level"]), unsafe_allow_html=True)
            st.markdown(_get_data_row("휴식 시", res["rest"]), unsafe_allow_html=True)
            st.markdown(_get_data_row("수의적 수축 시", res["vol"]), unsafe_allow_html=True)
            st.markdown(_get_data_row("판단", res["judge"], "비정상" in res["judge"]), unsafe_allow_html=True)
        st.markdown('<div style="height:1px; background:#f1f5f9; margin:10px 0;"></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🧠 데이터 판독 및 해석 논리</div>', unsafe_allow_html=True)
    for l in data["logic"]:
        st.markdown(f'<div style="font-size:0.9rem; color:#334155; margin-bottom:8px;">• {l}</div>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="diagnosis-box">
        <span style="font-size:0.9rem; font-weight:700; color:#475569;">🩺 의심 추정질환:</span> 
        <span style="font-size:0.95rem; font-weight:800; color:#b91c1c; margin-left:4px;">{data["diagnosis"]}</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="center-btn-container">', unsafe_allow_html=True)
    if st.button("다른 결과 분석", key="reset_input"): st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    render_bottom_navigation()
