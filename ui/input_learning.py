# ui/input_learning.py

import re
import streamlit as st
from ui.navigation import render_bottom_navigation

VIRTUAL_REPORTS = {
    "왼쪽 목/어깨 통증 및 팔 저림 (C6 신경뿌리병증 의심)": {
        "info": {"age": 45, "sex": "남성", "symptom": "왼쪽 목 통증 및 무감각, 엄지/검지 손가락 끝 저림, 팔꿉관절 굽힘력 감소", "side": "왼쪽"},
        "diagnosis": "왼쪽 C6 목 신경뿌리병증 (Cervical radiculopathy)",
        "ncs_sensory": [["정중신경 감각신경활동전위(Median SNAP)", "25 μV", "2.8 ms", "정상 범위"], ["자신경 감각신경활동전위(Ulnar SNAP)", "22 μV", "2.5 ms", "정상 범위"]],
        "ncs_motor": [["정중신경 복합근육활동전위(Median CMAP) 손목", "-", "8.5 mV", "3.5 ms", "정상 범위"], ["정중신경 복합근육활동전위(Median CMAP) 팔꿈치", "-", "8.1 mV", "7.8 ms", "정상 범위"]],
        "emg": [
            ["위팔두갈래근(Biceps brachii)", "C5-C6", "Fibrillation, Positive sharp wave", "Reduced MUAPs", "비정상 반응(활동성 탈신경 추정)"],
            ["긴노쪽손목폄근(ECRL)", "C6-C7", "Fibrillation, Positive sharp wave", "Giant MUAPs 출현, Reduced MUAPs", "비정상 반응(만성 재신경지배 동반)"],
            ["짧은엄지벌림근(APB)", "C8-T1", "Silent at rest", "Normal MUAPs", "정상 반응"],
            ["목 척추주위근(Cervical Paraspinal)", "C6", "Fibrillation, Positive sharp wave", "통증으로 인해 평가불가", "비정상 반응(활동성 탈신경 추정)"]
        ],
        "interpretation": [
            "감각신경활동전위(SNAP)가 정상 범위로 보존됩니다. 이는 감각 세포체가 위치한 뒤뿌리신경절(DRG)보다 몸쪽(Proximal)에서 목 신경뿌리 압박 병변이 일어났음을 입증합니다.",
            "침근전도검사(Needle EMG)에서 동일한 C6 신경 분절 지배를 공유하는 복수 근육들 및 목 척추주위근육에서 활동성 탈신경 자발전위가 검출되어 C6 목 신경뿌리병증으로 확진합니다."
        ],
        "emg_meaning": [
            "Fibrillation, Positive sharp wave: 신경 지배를 탈락한 개별 근섬유막의 전기적 불안정성을 고발하는 이상 자발전위입니다.",
            "Reduced MUAPs: 수의수축 시 동원 및 결합되는 운동단위 숫자의 정량적 감소 상태를 뜻합니다."
        ],
        "ddx": "목 디스크 협착 병변을 감별하기 위해 목 MRI 정밀 영상 검사와의 대조 분석이 요구됩니다."
    },
    "오른쪽 1~3번째 손가락 저림 및 야간통 (손목굴증후군 의심)": {
        "info": {"age": 52, "sex": "여성", "symptom": "오른쪽 1, 2, 3번째 손가락 노쪽 분포 영역 저림, 야간 통증 및 손목관절 굽힘 시 통증 악화", "side": "오른쪽"},
        "diagnosis": "오른쪽 손목굴증후군 (Carpal tunnel syndrome)",
        "ncs_sensory": [["정중신경 감각신경활동전위(Median SNAP)", "8 μV (감소/정상측 25 μV)", "4.8 ms (지연/정상측 2.8 ms)", "비정상 반응"], ["자신경 감각신경활동전위(Ulnar SNAP)", "25 μV", "2.6 ms", "정상 범위"]],
        "ncs_motor": [["정중신경 복합근육활동전위(Median CMAP) 손목", "-", "3.1 mV (감소/정상측 8.5 mV)", "5.5 ms (지연/정상측 3.5 ms)", "비정상 반응"], ["정중신경 복합근육활동전위(Median CMAP) 팔꿈치 자극", "-", "2.9 mV", "9.8 ms", "비정상 반응"]],
        "emg": [["짧은엄지벌림근(APB)", "C8-T1", "Silent at rest", "Normal MUAPs", "정상 반응"], ["첫째등쪽뼈사이근(FDI)", "C8-T1", "Silent at rest", "Normal MUAPs", "정상 반응"]],
        "interpretation": [
            "정중신경 감각전도 SNAP과 운동전도 복합근육활동전위(CMAP)의 잠복기 지연이 나타나 손목 영역의 국소 말이집탈락 압박 상태를 고시합니다.",
            "정중신경 진폭의 유의미한 감소가 관찰되어, 단순 말이집탈락을 넘어 운동 축삭 손상이 함께 전개되고 있음을 의미합니다."
        ],
        "emg_meaning": [
            "Silent at rest: 휴식 시 어떠한 비정상 전위 자발전위도 유발되지 않는 생리적 침묵 상태입니다.",
            "Normal MUAPs: 등척성/등장성 수의수축 요구도에 맞추어 하위 운동 단위들이 조화롭게 동원되는 양상입니다."
        ],
        "ddx": "목 신경뿌리 장애와의 감별을 위해 이학적 반사 검사 및 손목 정중신경 주행 부위 티넬 징후 확인이 동반되어야 합니다."
    },
    "왼쪽 허리 통증 및 엄지발가락 올림 약화 (L5 신경뿌리병증 의심)": {
        "info": {"age": 58, "sex": "여성", "symptom": "왼쪽 허리통증-종아리 가쪽 및 발등 통증, 보행 시 발목관절 등굽힘 약화로 발끝 끌림", "side": "왼쪽"},
        "diagnosis": "왼쪽 L5 허리 신경뿌리병증 (Lumbar radiculopathy)",
        "ncs_sensory": [["얕은종아리신경 감각신경활동전위(Superficial Peroneal SNAP)", "12 μV", "2.9 ms", "정상 범위"], ["장딴지신경 감각신경활동전위(Sural SNAP)", "15 μV", "3.1 ms", "정상 범위"]],
        "ncs_motor": [["종아리신경 복합근육활동전위(Peroneal CMAP) 발목", "-", "3.5 mV", "4.5 ms", "정상 범위"], ["종아리신경 복합근육활동전위(Peroneal CMAP) 오금", "-", "3.3 mV", "11.2 ms", "정상 범위"]],
        "emg": [
            ["앞정강근(Tibialis Anterior)", "L4-L5", "Fibrillation, Positive sharp wave", "Reduced MUAPs", "비정상 반응(활동성 탈신경 추정)"],
            ["긴종아리근(Peroneus Longus)", "L5-S1", "Fibrillation, Positive sharp wave", "Giant MUAPs 출현, Reduced MUAPs", "비정상 반응(만성 재신경지배 동반)"],
            ["가자미근(Soleus)", "S1-S2", "Silent at rest", "Normal MUAPs", "정상 반응"],
            ["허리 척추주위근(Lumbar Paraspinal)", "L5", "Fibrillation, Positive sharp wave", "통증으로 인해 평가불가", "비정상 반응(활동성 탈신경 추정)"]
        ],
        "interpretation": [
            "다리의 주요 표재 감각신경활동전위들이 정상 보존되어 병터가 허리 뒤뿌리신경절보다 몸쪽에 국한된 허리 신경뿌리 장애임을 지시합니다.",
            "L5 신경 분절의 지배를 받는 앞정강근 및 긴종아리근, 그리고 허리 척추주위근육에서 비정상 자발전위가 동시에 터져 나와 L5 허리 신경뿌리병증으로 정의됩니다."
        ],
        "emg_meaning": [
            "Giant MUAPs: 손상된 신경을 대신하여 생존 축삭이 발아해 들어가 해당 탈신경 근섬유를 만성 재지배한 결과물입니다."
        ],
        "ddx": "L4-L5 척수 신경뿌리의 디스크 압박 수준을 진단하기 위해 허리엉치 MRI 검사 의뢰가 추천됩니다."
    },
    "오른쪽 어깨 통증 및 손 내재근 위축 (가슴문증후군 의심)": {
        "info": {"age": 38, "sex": "여성", "symptom": "오른쪽 어깨 및 빗장뼈 하부 통증, 새끼손가락 쪽 감각 이상, 짧은엄지벌림근 위축 양상 동반", "side": "오른쪽"},
        "diagnosis": "오른쪽 가슴문증후군 (Thoracic outlet syndrome)",
        "ncs_sensory": [["가쪽아래팔피부신경 감각신경활동전위(LAC SNAP)", "25 μV", "2.1 ms", "정상 범위"], ["안쪽아래팔피부신경 감각신경활동전위(MAC SNAP)", "2 μV (감소/정상측 15 μV)", "3.9 ms (지연/정상측 2.1 ms)", "비정상 반응"]],
        "ncs_motor": [["정중신경 복합근육활동전위(Median CMAP) 손목", "-", "3.8 mV (감소/정상측 8.5 mV)", "4.0 ms", "비정상 반응"], ["자신경 복합근육활동전위(Ulnar CMAP) 손목", "-", "4.1 mV", "3.2 ms", "정상 범위"]],
        "emg": [
            ["짧은엄지벌림근(APB)", "C8-T1", "Silent at rest", "Giant MUAPs 출현, Reduced MUAPs", "비정상 반응(Gilliatt-Sumner hand)"],
            ["첫째등쪽뼈사이근(FDI)", "C8-T1", "Silent at rest", "Giant MUAPs 출현, Reduced MUAPs", "비정상 반응(Gilliatt-Sumner hand)"],
            ["위팔두갈래근(Biceps brachii)", "C5-C6", "Silent at rest", "Normal MUAPs", "정상 반응"],
            ["목 척추주위근(C8-T1)", "C8-T1", "Silent at rest", "Normal MUAPs", "정상 반응"]
        ],
        "interpretation": [
            "위팔신경얼기 하부 신경줄기가 빗장뼈 아래 통로에서 물리 압박을 받는 가슴문증후군 기전입니다. 안쪽아래팔피부신경 감각신경활동전위의 진폭이 극적으로 감소하여 신경얼기 수준의 먼쪽 변성을 가리칩니다.",
            "T1 우세 지배인 짧은엄지벌림근과 첫째등쪽뼈사이근에서 만성적인 거대운동단위활동전위가 관찰되는 반면, 목 척추주위근육은 완전 정상이므로 척수 신경뿌리를 배제하고 가슴문 영역의 압박성 마비로 확진합니다."
        ],
        "emg_meaning": [
            "Gilliatt-Sumner hand: 가슴문증후군 장기화로 인해 T1 운동 지배 가지가 소실되어, 짧은엄지벌림근을 중심으로 손 내재근이 심하게 위축되는 임상적 변성 양상입니다."
        ],
        "ddx": "목갈비근 단축 긴장을 감별하기 위한 Adson 검사 연계 및 이학적 가슴문 압박 가동 검사가 추천됩니다."
    }
}

