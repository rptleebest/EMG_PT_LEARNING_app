# ui/input_learning.py

import html
import re
import streamlit as st
from ui.navigation import render_bottom_navigation
from data.report_terms import REPORT_LANG_KO, REPORT_LANG_EN, LANGUAGE_OPTIONS, normalize_report_language
from data.virtual_reports import VIRTUAL_REPORTS, get_report_section_name

def get_input_learning_report_language() -> str:
    selected = st.radio("언어 모드", options=LANGUAGE_OPTIONS, index=0, horizontal=True, label_visibility="collapsed", key="v_lang")
    return normalize_report_language(selected)

def get_result_color_style(value: str, is_normal_side: bool = False) -> str:
    if is_normal_side:
        return ""
        
    text = str(value)
    if any(x in text for x in ["정상측", "병변측", "Normal (", "Affected ("]): 
        return ""

    abnormal_words = [
        "비정상", "감소", "지연", "소실", "탈신경", "측정불가", "차단", "항진", "초과", "증가", "저하", "급감", 
        "Abnormal", "Reduced", "Absent", "Delayed", "Incomplete", "Active", "drop", "block", "Slowed", "Hyper",
        "Fibrillation", "PSW", "섬유자발전위", "양성예파", "거대운동단위", "Giant"
    ]
    
    # 비정상 수치/용어는 붉은색으로 표기하되 글자 두께는 일반 두께 유지
    if any(w in text for w in abnormal_words): 
        return "color: #b91c1c;"
    
    # 정상 소견(녹색) 강조 제거 -> 아무 속성도 반환하지 않아 기본 검은색/회색 텍스트로 표시
    return ""

def _format_reason_text(text: str) -> str:
    text = str(text).strip()
    if re.match(r"^(\d+\))", text) or text.endswith(":"):
        return f'<div style="color:#1e40af; font-weight:700; margin-top:14px; margin-bottom:6px;">{html.escape(text)}</div>'
    return f'<div style="color:#334155; margin-bottom:8px; line-height:1.6; padding-left:14px; text-indent:-14px;">• {html.escape(text)}</div>'

def custom_korean_translate(text: str) -> str:
    raw = str(text)
    code_str = raw.lower().strip()
    
    code_mapping = {
        "ncs_normal": "정상 범위", "ncs_delayed": "잠복기 지연", "ncs_reduced": "진폭 감소", 
        "ncs_absent": "반응 소실", "ncs_conduction_block": "진폭 급감",
        "emg_normal": "정상 범위", "emg_active_denervation": "활동성 탈신경", 
        "emg_paraspinal_denervation": "활동성 탈신경", "emg_chronic_reinnervation": "만성 재신경지배", 
        "emg_active_chronic": "활동성+만성", "blink_delayed": "잠복기 지연", 
        "emg_absent": "통증으로 평가 불가",
        "blink_absent": "반응 소실", "blink_delayed_absent": "지연 및 소실",
        "fwave_delayed_absent": "지연 및 소실", "h_reflex_hyperactive": "진폭 과항진",
        "h_m_ratio_increased": "비율 증가"
    }
    if code_str in code_mapping: return code_mapping[code_str]

    replace_map = {
        "Silent": "전기적 침묵", "Normal recruitment": "정상 운동단위동원", "Reduced recruitment": "운동단위동원 감소",
        "No recruitment": "운동단위동원 불가", "Fibrillation/PSW": "섬유자발전위/양성예파",
        "Absent": "반응 소실", "Incomplete due to pain": "통증으로 평가 불가", "Giant MUAPs": "거대운동단위"
    }
    for eng, kor in replace_map.items():
        if eng in raw: raw = raw.replace(eng, kor)
    return raw

