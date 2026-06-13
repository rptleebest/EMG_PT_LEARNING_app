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

def get_result_color_style(value: str) -> str:
    text = str(value)
    abnormal_words = ["비정상", "감소", "지연", "소실", "탈신경", "측정불가", "차단", "항진", "초과", "증가", "저하", "급감", "Abnormal", "Reduced", "Absent", "Delayed", "Incomplete", "Active", "drop", "block", "Slowed", "Hyper"]
    normal_words = ["정상", "Normal", "Silent", "WNL", "침묵", "동원"]
    
    if any(w in text for w in abnormal_words): return "color: #991b1b; font-weight: 800;"
    if any(w in text for w in normal_words): return "color: #15803d; font-weight: 800;"
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
        "ncs_absent": "반응 소실", "ncs_conduction_block": "진폭 급감", "emg_normal": "정상 범위", 
        "emg_active_denervation": "활동성 탈신경", "emg_paraspinal_denervation": "활동성 탈신경", 
        "emg_chronic_reinnervation": "만성 재신경지배", "emg_active_chronic": "활동성+만성", 
        "blink_delayed": "잠복기 지연", "blink_absent": "반응 소실", "blink_delayed_absent": "지연 및 소실",
        "fwave_delayed_absent": "지연 및 소실", "h_reflex_hyperactive": "진폭 과항진", "h_m_ratio_increased": "비율 증가"
    }
    if code_str in code_mapping: return code_mapping[code_str]

    replace_map = {
        "Silent": "전기적 침묵", "Normal recruitment": "정상 동원", "Reduced recruitment": "동원 감소",
        "No recruitment": "동원 불가", "Fibrillation/PSW": "섬유자발전위/양성예파", "Absent": "반응 소실",
        "Incomplete due to pain": "통증으로 평가 불가", "Giant MUAPs": "거대운동단위"
    }
    for eng, kor in replace_map.items():
        if eng in raw: raw = raw.replace(eng, kor)
    return raw

def custom_english_translate(text: str) -> str:
    raw = str(text)
    mapping = {
        "정상 범위": "Within Normal Limits", "비정상 (활동성 탈신경)": "Abnormal (Active denervation)",
        "통증으로 평가 불가": "Incomplete due to pain", "비정상 (진폭 감소 / 잠복기 지연)": "Abnormal (Reduced Amp. & Delayed Lat.)",
        "비정상 (전도속도 저하)": "Abnormal (Slowed NCV)", "비정상 (진폭 급감 / 국소 전도차단 의심)": "Abnormal (Conduction block)",
        "비정상 (진폭 감소)": "Abnormal (Reduced amp)", "비정상 (반응 소실)": "Abnormal (Absent)",
        "비정상 (동원 감소)": "Abnormal (Reduced recruitment)", "비정상 (동원 불가)": "Abnormal (No recruitment)",
        " (감소)": " (Reduced)", " (지연)": " (Delayed)", " (저하)": " (Slowed)", " (급감)": " (Drop)", 
        " (소실)": " (Absent)", " (항진)": " (Hyper)", " (초과)": " (Increased)", "오른쪽": "Rt", "왼쪽": "Lt", "양측": "Bilateral",
        "팔꿈치 아래": "Below elbow", "팔꿈치 위": "Above elbow", "나선고랑 위": "Above spiral groove", "종아리뼈머리 아래": "Below Fib. head",
        "종아리뼈머리": "Fibular head", "무릎 위": "Above knee", "고샅부위": "Groin", "손목": "Wrist", "팔꿈치": "Elbow",
        "아래팔": "Forearm", "위팔": "Arm", "발목": "Ankle", "오금": "Popliteal", "겨드랑이": "Axilla", "귀앞": "Preauricular",
        "정중신경 첫째 가지": "Median (digit1)", "정중신경 둘째 가지": "Median (digit2)", "정중신경 셋째 가지": "Median (digit3)",
        "자신경 다섯째 가지": "Ulnar (digit5)", "등쪽자신경": "Dorsal Ulnar Cutaneous", "가쪽아래팔피부신경": "Lat. Antebrachial Cutaneous",
        "안쪽아래팔피부신경": "Med. Antebrachial Cutaneous", "얕은종아리신경": "Superficial Peroneal", "얼굴신경 코근": "Facial (Nasalis)",
        "얼굴신경 눈둘레근": "Facial (Orbicularis Oculi)", "근육피부신경": "Musculocutaneous", "정중신경": "Median",
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
        "입둘레근": "Orbicularis Oris", "이마근": "Frontalis", "깨물근": "Masseter", "무반응": "Absent", "측정불가": "N/A"
    }
    for k in sorted(mapping.keys(), key=len, reverse=True):
        if k in raw: raw = raw.replace(k, mapping[k])
    return raw

