# utils/formatters.py

"""
결과 텍스트 정규화 및 표시용 포매터.
"""

from typing import Any

from data.terms import (
    NCS_NORMAL,
    NCS_DELAYED,
    NCS_REDUCED,
    NCS_ABSENT,
    NCS_CONDUCTION_BLOCK,
    EMG_NORMAL,
    EMG_ACTIVE_DENERVATION,
    EMG_PARASPINAL_DENERVATION,
    EMG_CHRONIC_REINNERVATION,
    EMG_ACTIVE_CHRONIC,
    EMG_FASCICULATION,
    EMG_NO_RESPONSE,
    FWAVE_DELAYED_ABSENT,
    H_REFLEX_HYPERACTIVE,
    H_M_RATIO_INCREASED,
    BLINK_DELAYED,
    BLINK_DELAYED_ABSENT,
)


NORMALIZED_TEXT_MAP = {
    None: "",
    "": "",
    "normal": "정상 범위",
    "Normal": "정상 범위",
    "정상": "정상 범위",
    "정상 범위": "정상 범위",
    "정상 (Normal)": "정상 범위",
    "정상 범위(within normal limits)": "정상 범위",
    "정상 범위 (within normal limits)": "정상 범위",

    NCS_NORMAL: "정상 범위",
    NCS_DELAYED: "잠복기 지연",
    NCS_REDUCED: "진폭 감소",
    NCS_ABSENT: "반응 소실",
    NCS_CONDUCTION_BLOCK: "전도차단",

    EMG_NORMAL: "휴식 시 Silent at rest / 수의수축 시 Normal MU recruitment",
    EMG_ACTIVE_DENERVATION: "휴식 시 fibrillation potential, positive sharp wave / 수의수축 시 Reduced MU recruitment",
    EMG_PARASPINAL_DENERVATION: "휴식 시 fibrillation potential, positive sharp wave / 수의수축 시 통증으로 인해 평가불가",
    EMG_CHRONIC_REINNERVATION: "휴식 시 Silent at rest / 수의수축 시 Giant MUAPs 및 Reduced MU recruitment",
    EMG_ACTIVE_CHRONIC: "휴식 시 fibrillation potential, positive sharp wave / 수의수축 시 Giant MUAPs 및 Reduced MU recruitment",
    EMG_FASCICULATION: "휴식 시 fasciculation potential / 수의수축 시 Reduced MU recruitment",
    EMG_NO_RESPONSE: "휴식 시 Silent at rest / 수의수축 시 No MUAPs on volition",

    FWAVE_DELAYED_ABSENT: "F파 지연 또는 소실",
    H_REFLEX_HYPERACTIVE: "H-반사 항진",
    H_M_RATIO_INCREASED: "H/M 비율 증가",
    BLINK_DELAYED: "눈깜빡반사 지연",
    BLINK_DELAYED_ABSENT: "눈깜빡반사 지연 또는 소실",

    "감소 (Reduced)": "진폭 감소",
    "잠복기 지연 (Delayed latency)": "잠복기 지연",
    "무반응 (No response)": "반응 소실",
    "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)": "비정상 자발전위 출현",
    "비정상 자발전위 (Fibrillation, Positive sharp wave 등) 출현": "비정상 자발전위 출현",
    "무반응 / 전기적 침묵 (Electrical silence)": "무반응/전기적 침묵",
    "지연 또는 소실 (Delayed/Absent)": "지연 또는 소실",
    "항진 또는 문턱값 감소 (Hyperactive / lower threshold)": "항진 또는 문턱값 감소",
    "증가 가능 (May be increased)": "증가 가능",
    "지연 (Delayed)": "지연",
    "소실 (Absent)": "소실",
}


def normalize_result_text(value: Any) -> str:
    """결과값을 화면 표시용 짧은 표준 문구로 변환합니다."""
    if value is None:
        return ""

    text = str(value).strip()
    if text == "":
        return ""

    return NORMALIZED_TEXT_MAP.get(text, text)


def summarize_status(left: Any, right: Any, side: str = "미선택") -> str:
    """좌우 결과를 병변측 정보에 맞추어 요약합니다."""
    left_disp = normalize_result_text(left)
    right_disp = normalize_result_text(right)

    if str(right).strip() == "":
        return f"결과: {left_disp}"

    if side in {"양측", "양쪽"}:
        return f"좌측: {left_disp} / 우측: {right_disp}"

    if side in {"좌", "왼쪽"}:
        return f"좌측(병변측): {left_disp} / 우측(정상측): {right_disp}"

    if side in {"우", "오른쪽"}:
        return f"좌측(정상측): {left_disp} / 우측(병변측): {right_disp}"

    return f"좌측: {left_disp} / 우측: {right_disp}"


def severity_text(total_abnormal: int, no_response_count: int = 0) -> str:
    """비정상 항목 수와 무반응 수에 따라 교육용 중증도를 반환합니다."""
    if no_response_count >= 2 or total_abnormal >= 6:
        return "중등도 이상"
    if total_abnormal >= 3:
        return "경도-중등도"
    if total_abnormal >= 1:
        return "경도"
    return "뚜렷한 이상 없음"


def side_to_korean(side: str) -> str:
    """측 정보를 화면용 한글 표기로 통일합니다."""
    if side in {"우", "오른쪽", "Right", "right"}:
        return "오른쪽"
    if side in {"좌", "왼쪽", "Left", "left"}:
        return "왼쪽"
    if side in {"양측", "양쪽", "Both", "both", "bilateral"}:
        return "양쪽"
    return side or "-"
