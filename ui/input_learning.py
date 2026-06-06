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
)

from data.virtual_reports import (
    VIRTUAL_REPORTS,
    get_section_title,
    get_table_headers,
    convert_rows_for_language,
)


def get_input_learning_report_language() -> str:
    """
    가상 검사결과표 출력 언어를 선택합니다.

    기본값:
    - 한글 신용어 모드

    선택값:
    - 실제 검사결과표 영문 모드
    """
    selected_language = st.radio(
        "검사결과표 출력 모드",
        options=LANGUAGE_OPTIONS,
        index=0,
        horizontal=True,
        key="input_learning_report_language_selector",
        help=(
            "가상 검사결과표는 기본적으로 한글 신용어 모드로 표시됩니다. "
            "실제 임상 근전도 검사결과표에 가까운 형태가 필요하면 영문 모드를 선택하세요."
        ),
    )

    return normalize_report_language(selected_language)


def is_emg_applicable_case(selected_case_name: str) -> bool:
    """
    선택된 가상 결과표에서 침근전도검사 표를 표시할지 판단합니다.
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


def get_result_color_style(value: str) -> str:
    """
    표의 마지막 판정 칸 색상 스타일을 반환합니다.
    """
    text = str(value)

    abnormal_words = [
        "비정상",
        "침범",
        "확진",
        "마비",
        "소실",
        "감소",
        "지연",
        "전도차단",
        "Abnormal",
        "Reduced",
        "Delayed",
        "Absent",
        "No response",
        "Conduction block",
        "conduction block",
        "Gilliatt-Sumner",
    ]

    normal_words = [
        "정상",
        "Within normal limits",
        "Normal",
    ]

    if any(word in text for word in abnormal_words):
        return "color: #991b1b; font-weight: 600;"

    if any(word in text for word in normal_words):
        return "color: #15803d; font-weight: 600;"

    return ""


def create_responsive_table(headers: list, rows: list, table_id: str) -> str:
    """
    모바일 대응형 HTML 표를 생성합니다.
    """
    safe_table_id = html.escape(str(table_id), quote=True)

    css = f"""
    <style>
        #{safe_table_id} {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 16px;
            font-size: 0.86rem;
        }}

        #{safe_table_id} th {{
            background-color: #f1f5f9;
            padding: 10px;
            border-bottom: 2px solid #cbd5e1;
            text-align: center;
            color: #1e293b;
            font-weight: 700;
        }}

        #{safe_table_id} td {{
            padding: 10px;
            border-bottom: 1px solid #e2e8f0;
            text-align: center;
            color: #334155;
            line-height: 1.5;
            font-weight: 400;
        }}

        #{safe_table_id} td.left-align {{
            text-align: left;
            font-weight: 600;
            color: #1e3a8a;
        }}

        @media screen and (max-width: 768px) {{
            #{safe_table_id} thead {{
                display: none;
            }}

            #{safe_table_id} tr {{
                display: block;
                border: 1px solid #e2e8f0;
                border-radius: 8px;
                margin-bottom: 12px;
                background: #ffffff;
                padding: 6px;
            }}

            #{safe_table_id} td {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                gap: 12px;
                border-bottom: 1px solid #f1f5f9;
                padding: 8px 10px;
                text-align: right;
            }}

            #{safe_table_id} td:last-child {{
                border-bottom: none;
            }}

            #{safe_table_id} td::before {{
                content: attr(data-label);
                font-weight: 600;
                color: #475569;
                text-align: left;
                font-size: 0.8rem;
                flex: 0 0 38%;
            }}

            #{safe_table_id} td > span {{
                flex: 1;
                text-align: right;
                word-break: keep-all;
                font-weight: 400;
            }}

            #{safe_table_id} td.left-align {{
                justify-content: center;
                background: #f8fafc;
                border-radius: 6px 6px 0 0;
                text-align: center;
                padding: 10px;
            }}

            #{safe_table_id} td.left-align::before {{
                content: none;
            }}

            #{safe_table_id} td.left-align > span {{
                text-align: center;
                font-weight: 600;
            }}
        }}
    </style>
    """

    header_html = ""

    for header in headers:
        safe_header = html.escape(str(header), quote=True)
        header_html += f"<th>{safe_header}</th>"

    tr_html = ""

    for row in rows:
        td_html = ""

        for idx, col in enumerate(row):
            raw_col = str(col)
            escaped_col = html.escape(raw_col, quote=True)
            formatted_col = escaped_col.replace(" / ", "<br/>")

            if idx < len(headers):
                header_label = html.escape(str(headers[idx]), quote=True)
            else:
                header_label = ""

            cls = "left-align" if idx == 0 else ""
            color_style = ""

            if idx == len(row) - 1:
                color_style = get_result_color_style(raw_col)

            td_html += (
                f"<td data-label='{header_label}' class='{cls}' style='{color_style}'>"
                f"<span>{formatted_col}</span>"
                f"</td>"
            )

        tr_html += f"<tr>{td_html}</tr>"

    return (
        f"{css}"
        f"<table id='{safe_table_id}'>"
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

    st.markdown(
        '<div class="info-card">',
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="case-title-mobile">👤 환자 사례: {html.escape(str(selected_case_name))}</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        (
            '<div class="case-subtitle-mobile">'
            '<span class="label-strong">연령/성별:</span> '
            f'<span class="result-value">{html.escape(str(age))}세 / {html.escape(str(sex))}</span>'
            '&nbsp;|&nbsp;'
            '<span class="label-strong">병변측:</span> '
            f'<span class="result-value">{html.escape(str(side))}</span>'
            '</div>'
        ),
        unsafe_allow_html=True,
    )

    st.markdown(
        (
            '<div class="case-text-block" style="margin-top:10px;">'
            '<span class="label-strong">주요 임상 증상:</span> '
            f'<span class="result-value">{html.escape(str(symptom))}</span>'
            '</div>'
        ),
        unsafe_allow_html=True,
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True,
    )


def render_virtual_report_tables(
    data: dict,
    selected_case_name: str,
    language: str,
) -> None:
    """
    선택된 가상 검사결과표의 NCS/EMG 표를 출력합니다.
    """
    language = normalize_report_language(language)

    info = data.get("info", {})
    side = info.get("side", "")

    sensory_rows = convert_rows_for_language(
        rows=data.get("ncs_sensory", []),
        language=language,
    )

    motor_rows = convert_rows_for_language(
        rows=data.get("ncs_motor", []),
        language=language,
    )

    emg_rows = convert_rows_for_language(
        rows=data.get("emg", []),
        language=language,
    )

    sensory_headers = get_table_headers("sensory", language)
    motor_headers = get_table_headers("motor", language)
    emg_headers = get_table_headers("emg", language)

    sensory_title = get_section_title("sensory", language)
    motor_title = get_section_title("motor", language)
    emg_title = get_section_title("emg", language)

    if language == REPORT_LANG_EN:
        report_label = "EMG Report Result Table"
        side_label = "Involved side"
        side_value = translate_term(side, language)
    else:
        report_label = "근전도 검사결과표"
        side_label = "병변측"
        side_value = side

    st.markdown(
        '<div class="section-card">',
        unsafe_allow_html=True,
    )

    st.markdown(
        (
            f'<div class="case-section-label">📋 {html.escape(str(report_label))} '
            f'(NCS & Needle EMG): {html.escape(str(side_label))} '
            f'({html.escape(str(side_value))})</div>'
        ),
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="finding-highlight">{html.escape(str(sensory_title))}</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        create_responsive_table(
            headers=sensory_headers,
            rows=sensory_rows,
            table_id="sensory_tbl",
        ),
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="finding-highlight">{html.escape(str(motor_title))}</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        create_responsive_table(
            headers=motor_headers,
            rows=motor_rows,
            table_id="motor_tbl",
        ),
        unsafe_allow_html=True,
    )

    if is_emg_applicable_case(selected_case_name):
        st.markdown(
            f'<div class="finding-highlight">{html.escape(str(emg_title))}</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            create_responsive_table(
                headers=emg_headers,
                rows=emg_rows,
                table_id="emg_tbl",
            ),
            unsafe_allow_html=True,
        )

    st.markdown(
        "</div>",
        unsafe_allow_html=True,
    )


def render_interpretation_result(
    data: dict,
    selected_case_name: str,
) -> None:
    """
    선택된 가상 검사결과표의 임상 추론 및 생리학적 해석을 출력합니다.
    """
    diagnosis = data.get("diagnosis", "")
    interpretation = data.get("interpretation", [])
    emg_meaning = data.get("emg_meaning", [])
    ddx = data.get("ddx", "")

    st.markdown(
        '<div class="result-card">',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="result-title">✅ 임상 추론 및 생리학적 해석 결과</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        (
            '<div class="case-text-block" '
            'style="background:#fff1f2!important; border-left-color:#fecdd3!important;">'
            '<span class="label-strong text-red">최종 교육용 진단:</span> '
            f'<span class="result-value text-red" style="font-weight:700!important;">'
            f'{html.escape(str(diagnosis))}'
            '</span>'
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
            f'<div class="finding-subtext">• {html.escape(str(item))}</div>',
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
            meaning_text = str(meaning)
            parts = meaning_text.split(":", 1)

            if len(parts) == 2:
                title = html.escape(parts[0])
                body = html.escape(parts[1])

                st.markdown(
                    (
                        '<div class="finding-subtext">'
                        f'<span class="label-strong text-blue">{title}:</span>'
                        f'<span class="result-value">{body}</span>'
                        '</div>'
                    ),
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f'<div class="finding-subtext">• {html.escape(meaning_text)}</div>',
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
        f'<div class="finding-subtext">• {html.escape(str(ddx))}</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True,
    )


def render_reset_button() -> None:
    """
    다른 결과 분석 버튼을 출력합니다.
    """
    st.markdown(
        '<div style="text-align: center; margin-top: 20px; margin-bottom: 20px;">',
        unsafe_allow_html=True,
    )

    if st.button(
        "🔄 다른 검사결과표 보기",
        type="secondary",
        key="reset_input_report_btn",
    ):
        st.session_state["input_reset_counter"] += 1
        st.rerun()

    st.markdown(
        "</div>",
        unsafe_allow_html=True,
    )


def render_input_learning():
    """
    가상 검사결과표 해석 모드를 렌더링합니다.
    """
    st.markdown(
        '<div class="main-title">가상 검사결과표 해석</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        (
            '<div class="subtle">'
            '임상 수치 데이터 기반의 가상 검사결과표를 통해 '
            '신경전도검사와 침근전도검사의 전기생리학적 해석 논리를 훈련합니다.'
            '</div>'
        ),
        unsafe_allow_html=True,
    )

    if "input_reset_counter" not in st.session_state:
        st.session_state["input_reset_counter"] = 0

    st.markdown(
        '<div class="section-card">',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="case-section-label">🌐 검사결과표 표시 방식 선택</div>',
        unsafe_allow_html=True,
    )

    selected_language = get_input_learning_report_language()

    if selected_language == REPORT_LANG_EN:
        st.caption(
            "현재 검사결과표는 실제 임상 EMG report에 가까운 영문 모드로 표시됩니다. "
            "임상 추론 및 해석 설명은 학습 목적상 한글 중심으로 유지됩니다."
        )
    else:
        st.caption(
            "현재 검사결과표는 한글 신용어 기본 모드로 표시됩니다."
        )

    st.markdown(
        "</div>",
        unsafe_allow_html=True,
    )

    dynamic_radio_key = f"input_report_selector_{st.session_state['input_reset_counter']}"

    st.markdown(
        '<div class="section-card">',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="case-section-label">📋 학습할 가상 검사결과표 선택</div>',
        unsafe_allow_html=True,
    )

    case_names = ["선택 안 함"] + list(VIRTUAL_REPORTS.keys())

    selected = st.radio(
        "가상 검사결과표 리스트",
        case_names,
        key=dynamic_radio_key,
        label_visibility="collapsed",
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True,
    )

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
