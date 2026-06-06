# ui/input_learning.py

import html
import streamlit as st
from ui.navigation import render_bottom_navigation

from data.report_terms import (
    REPORT_LANG_KO,
    REPORT_LANG_EN,
    LANGUAGE_OPTIONS,
    normalize_report_language,
    translate_term,
    translate_rows,
    get_report_headers,
)

def get_input_learning_report_language() -> str:
    """
    가상 검사결과표 출력 언어를 선택합니다.

    기본값:
    - 한글 신용어 모드

    선택값:
    - 실제 검사결과표 영문 모드
    """
    if REPORT_LANG_KO in LANGUAGE_OPTIONS:
        default_index = LANGUAGE_OPTIONS.index(REPORT_LANG_KO)
    else:
        default_index = 0

    selected_language = st.radio(
        "검사결과표 출력 모드",
        options=LANGUAGE_OPTIONS,
        index=default_index,
        horizontal=True,
        key="input_learning_report_language_selector",
        help=(
            "가상 검사결과표는 기본적으로 한글 신용어 모드로 표시됩니다. "
            "실제 임상 근전도 검사결과표에 가까운 형태가 필요하면 영문 모드를 선택하세요."
        ),
    )

    return normalize_report_language(selected_language)


def get_section_title(section_key: str, language: str) -> str:
    """
    검사결과표 섹션 제목을 언어 모드에 맞게 반환합니다.
    """
    language = normalize_report_language(language)

    section_title_map = {
        REPORT_LANG_KO: {
            "sensory": "⚡ 감각신경전도검사",
            "motor": "⚡ 운동신경전도검사",
            "emg": "🪡 침근전도검사",
        },
        REPORT_LANG_EN: {
            "sensory": "⚡ Sensory NCS",
            "motor": "⚡ Motor NCS",
            "emg": "🪡 Needle EMG",
        },
    }

    return section_title_map.get(language, section_title_map[REPORT_LANG_KO]).get(
        section_key,
        section_key,
    )


def get_table_headers(section_key: str, language: str) -> list:
    """
    검사결과표 헤더를 언어 모드에 맞게 반환합니다.
    """
    language = normalize_report_language(language)

    if section_key == "sensory":
        headers = get_report_headers("sensory", language)
        if headers:
            return headers

        if language == REPORT_LANG_EN:
            return ["Nerve", "Amplitude", "Latency", "Interpretation"]

        return ["검사 신경", "진폭 수치", "잠복기 수치", "판단"]

    if section_key == "motor":
        headers = get_report_headers("motor", language)
        if headers:
            return headers

        if language == REPORT_LANG_EN:
            return ["Nerve", "Stimulation site", "Amplitude", "Latency", "Interpretation"]

        return ["검사 신경", "자극 위치", "진폭 수치", "잠복기 수치", "판단"]

    if section_key == "emg":
        headers = get_report_headers("emg", language)
        if headers:
            return headers

        if language == REPORT_LANG_EN:
            return ["Muscle", "Root", "Rest", "Volition", "Interpretation"]

        return ["검사 근육", "해당 분절", "휴식 시 반응", "수의수축 시 반응", "판단"]

    return []


def convert_rows_for_language(rows: list, language: str) -> list:
    """
    검사결과표 행 데이터를 선택 언어에 맞게 변환합니다.

    주의:
    - 원본 VIRTUAL_REPORTS 데이터는 수정하지 않습니다.
    - 출력 직전에만 변환합니다.
    """
    language = normalize_report_language(language)

    if not rows:
        return []

    if language == REPORT_LANG_KO:
        return rows

    return translate_rows(rows, language)


def convert_text_for_language(text: str, language: str) -> str:
    """
    단일 텍스트를 선택 언어에 맞게 변환합니다.

    주로 검사표 내부의 짧은 용어 변환에 사용합니다.
    긴 교육용 해석 문장은 한글 학습 효과를 위해 원문을 유지합니다.
    """
    language = normalize_report_language(language)

    if language == REPORT_LANG_KO:
        return str(text)

    return translate_term(text, language)