def custom_english_translate(text: str) -> str:
    raw = str(text)
    mapping = {
        "정상 범위": "Within Normal Limits", 
        "비정상 (활동성 탈신경)": "Abnormal (Active denervation)",
        "통증으로 평가 불가": "Incomplete due to pain", 
        "비정상 (진폭 감소 / 잠복기 지연)": "Abnormal (Reduced Amp. & Delayed Lat.)",
        "비정상 (손목 지연 지속)": "Abnormal (Persistent wrist delay)",
        "비정상 (전도속도 저하)": "Abnormal (Slowed NCV)", 
        "비정상 (진폭 급감 / 국소 전도차단 의심)": "Abnormal (Conduction block)",
        "비정상 (진폭 감소)": "Abnormal (Reduced amp)", 
        "비정상 (반응 소실)": "Abnormal (Absent)",
        "비정상 (동원 감소)": "Abnormal (Reduced recruitment)", 
        "비정상 (동원 불가)": "Abnormal (No recruitment)",
        " (감소)": " (Reduced)", " (지연)": " (Delayed)", " (저하)": " (Slowed)", " (급감)": " (Drop)", 
        " (소실)": " (Absent)", " (항진)": " (Hyper)", " (초과)": " (Increased)", 
        "정상측(Rt)": "Normal (Rt)", "정상측(Lt)": "Normal (Lt)",
        "병변측(Rt)": "Affected (Rt)", "병변측(Lt)": "Affected (Lt)",
        "정상측": "Normal", "병변측": "Affected",
        "오른쪽": "Rt", "왼쪽": "Lt", "양측": "Bilateral",
        "팔꿈치 아래": "Below elbow", "팔꿈치 위": "Above elbow", "나선고랑 위": "Above spiral groove", "종아리뼈머리 아래": "Below Fib. head",
        "종아리뼈머리": "Fibular head", "무릎 위": "Above knee", "고샅부위": "Groin", "손목": "Wrist", "팔꿈치": "Elbow",
        "아래팔": "Forearm", "위팔": "Arm", "발목": "Ankle", "오금": "Popliteal", "겨드랑이": "Axilla", "귀앞": "Preauricular",
        "정중신경 첫째 가지": "Median (digit1)", "정중신경 둘째 가지": "Median (digit2)", "정중신경 셋째 가지": "Median (digit3)",
        "자신경 다섯째 가지": "Ulnar (digit5)", "등쪽자신경": "Dorsal Ulnar Cutaneous", "가쪽아래팔피부신경": "Lat. Antebrachial Cutaneous",
        "안쪽아래팔피부신경": "Med. Antebrachial Cutaneous", "얕은종아리신경": "Superficial Peroneal", "얼굴신경(코근)": "Facial (Nasalis)",
        "얼굴신경(눈둘레근)": "Facial (Orbicularis Oculi)", "근육피부신경": "Musculocutaneous", "정중신경": "Median",
        "자신경": "Ulnar", "노신경": "Radial", "종아리신경": "Peroneal", "장딴지신경": "Sural", "정강신경": "Tibial",
        "두렁신경": "Saphenous", "넓적다리신경": "Femoral", "삼차신경": "Trigeminal", "얼굴신경": "Facial",
        "깊은손가락굽힘근 4-다섯째 가지": "FDP (digit 4-5)", "넓적다리두갈래근 짧은갈래": "Biceps Femoris (Short)",
        "목 척추주위근": "Cervical Paraspinal", "허리 척추주위근": "Lumbar Paraspinal", "긴노쪽손목폄근": "ECRL",
        "넓적다리근막긴장근": "Tensor Fasciae Latae", "넓적다리네갈래근": "Quadriceps Femoris", "위팔두갈래근": "Biceps Brachii",
        "위팔세갈래근": "Triceps Brachii", "노쪽손목굽힘근": "Flexor Carpi Radialis", "자쪽손목굽힘근": "Flexor Carpi Ulnaris",
        "첫째등쪽뼈사이근": "First Dorsal Interosseous", "짧은엄지벌림근": "Abductor Pollicis Brevis", "짧은발가락폄근": "Extensor Digitorum Brevis",
        "안쪽장딴지근": "Medial Gastrocnemius", "어깨세모근": "Deltoid", "위팔노근": "Brachioradialis", "원엎침근": "Pronator Teres",
        "손가락폄근": "Extensor Digitorum Communis", "고유집게폄근": "Extensor Indicis Proprius", "깊은손가락굽힘근": "Flexor Digitorum Profundus",
        "새끼벌림근": "Abductor Digiti Minimi", "엉덩허리근": "Iliopsoas", "가쪽넓은근": "Vastus Lateralis", "앞정강근": "Tibialis Anterior",
        "긴종아리근": "Peroneus Longus", "가자미근": "Soleus", "큰볼기근": "Gluteus Maximus", "눈둘레근": "Orbicularis Oculi",
        "입둘레근": "Orbicularis Oris", "이마근": "Frontalis", "깨물근": "Masseter", "무반응": "Absent", "측정불가": "N/A",
        " (우)": " (Rt)", " (좌)": " (Lt)", " (Rt)": " (Rt)", " (Lt)": " (Lt)"
    }
    for k in sorted(mapping.keys(), key=len, reverse=True):
        if k in raw: raw = raw.replace(k, mapping[k])
    return raw

