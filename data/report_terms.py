# data/virtual_reports.py

"""
가상 검사결과표 해석 모드에서 사용하는 데이터와 변환 유틸리티.

역할:
- VIRTUAL_REPORTS 사례 데이터 보관
- 한글 신용어 모드 / 실제 검사결과표 영문 모드 전환
- 검사표 헤더, 섹션명, 행 변환 제공
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


REPORT_TITLE_KO = "가상 검사결과표"
REPORT_TITLE_EN = "Virtual EMG Report"

REPORT_SUBTITLE_KO = "한글 신용어 기본 모드"
REPORT_SUBTITLE_EN = "English mode for actual EMG report"

REPORT_SECTIONS = [
    "sensory",
    "motor",
    "emg",
]


VIRTUAL_REPORTS = {
    "왼쪽 목/어깨 통증 및 팔 저림 (C6 신경뿌리병증 의심)": {
        "info": {
            "age": 45,
            "sex": "남성",
            "symptom": "왼쪽 목 통증 및 무감각, 엄지/검지 손가락 끝 저림, 팔꿉관절 굽힘력 감소",
            "side": "왼쪽",
        },
        "diagnosis": "왼쪽 C6 목 신경뿌리병증",
        "ncs_sensory": [
            ["정중신경 (Median SNAP)", "25 μV", "2.8 ms", "정상 범위"],
            ["자신경 (Ulnar SNAP)", "22 μV", "2.5 ms", "정상 범위"],
        ],
        "ncs_motor": [
            ["정중신경 (Median CMAP)", "손목 자극", "8.5 mV", "3.5 ms", "정상 범위"],
            ["정중신경 (Median CMAP)", "팔꿈치 자극", "8.1 mV", "7.8 ms", "정상 범위"],
        ],
        "emg": [
            [
                "위팔두갈래근 (Biceps brachii)",
                "C5-C6",
                "fibrillation potential, positive sharp wave",
                "Reduced MU recruitment",
                "비정상 (활동성 탈신경)",
            ],
            [
                "긴노쪽손목폄근 (ECRL)",
                "C6-C7",
                "fibrillation potential, positive sharp wave",
                "Giant MUAPs 출현 및 Reduced MU recruitment",
                "비정상 (만성 재신경지배 동반)",
            ],
            [
                "짧은엄지벌림근 (APB)",
                "C8-T1",
                "Silent at rest",
                "Normal MU recruitment",
                "정상 범위",
            ],
            [
                "목 척추주위근 (Cervical paraspinal)",
                "C6",
                "fibrillation potential, positive sharp wave",
                "통증으로 인해 평가불가",
                "비정상 (활동성 탈신경)",
            ],
        ],
        "interpretation": [
            "감각신경활동전위가 정상 범위로 보존되어 병변이 뒤뿌리신경절보다 몸쪽의 신경뿌리 수준에 있음을 시사합니다.",
            "C6 분절 지배 근육과 목 척추주위근에서 활동성 탈신경 소견이 관찰되어 C6 목 신경뿌리병증에 합당합니다.",
        ],
        "emg_meaning": [
            "fibrillation potential, positive sharp wave: 탈신경된 근섬유막의 전기적 불안정성을 의미합니다.",
            "Reduced MU recruitment: 수의수축 시 동원 가능한 운동단위 수가 감소한 상태입니다.",
        ],
        "ddx": "목 디스크 또는 추간공 협착 여부를 확인하기 위해 목 MRI와 임상 진찰 소견을 함께 비교해야 합니다.",
    },

    "오른쪽 1~3번째 손가락 저림 및 야간통 (손목굴증후군 의심)": {
        "info": {
            "age": 52,
            "sex": "여성",
            "symptom": "오른쪽 1, 2, 3번째 손가락 저림, 야간 통증 및 손목 굽힘 시 증상 악화",
            "side": "오른쪽",
        },
        "diagnosis": "오른쪽 손목굴증후군",
        "ncs_sensory": [
            ["정중신경 (Median SNAP)", "8 μV", "4.8 ms", "진폭: 감소 / 잠복기: 지연"],
            ["자신경 (Ulnar SNAP)", "25 μV", "2.6 ms", "정상 범위"],
        ],
        "ncs_motor": [
            ["정중신경 (Median CMAP)", "손목", "3.1 mV", "5.5 ms", "진폭: 감소 / 잠복기: 지연"],
            ["정중신경 (Median CMAP)", "팔꿈치 자극", "2.9 mV", "9.8 ms", "진폭: 감소"],
        ],
        "emg": [
            ["짧은엄지벌림근 (APB)", "C8-T1", "Silent at rest", "Normal MU recruitment", "정상 범위"],
            ["첫째등쪽뼈사이근 (FDI)", "C8-T1", "Silent at rest", "Normal MU recruitment", "정상 범위"],
        ],
        "interpretation": [
            "정중신경 감각 및 운동 전도에서 잠복기 지연이 관찰되어 손목굴 부위 국소 압박성 말이집탈락 병변을 시사합니다.",
            "정중신경 진폭 감소가 동반되어 축삭 손상 가능성도 함께 고려해야 합니다.",
        ],
        "emg_meaning": [
            "Silent at rest: 휴식 시 비정상 자발전위가 관찰되지 않는 상태입니다.",
            "Normal MU recruitment: 수의수축 시 운동단위 동원이 정상적으로 이루어지는 상태입니다.",
        ],
        "ddx": "목 신경뿌리병증과 감별하기 위해 신경학적 진찰, 티넬 징후, 팔렌 검사 등을 함께 확인해야 합니다.",
    },

    "왼쪽 허리 통증 및 엄지발가락 올림 약화 (L5 신경뿌리병증 의심)": {
        "info": {
            "age": 58,
            "sex": "여성",
            "symptom": "왼쪽 허리통증, 종아리 가쪽 및 발등 통증, 발목 등굽힘 약화로 발끝 끌림",
            "side": "왼쪽",
        },
        "diagnosis": "왼쪽 L5 허리 신경뿌리병증",
        "ncs_sensory": [
            ["얕은종아리신경 (Superficial peroneal SNAP)", "12 μV", "2.9 ms", "정상 범위"],
            ["장딴지신경 (Sural SNAP)", "15 μV", "3.1 ms", "정상 범위"],
        ],
        "ncs_motor": [
            ["종아리신경 (Peroneal CMAP)", "발목", "3.5 mV", "4.5 ms", "정상 범위"],
            ["종아리신경 (Peroneal CMAP)", "오금", "3.3 mV", "11.2 ms", "정상 범위"],
        ],
        "emg": [
            ["앞정강근 (Tibialis anterior)", "L4-L5", "fibrillation potential, positive sharp wave", "Reduced MU recruitment", "비정상 (활동성 탈신경)"],
            ["긴종아리근 (Peroneus longus)", "L5-S1", "fibrillation potential, positive sharp wave", "Giant MUAPs 출현 및 Reduced MU recruitment", "비정상 (만성 재신경지배 동반)"],
            ["가자미근 (Soleus)", "S1-S2", "Silent at rest", "Normal MU recruitment", "정상 범위"],
            ["허리 척추주위근 (Lumbar paraspinal)", "L5", "fibrillation potential, positive sharp wave", "통증으로 인해 평가불가", "비정상 (활동성 탈신경)"],
        ],
        "interpretation": [
            "다리의 표재 감각신경활동전위가 보존되어 병변이 뒤뿌리신경절보다 몸쪽의 허리 신경뿌리 수준에 있음을 시사합니다.",
            "L5 지배 근육과 허리 척추주위근에서 탈신경 소견이 동반되어 L5 허리 신경뿌리병증에 합당합니다.",
        ],
        "emg_meaning": [
            "Giant MUAP: 과거 축삭 손상 후 재신경지배가 진행되었음을 시사하는 만성 신경성 변화입니다.",
        ],
        "ddx": "L4-L5 또는 L5-S1 추간판 병변 확인을 위해 허리엉치 MRI와 임상 증상 비교가 필요합니다.",
    },

    "오른쪽 발처짐 및 종아리 가쪽 감각 저하 (온종아리신경 마비 의심)": {
        "info": {
            "age": 32,
            "sex": "남성",
            "symptom": "오랫동안 다리를 꼬고 앉은 뒤 오른쪽 발목 등굽힘 불능 및 보행 시 발처짐",
            "side": "오른쪽",
        },
        "diagnosis": "오른쪽 온종아리신경 마비",
        "ncs_sensory": [
            ["얕은종아리신경 (Superficial peroneal SNAP)", "4 μV", "3.8 ms", "진폭: 감소 / 잠복기: 지연"],
            ["장딴지신경 (Sural SNAP)", "16 μV", "3.0 ms", "정상 범위"],
        ],
        "ncs_motor": [
            ["종아리신경 (Peroneal CMAP)", "발목", "4.5 mV", "4.8 ms", "정상 범위"],
            ["종아리신경 (Peroneal CMAP)", "종아리뼈머리 자극", "1.1 mV", "무반응", "진폭: 감소 (국소 전도차단)"],
        ],
        "emg": [
            ["앞정강근 (Tibialis anterior)", "L4-L5", "Silent at rest", "No MUAPs on volition", "비정상 (전도 완전 마비)"],
            ["긴종아리근 (Peroneus longus)", "L5-S1", "Silent at rest", "Reduced MU recruitment", "비정상 (동원 감소)"],
            ["허리 척추주위근 (Lumbar paraspinal)", "L5", "Silent at rest", "Normal MU recruitment", "정상 범위"],
        ],
        "interpretation": [
            "종아리뼈머리 부위 자극에서 복합근육활동전위 진폭 감소가 관찰되어 국소 전도차단을 시사합니다.",
            "허리 척추주위근이 정상으로 보존되어 L5 신경뿌리병증보다는 말초 온종아리신경 병변에 합당합니다.",
        ],
        "emg_meaning": [
            "Conduction block: 축삭이 완전히 소실되지 않았더라도 국소 압박으로 전기 자극 전달이 차단된 상태입니다.",
        ],
        "ddx": "보행 보조기, 압박 회피, 종아리뼈머리 부위 외부 압박 요인 제거가 중요합니다.",
    },

    "양측 발끝 저림 및 감각 저하 (당뇨병성 다발신경병증 의심)": {
        "info": {
            "age": 68,
            "sex": "남성",
            "symptom": "양 발바닥의 대칭적인 저림, 화끈거림, 무감각",
            "side": "양측",
        },
        "diagnosis": "길이의존성 축삭성 다발신경병증",
        "ncs_sensory": [
            ["장딴지신경 (Sural SNAP) 오른쪽", "무반응", "무반응", "반응 소실"],
            ["정중신경 (Median SNAP) 오른쪽", "18 μV", "3.4 ms", "정상 범위"],
        ],
        "ncs_motor": [
            ["정강신경 (Tibial CMAP) 오른쪽", "발목", "1.5 mV", "6.2 ms", "진폭: 감소 / 잠복기: 지연"],
            ["정강신경 (Tibial CMAP) 오른쪽", "오금", "1.2 mV", "15.2 ms", "진폭: 감소"],
        ],
        "emg": [
            ["앞정강근 (Tibialis anterior)", "L4-L5", "fibrillation potential, positive sharp wave", "Reduced MU recruitment", "비정상 (대칭적 말초 축삭 퇴행)"],
            ["위팔두갈래근 (Biceps brachii)", "C5-C6", "Silent at rest", "Normal MU recruitment", "정상 범위"],
        ],
        "interpretation": [
            "먼쪽 감각신경인 장딴지신경 반응 소실이 관찰되어 길이의존성 축삭 손상을 시사합니다.",
            "상지보다 하지의 먼쪽 신경에서 이상이 두드러져 당뇨병성 다발신경병증 양상에 합당합니다.",
        ],
        "emg_meaning": [
            "Dying-back pattern: 신경 세포체에서 먼 축삭 말단부터 퇴행하는 길이의존성 축삭 손상 양상입니다.",
        ],
        "ddx": "혈당 조절 상태, 당화혈색소, 비타민 결핍, 신장기능 등을 함께 평가해야 합니다.",
    },

    "왼쪽 갑작스러운 한쪽 얼굴 마비 (얼굴신경마비 의심)": {
        "info": {
            "age": 29,
            "sex": "남성",
            "symptom": "급격히 발현된 왼쪽 얼굴 전반 마비, 이마 주름 소실, 왼쪽 눈 감김 불능, 입꼬리 비대칭",
            "side": "왼쪽",
        },
        "diagnosis": "왼쪽 특발성 얼굴신경마비",
        "ncs_sensory": [
            ["오른쪽 이마 자극 (V1 분지)", "22 μV", "2.1 ms", "정상 범위"],
            ["왼쪽 이마 자극 (V1 분지)", "21 μV", "2.2 ms", "정상 범위"],
        ],
        "ncs_motor": [
            ["오른쪽 얼굴신경 (Facial CMAP)", "코근", "3.2 mV", "2.8 ms", "정상 범위"],
            ["왼쪽 얼굴신경 (Facial CMAP)", "코근", "1.1 mV", "4.5 ms", "진폭: 감소 / 잠복기: 지연"],
        ],
        "emg": [
            ["눈둘레근 (Orbicularis oculi)", "얼굴신경 지배", "Silent at rest", "Normal MU recruitment", "정상 범위"],
        ],
        "interpretation": [
            "왼쪽 얼굴신경 자극 시 복합근육활동전위 진폭이 정상측보다 크게 감소하여 말초 얼굴신경 운동 축삭 손상을 시사합니다.",
            "이마 주름 소실과 눈 감김 불능을 동반한 말초성 얼굴마비 양상으로 벨마비에 합당합니다.",
        ],
        "emg_meaning": [
            "급성기에는 침근전도에서 탈신경 자발전위가 아직 뚜렷하지 않을 수 있습니다.",
            "얼굴신경 복합근육활동전위는 좌우 진폭 비대칭을 통해 운동 축삭 손상 정도를 추정하는 데 도움이 됩니다.",
        ],
        "ddx": "중추성 얼굴마비는 이마 주름이 비교적 보존될 수 있으므로, 이마 움직임과 다른 신경학적 징후를 함께 확인해야 합니다.",
    },
}


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


def get_section_title(section: str, language: str) -> str:
    language = normalize_report_language(language)

    if language == REPORT_LANG_EN:
        mapping = {
            "sensory": "⚡ Sensory NCS",
            "motor": "⚡ Motor NCS",
            "emg": "🪡 Needle EMG",
        }
    else:
        mapping = {
            "sensory": "⚡ 감각신경전도검사",
            "motor": "⚡ 운동신경전도검사",
            "emg": "🪡 침근전도검사",
        }

    return mapping.get(section, section)


def get_table_headers(section: str, language: str) -> list:
    return get_report_headers(section, language)


def convert_rows_for_language(rows: list, language: str) -> list:
    language = normalize_report_language(language)

    if language == REPORT_LANG_KO:
        return rows

    return translate_rows(rows, language)


def convert_text_for_language(text: str, language: str) -> str:
    language = normalize_report_language(language)

    if language == REPORT_LANG_KO:
        return str(text)

    return translate_term(text, language)


def get_available_languages() -> list:
    return list(LANGUAGE_OPTIONS)


def is_report_korean(language: str) -> bool:
    return normalize_report_language(language) == REPORT_LANG_KO


def is_report_english(language: str) -> bool:
    return normalize_report_language(language) == REPORT_LANG_EN