def is_emg_applicable_case(selected_case_name: str) -> bool:
    """
    선택된 가상 결과표에서 침근전도검사 표를 표시할지 판단합니다.

    현재 업로드 데이터 기준:
    - 눈꺼풀/눈깜빡반사 중심 사례는 침근전도검사 핵심 사례가 아님
    - 뇌졸중 H-반사 사례도 침근전도검사 핵심 사례가 아님
    """
    excluded_keywords = [
        "눈꺼풀",
        "눈깜빡",
        "눈깜박",
        "뇌졸중",
        "H-반사",
        "H-reflex",
    ]

    for keyword in excluded_keywords:
        if keyword in selected_case_name:
            return False

    return True


def create_responsive_table(headers, rows, table_id):
    """
    모바일 대응형 HTML 표를 생성합니다.
    """
    css = f"""
    <style>
        #{table_id} {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 16px;
            font-size: 0.86rem;
        }}

        #{table_id} th {{
            background-color: #f1f5f9;
            padding: 10px;
            border-bottom: 2px solid #cbd5e1;
            text-align: center;
            color: #1e293b;
            font-weight: 700;
        }}

        #{table_id} td {{
            padding: 10px;
            border-bottom: 1px solid #e2e8f0;
            text-align: center;
            color: #334155;
            line-height: 1.5;
            font-weight: 400;
        }}

        #{table_id} td.left-align {{
            text-align: left;
            font-weight: 600;
            color: #1e3a8a;
        }}

        @media screen and (max-width: 768px) {{
            #{table_id} thead {{
                display: none;
            }}

            #{table_id} tr {{
                display: block;
                border: 1px solid #e2e8f0;
                border-radius: 8px;
                margin-bottom: 12px;
                background: #ffffff;
                padding: 6px;
            }}

            #{table_id} td {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                gap: 12px;
                border-bottom: 1px solid #f1f5f9;
                padding: 8px 10px;
                text-align: right;
            }}

            #{table_id} td:last-child {{
                border-bottom: none;
            }}

            #{table_id} td::before {{
                content: attr(data-label);
                font-weight: 600;
                color: #475569;
                text-align: left;
                font-size: 0.8rem;
                flex: 0 0 38%;
            }}

            #{table_id} td > span {{
                flex: 1;
                text-align: right;
                word-break: keep-all;
                font-weight: 400;
            }}

            #{table_id} td.left-align {{
                justify-content: center;
                background: #f8fafc;
                border-radius: 6px 6px 0 0;
                text-align: center;
                padding: 10px;
            }}

            #{table_id} td.left-align::before {{
                content: none;
            }}

            #{table_id} td.left-align > span {{
                text-align: center;
                font-weight: 600;
            }}
        }}
    </style>
    """

    tr_html = ""

    for row in rows:
        td_html = ""

        for idx, col in enumerate(row):
            col = str(col)
            cls = "left-align" if idx == 0 else ""
            color_style = ""

            if idx == len(row) - 1:
                if "정상" in col and "비정상" not in col:
                    color_style = "color: #15803d; font-weight: 600;"
                elif any(
                    abnormal_word in col
                    for abnormal_word in [
                        "비정상",
                        "침범",
                        "확진",
                        "마비",
                        "소실",
                        "감소",
                        "지연",
                        "전도차단",
                        "Conduction block",
                        "Absent",
                        "Reduced",
                        "Delayed",
                        "Abnormal",
                        "Gilliatt-Sumner",
                    ]
                ):
                    color_style = "color: #991b1b; font-weight: 600;"

            if idx < len(headers):
                header_label = headers[idx]
            else:
                header_label = ""

            formatted_col = col.replace(" / ", "<br/>")

            td_html += (
                f"<td data-label='{header_label}' class='{cls}' style='{color_style}'>"
                f"<span>{formatted_col}</span>"
                f"</td>"
            )

        tr_html += f"<tr>{td_html}</tr>"

    header_html = "".join([f"<th>{header}</th>" for header in headers])

    return (
        f"{css}"
        f"<table id='{table_id}'>"
        f"<thead><tr>{header_html}</tr></thead>"
        f"<tbody>{tr_html}</tbody>"
        f"</table>"
    )