def create_standard_responsive_table(headers: list, rows: list) -> str:
    if not rows: return ""
    css = """<style>
    .st-table { width: 100%; border-collapse: collapse; margin-bottom: 12px; font-size: 0.92rem; }
    .st-table th { background-color: #f8fafc; padding: 10px 8px; border-bottom: 2px solid #cbd5e1; text-align: center !important; color: #1e293b; font-weight: 800; white-space: nowrap; }
    .st-table th:first-child { text-align: left !important; padding-left: 16px; }
    .st-table td { padding: 10px 8px; border-bottom: 1px solid #e2e8f0; text-align: center !important; color: #334155; }
    .st-table td.fst-col { font-weight: 800; color: #1e3a8a; text-align: left !important; padding-left: 16px; }
    @media screen and (max-width: 768px) {
        .st-table thead { display: none; }
        .st-table tr { display: block; border: 1px solid #cbd5e1; border-radius: 8px; margin-bottom: 16px; background: #ffffff; overflow: hidden; }
        .st-table td { display: flex; align-items: flex-start; gap: 12px; border-bottom: 1px dashed #e2e8f0; padding: 10px 12px 10px 24px; text-align: left !important; }
        .st-table td:last-child { border-bottom: none; }
        .st-table td::before { content: attr(data-label); font-weight: 800; color: #64748b; text-align: left !important; font-size: 0.85rem; flex: 0 0 38%; margin-top: 2px; }
        .st-table td > span { flex: 1; text-align: left !important; word-break: keep-all; font-weight: 400; color: #334155; line-height: 1.4; }
        .st-table td.fst-col { display: flex; flex-direction: row; justify-content: flex-start; background: #f1f5f9; padding: 12px 16px; border-bottom: 2px solid #cbd5e1; }
        .st-table td.fst-col::before { display: none; }
        .st-table td.fst-col > span { text-align: left !important; font-weight: 800; color: #1e3a8a; font-size: 0.95rem; }
        .st-table td.fst-col > span::before { content: "🔹 "; }
    }
    </style>"""
    header_html = "".join([f"<th>{html.escape(h)}</th>" for h in headers])
    tr_html = ""
    for row in rows:
        td_html = ""
        for idx, col in enumerate(row):
            cls = "fst-col" if idx == 0 else ""
            color_style = get_result_color_style(str(col)) if idx > 0 else ""
            h_lbl = html.escape(str(headers[idx])) if idx < len(headers) else ""
            td_html += f"<td data-label='{h_lbl}' class='{cls}' style='{color_style}'><span>{html.escape(str(col))}</span></td>"
        tr_html += f"<tr>{td_html}</tr>"
    return f"{css}<table class='st-table'><thead><tr>{header_html}</tr></thead><tbody>{tr_html}</tbody></table>"

