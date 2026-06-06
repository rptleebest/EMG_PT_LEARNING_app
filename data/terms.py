# data/terms.py

"""
전기진단 교육 앱에서 공통으로 사용하는 표준 결과 상수와 표기 변환 함수.

설계 원칙:
- 내부 판독 로직에서는 짧고 안정적인 코드값을 사용합니다.
- 화면 출력에서는 한글 중심 + 필요한 영문 병기를 사용합니다.
- 기존 cases.py에서 사용 중인 legacy 상수 문자열도 함께 인식합니다.
"""

# ---------------------------------------------------------------------
# NCS 결과 상수
# ---------------------------------------------------------------------
NCS_NORMAL = "ncs_normal"
NCS_DELAYED = "ncs_delayed"
NCS_REDUCED = "ncs_reduced"
NCS_ABSENT = "ncs_absent"
NCS_CONDUCTION_BLOCK = "ncs_conduction_block"

# ---------------------------------------------------------------------
# EMG 결과 상수
# ---------------------------------------------------------------------
EMG_NORMAL = "emg_normal"
EMG_ACTIVE_DENERVATION = "emg_active_denervation"
EMG_PARASPINAL_DENERVATION = "emg_paraspinal_denervation"
EMG_CHRONIC_REINNERVATION = "emg_chronic_reinnervation"
EMG_ACTIVE_CHRONIC = "emg_active_chronic"
EMG_FASCICULATION = "emg_fasciculation"
EMG_NO_RESPONSE = "emg_no_response"

# ---------------------------------------------------------------------
# F-wave / H-reflex / Blink reflex 결과 상수
# ---------------------------------------------------------------------
FWAVE_DELAYED_ABSENT = "fwave_delayed_absent"
H_REFLEX_HYPERACTIVE = "h_reflex_hyperactive"
H_M_RATIO_INCREASED = "h_m_ratio_increased"
BLINK_DELAYED = "blink_delayed"
BLINK_DELAYED_ABSENT = "blink_delayed_absent"

# ---------------------------------------------------------------------
# 표준 출력 라벨
# ---------------------------------------------------------------------
NCS_LABELS = {
    NCS_NORMAL: "정상 범위",
    NCS_DELAYED: "잠복기 지연",
    NCS_REDUCED: "진폭 감소",
    NCS_ABSENT: "반응 소실",
    NCS_CONDUCTION_BLOCK: "전도차단",
}

EMG_LABELS = {
    EMG_NORMAL: "휴식 시 Silent at rest / 수의수축 시 Normal MU recruitment",
    EMG_ACTIVE_DENERVATION: "휴식 시 fibrillation potential, positive sharp wave / 수의수축 시 Reduced MU recruitment",
    EMG_PARASPINAL_DENERVATION: "휴식 시 fibrillation potential, positive sharp wave / 수의수축 시 통증으로 인해 평가불가",
    EMG_CHRONIC_REINNERVATION: "휴식 시 Silent at rest / 수의수축 시 Giant MUAPs 및 Reduced MU recruitment",
    EMG_ACTIVE_CHRONIC: "휴식 시 fibrillation potential, positive sharp wave / 수의수축 시 Giant MUAPs 및 Reduced MU recruitment",
    EMG_FASCICULATION: "휴식 시 fasciculation potential / 수의수축 시 Reduced MU recruitment",
    EMG_NO_RESPONSE: "휴식 시 Silent at rest / 수의수축 시 No MUAPs on volition",
}

SPECIAL_LABELS = {
    FWAVE_DELAYED_ABSENT: "F파 최소잠복기 지연 또는 소실",
    H_REFLEX_HYPERACTIVE: "H-반사 항진",
    H_M_RATIO_INCREASED: "H/M 비율 증가",
    BLINK_DELAYED: "눈깜빡반사 지연",
    BLINK_DELAYED_ABSENT: "눈깜빡반사 지연 또는 소실",
}

# ---------------------------------------------------------------------
# 기존 코드 호환 별칭
# ---------------------------------------------------------------------
NCS_DELAY = NCS_DELAYED
NCS_DECREASED = NCS_REDUCED
NCS_LOST = NCS_ABSENT

EMG_DENERVATION = EMG_ACTIVE_DENERVATION
EMG_PARASPINAL = EMG_PARASPINAL_DENERVATION
EMG_FASC = EMG_FASCICULATION


def ncs_term_label(value: str) -> str:
    """NCS 결과 상수를 표준 라벨로 변환합니다."""
    if value is None:
        return ""
    return NCS_LABELS.get(str(value).strip(), str(value).strip())


def emg_term_label(value: str) -> str:
    """EMG 결과 상수를 표준 라벨로 변환합니다."""
    if value is None:
        return ""
    return EMG_LABELS.get(str(value).strip(), str(value).strip())


def special_term_label(value: str) -> str:
    """F-wave, H-reflex, Blink reflex 결과 상수를 표준 라벨로 변환합니다."""
    if value is None:
        return ""
    return SPECIAL_LABELS.get(str(value).strip(), str(value).strip())


def term_label(value: str, domain: str = "") -> str:
    """domain 정보가 있을 때 결과값을 가장 적절한 표준 라벨로 변환합니다."""
    if value is None:
        return ""

    value = str(value).strip()

    if domain in {"sensory", "motor"}:
        return ncs_term_label(value)

    if domain == "muscle":
        return emg_term_label(value)

    if domain in {"h_reflex", "h_ratio", "f_wave", "blink", "reflex"}:
        return special_term_label(value)

    if value in NCS_LABELS:
        return ncs_term_label(value)
    if value in EMG_LABELS:
        return emg_term_label(value)
    if value in SPECIAL_LABELS:
        return special_term_label(value)

    return value


def is_normal_code(value: str) -> bool:
    """내부 상수 또는 표기 문자열 기준 정상 여부를 판정합니다."""
    if value is None:
        return False

    text = str(value).strip().lower()
    if text == "":
        return False

    normal_values = {
        NCS_NORMAL,
        EMG_NORMAL,
        "normal",
        "ncs normal",
        "emg normal",
        "정상",
        "정상 범위",
        "정상 범위(within normal limits)",
        "정상 범위 (within normal limits)",
    }

    if text in {v.lower() for v in normal_values}:
        return True

    if "정상 범위" in text and "비정상" not in text:
        return True

    if "silent at rest" in text and "normal mu recruitment" in text:
        return True

    return False


def is_abnormal_code(value: str) -> bool:
    """내부 상수 또는 표기 문자열 기준 비정상 여부를 판정합니다."""
    if value is None:
        return False

    text = str(value).strip()
    if text == "":
        return False

    return not is_normal_code(text)
