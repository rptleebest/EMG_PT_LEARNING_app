# ui/input_learning.py

import streamlit as st
from data.constants import ANATOMY, DOMAIN_RESULT_OPTIONS
from engine.inference import analyze_manual_input
from ui.navigation import render_bottom_navigation

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
            ["위팔두갈래근 (Biceps Brachii)", "C5-C6 지배 분절", "Fibrillation potentials 및<br/>Positive sharp waves 출현", "Reduced MU recruitment", "비정상 (활동성 탈신경 상태)"],
            ["노쪽손목폄근 (Extensor Carpi Radialis)", "C6-C7 지배 분절", "Fibrillation potentials 및<br/>Positive sharp waves 출현", "Giant MUAPs 출현 및<br/>Reduced MU recruitment", "비정상 (만성 재신경지배 상태)"],
            ["짧은엄지벌림근 (Abductor Pollicis APB)", "C8-T1 지배 분절", "Silent at rest (전기적 침묵)", "Normal MU recruitment", "정상"],
            ["목 척추주위근 (Cervical Paraspinal)", "C6 Root 수준", "Fibrillation potentials 및<br/>Positive sharp waves 출현", "통증으로 인해 동원 제한", "비정상 (활동성 탈신경 상태)"]
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
            ["짧은엄지벌림근 (Abductor Pollicis APB)", "C8-T1 지배 분절", "Positive sharp waves 출현", "Giant MUAPs 출현 및<br/>Reduced MU recruitment", "비정상 (만성 재신경지배 상태)"],
            ["첫째등쪽뼈사이근 (First Dorsal FDI)", "C8-T1 지배 분절", "Silent at rest (전기적 침묵)", "Normal MU recruitment", "정상"]
        ],
        "interpretation": [
            "정중신경에서만 말이집탈락성을 의미하는 국소 전도 잠복기 지연 및 진폭 감소가 확인됩니다.",
            "목 척추주위근이 완전히 정상이므로 C8-T1 신경뿌리병증을 원천 배제할 수 있으며, 손목 부위에 한정된 국소 포착성 단일신경병증입니다."
        ],
        "emg_meaning": [
            "진폭 감소 및 Giant MUAPs: 단순 수초 손상 단계를 지나 신경 내부 축삭(axon) 사멸과 그에 따른 우회로 만성 측부 재지배가 일어났음을 나타냅니다."
        ],
        "ddx": "동일 수근관 부위 포착을 악화시키는 당뇨 및 갑상선 질환 등 전신 대사질환 배제가 병행되어야 합니다."
    }
}