def render_patient_info(selected_case_name: str, data: dict) -> None:
    """
    선택된 가상 결과표의 환자 정보를 출력합니다.
    """
    info = data.get("info", {})

    age = info.get("age", "")
    sex = info.get("sex", "")
    side = info.get("side", "")
    symptom = info.get("symptom", "")

    st.markdown('<div class="info-card">', unsafe_allow_html=True)

    st.markdown(
        f'<div class="case-title-mobile">👤 환자 사례: {selected_case_name}</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        (
            '<div class="case-subtitle-mobile">'
            f'<span class="label-strong">연령/성별:</span> '
            f'<span class="result-value">{age}세 / {sex}</span>'
            '&nbsp;|&nbsp;'
            f'<span class="label-strong">병변측:</span> '
            f'<span class="result-value">{side}</span>'
            '</div>'
        ),
        unsafe_allow_html=True,
    )

    st.markdown(
        (
            '<div class="case-text-block" style="margin-top:10px;">'
            '<span class="label-strong">주요 임상 증상:</span> '
            f'<span class="result-value">{symptom}</span>'
            '</div>'
        ),
        unsafe_allow_html=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)


def render_virtual_report_tables(data: dict, selected_case_name: str, language: str) -> None:
    """
    선택된 가상 검사결과표의 NCS/EMG 표를 출력합니다.
    """
    language = normalize_report_language(language)
    info = data.get("info", {})
    side = info.get("side", "")

    ncs_sensory_rows = convert_rows_for_language(data.get("ncs_sensory", []), language)
    ncs_motor_rows = convert_rows_for_language(data.get("ncs_motor", []), language)
    emg_rows = convert_rows_for_language(data.get("emg", []), language)

    sensory_headers = get_table_headers("sensory", language)
    motor_headers = get_table_headers("motor", language)
    emg_headers = get_table_headers("emg", language)

    sensory_title = get_section_title("sensory", language)
    motor_title = get_section_title("motor", language)
    emg_title = get_section_title("emg", language)

    if language == REPORT_LANG_EN:
        report_label = "EMG Report Result Table"
        side_label = "Involved side"
    else:
        report_label = "근전도 결과표"
        side_label = "병변측"

    st.markdown('<div class="section-card">', unsafe_allow_html=True)

    st.markdown(
        (
            f'<div class="case-section-label">📋 {report_label} '
            f'(NCS & Needle EMG): {side_label} ({side})</div>'
        ),
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="finding-highlight">{sensory_title}</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        create_responsive_table(
            sensory_headers,
            ncs_sensory_rows,
            "sensory_tbl",
        ),
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="finding-highlight">{motor_title}</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        create_responsive_table(
            motor_headers,
            ncs_motor_rows,
            "motor_tbl",
        ),
        unsafe_allow_html=True,
    )

    if is_emg_applicable_case(selected_case_name):
        st.markdown(
            f'<div class="finding-highlight">{emg_title}</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            create_responsive_table(
                emg_headers,
                emg_rows,
                "emg_tbl",
            ),
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)


