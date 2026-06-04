# data/terms.py

"""
신용어 한글(영어) 표준 용어 및 결과 상수 정의.

이 파일은 데이터 내부 코드값과 화면 표시용 문구를 분리하기 위한 기준 파일입니다.
사례 학습에서는 지나치게 긴 원문식 표현을 줄이고,
가상 결과표 판독에서는 실제 결과표 용어를 유지하는 방향으로 사용합니다.
"""

# ---------------------------------------------------------------------
# NCS 결과 상수
# ---------------------------------------------------------------------
NCS_NORMAL = "ncs_normal"
NCS_DELAYED = "ncs_delayed"
NCS_REDUCED = "ncs_reduced"
NCS_CONDUCTION_BLOCK = "ncs_conduction_block"
NCS_ABSENT = "ncs_absent"

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


def ncs_term_label(value: str) -> str:
    """
    사례 학습용 NCS 간략 표기.
    괄호 설명은 판독 기준 팁에서 제시하므로 표 안에서는 삭제합니다.
    """
    mapping = {
        NCS_NORMAL: "정상 범위",
        NCS_DELAYED: "잠복기 지연",
        NCS_REDUCED: "진폭 감소",
        NCS_CONDUCTION_BLOCK: "전도차단",
        NCS_ABSENT: "반응 소실",
        "normal": "정상 범위",
        "delayed": "잠복기 지연",
        "reduced": "진폭 감소",
        "absent": "반응 소실",
    }
    return mapping.get(value, str(value))


def ncs_amplitude_latency(value: str) -> dict:
    """
    사례 학습용 간략 NCS 결과.
    요청사항:
    - 판단 열은 삭제
    - 진폭/잠복기 칸에는 감소/지연/정상 범위만 표기
    - 괄호 설명 삭제
    """
    mapping = {
        NCS_NORMAL: {"amplitude": "정상 범위", "latency": "정상 범위"},
        NCS_DELAYED: {"amplitude": "정상 범위", "latency": "지연"},
        NCS_REDUCED: {"amplitude": "감소", "latency": "정상 범위"},
        NCS_CONDUCTION_BLOCK: {"amplitude": "감소", "latency": "정상 범위"},
        NCS_ABSENT: {"amplitude": "반응 소실", "latency": "반응 소실"},
        "normal": {"amplitude": "정상 범위", "latency": "정상 범위"},
        "delayed": {"amplitude": "정상 범위", "latency": "지연"},
        "reduced": {"amplitude": "감소", "latency": "정상 범위"},
        "absent": {"amplitude": "반응 소실", "latency": "반응 소실"},
    }
    return mapping.get(
        value,
        {"amplitude": str(value), "latency": ""},
    )


def emg_case_label(value: str) -> dict:
    """
    사례 학습용 침근전도 간략 표기.

    교수님 요청 검토 반영:
    - 사례 학습에서는 실제 전위명을 모두 표에 넣으면 초심자에게 과부하가 될 수 있음.
    - 따라서 표에서는 '비정상 자발전위 출현', '운동단위 동원감소'처럼 단순화.
    - 실제 전위명은 판독 기준 팁과 통합 해석에서 설명.
    """
    mapping = {
        EMG_NORMAL: {
            "rest": "정상 반응",
            "volition": "정상 운동단위 동원",
        },
        EMG_ACTIVE_DENERVATION: {
            "rest": "비정상 자발전위 출현",
            "volition": "운동단위 동원감소",
        },
        EMG_PARASPINAL_DENERVATION: {
            "rest": "비정상 자발전위 출현",
            "volition": "평가 제한",
        },
        EMG_CHRONIC_REINNERVATION: {
            "rest": "정상 반응",
            "volition": "만성 재신경지배 소견 / 운동단위 동원감소",
        },
        EMG_ACTIVE_CHRONIC: {
            "rest": "비정상 자발전위 출현",
            "volition": "만성 재신경지배 소견 / 운동단위 동원감소",
        },
        EMG_FASCICULATION: {
            "rest": "근육다발수축전위 출현",
            "volition": "운동단위 동원감소",
        },
        EMG_NO_RESPONSE: {
            "rest": "정상 반응",
            "volition": "운동단위 동원 불가",
        },
        "normal": {
            "rest": "정상 반응",
            "volition": "정상 운동단위 동원",
        },
    }
    return mapping.get(
        value,
        {
            "rest": str(value),
            "volition": "",
        },
    )


def emg_actual_label(value: str) -> dict:
    """
    가상 결과표 판독학습용 실제 전위명 표기.
    실제 근전도 결과표와 유사하게 영문 전위명을 유지합니다.
    """
    mapping = {
        EMG_NORMAL: {
            "rest": "Silent at rest",
            "volition": "Normal MU recruitment",
        },
        EMG_ACTIVE_DENERVATION: {
            "rest": "fibrillation potential, positive sharp wave",
            "volition": "Reduced MU recruitment",
        },
        EMG_PARASPINAL_DENERVATION: {
            "rest": "fibrillation potential, positive sharp wave",
            "volition": "Pain-limited evaluation",
        },
        EMG_CHRONIC_REINNERVATION: {
            "rest": "Silent at rest",
            "volition": "Giant MUAPs with reduced recruitment",
        },
        EMG_ACTIVE_CHRONIC: {
            "rest": "fibrillation potential, positive sharp wave",
            "volition": "Giant MUAPs with reduced recruitment",
        },
        EMG_FASCICULATION: {
            "rest": "fasciculation potential",
            "volition": "Reduced MU recruitment",
        },
        EMG_NO_RESPONSE: {
            "rest": "Silent at rest",
            "volition": "No MUAPs on volition",
        },
    }
    return mapping.get(
        value,
        {
            "rest": str(value),
            "volition": "",
        },
    )


def special_term_label(value: str) -> str:
    mapping = {
        FWAVE_DELAYED_ABSENT: "지연 또는 소실",
        H_REFLEX_HYPERACTIVE: "항진",
        H_M_RATIO_INCREASED: "H/M 비율 증가",
        BLINK_DELAYED: "지연",
        BLINK_DELAYED_ABSENT: "지연 또는 소실",
        NCS_NORMAL: "정상 범위",
        "normal": "정상 범위",
    }
    return mapping.get(value, str(value))


def is_normal_code(value: str) -> bool:
    return value in {
        NCS_NORMAL,
        EMG_NORMAL,
        "normal",
        "정상",
        "정상 범위",
    }


# ---------------------------------------------------------------------
# 호환성 별칭
# ---------------------------------------------------------------------
NCS_DELAY = NCS_DELAYED
NCS_DECREASED = NCS_REDUCED
NCS_LOST = NCS_ABSENT

EMG_DENERVATION = EMG_ACTIVE_DENERVATION
EMG_PARASPINAL = EMG_PARASPINAL_DENERVATION
EMG_FASC = EMG_FASCICULATION