# --- [핵심 추가] PC와 모바일을 완벽하게 분리하는 반응형 HTML 렌더러 ---
def generate_virtual_report_html(headers: list, rows: list, lesion_side: str, is_eng: bool) -> str:
    side_idx = headers.index("Side") if "Side" in headers else (headers.index("측정측") if "측정측" in headers else -1)
    interp_idx = headers.index("Interpretation") if "Interpretation" in headers else (headers.index("판독") if "판독" in headers else -1)

    # 측정측 컬럼이 없는 특수검사 등은 일반 테이블로 폴백(Fallback) 처리
    if side_idx == -1 or interp_idx == -1:
        return create_standard_responsive_table(headers, rows)

    base_headers = headers[:side_idx]
    val_headers = headers[side_idx+1:interp_idx]

    grouped = {}
    for row in rows:
        if len(row) <= interp_idx: continue
        base_key = tuple(row[:side_idx])
        side_val = str(row[side_idx]).strip()
        vals = row[side_idx+1:interp_idx]
        interp = row[interp_idx]

        if base_key not in grouped: grouped[base_key] = {"Rt": None, "Lt": None, "Bil": None}

        if side_val in ["오른쪽", "Rt", "우측"]: grouped[base_key]["Rt"] = {"vals": vals, "interp": interp}
        elif side_val in ["왼쪽", "Lt", "좌측"]: grouped[base_key]["Lt"] = {"vals": vals, "interp": interp}
        else: grouped[base_key]["Bil"] = {"vals": vals, "interp": interp}

    is_bilateral = "양측" in lesion_side or "Bilateral" in lesion_side
    if "오른쪽" in lesion_side or "Rt" in lesion_side:
        aff_key, nor_key = "Rt", "Lt"
        aff_label = "병변측(우)" if not is_eng else "Affected(Rt)"
        nor_label = "정상측(좌)" if not is_eng else "Normal(Lt)"
    elif "왼쪽" in lesion_side or "Lt" in lesion_side:
        aff_key, nor_key = "Lt", "Rt"
        aff_label = "병변측(좌)" if not is_eng else "Affected(Lt)"
        nor_label = "정상측(우)" if not is_eng else "Normal(Rt)"
    else:
        aff_key, nor_key = "Bil", None
        aff_label = "우측" if not is_eng else "Rt"
        nor_label = "좌측" if not is_eng else "Lt"

    html_str = "<div class='compare-table-container'>"

    # --- 1. PC용 테이블 (정상측 먼저, 병변측 나중) ---
    html_str += "<table class='pc-compare-table'>"
    html_str += "<thead><tr>"
    for bh in base_headers: html_str += f"<th rowspan='2'>{bh}</th>"
    
    if is_bilateral:
        html_str += f"<th colspan='{len(val_headers)}'>좌측 (Lt)</th><th colspan='{len(val_headers)}'>우측 (Rt)</th>"
    else:
        html_str += f"<th colspan='{len(val_headers)}'>{nor_label}</th><th colspan='{len(val_headers)}'>{aff_label}</th>"
        
    html_str += f"<th rowspan='2'>{'판독' if not is_eng else 'Interpretation'}</th></tr><tr>"
    for _ in range(2):
        for vh in val_headers: html_str += f"<th>{vh}</th>"
    html_str += "</tr></thead><tbody>"

    for base_key, data in grouped.items():
        if is_bilateral:
            nor_d = data["Lt"] if data["Lt"] else data["Bil"]
            aff_d = data["Rt"] if data["Rt"] else data["Bil"]
        else:
            nor_d = data[nor_key]
            aff_d = data[aff_key] if data[aff_key] else data["Bil"]

        html_str += "<tr>"
        for bk in base_key: html_str += f"<td class='base-col'>{bk}</td>"
        
        # 정상측 수치
        for i in range(len(val_headers)):
            v = nor_d["vals"][i] if nor_d and i < len(nor_d["vals"]) else "-"
            html_str += f"<td style='{get_result_color_style(v)}'>{v}</td>"
            
        # 병변측 수치
        for i in range(len(val_headers)):
            v = aff_d["vals"][i] if aff_d and i < len(aff_d["vals"]) else "-"
            html_str += f"<td style='{get_result_color_style(v)}'>{v}</td>"

        # 판독
        interp_val = aff_d["interp"] if aff_d else (nor_d["interp"] if nor_d else "-")
        html_str += f"<td style='{get_result_color_style(interp_val)}'>{interp_val}</td></tr>"
    html_str += "</tbody></table>"

    # --- 2. 모바일용 카드 UI (신경마다 파라미터별로 정상/병변 위아래 비교) ---
    html_str += "<div class='mobile-compare-cards'>"
    for base_key, data in grouped.items():
        if is_bilateral:
            nor_d = data["Lt"] if data["Lt"] else data["Bil"]
            aff_d = data["Rt"] if data["Rt"] else data["Bil"]
        else:
            nor_d = data[nor_key]
            aff_d = data[aff_key] if data[aff_key] else data["Bil"]

        title = " - ".join(base_key)
        html_str += f"<div class='m-card'><div class='m-card-title'>🔹 {title}</div>"

        # 파라미터별(진폭, 잠복기 등) 반복
        for i, vh in enumerate(val_headers):
            n_val = nor_d["vals"][i] if nor_d and i < len(nor_d["vals"]) else "-"
            a_val = aff_d["vals"][i] if aff_d and i < len(aff_d["vals"]) else "-"
            
            html_str += f"""
            <div class='m-card-row'>
                <div class='m-row-label'>📌 {vh}</div>
                <div class='m-row-vals'>
                    <div class='m-val-item'><span class='m-side-badge nor'>{nor_label}</span> <span style='{get_result_color_style(n_val)}'>{n_val}</span></div>
                    <div class='m-val-item'><span class='m-side-badge aff'>{aff_label}</span> <span style='{get_result_color_style(a_val)}'>{a_val}</span></div>
                </div>
            </div>
            """
        interp_val = aff_d["interp"] if aff_d else (nor_d["interp"] if nor_d else "-")
        html_str += f"""
        <div class='m-card-interp'>
            <span class='m-interp-label'>{'병변측 판독' if not is_eng else 'Interpretation'}</span>
            <span style='{get_result_color_style(interp_val)}'>{interp_val}</span>
        </div>
        </div>
        """
    html_str += "</div></div>"

    css = """<style>
    .compare-table-container { margin-bottom: 24px; }
    /* PC CSS */
    .pc-compare-table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
    .pc-compare-table th { background: #f8fafc; padding: 10px; border: 1px solid #cbd5e1; text-align: center; font-weight: 800; color: #1e293b; white-space: nowrap; }
    .pc-compare-table td { padding: 10px; border: 1px solid #e2e8f0; text-align: center; color: #334155; }
    .pc-compare-table .base-col { font-weight: 800; color: #1e3a8a; text-align: left; background: #f1f5f9; }
    .mobile-compare-cards { display: none; }
    
    /* 모바일 CSS */
    @media screen and (max-width: 768px) {
        .pc-compare-table { display: none; }
        .mobile-compare-cards { display: flex; flex-direction: column; gap: 16px; }
        .m-card { border: 1px solid #cbd5e1; border-radius: 8px; background: #fff; box-shadow: 0 2px 4px rgba(0,0,0,0.05); overflow:hidden;}
        .m-card-title { background: #eff6ff; padding: 12px 16px; font-weight: 800; color: #1d4ed8; font-size: 1.05rem; border-bottom: 2px solid #bfdbfe; }
        .m-card-row { padding: 12px 16px; border-bottom: 1px dashed #e2e8f0; }
        .m-row-label { font-weight: 800; color: #475569; margin-bottom: 8px; font-size: 0.95rem; }
        .m-row-vals { display: flex; flex-direction: column; gap: 8px; padding-left: 8px;}
        .m-val-item { display: flex; align-items: center; justify-content: flex-start; }
        .m-side-badge { padding: 2px 8px; border-radius: 4px; font-size: 0.85rem; font-weight: 700; min-width: 80px; text-align: center; margin-right: 12px; }
        .m-side-badge.nor { background: #f1f5f9; color: #475569; border: 1px solid #cbd5e1; }
        .m-side-badge.aff { background: #fef2f2; color: #991b1b; border: 1px solid #fecaca; }
        .m-card-interp { padding: 12px 16px; background: #f8fafc; display: flex; flex-direction: column; gap: 6px;}
        .m-interp-label { font-weight: 800; color: #1e293b; font-size: 0.95rem; }
    }
    </style>"""
    return css + html_str

