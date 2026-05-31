# data/terms.py

"""
신용어 한글(영어) 표준 용어 및 결과 상수 정의.

주의:
- 이 파일은 사례 데이터와 해석 로직에서 공통으로 사용하는 표준 용어를 정의합니다.
- 표기 일관성을 위해 한글(영어) 순서를 기본으로 합니다.
- 기존 코드 호환성을 위해 일부 별칭(alias)을 함께 제공합니다.
"""

# ---------------------------------------------------------------------
# NCS 결과 상수
# ---------------------------------------------------------------------
NCS_NORMAL = "normal"
NCS_DELAYED = "delayed"          # 잠복기 지연 / 전도 지연
NCS_REDUCED = "reduced"          # 진폭 감소
NCS_ABSENT = "absent"            # 반응 소실

# ---------------------------------------------------------------------
# EMG 결과 상수
# ---------------------------------------------------------------------
EMG_NORMAL = "normal"
EMG_ACTIVE_DENERVATION = "active_denervation"
EMG_PARASPINAL_DENERVATION = "paraspinal_denervation"
EMG_FASCICULATION = "fasciculation"

# ---------------------------------------------------------------------
# F-wave / H-reflex / Blink reflex 결과 상수
# ---------------------------------------------------------------------
FWAVE_DELAYED_ABSENT = "delayed_or_absent"
H_REFLEX_HYPERACTIVE = "hyperactive"
H_M_RATIO_INCREASED = "increased"
BLINK_DELAYED = "delayed"
BLINK_DELAYED_ABSENT = "delayed_or_absent"

# ---------------------------------------------------------------------
# 표준 표기 함수
# ---------------------------------------------------------------------
def ncs_term_label(value: str) -> str:
    """NCS 결과 상수를 신용어 한글(영어) 표기로 반환."""
    mapping = {
        NCS_NORMAL: "정상(normal)",
        NCS_DELAYED: "잠복기 지연(delayed)",
        NCS_REDUCED: "진폭 감소(reduced)",
        NCS_ABSENT: "반응 소실(absent)",
    }
    return mapping.get(value, value)

def emg_term_label(value: str) -> str:
    """EMG 결과 상수를 신용어 한글(영어) 표기로 반환."""
    mapping = {
        EMG_NORMAL: "정상(normal)",
        EMG_ACTIVE_DENERVATION: "활동성 탈신경(active denervation)",
        EMG_PARASPINAL_DENERVATION: "척추주위근 탈신경(paraspinal denervation)",
        EMG_FASCICULATION: "근육다발수축(fasciculation)",
    }
    return mapping.get(value, value)

def special_term_label(value: str) -> str:
    """기타 전기생리 결과 상수를 신용어 한글(영어) 표기로 반환."""
    mapping = {
        FWAVE_DELAYED_ABSENT: "지연 또는 소실(delayed or absent)",
        H_REFLEX_HYPERACTIVE: "항진(hyperactive)",
        H_M_RATIO_INCREASED: "H/M 비율 증가(increased H/M ratio)",
        BLINK_DELAYED: "지연(delayed)",
        BLINK_DELAYED_ABSENT: "지연 또는 소실(delayed or absent)",
    }
    return mapping.get(value, value)

# ---------------------------------------------------------------------
# 호환성 별칭
# ---------------------------------------------------------------------
NCS_DELAY = NCS_DELAYED
NCS_DECREASED = NCS_REDUCED
NCS_LOST = NCS_ABSENT

EMG_DENERVATION = EMG_ACTIVE_DENERVATION
EMG_PARASPINAL = EMG_PARASPINAL_DENERVATION
EMG_FASC = EMG_FASCICULATION