def render_interpretation_result(data: dict, selected_case_name: str) -> None:
    """
    선택된 가상 검사결과표의 임상 추론 및 생리학적 해석을 출력합니다.

    설명 영역은 교육 목적이므로 한글 중심으로 유지합니다.
    """
    diagnosis = data.get("diagnosis", "")
    interpretation = data.get("interpretation", [])
    emg_meaning = data.get("emg_meaning", [])
    ddx = data.get("ddx", "")

    st.markdown('<div class="result-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="result-title">✅ 임상 추론 및 생리학적 해석 결과</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        (
            '<div class="case-text-block" '
            'style="background:#fff1f2!important; border-left-color:#fecdd3!important;">'
            '<span class="label-strong text-red">최종 교육용 진단:</span> '
            f'<span class="result-value text-red" style="font-weight:700!important;">{diagnosis}</span>'
            '</div>'
        ),
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="result-label">🧠 데이터 해석 논리</div>',
        unsafe_allow_html=True,
    )

    for item in interpretation:
        st.markdown(
            f'<div class="finding-subtext">• {item}</div>',
            unsafe_allow_html=True,
        )

    if is_emg_applicable_case(selected_case_name):
        st.markdown(
            (
                '<div class="result-label" '
                'style="border-left-color:#d97706!important; background:#fffbeb!important;">'
                '🔬 침근전도 소견 생리학적 의미'
                '</div>'
            ),
            unsafe_allow_html=True,
        )

        for meaning in emg_meaning:
            parts = meaning.split(":", 1)

            if len(parts) == 2:
                st.markdown(
                    (
                        '<div class="finding-subtext">'
                        f'<span class="label-strong text-blue">{parts[0]}:</span>'
                        f'<span class="result-value">{parts[1]}</span>'
                        '</div>'
                    ),
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f'<div class="finding-subtext">• {meaning}</div>',
                    unsafe_allow_html=True,
                )

    st.markdown(
        (
            '<div class="result-label" '
            'style="border-left-color:#9333ea!important; background:#fdf4ff!important;">'
            '🧭 감별 진단 및 추가 검사'
            '</div>'
        ),
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="finding-subtext">• {ddx}</div>',
        unsafe_allow_html=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)


def render_reset_button() -> None:
    """
    다른 결과 분석 버튼을 출력합니다.
    """
    st.markdown(
        '<div style="text-align: center; margin-top: 20px; margin-bottom: 20px;">',
        unsafe_allow_html=True,
    )

    if st.button(
        "🔄 다른 결과 분석",
        type="secondary",
        key="reset_input_report_btn",
    ):
        st.session_state["input_reset_counter"] += 1
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


def render_input_learning():
    """
    가상 검사결과표 판독학습 화면을 렌더링합니다.

    이 화면은 근전도 해석 및 보조 진단 앱의 두 번째 축인
    '가상 검사결과표 해석 모드'에 해당합니다.
    """
    st.markdown(
        '<div class="main-title">가상 결과표 판독학습</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        (
            '<div class="subtle">'
            '임상 수치 데이터 기반의 가상 결과지를 통해 전기생리학적 해석 논리를 훈련합니다.'
            '</div>'
        ),
        unsafe_allow_html=True,
    )

    if "input_reset_counter" not in st.session_state:
        st.session_state["input_reset_counter"] = 0

    st.markdown('<div class="section-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="case-section-label">🌐 검사결과표 표시 방식 선택</div>',
        unsafe_allow_html=True,
    )

    selected_language = get_input_learning_report_language()

    if selected_language == REPORT_LANG_EN:
        st.caption(
            "현재 검사결과표는 실제 임상 EMG report에 가까운 영문 모드로 표시됩니다. "
            "해석 설명은 학습 목적상 한글 중심으로 유지됩니다."
        )
    else:
        st.caption(
            "현재 검사결과표는 한글 신용어 기본 모드로 표시됩니다."
        )

    st.markdown("</div>", unsafe_allow_html=True)

    dynamic_radio_key = f"input_report_selector_{st.session_state['input_reset_counter']}"

    st.markdown('<div class="section-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="case-section-label">📋 학습할 가상 결과지 선택 (실시간 판독형)</div>',
        unsafe_allow_html=True,
    )

    case_names = ["선택 안 함"] + list(VIRTUAL_REPORTS.keys())

    selected = st.radio(
        "가상 결과지 리스트",
        case_names,
        key=dynamic_radio_key,
        label_visibility="collapsed",
    )

    st.markdown("</div>", unsafe_allow_html=True)

    if selected != "선택 안 함":
        data = VIRTUAL_REPORTS[selected]

        render_patient_info(
            selected_case_name=selected,
            data=data,
        )

        render_virtual_report_tables(
            data=data,
            selected_case_name=selected,
            language=selected_language,
        )

        render_interpretation_result(
            data=data,
            selected_case_name=selected,
        )

        render_reset_button()

    render_bottom_navigation()


def app():
    """
    외부 라우터에서 app() 형태로 호출할 수 있도록 제공하는 진입점입니다.
    """
    render_input_learning()


if __name__ == "__main__":
    render_input_learning()