def format_title_box(kor):
    return f"<div class='title-box'><div class='title-kor'>{kor}</div></div>"

def format_middle_title(kor):
    return f"<div class='sub-title'>{kor}</div>"

def format_nerve_name_eng_below(text):
    """한글 아래 영문을 작은 글씨로 떨어뜨려 괄호로 인한 어색한 여백 발생 원천 차단"""
    if not text: return ""
    text = str(text)
    m = re.match(r'^(.*?)\s*\((.*?)\)$', text)
    if m:
        kor = m.group(1).strip()
        eng = m.group(2).strip()
        words = eng.split()
        res = []
        acronyms = {"SNAP", "CMAP", "MUAP", "MUAPS", "NCS", "EMG", "MAS", "DRT", "UMN", "LMN", "TA", "ECR", "EIP", "ADM", "FDI", "EHL", "PL", "R1", "R2", "H", "F", "MU"}
        for w in words:
            clean_w = re.sub(r'[^a-zA-Z]', '', w).upper()
            if clean_w in acronyms: res.append(w.upper())
            else: res.append(w.lower())
        eng_formatted = ' '.join(res)
        return f"<div style='font-size:0.95rem; font-weight:800; color:#1e293b; margin-bottom:2px;'>{kor}</div><div style='font-size:0.8rem; font-weight:500; color:#64748b; line-height:1.1;'>{eng_formatted}</div>"
    else:
        return f"<div style='font-size:0.95rem; font-weight:800; color:#1e293b;'>{text}</div>"