def render_input_learning():
    st.markdown('<div class="main-title">가상 근전도 결과표 판독 학습</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtle">임상 결과 수치를 직접 대입하여 실시간 판독 추론 알고리즘을 체험하거나, 질환별 전형적인 결과표를 입체적으로 학습합니다.</div>', unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["📚 질환별 결과표 분석 (PC/모바일 반응형)", "🔬 가상 판독 시뮬레이터 (수치 대입형)"])

    # ---------------------------------------------------------
    # TAB 1: 질환별 결과표 분석
    # ---------------------------------------------------------
    with tab1:
        if "selected_report_case" not in st.session_state:
            st.session_state["selected_report_case"] = None

        # 1 & 4. 처음 진입 시 자동으로 첫 항목이 체크되는 현상을 방지하기 위해 '선택 안 함' 도입
        if st.session_state["selected_report_case"] is None:
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown('<div class="case-section-label">📋 학습할 환자 사례 선택</div>', unsafe_allow_html=True)
            
            chosen = st.radio(
                "질환 가이드 리스트",
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

            # 모바일 최적화 반응형 렌더링 헬퍼
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
                            elif "비정상" in col or "침범" in col or "확진" in col or "마비" in col:
                                color_style = "color: #dc2626; font-weight: 800;"
                        
                        td_html += f"<td data-label='{headers[idx]}' class='{cls}' style='{color_style}'><span>{col}</span></td>"
                    tr_html += f"<tr>{td_html}</tr>"
                return f'{css}<table id="{table_id}"><thead><tr>{"".join([f"<th>{h}</th>" for h in headers])}</tr></thead><tbody>{tr_html}</tbody></table>'

            # 5. 표제어 수정 적용: 근전도 결과표 (NCS & Needle EMG): 병변측
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown(f'<div class="case-section-label">📋 근전도 결과표 (NCS & Needle EMG): 병변측 ({data["info"]["side"]})</div>', unsafe_allow_html=True)

            st.markdown('<div class="finding-highlight">⚡ 감각신경전도검사 (Sensory NCS)</div>', unsafe_allow_html=True)
            st.markdown(create_responsive_table(["검사 신경", "진폭 판독", "잠복기 판독", "최종 판정 및 정상 기준"], data["ncs_sensory"], "sensory_tbl"), unsafe_allow_html=True)

            st.markdown('<div class="finding-highlight">⚡ 운동신경전도검사 (Motor NCS)</div>', unsafe_allow_html=True)
            st.markdown(create_responsive_table(["검사 신경", "자극 위치", "진폭 판독", "잠복기 판독", "최종 판정"], data["ncs_motor"], "motor_tbl"), unsafe_allow_html=True)

            st.markdown('<div class="finding-highlight">🪡 침근전도검사 (Needle EMG)</div>', unsafe_allow_html=True)
            st.markdown(create_responsive_table(["검사 근육", "해당 분절 (Root)", "휴식 시 반응 (Rest)", "근수축 시 반응 (Volition)", "근생리 상태 진단"], data["emg"], "emg_tbl"), unsafe_allow_html=True)

            # 7. 약어 해설 사전 보강
            st.markdown("""
            <div class="info-legend-box" style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:8px; padding:10px; margin-top:15px; font-size:0.83rem; line-height:1.45;">
                ℹ️ <b>결과표 약어 해설 사전:</b><br/>
                • <b>Silent at rest:</b> 휴식 시 생리적 무반응(정상 상태)<br/>
                • <b>Fibrillation potential:</b> 섬유자발전위 (축삭 사멸 시 개별 근섬유의 단독 미세 수축)<br/>
                • <b>Positive sharp wave:</b> 양성예파 (탈신경된 근섬유 침 자극 시 유발되는 비정상 자발활동)<br/>
                • <b>MU recruitment:</b> 운동단위 동원패턴 (근수축 강도에 비례한 운동단위 참여도)<br/>
                • <b>MUAPs:</b> 운동단위활동전위 (Motor Unit Action Potentials)<br/>
                • <b>Giant MUAP:</b> 거대 운동단위전위 (만성 변성 후 인접 신경의 Sprouting을 통한 가지치기 재신경화 파형)
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

            # 6. 다른 케이스 선택 버튼 배치 (초기화 회귀 대응)
            st.markdown('<div style="text-align: center; margin-top: 15px; margin-bottom: 25px;">', unsafe_allow_html=True)
            if st.button("🔄 다른 임상 케이스 분석하기", key="reset_report_case_btn"):
                st.session_state["selected_report_case"] = None
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    # ---------------------------------------------------------
    # TAB 2: 가상 판독 시뮬레이터 (수치 대입형)
    # ---------------------------------------------------------
    with tab2:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="case-section-label">🔬 자율 신경/근육 전기적 소견 대입기</div>', unsafe_allow_html=True)
        st.write("학생이 가상의 환자 판독값을 조합해 넣으면 알고리즘 분석기를 통해 실시간 주 진단을 유도합니다.")

        selected_findings = {}

        st.markdown('<div class="finding-highlight">⚡ 감각신경계 (Sensory Pathway) 선택</div>', unsafe_allow_html=True)
        for item in ["정중신경 감각신경활동전위 (Median SNAP)", "자신경 감각신경활동전위 (Ulnar SNAP)", "노신경 표재감각신경활동전위 (Superficial Radial SNAP)"]:
            selected_findings[item] = st.selectbox(
                f"{item} 결과",
                DOMAIN_RESULT_OPTIONS["sensory"],
                key=f"manual_sensory_{item}"
            )

        st.markdown('<div class="finding-highlight">⚡ 운동신경계 (Motor Pathway) 선택</div>', unsafe_allow_html=True)
        for item in ["정중신경 복합근육활동전위 (Median CMAP)", "자신경 복합근육활동전위 (Ulnar CMAP)", "노신경 복합근육활동전위 (Radial CMAP)"]:
            selected_findings[item] = st.selectbox(
                f"{item} 결과",
                DOMAIN_RESULT_OPTIONS["motor"],
                key=f"manual_motor_{item}"
            )

        st.markdown('<div class="finding-highlight">🪡 근육 침근전도계 (Needle EMG Pathway) 선택</div>', unsafe_allow_html=True)
        for item in ["목 척추주위근 (Cervical Paraspinal)", "짧은엄지벌림근 (Abductor Pollicis Brevis, APB)", "첫째등쪽뼈사이근 (First Dorsal Interosseous, FDI)", "노쪽손목폄근 (Extensor Carpi Radialis)"]:
            selected_findings[item] = st.selectbox(
                f"{item} 결과",
                DOMAIN_RESULT_OPTIONS["muscle"],
                key=f"manual_muscle_{item}"
            )

        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div style="text-align: center; margin-top: 15px; margin-bottom: 25px;">', unsafe_allow_html=True)
        if st.button("📊 선택한 수치 조합 판독 실행", type="primary", key="run_simulation_btn"):
            res = analyze_manual_input(selected_findings, ANATOMY)

            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown(f'<div class="result-title">🎯 실시간 판독 추론 결과 ({res["severity"]})</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="result-text"><b>의심 병변 위치 1순위:</b> {res["final_dx"]}</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="result-label">🧠 분석 근거</div>', unsafe_allow_html=True)
            for reason in res["reasons"]:
                st.markdown(f'<div class="result-text">• {reason}</div>', unsafe_allow_html=True)
                
            if res["suggestions"]:
                st.markdown('<div class="result-label">🧭 학습 추천 가이드</div>', unsafe_allow_html=True)
                for sug in res["suggestions"]:
                    st.markdown(f'<div class="result-text">• {sug}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    render_bottom_navigation()