def create_responsive_table(headers: list, rows: list) -> str:
    if not rows: return ""
    css = """<style>
    /* PC 환경 기본 스타일 */
    .clinical-table { width: 100%; border-collapse: collapse; margin-bottom: 20px; font-size: 0.95rem; }
    .clinical-table th { background-color: #f8fafc; padding: 12px 10px; border-bottom: 2px solid #cbd5e1; text-align: center !important; color: #1e293b; font-weight: 800; white-space: nowrap; }
    .clinical-table th:first-child, .clinical-table th:last-child { text-align: left !important; padding-left: 16px; }
    
    /* 일반 데이터 셀: 두께 일반(400) 고정 */
    .clinical-table td { padding: 10px 12px; border-bottom: 1px solid #e2e8f0; text-align: center !important; color: #334155; vertical-align: middle; font-weight: 400; }
    .clinical-table td.fst-col { font-weight: 800; color: #1e3a8a; text-align: left !important; padding-left: 16px; }
    /* 마지막 판독 결과만 볼드 처리 */
    .clinical-table td:last-child { text-align: left !important; padding-left: 16px; font-weight: 700; line-height: 1.4;}

    /* 모바일 환경 */
    @media screen and (max-width: 768px) {
        .clinical-table, .clinical-table thead, .clinical-table tbody, .clinical-table th, .clinical-table td, .clinical-table tr { display: block; }
        .clinical-table thead { display: none; }
        .clinical-table tr { margin-bottom: 16px; border: 1px solid #cbd5e1; border-radius: 10px; background: #ffffff; box-shadow: 0 4px 6px rgba(0,0,0,0.05); overflow: hidden; }
        .clinical-table td { display: flex; justify-content: space-between; align-items: center; padding: 12px 16px; border-bottom: 1px dashed #e2e8f0; text-align: right !important; }
        .clinical-table td::before { content: attr(data-label); font-weight: 700; color: #64748b; font-size: 0.85rem; text-align: left !important; flex: 0 0 40%; }
        
        /* 모바일 데이터 스팬 두께 일반(400) 고정 */
        .clinical-table td > span { flex: 1; word-break: keep-all; font-weight: 400; color: #334155;}
        
        .clinical-table td:first-child { background: #eff6ff; padding: 14px 16px; border-bottom: 2px solid #bfdbfe; justify-content: flex-start; }
        .clinical-table td:first-child::before { display: none; }
        .clinical-table td:first-child > span { text-align: left !important; font-weight: 800; color: #1d4ed8; font-size: 1.05rem; }
        .clinical-table td:first-child > span::before { content: "🔹 "; }
        .clinical-table td:last-child { flex-direction: column; align-items: flex-start; background-color: #f8fafc; border-bottom: none; padding-top: 14px; padding-bottom: 14px; }
        .clinical-table td:last-child::before { margin-bottom: 6px; color: #1e3a8a; font-size: 0.95rem; content: "📝 " attr(data-label); width: 100%; }
        .clinical-table td:last-child > span { text-align: left !important; width: 100%; font-size: 0.95rem; font-weight: 700;}
    }
    </style>"""
    
    header_html = "".join([f"<th>{html.escape(h)}</th>" for h in headers])
    tr_html = ""
    for row in rows:
        is_normal_side = any("정상측" in str(c) or "Normal (" in str(c) for c in row)
        td_html = ""
        for idx, col in enumerate(row):
            cls = "fst-col" if idx == 0 else ""
            color_style = get_result_color_style(str(col), is_normal_side) if idx > 0 else ""
            h_lbl = html.escape(headers[idx]) if idx < len(headers) else ""
            td_html += f"<td data-label='{h_lbl}' class='{cls}' style='{color_style}'><span>{html.escape(str(col))}</span></td>"
        tr_html += f"<tr>{td_html}</tr>"
    return f"{css}<table class='clinical-table'><thead><tr>{header_html}</tr></thead><tbody>{tr_html}</tbody></table>"