def _get_data_row(lbl, val, is_bad=False):
    color = "txt-red" if is_bad else ("txt-green" if "정상 범위" in val or "정상 반응" in val else "txt-normal")
    return f'<div class="data-row"><div class="data-label">{lbl}</div><div class="data-value {color}">{val}</div></div>'

def render_interpretation_text(lines):
    for x in lines:
        clean_text = re.sub(r'\([a-zA-Z\s\-]+\)', '', str(x)).replace("  ", " ").strip()
        if ":" in clean_text:
            parts = clean_text.split(":", 1)
            st.markdown(f'<div style="font-size:0.9rem; margin-bottom:8px;"><span style="font-weight:800; color:#1d4ed8;">{parts[0]}:</span> <span style="color:#334155;">{parts[1]}</span></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div style="font-size:0.9rem; color:#334155; margin-bottom:8px;">• {clean_text}</div>', unsafe_allow_html=True)

def render_input_learning():
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">가상 결과지 선택</div>', unsafe_allow_html=True)

    case_names = ["선택 안 함"] + list(VIRTUAL_REPORTS.keys())
    if "input_reset_counter" not in st.session_state: st.session_state["input_reset_counter"] = 0
    selected = st.radio("결과지 선택", case_names, key=f"report_{st.session_state['input_reset_counter']}", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

    if selected != "선택 안 함":
        data = VIRTUAL_REPORTS[selected]

        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.markdown(f'<div style="font-weight:800; font-size:0.95rem; color:#0f172a; margin-bottom:6px;">👤 환자 사례: {selected}</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="font-size:0.85rem; color:#475569;">연령/성별: {data["info"]["age"]}세 / {data["info"]["sex"]} &nbsp;|&nbsp; 병변측: {data["info"]["side"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="margin-top:10px;"><div style="font-size:0.9rem; font-weight:800; color:#0f172a; margin-bottom:4px;">주요 임상 증상:</div><div style="font-size:0.9rem; color:#334155;">{data["info"]["symptom"]}</div></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        def render_table_section(title_kor, headers, rows):
            st.markdown(format_middle_title(title_kor), unsafe_allow_html=True)
            for row in rows:
                nerve = row[0]
                # 🚨 시각적 블록화 (박스 없이 여백과 백그라운드로만 처리)
                st.markdown(f'<div style="background:#f8fafc; padding:12px; border-radius:8px; margin-bottom:12px;">{format_nerve_name_eng_below(nerve)}<div style="margin-top:8px;">', unsafe_allow_html=True)
                
                for idx, col in enumerate(row[1:]):
                    col_str = str(col)
                    if col_str == "-": continue
                    is_bad = any(x in col_str for x in ["비정상", "감소", "지연", "Gilliatt"])
                    st.markdown(_get_data_row(headers[idx+1], col_str, is_bad), unsafe_allow_html=True)
                st.markdown('</div></div>', unsafe_allow_html=True)

        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="section-title">근전도 검사 결과 (병변측: {data["info"]["side"]})</div>', unsafe_allow_html=True)

        render_table_section("🖐️ 감각신경전도검사", ["검사 신경", "진폭", "잠복기", "판단"], data["ncs_sensory"])
        render_table_section("⚡ 운동신경전도검사", ["검사 신경", "자극 위치", "진폭", "잠복기", "판단"], data["ncs_motor"])
        render_table_section("🪡 침근전도검사", ["검사 근육", "지배 수준", "휴식 시", "수의적 수축 시", "판단"], data["emg"])
        st.markdown('</div>', unsafe_allow_html=True)

        # 🚨 진단명 포맷팅 적용 (글자크기 동일, 라벨만 회색)
        kor_diag = data['diagnosis'].split('(')[0].strip()
        eng_diag = f"({data['diagnosis'].split('(')[1]}" if '(' in data['diagnosis'] else ""
        
        st.markdown(f"""
        <div style="background:#f8fafc; border-left:4px solid #64748b; padding:14px; border-radius:6px; margin-bottom:20px;">
            <span style="font-size:1.0rem; font-weight:800; color:#475569; margin-right:8px;">의심질환 추정 진단명:</span>
            <span style="font-size:1.0rem; font-weight:800; color:#b91c1c;">{kor_diag}</span>
            <span style="font-size:0.85rem; font-weight:500; color:#94a3b8; margin-left:4px;">{eng_diag}</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">검사 결과 통합 해석</div>', unsafe_allow_html=True)
        
        st.markdown(format_middle_title("신경전도 해석 포인트"), unsafe_allow_html=True)
        render_interpretation_text(data["interpretation"])
        
        st.markdown(format_middle_title("침근전도 소견 생리학적 의미"), unsafe_allow_html=True)
        render_interpretation_text(data["emg_meaning"])
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">감별진단 포인트</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="case-bullet">{data["ddx"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="nav-wrapper" style="margin-top: 24px; margin-bottom: 12px;">', unsafe_allow_html=True)
        col_l, col_c, col_r = st.columns([1, 1.5, 1])
        with col_c:
            if st.button("다른 결과 분석", type="primary", use_container_width=True):
                st.session_state["input_reset_counter"] += 1
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    render_bottom_navigation()
