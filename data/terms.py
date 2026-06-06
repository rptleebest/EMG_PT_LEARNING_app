# data/terms.py

"""
EMG/NCS 판독 앱에서 사용하는 내부 코드값, 화면 표시용 용어, 호환용 용어 사전.

이 파일의 역할:
1. data.constants.py에서 불러오는 내부 코드값 제공
2. ui.case_learning.py에서 불러오는 ncs_amplitude_latency, emg_case_label, special_term 제공
3. 기존 코드가 함수처럼 쓰거나 dict처럼 써도 최대한 깨지지 않도록 호환 처리
"""


# -------------------------------------------------------------------
# NCS 내부 코드값
# -------------------------------------------------------------------
NCS_NORMAL = "ncs_normal"
NCS_DELAYED = "ncs_delayed"
NCS_REDUCED = "ncs_reduced"
NCS_ABSENT = "ncs_absent"
NCS_CONDUCTION_BLOCK = "ncs_conduction_block"


# -------------------------------------------------------------------
# EMG 내부 코드값
# -------------------------------------------------------------------
EMG_NORMAL = "emg_normal"
EMG_ACTIVE_DENERVATION = "emg_active_denervation"
EMG_CHRONIC_REINNERVATION = "emg_chronic_reinnervation"
EMG_FASCICULATION = "emg_fasciculation"
EMG_NO_RESPONSE = "emg_no_response"


# -------------------------------------------------------------------
# 특수검사 내부 코드값
# -------------------------------------------------------------------
FWAVE_DELAYED_ABSENT = "fwave_delayed_absent"
H_REFLEX_HYPERACTIVE = "h_reflex_hyperactive"
H_M_RATIO_INCREASED = "h_m_ratio_increased"
BLINK_DELAYED = "blink_delayed"
BLINK_DELAYED_ABSENT = "blink_delayed_absent"


class TermLookup(dict):
    """
    dict처럼도 쓰고 함수처럼도 쓸 수 있는 호환용 사전입니다.

    사용 가능 예:
    - ncs_amplitude_latency.get(code)
    - ncs_amplitude_latency[code]
    - ncs_amplitude_latency(code)
    - ncs_amplitude_latency()
    """

    def __call__(self, key=None, default=""):
        if key is None:
            return self

        return self.get(key, default if default != "" else str(key))


# -------------------------------------------------------------------
# NCS 결과 표시/해석 라벨
# -------------------------------------------------------------------
ncs_amplitude_latency = TermLookup(
    {
        NCS_NORMAL: "정상 범위: 진폭과 잠복기가 정상 범위입니다.",
        NCS_DELAYED: "잠복기 지연: 말이집탈락 또는 압박성 전도 지연 가능성을 시사합니다.",
        NCS_REDUCED: "진폭 감소: 축삭 손상 또는 전도차단 가능성을 시사합니다.",
        NCS_ABSENT: "반응 소실: 심한 축삭 손상 또는 전도 실패 가능성을 시사합니다.",
        NCS_CONDUCTION_BLOCK: "전도차단: 국소 압박이나 말이집탈락성 병변 가능성을 시사합니다.",

        "정상": "정상 범위: 진폭과 잠복기가 정상 범위입니다.",
        "정상 범위": "정상 범위: 진폭과 잠복기가 정상 범위입니다.",
        "잠복기 지연": "잠복기 지연: 말이집탈락 또는 압박성 전도 지연 가능성을 시사합니다.",
        "진폭 감소": "진폭 감소: 축삭 손상 또는 전도차단 가능성을 시사합니다.",
        "반응 소실": "반응 소실: 심한 축삭 손상 또는 전도 실패 가능성을 시사합니다.",
        "전도차단": "전도차단: 국소 압박이나 말이집탈락성 병변 가능성을 시사합니다.",
        "무반응": "무반응: 심한 축삭 손상 또는 전도 실패 가능성을 시사합니다.",
    }
)


# -------------------------------------------------------------------
# EMG 결과 표시/해석 라벨
# -------------------------------------------------------------------
emg_case_label = TermLookup(
    {
        EMG_NORMAL: "정상 침근전도 소견",
        EMG_ACTIVE_DENERVATION: "활동성 탈신경 소견",
        EMG_CHRONIC_REINNERVATION: "만성 재신경지배 소견",
        EMG_FASCICULATION: "섬유다발수축전위 소견",
        EMG_NO_RESPONSE: "운동단위 동원 불가",

        "normal": "정상 침근전도 소견",
        "active_denervation": "활동성 탈신경 소견",
        "chronic_reinnervation": "만성 재신경지배 소견",
        "fasciculation": "섬유다발수축전위 소견",
        "no_response": "운동단위 동원 불가",

        "정상": "정상 침근전도 소견",
        "정상 범위": "정상 침근전도 소견",
        "활동성 탈신경": "활동성 탈신경 소견",
        "만성 재신경지배": "만성 재신경지배 소견",
        "섬유다발수축전위": "섬유다발수축전위 소견",
        "동원 불가": "운동단위 동원 불가",
    }
)