def render_input_learning():
    st.markdown('<div class="main-title">가상 검사결과표 해석 모드</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-desc">실제 임상과 동일한 비교 데이터를 통해 병변 위치를 스스로 추론합니다.</div>', unsafe_allow_html=True)
    st.markdown('<hr style="border-top: 1px dotted #cbd5e1; margin-bottom: 20px;">', unsafe_allow_html=True)

    if "v_reset_counter" not in st.session_state: st.session_state["v_reset_counter"] = 0
    case_names = ["선택 안 함"] + list(VIRTUAL_REPORTS.keys())
    
    st.markdown('<div class="sub-title">📋 학습할 가상 검사결과표 선택</div>', unsafe_allow_html=True)
    selected = st.radio("리스트", case_names, index=0, key=f"v_rad_{st.session_state['v_reset_counter']}", label_visibility="collapsed")

    if selected != "선택 안 함":
        render_virtual_report_inline(selected)

    render_bottom_navigation()

def render_virtual_report_inline(case_name: str):
    data = VIRTUAL_REPORTS[case_name]

    st.markdown('<hr style="border-top: 2px solid #94a3b8; margin: 2rem 0;">', unsafe_allow_html=True)
    
    info = data.get("info", {})
    st.markdown('<div class="section-label">👤 환자 기본 정보</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="info-row"><div class="info-label">연령/성별</div><div class="info-value">{info.get("age")}세 / {info.get("sex")}</div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="info-row"><div class="info-label">병변 호소측</div><div class="info-value">{info.get("side")}</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="info-row" style="border:none;"><div class="info-label">주요 증상</div><div class="info-value"></div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="left-border-box">• {info.get("symptom")}</div>', unsafe_allow_html=True)
    
    st.markdown('<hr style="border-top: 1px dashed #cbd5e1; margin: 1.5rem 0;">', unsafe_allow_html=True)

    st.markdown('<div style="font-weight:800; color:#0f172a; margin-bottom:12px; font-size:1.05rem;">⚙️ 검사결과표 언어 모드 변경</div>', unsafe_allow_html=True)
    selected_language = get_input_learning_report_language()
    
    lang = normalize_report_language(selected_language)
    is_eng = lang == REPORT_LANG_EN

    sen_hdrs = ["Nerve", "Side", "Amplitude", "Latency", "Interpretation"] if is_eng else ["검사 신경", "측정측", "진폭", "잠복기", "판독"]
    mot_hdrs = ["Nerve", "Stim Site", "Side", "Amplitude", "Latency", "NCV", "Interpretation"] if is_eng else ["검사 신경", "자극 위치", "측정측", "진폭", "잠복기", "전도속도(NCV)", "판독"]
    emg_hdrs = ["Muscle", "Segment", "Rest", "Volition", "Interpretation"] if is_eng else ["검사 근육", "분절", "휴식 시", "수의수축 시", "판독"]
    spec_hdrs = ["Test", "Condition", "Result", "Interpretation"] if is_eng else ["검사 항목", "조건/측정측", "결과", "상세 수치 및 판독"]

    def _tr(mat): 
        if is_eng: return [[custom_english_translate(str(c)) for c in row] for row in mat]
        else: return [[custom_korean_translate(str(c)) for c in row] for row in mat]

    teaching = data.get("teaching_diagnosis", {})

    if data.get("ncs_sensory") or data.get("ncs_motor"):
        st.markdown("""
        <div style="background:#fef3c7; padding:14px; margin-top:24px; margin-bottom:16px; border-radius:6px; border-left:5px solid #f59e0b;">
            <div style="font-size:0.95rem; font-weight:800; color:#b45309; margin-bottom:6px;">💡 [임상 실무 팁] 양측 검사와 편측 검사</div>
            <div style="font-size:0.9rem; color:#451a03; line-height:1.6;">
                근전도 검사는 환자의 통증과 검사 시간을 줄이기 위해 기본적으로 <b>병변 호소측</b>만 선별하여 검사합니다. 
                단, 손목굴증후군 등과 같이 국소 포착 병변이 의심되거나 병변측 결과가 뚜렷하게 비정상일 경우, 환자 본인의 정상적인 고유 수치와 비교하기 위해 <b>신경전도검사의 경우에서만 반대쪽(정상측) 신경을 대조군으로 함께 검사</b>합니다.
            </div>
        </div>
        """, unsafe_allow_html=True)

    if data.get("ncs_sensory"):
        st.markdown(f'<div class="section-label" style="margin-top:16px;">⚡ {get_report_section_name("sensory", lang)}</div>', unsafe_allow_html=True)
        st.markdown(create_responsive_table(sen_hdrs, _tr(data.get("ncs_sensory", []))), unsafe_allow_html=True)

    if data.get("ncs_motor"):
        st.markdown(f'<div class="section-label" style="margin-top:32px;">⚡ {get_report_section_name("motor", lang)}</div>', unsafe_allow_html=True)
        st.markdown(create_responsive_table(mot_hdrs, _tr(data.get("ncs_motor", []))), unsafe_allow_html=True)

    if (data.get("ncs_sensory") or data.get("ncs_motor")) and "ncs_reason" in teaching:
        with st.expander("🔍 신경전도검사 결과 해석"):
            st.markdown("""
            <div style="background:#f1f5f9; padding:12px; margin-bottom:12px; border-radius:4px; border-left:4px solid #cbd5e1;">
                <div style="font-size:0.95rem; font-weight:800; color:#1e3a8a; margin-bottom:6px;">💡 [참고] 신경전도속도(NCV) 임상 정상 기준치</div>
                <div style="font-size:0.9rem; margin-bottom:4px; color:#334155;">• <b>상지(팔) 신경:</b> 일반적으로 <b>50 m/s 이상</b> 정상</div>
                <div style="font-size:0.9rem; margin-bottom:4px; color:#334155;">• <b>하지(다리) 신경:</b> 일반적으로 <b>40 m/s 이상</b> 정상</div>
                <div style="font-size:0.85rem; color:#64748b; margin-top:4px;">* 속도가 기준치 미만으로 저하된 경우, 말이집(Myelin) 손상성 지연이나 국소 포착(Entrapment)을 의심할 수 있습니다.</div>
            </div>
            """, unsafe_allow_html=True)
            for r in teaching["ncs_reason"]:
                st.markdown(_format_reason_text(r), unsafe_allow_html=True)

    if data.get("special"):
        spec_title = "Special & Late Responses" if is_eng else "특수 및 후기반응 검사"
        st.markdown(f'<div class="section-label" style="margin-top:32px;">⚡ {spec_title}</div>', unsafe_allow_html=True)
        st.markdown(create_responsive_table(spec_hdrs, _tr(data.get("special", []))), unsafe_allow_html=True)
        if "emg_reason" in teaching and not data.get("emg"):
            with st.expander("🔍 특수 검사 소견 해석"):
                for r in teaching["emg_reason"]: 
                    st.markdown(_format_reason_text(r), unsafe_allow_html=True)

    if data.get("emg"):
        st.markdown(f'<div class="section-label" style="margin-top:32px;">🪡 {get_report_section_name("emg", lang)}</div>', unsafe_allow_html=True)
        st.markdown(create_responsive_table(emg_hdrs, _tr(data.get("emg", []))), unsafe_allow_html=True)
        if "emg_reason" in teaching:
            with st.expander("🔍 침근전도검사 결과 해석"):
                st.markdown("""
                <div style="background:#f1f5f9; padding:12px; margin-bottom:12px; border-radius:4px; border-left:4px solid #cbd5e1;">
                    <div style="font-size:0.95rem; margin-bottom:6px;"><span style="color:#1e3a8a; font-weight:800;">• 활동성 탈신경 (Active Denervation):</span> 현재 신경 손상이 활발히 진행 중인 상태 (자발전위 관찰)</div>
                    <div style="font-size:0.95rem; margin-bottom:6px;"><span style="color:#1e3a8a; font-weight:800;">• 만성 재신경지배 (Chronic Reinnervation):</span> 신경 손상 후 회복을 시도하는 만성기 (거대운동단위 관찰)</div>
                    <div style="font-size:0.95rem;"><span style="color:#1e3a8a; font-weight:800;">• 수의수축 시 동원 감소 또는 소실 (Reduced Recruitment or Absent):</span> 신경 손상으로 인해 부분 탈신경으로 근력 저하 또는 완전 탈신경으로 완전 마비된 상태</div>
                    <div style="font-size:0.95rem;"><span style="color:#1e3a8a; font-weight:800;">• 휴식 시 관찰되는 비정상적인 자발전위 (Rest):</span> 섬유자발전위(fibrillation), 양성예파(positive sharp wave, PSW)</div>
                    <div style="font-size:0.95rem;"><span style="color:#1e3a8a; font-weight:800;">• 휴식 시 정상적인 반응 (Rest):</span> 전기적 침묵(Silent)</div>                    
                </div>
                """, unsafe_allow_html=True)
                for r in teaching["emg_reason"]: 
                    st.markdown(_format_reason_text(r), unsafe_allow_html=True)

    st.markdown('<hr style="border-top: 2px dashed #cbd5e1; margin: 2.5rem 0 1.5rem 0;">', unsafe_allow_html=True)
    
    is_stroke_case = "뇌졸중" in case_name

    section_title = "✅ 임상적 통합 해석" if is_stroke_case else "✅ 임상적 통합 해석 및 감별진단"
    st.markdown(f'<div class="section-label">{section_title}</div>', unsafe_allow_html=True)
    
    if "integration" in teaching:
        st.markdown('<div class="sub-title">🔹 검사 결과 통합 결론</div>', unsafe_allow_html=True)
        st.markdown('<div class="left-border-box" style="border-left-color:#3b82f6;">', unsafe_allow_html=True)
        for r in teaching["integration"]: 
            st.markdown(f'<div style="margin-bottom:8px;">• {r}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
            
    box_label = "경직(spasticity) 평가 : " if is_stroke_case else "임상적 추정진단 (R/O) : "
    st.markdown(
        f'<div style="background:#fdf2f8; border:1px solid #fbcfe8; padding:12px 16px; border-radius:8px; margin-top:16px;">'
        f'<span style="font-size:1.05rem; color:#9d174d; font-weight:700;">{box_label}</span>'
        f'<span style="font-size:1.05rem; color:#9d174d; font-weight:800;">{teaching.get("summary")}</span>'
        f'</div>', unsafe_allow_html=True
    )

    if "differential_diagnosis" in data and not is_stroke_case:
        st.markdown('<div class="sub-title" style="margin-top:24px;">🧭 유사 질환과의 감별진단</div>', unsafe_allow_html=True)
        for ddx in data["differential_diagnosis"]:
            name = ddx.get('name', '')
            why = ddx.get('why_consider', '')
            how = ddx.get('how_to_differentiate', '')
            tip = ddx.get('practical_tip', '')
            
            ddx_html = f"<div style='font-size:1.05rem; font-weight:800; color:#4f46e5; margin-bottom:12px;'>{name}</div>"
            if why: ddx_html += f"<div style='color:#475569; line-height:1.6; margin-bottom:8px;'><span style='font-weight:700; color:#334155;'>🤔 고려 이유: </span>{why}</div>"
            if how: ddx_html += f"<div style='color:#475569; line-height:1.6; margin-bottom:8px;'><span style='font-weight:700; color:#334155;'>🔎 감별 포인트: </span>{how}</div>"
            if tip: ddx_html += f"<div style='color:#ea580c; line-height:1.6; margin-top:12px; font-weight:600; background:#fff7ed; padding:8px 12px; border-radius:6px; border-left:3px solid #ea580c;'>💡 임상 꿀팁: {tip}</div>"
            
            st.markdown(f"""
            <div class="ddx-box" style="background:#f8fafc; border:1px solid #e2e8f0; padding:16px; border-radius:8px; margin-bottom:16px; border-left: 4px solid #4f46e5; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">
                {ddx_html}
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div style="height: 32px;"></div>', unsafe_allow_html=True)
    if st.button("👆 다른 검사결과표 선택하기", type="primary"):
        st.session_state["v_reset_counter"] += 1
        st.rerun()

def app(): pass
