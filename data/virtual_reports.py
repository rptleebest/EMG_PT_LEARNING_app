# data/virtual_reports.py

"""
가상근전도검사표와 실제 근전도 검사표를 함께 출력하기 위한 데이터 및 변환 도구.

핵심 기능:
- 기본 모드는 한글 신용어 가상근전도검사표
- 선택 모드는 실제 검사표 영문 출력
- 표 출력 시 누락 없이 동일한 구조 유지
- 기존 사례 데이터를 건드리지 않고 출력 문자열만 변환
"""

from data.report_terms import (
    REPORT_LANG_KO,
    REPORT_LANG_EN,
    LANGUAGE_OPTIONS,
    normalize_report_language,
    translate_term,
    translate_row,
    translate_rows,
    get_report_headers,
)

# ------------------------------------------------------------
# 공용 표시 문자열
# ------------------------------------------------------------
REPORT_TITLE_KO = "가상근전도검사표"
REPORT_TITLE_EN = "Virtual EMG Report"

REPORT_SUBTITLE_KO = "한글 신용어 기본 모드"
REPORT_SUBTITLE_EN = "English mode for actual EMG report"

REPORT_MODE_DEFAULT = REPORT_LANG_KO
REPORT_MODE_ENGLISH = REPORT_LANG_EN


# ------------------------------------------------------------
# 검사표 구조 템플릿
# ------------------------------------------------------------
REPORT_SECTIONS = ["sensory", "motor", "emg"]


# ------------------------------------------------------------
# 가상 검사표 샘플 데이터
# - UI에서 사례별로 불러와 출력할 때 쓰는 표 구조 예시
# - 실제 값은 data.cases.CASE_LIBRARY를 기반으로 조합될 수 있음
# ------------------------------------------------------------
VIRTUAL_REPORT_TEMPLATE = {
    "sensory": [
        ["정중신경", "정상 범위", "정상", "정상"],
        ["자신경", "정상 범위", "정상", "정상"],
        ["노신경", "정상 범위", "정상", "정상"],
    ],
    "motor": [
        ["정중신경", "손목", "정상", "정상", "정상"],
        ["자신경", "팔꿈치", "정상", "정상", "정상"],
        ["노신경", "팔꿈치", "정상", "정상", "정상"],
        ["정강신경", "발목", "정상", "정상", "정상"],
        ["종아리신경", "종아리뼈머리", "정상", "정상", "정상"],
    ],
    "emg": [
        ["짧은엄지벌림근", "손목굴", "정상", "정상", "정상"],
        ["첫째등쪽뼈사이근", "자경부위", "정상", "정상", "정상"],
        ["앞정강근", "허리 4-5", "정상", "정상", "정상"],
        ["긴엄지폄근", "허리 5", "정상", "정상", "정상"],
    ],
}


# ------------------------------------------------------------
# 한글/영문 제목 및 섹션 헤더
# ------------------------------------------------------------
def get_report_title(language: str) -> str:
    language = normalize_report_language(language)
    if language == REPORT_LANG_EN:
        return REPORT_TITLE_EN
    return REPORT_TITLE_KO


def get_report_subtitle(language: str) -> str:
    language = normalize_report_language(language)
    if language == REPORT_LANG_EN:
        return REPORT_SUBTITLE_EN
    return REPORT_SUBTITLE_KO


def get_report_section_name(section: str, language: str) -> str:
    language = normalize_report_language(language)
    mapping = {
        REPORT_LANG_KO: {
            "sensory": "감각신경전도검사",
            "motor": "운동신경전도검사",
            "emg": "침근전도검사",
        },
        REPORT_LANG_EN: {
            "sensory": "Sensory NCS",
            "motor": "Motor NCS",
            "emg": "Needle EMG",
        },
    }
    return mapping.get(language, mapping[REPORT_LANG_KO]).get(section, section)


# ------------------------------------------------------------
# 표 데이터 변환
# ------------------------------------------------------------
def convert_report_template(language: str) -> dict:
    """
    VIRTUAL_REPORT_TEMPLATE를 선택 언어로 변환합니다.

    반환값 구조:
    {
        "sensory": [[...], [...]],
        "motor": [[...], [...]],
        "emg": [[...], [...]]
    }
    """
    language = normalize_report_language(language)

    converted = {}
    for section in REPORT_SECTIONS:
        rows = VIRTUAL_REPORT_TEMPLATE.get(section, [])
        converted[section] = translate_rows(rows, language)
    return converted


def get_report_table(section: str, language: str) -> list:
    """섹션별 표를 선택 언어로 반환합니다."""
    language = normalize_report_language(language)
    rows = VIRTUAL_REPORT_TEMPLATE.get(section, [])
    return translate_rows(rows, language)


def get_report_table_with_headers(section: str, language: str) -> dict:
    """
    섹션별 헤더와 행을 함께 반환합니다.

    반환형:
    {
        "headers": [...],
        "rows": [...]
    }
    """
    language = normalize_report_language(language)
    return {
        "headers": get_report_headers(section, language),
        "rows": get_report_table(section, language),
    }


def get_full_virtual_report(language: str) -> dict:
    """
    전체 가상근전도검사표를 선택 언어로 반환합니다.
    """
    language = normalize_report_language(language)
    return {
        "title": get_report_title(language),
        "subtitle": get_report_subtitle(language),
        "sections": {
            section: get_report_table_with_headers(section, language)
            for section in REPORT_SECTIONS
        },
    }


# ------------------------------------------------------------
# 실제 판독 예시용 문자열 생성
# ------------------------------------------------------------
def render_rows_as_text(rows: list) -> str:
    """
    표 행을 사람이 읽을 수 있는 텍스트로 이어붙입니다.
    UI에서 별도 표 렌더링이 없을 때 보조용으로 사용합니다.
    """
    lines = []
    for row in rows:
        lines.append(" | ".join([str(item) for item in row]))
    return "\n".join(lines)


def render_section_as_text(section: str, language: str) -> str:
    """
    섹션 1개를 텍스트 블록으로 반환합니다.
    """
    language = normalize_report_language(language)
    section_name = get_report_section_name(section, language)
    headers = get_report_headers(section, language)
    rows = get_report_table(section, language)

    text = [f"[{section_name}]"]
    if headers:
        text.append(" | ".join(headers))
    if rows:
        text.append(render_rows_as_text(rows))
    return "\n".join(text)


def render_full_report_as_text(language: str) -> str:
    """
    전체 가상근전도검사표를 텍스트로 렌더링합니다.
    """
    language = normalize_report_language(language)

    blocks = [
        get_report_title(language),
        get_report_subtitle(language),
    ]

    for section in REPORT_SECTIONS:
        blocks.append(render_section_as_text(section, language))

    return "\n\n".join(blocks)


# ------------------------------------------------------------
# 유틸리티
# ------------------------------------------------------------
def is_report_korean(language: str) -> bool:
    return normalize_report_language(language) == REPORT_LANG_KO


def is_report_english(language: str) -> bool:
    return normalize_report_language(language) == REPORT_LANG_EN


def get_available_languages() -> list:
    return list(LANGUAGE_OPTIONS)