# -------------------------------------------------------------------
# 특수 용어 설명
# -------------------------------------------------------------------
special_term = TermLookup(
    {
        "SNAP": "감각신경활동전위입니다. 감각신경의 축삭 기능을 평가합니다.",
        "CMAP": "복합근육활동전위입니다. 운동신경과 근육 반응을 평가합니다.",
        "MUAP": "운동단위활동전위입니다. 침근전도에서 운동단위의 형태와 동원 양상을 평가합니다.",
        "Giant MUAP": "거대 운동단위활동전위입니다. 과거 축삭 손상 후 재신경지배가 진행된 만성 신경성 변화를 시사합니다.",
        "Reduced MU recruitment": "수의수축 시 동원 가능한 운동단위 수가 감소한 상태입니다.",
        "No MUAPs on volition": "수의수축을 시도해도 운동단위활동전위가 관찰되지 않는 상태입니다.",
        "Silent at rest": "휴식 시 비정상 자발전위가 관찰되지 않는 상태입니다.",
        "fibrillation potential": "탈신경된 근섬유에서 나타날 수 있는 비정상 자발전위입니다.",
        "positive sharp wave": "탈신경 또는 근섬유막 불안정성과 관련된 비정상 자발전위입니다.",
        "Fibrillation": "탈신경된 근섬유에서 나타날 수 있는 비정상 자발전위입니다.",
        "Positive sharp wave": "탈신경 또는 근섬유막 불안정성과 관련된 비정상 자발전위입니다.",
        "conduction block": "국소 부위에서 신경 자극 전달이 차단되는 소견입니다.",
        "Conduction block": "국소 부위에서 신경 자극 전달이 차단되는 소견입니다.",
        "Sural sparing": "장딴지신경 감각반응이 비교적 보존되는 양상으로, 일부 급성 염증성 탈말이집성 다발신경병증에서 관찰될 수 있습니다.",
        "Sural sparing effect": "장딴지신경 감각반응이 비교적 보존되는 양상으로, 기얭-바레 증후군 감별에 참고될 수 있습니다.",
        "Gilliatt-Sumner hand": "가슴문증후군에서 T1 우세 손 내재근 위축이 두드러지는 양상입니다.",
        "H-reflex": "S1 반사경로를 평가하는 데 활용되는 전기생리학적 반사 검사입니다.",
        "F-wave": "말초신경의 근위부 전도 이상을 평가하는 데 도움이 되는 후기 반응입니다.",
        "Blink reflex": "삼차신경, 뇌줄기, 얼굴신경을 포함하는 반사경로 평가입니다.",
    }
)


# -------------------------------------------------------------------
# 일반 용어 설명
# -------------------------------------------------------------------
TERM_EXPLANATIONS = TermLookup(
    {
        "radiculopathy": "신경뿌리병증입니다. 병변이 뒤뿌리신경절보다 몸쪽에 있으면 감각신경활동전위가 보존될 수 있습니다.",
        "neuropathy": "말초신경병증입니다. 병변 위치에 따라 감각 및 운동신경전도 이상이 함께 나타날 수 있습니다.",
        "plexopathy": "신경얼기병증입니다. 여러 말초신경 영역을 침범하면서 척추주위근은 보존되는 양상이 감별에 중요합니다.",
        "polyneuropathy": "다발신경병증입니다. 대칭적, 길이의존성, 원위부 우세 양상이 흔합니다.",
        "demyelination": "말이집탈락입니다. 잠복기 지연, 전도속도 저하, 전도차단이 주요 단서가 될 수 있습니다.",
        "axonal loss": "축삭 손상입니다. 진폭 감소와 침근전도 탈신경 소견이 주요 단서가 될 수 있습니다.",
    }
)


def get_ncs_description(code_or_text: str) -> str:
    """
    NCS 코드 또는 텍스트에 대한 설명을 반환합니다.
    """
    return ncs_amplitude_latency(code_or_text)


def get_emg_description(code_or_text: str) -> str:
    """
    EMG 코드 또는 텍스트에 대한 설명을 반환합니다.
    """
    return emg_case_label(code_or_text)


def get_special_term_description(term: str) -> str:
    """
    특수 용어 설명을 반환합니다.
    """
    return special_term(term)


def explain_term(term: str) -> str:
    """
    일반 용어 또는 특수 용어 설명을 반환합니다.
    """
    if term in special_term:
        return special_term(term)

    if term in TERM_EXPLANATIONS:
        return TERM_EXPLANATIONS(term)

    return str(term)


def normalize_result_code(value: str) -> str:
    """
    화면 표시 문자열 또는 내부 코드값을 가능한 범위에서 표준 내부 코드값으로 변환합니다.
    """
    text = str(value)

    mapping = {
        "정상": NCS_NORMAL,
        "정상 범위": NCS_NORMAL,
        "잠복기 지연": NCS_DELAYED,
        "진폭 감소": NCS_REDUCED,
        "반응 소실": NCS_ABSENT,
        "무반응": NCS_ABSENT,
        "전도차단": NCS_CONDUCTION_BLOCK,
        "국소 전도차단": NCS_CONDUCTION_BLOCK,
        "활동성 탈신경": EMG_ACTIVE_DENERVATION,
        "만성 재신경지배": EMG_CHRONIC_REINNERVATION,
        "섬유다발수축전위": EMG_FASCICULATION,
        "동원 불가": EMG_NO_RESPONSE,
    }

    if text in mapping:
        return mapping[text]

    return text


def is_abnormal_result(value: str) -> bool:
    """
    결과 문자열이 비정상 소견을 포함하는지 간단히 판정합니다.
    """
    text = str(value)

    abnormal_keywords = [
        "비정상",
        "감소",
        "지연",
        "소실",
        "무반응",
        "전도차단",
        "탈신경",
        "재신경지배",
        "동원 불가",
        "Reduced",
        "Delayed",
        "Absent",
        "No response",
        "Conduction block",
        "denervation",
        "reinnervation",
    ]

    return any(keyword in text for keyword in abnormal_keywords)


def is_normal_result(value: str) -> bool:
    """
    결과 문자열이 정상 소견을 포함하는지 간단히 판정합니다.
    """
    text = str(value)

    normal_keywords = [
        "정상",
        "정상 범위",
        "Normal",
        "Within normal limits",
        "Silent at rest",
    ]

    return any(keyword in text for keyword in normal_keywords) and not is_abnormal_result(text)