def render_input_learning():
    st.markdown('<div class="main-title">가상 검사결과표 해석 모드</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-desc">실제 임상과 동일한 양측 비교 데이터를 통해 병변 위치를 스스로 추론합니다.</div>', unsafe_allow_html=True)
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
    lesion_side = info.get("side", "")

    sen_hdrs = ["Nerve", "Side", "Amplitude", "Latency", "Interpretation"] if is_eng else ["검사 신경", "측정측", "진폭", "잠복기", "판독"]
    mot_hdrs = ["Nerve", "Stim Site", "Side", "Amplitude", "Latency", "NCV", "Interpretation"] if is_eng else ["검사 신경", "자극 위치", "측정측", "진폭", "잠복기", "전도속도(NCV)", "판독"]
    emg_hdrs = ["Muscle", "Segment", "Side", "Rest", "Volition", "Interpretation"] if is_eng else ["검사 근육", "분절", "측정측", "휴식 시", "수의수축", "판독"]
    spec_hdrs = ["Test", "Condition", "Result", "Interpretation"] if is_eng else ["검사 항목", "조건/측정측", "결과", "상세 수치 및 판독"]

    def _tr(mat): 
        if is_eng: return [[custom_english_translate(str(c)) for c in row] for row in mat]
        else: return [[custom_korean_translate(str(c)) for c in row] for row in mat]

    teaching = data.get("teaching_diagnosis", {})

    # 여기서 에러 없이 안전하게 호출됩니다.
    if data.get("ncs_sensory"):
        st.markdown(f'<div class="section-label" style="margin-top:32px;">⚡ {get_report_section_name("sensory", lang)}</div>', unsafe_allow_html=True)
        st.markdown(generate_virtual_report_html(sen_hdrs, _tr(data.get("ncs_sensory", [])), lesion_side, is_eng), unsafe_allow_html=True)

    if data.get("ncs_motor"):
        st.markdown(f'<div class="section-label" style="margin-top:32px;">⚡ {get_report_section_name("motor", lang)}</div>', unsafe_allow_html=True)
        st.markdown(generate_virtual_report_html(mot_hdrs, _tr(data.get("ncs_motor", [])), lesion_side, is_eng), unsafe_allow_html=True)

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
        st.markdown(generate_virtual_report_html(spec_hdrs, _tr(data.get("special", [])), lesion_side, is_eng), unsafe_allow_html=True)
        if "emg_reason" in teaching and not data.get("emg"):
            with st.expander("🔍 특수 검사 소견 해석"):
                for r in teaching["emg_reason"]: 
                    st.markdown(_format_reason_text(r), unsafe_allow_html=True)

    if data.get("emg"):
        st.markdown(f'<div class="section-label" style="margin-top:32px;">🪡 {get_report_section_name("emg", lang)}</div>', unsafe_allow_html=True)
        st.markdown(generate_virtual_report_html(emg_hdrs, _tr(data.get("emg", [])), lesion_side, is_eng), unsafe_allow_html=True)
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
            if why:
                ddx_html += f"<div style='color:#475569; line-height:1.6; margin-bottom:8px;'><span style='font-weight:700; color:#334155;'>🤔 고려 이유: </span>{why}</div>"
            if how:
                ddx_html += f"<div style='color:#475569; line-height:1.6; margin-bottom:8px;'><span style='font-weight:700; color:#334155;'>🔎 감별 포인트: </span>{how}</div>"
            if tip:
                ddx_html += f"<div style='color:#ea580c; line-height:1.6; margin-top:12px; font-weight:600; background:#fff7ed; padding:8px 12px; border-radius:6px; border-left:3px solid #ea580c;'>💡 임상 꿀팁: {tip}</div>"
            
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
