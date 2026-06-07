# data/terms.py

"""
EMG/NCS 판독 앱에서 사용하는 내부 코드값, 화면 표시용 용어, 호환용 용어 사전.

역할:
1. data.constants.py에서 사용하는 NCS/EMG/특수검사 내부 코드 제공
2. data.cases.py에서 사용하는 사례 판독 코드 제공
3. ui.case_learning.py에서 사용하는 ncs_amplitude_latency, emg_case_label, special_term 제공
4. 기존 코드가 dict처럼 쓰거나 함수처럼 써도 최대한 깨지지 않도록 호환 처리
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
# NCS 추가 호환 코드값
# -------------------------------------------------------------------
NCS_PROLONGED_LATENCY = "ncs_prolonged_latency"
NCS_LOW_AMPLITUDE = "ncs_low_amplitude"
NCS_SLOW_CONDUCTION = "ncs_slow_conduction"
NCS_TEMPORAL_DISPERSION = "ncs_temporal_dispersion"
NCS_DEMYELINATING = "ncs_demyelinating"
NCS_AXONAL_LOSS = "ncs_axonal_loss"
NCS_MIXED_ABNORMAL = "ncs_mixed_abnormal"
NCS_SURAL_SPARING = "ncs_sural_sparing"
NCS_FOCAL_SLOWING = "ncs_focal_slowing"
NCS_ENTRAPMENT = "ncs_entrapment"
NCS_SIDE_TO_SIDE_DIFFERENCE = "ncs_side_to_side_difference"


# -------------------------------------------------------------------
# EMG 내부 코드값
# -------------------------------------------------------------------
EMG_NORMAL = "emg_normal"
EMG_ACTIVE_DENERVATION = "emg_active_denervation"
EMG_CHRONIC_REINNERVATION = "emg_chronic_reinnervation"
EMG_FASCICULATION = "emg_fasciculation"
EMG_NO_RESPONSE = "emg_no_response"


# -------------------------------------------------------------------
# EMG 추가 호환 코드값
# data/cases.py에서 직접 import하는 이름 포함
# -------------------------------------------------------------------
EMG_PARASPINAL_DENERVATION = "emg_paraspinal_denervation"
EMG_ACTIVE_CHRONIC = "emg_active_chronic"

EMG_ACTIVE_CHRONIC_DENERVATION = "emg_active_chronic_denervation"
EMG_CHRONIC_NEUROGENIC_CHANGE = "emg_chronic_neurogenic_change"
EMG_REDUCED_RECRUITMENT = "emg_reduced_recruitment"
EMG_GIANT_MUAP = "emg_giant_muap"
EMG_MYOKYMIC_DISCHARGE = "emg_myokymic_discharge"
EMG_COMPLEX_REPETITIVE_DISCHARGE = "emg_complex_repetitive_discharge"
EMG_POSITIVE_SHARP_WAVE = "emg_positive_sharp_wave"
EMG_FIBRILLATION = "emg_fibrillation"
EMG_NO_VOLUNTARY_MUAP = "emg_no_voluntary_muap"
EMG_NORMAL_RECRUITMENT = "emg_normal_recruitment"
EMG_POOR_ACTIVATION = "emg_poor_activation"


# -------------------------------------------------------------------
# 특수검사 내부 코드값
# -------------------------------------------------------------------
FWAVE_DELAYED_ABSENT = "fwave_delayed_absent"
H_REFLEX_HYPERACTIVE = "h_reflex_hyperactive"
H_M_RATIO_INCREASED = "h_m_ratio_increased"
BLINK_DELAYED = "blink_delayed"
BLINK_DELAYED_ABSENT = "blink_delayed_absent"


# -------------------------------------------------------------------
# 특수검사 추가 호환 코드값
# -------------------------------------------------------------------
FWAVE_NORMAL = "fwave_normal"
FWAVE_DELAYED = "fwave_delayed"
FWAVE_ABSENT = "fwave_absent"

H_REFLEX_NORMAL = "h_reflex_normal"
H_REFLEX_DELAYED = "h_reflex_delayed"
H_REFLEX_ABSENT = "h_reflex_absent"

BLINK_NORMAL = "blink_normal"


class TermLookup(dict):
    """
    dict처럼도 쓰고 함수처럼도 쓸 수 있는 호환용 사전입니다.

    사용 예:
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
        NCS_CONDUCTION_BLOCK: "전도차단: 국소 압박 또는 말이집탈락성 병변 가능성을 시사합니다.",

        NCS_PROLONGED_LATENCY: "잠복기 연장: 말이집탈락 또는 압박성 전도 지연 가능성을 시사합니다.",
        NCS_LOW_AMPLITUDE: "저진폭: 축삭 손상 또는 심한 전도차단 가능성을 시사합니다.",
        NCS_SLOW_CONDUCTION: "전도속도 저하: 말이집탈락성 병변 가능성을 시사합니다.",
        NCS_TEMPORAL_DISPERSION: "시간적 분산: 말이집탈락성 전도 이상에서 관찰될 수 있습니다.",
        NCS_DEMYELINATING: "말이집탈락성 전도 이상: 잠복기 지연, 전도속도 저하, 전도차단 등이 단서입니다.",
        NCS_AXONAL_LOSS: "축삭 손상: 주로 진폭 감소 또는 반응 소실로 나타납니다.",
        NCS_MIXED_ABNORMAL: "혼합성 이상: 축삭 손상과 말이집탈락성 변화가 함께 의심됩니다.",
        NCS_SURAL_SPARING: "장딴지신경 보존 양상: 일부 급성 염증성 탈말이집성 다발신경병증에서 참고됩니다.",
        NCS_FOCAL_SLOWING: "국소 전도 지연: 포착성 신경병증 또는 국소 압박 병변을 시사할 수 있습니다.",
        NCS_ENTRAPMENT: "포착성 신경병증 양상: 특정 해부학적 통로에서 압박이 의심됩니다.",
        NCS_SIDE_TO_SIDE_DIFFERENCE: "좌우 차이 증가: 병변측 신경 기능 저하 가능성을 시사합니다.",

        FWAVE_DELAYED_ABSENT: "F파 지연 또는 소실: 근위부 전도 이상 또는 말이집탈락성 병변 가능성을 시사합니다.",
        FWAVE_NORMAL: "F파 정상: 근위부 전도 이상의 뚜렷한 증거가 없습니다.",
        FWAVE_DELAYED: "F파 지연: 근위부 전도 지연 가능성을 시사합니다.",
        FWAVE_ABSENT: "F파 소실: 근위부 전도 이상 또는 심한 말초신경 침범 가능성을 시사합니다.",

        H_REFLEX_HYPERACTIVE: "H-반사 항진: 척수반사 흥분성 증가 또는 중추성 경직 평가에 참고됩니다.",
        H_M_RATIO_INCREASED: "H/M 비율 증가: 반사 흥분성 증가와 경직 정도 평가에 참고됩니다.",
        H_REFLEX_NORMAL: "H-반사 정상 범위입니다.",
        H_REFLEX_DELAYED: "H-반사 지연: S1 반사경로 이상 가능성을 시사합니다.",
        H_REFLEX_ABSENT: "H-반사 소실: S1 신경뿌리 또는 말초 반사경로 이상 가능성을 시사합니다.",

        BLINK_NORMAL: "눈깜빡반사 정상 범위입니다.",
        BLINK_DELAYED: "눈깜빡반사 지연: 삼차신경-뇌줄기-얼굴신경 반사경로 중 일부 전도 지연 가능성을 시사합니다.",
        BLINK_DELAYED_ABSENT: "눈깜빡반사 지연 또는 소실: 반사경로 이상 가능성을 시사합니다.",

        "정상": "정상 범위: 진폭과 잠복기가 정상 범위입니다.",
        "정상 범위": "정상 범위: 진폭과 잠복기가 정상 범위입니다.",
        "잠복기 지연": "잠복기 지연: 말이집탈락 또는 압박성 전도 지연 가능성을 시사합니다.",
        "진폭 감소": "진폭 감소: 축삭 손상 또는 전도차단 가능성을 시사합니다.",
        "반응 소실": "반응 소실: 심한 축삭 손상 또는 전도 실패 가능성을 시사합니다.",
        "전도차단": "전도차단: 국소 압박 또는 말이집탈락성 병변 가능성을 시사합니다.",
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
        EMG_PARASPINAL_DENERVATION: "척추주위근 탈신경 소견",
        EMG_CHRONIC_REINNERVATION: "만성 재신경지배 소견",
        EMG_ACTIVE_CHRONIC: "활동성 탈신경과 만성 재신경지배가 함께 관찰되는 소견",
        EMG_FASCICULATION: "섬유다발수축전위 소견",
        EMG_NO_RESPONSE: "운동단위 동원 불가",

        EMG_ACTIVE_CHRONIC_DENERVATION: "활동성 탈신경과 만성 재신경지배가 함께 관찰되는 소견",
        EMG_CHRONIC_NEUROGENIC_CHANGE: "만성 신경성 변화",
        EMG_REDUCED_RECRUITMENT: "운동단위 동원 감소",
        EMG_GIANT_MUAP: "거대 운동단위활동전위",
        EMG_MYOKYMIC_DISCHARGE: "근파동방전 소견",
        EMG_COMPLEX_REPETITIVE_DISCHARGE: "복합반복방전 소견",
        EMG_POSITIVE_SHARP_WAVE: "양성예파 소견",
        EMG_FIBRILLATION: "섬유자발전위 소견",
        EMG_NO_VOLUNTARY_MUAP: "수의수축 시 운동단위활동전위 관찰 불가",
        EMG_NORMAL_RECRUITMENT: "정상 운동단위 동원",
        EMG_POOR_ACTIVATION: "불충분한 수의 활성화",

        "normal": "정상 침근전도 소견",
        "active_denervation": "활동성 탈신경 소견",
        "paraspinal_denervation": "척추주위근 탈신경 소견",
        "chronic_reinnervation": "만성 재신경지배 소견",
        "active_chronic": "활동성 탈신경과 만성 재신경지배가 함께 관찰되는 소견",
        "fasciculation": "섬유다발수축전위 소견",
        "no_response": "운동단위 동원 불가",

        "정상": "정상 침근전도 소견",
        "정상 범위": "정상 침근전도 소견",
        "활동성 탈신경": "활동성 탈신경 소견",
        "척추주위근 탈신경": "척추주위근 탈신경 소견",
        "만성 재신경지배": "만성 재신경지배 소견",
        "활동성 만성": "활동성 탈신경과 만성 재신경지배가 함께 관찰되는 소견",
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
        "Giant MUAPs": "거대 운동단위활동전위입니다. 만성 재신경지배를 시사할 수 있습니다.",
        "Reduced MU recruitment": "수의수축 시 동원 가능한 운동단위 수가 감소한 상태입니다.",
        "Normal MU recruitment": "수의수축 시 운동단위 동원이 정상적으로 이루어지는 상태입니다.",
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
        "H/M ratio": "H-반사 최대 진폭과 M파 최대 진폭의 비율로, 척수반사 흥분성을 정량화하는 데 활용됩니다.",
        "F-wave": "말초신경의 근위부 전도 이상을 평가하는 데 도움이 되는 후기 반응입니다.",
        "Blink reflex": "삼차신경, 뇌줄기, 얼굴신경을 포함하는 반사경로 평가입니다.",
        "Dorsal root ganglion": "뒤뿌리신경절입니다. 신경뿌리병증과 말초신경병증 감별에서 중요합니다.",
        "DRG": "뒤뿌리신경절입니다. 병변이 이보다 몸쪽이면 감각신경활동전위가 보존될 수 있습니다.",
        "Axonal loss": "축삭 손상입니다. 진폭 감소와 침근전도 탈신경 소견이 주요 단서가 됩니다.",
        "Demyelination": "말이집탈락입니다. 잠복기 지연, 전도속도 저하, 전도차단 등이 주요 단서입니다.",
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
        "radiculopathy_snap": "신경뿌리병증에서는 감각신경활동전위가 정상으로 보존되는 경우가 많습니다.",
        "peripheral_neuropathy_snap": "말초신경병증에서는 병변 위치가 뒤뿌리신경절보다 먼쪽이면 감각신경활동전위 진폭이 감소할 수 있습니다.",
    }
)

# -------------------------------------------------------------------
# ImportError 방지용 최종 호환 블록
# ui.case_learning.py / data.cases.py 호환
# -------------------------------------------------------------------

# NCS 기본 코드
NCS_NORMAL = globals().get("NCS_NORMAL", "ncs_normal")
NCS_DELAYED = globals().get("NCS_DELAYED", "ncs_delayed")
NCS_REDUCED = globals().get("NCS_REDUCED", "ncs_reduced")
NCS_ABSENT = globals().get("NCS_ABSENT", "ncs_absent")
NCS_CONDUCTION_BLOCK = globals().get("NCS_CONDUCTION_BLOCK", "ncs_conduction_block")

# EMG 기본 코드
EMG_NORMAL = globals().get("EMG_NORMAL", "emg_normal")
EMG_ACTIVE_DENERVATION = globals().get("EMG_ACTIVE_DENERVATION", "emg_active_denervation")
EMG_PARASPINAL_DENERVATION = globals().get("EMG_PARASPINAL_DENERVATION", "emg_paraspinal_denervation")
EMG_CHRONIC_REINNERVATION = globals().get("EMG_CHRONIC_REINNERVATION", "emg_chronic_reinnervation")
EMG_ACTIVE_CHRONIC = globals().get("EMG_ACTIVE_CHRONIC", "emg_active_chronic")
EMG_FASCICULATION = globals().get("EMG_FASCICULATION", "emg_fasciculation")
EMG_NO_RESPONSE = globals().get("EMG_NO_RESPONSE", "emg_no_response")

# 특수검사 코드
FWAVE_DELAYED_ABSENT = globals().get("FWAVE_DELAYED_ABSENT", "fwave_delayed_absent")
H_REFLEX_HYPERACTIVE = globals().get("H_REFLEX_HYPERACTIVE", "h_reflex_hyperactive")
H_M_RATIO_INCREASED = globals().get("H_M_RATIO_INCREASED", "h_m_ratio_increased")
BLINK_DELAYED = globals().get("BLINK_DELAYED", "blink_delayed")
BLINK_DELAYED_ABSENT = globals().get("BLINK_DELAYED_ABSENT", "blink_delayed_absent")


class TermLookup(dict):
    """
    dict처럼도 쓰고 함수처럼도 쓸 수 있는 호환용 사전.
    """
    def __call__(self, key=None, default=""):
        if key is None:
            return self
        return self.get(key, default if default != "" else str(key))


# ui.case_learning.py에서 import하는 이름 1
ncs_amplitude_latency = globals().get(
    "ncs_amplitude_latency",
    TermLookup(
        {
            NCS_NORMAL: "정상 범위: 진폭과 잠복기가 정상 범위입니다.",
            NCS_DELAYED: "잠복기 지연: 말이집탈락 또는 압박성 전도 지연 가능성을 시사합니다.",
            NCS_REDUCED: "진폭 감소: 축삭 손상 또는 전도차단 가능성을 시사합니다.",
            NCS_ABSENT: "반응 소실: 심한 축삭 손상 또는 전도 실패 가능성을 시사합니다.",
            NCS_CONDUCTION_BLOCK: "전도차단: 국소 압박 또는 말이집탈락성 병변 가능성을 시사합니다.",
            FWAVE_DELAYED_ABSENT: "F파 지연 또는 소실: 근위부 전도 이상 가능성을 시사합니다.",
            H_REFLEX_HYPERACTIVE: "H-반사 항진: 척수반사 흥분성 증가를 시사합니다.",
            H_M_RATIO_INCREASED: "H/M 비율 증가: 경직 또는 반사 흥분성 증가 평가에 참고됩니다.",
            BLINK_DELAYED: "눈깜빡반사 지연: 반사경로 전도 지연 가능성을 시사합니다.",
            BLINK_DELAYED_ABSENT: "눈깜빡반사 지연 또는 소실: 반사경로 이상 가능성을 시사합니다.",
        }
    ),
)

# ui.case_learning.py에서 import하는 이름 2
emg_case_label = globals().get(
    "emg_case_label",
    TermLookup(
        {
            EMG_NORMAL: "정상 침근전도 소견",
            EMG_ACTIVE_DENERVATION: "활동성 탈신경 소견",
            EMG_PARASPINAL_DENERVATION: "척추주위근 탈신경 소견",
            EMG_CHRONIC_REINNERVATION: "만성 재신경지배 소견",
            EMG_ACTIVE_CHRONIC: "활동성 탈신경과 만성 재신경지배가 함께 관찰되는 소견",
            EMG_FASCICULATION: "섬유다발수축전위 소견",
            EMG_NO_RESPONSE: "운동단위 동원 불가",
        }
    ),
)

# ui.case_learning.py에서 import하는 이름 3
special_term = globals().get(
    "special_term",
    TermLookup(
        {
            "SNAP": "감각신경활동전위입니다. 감각신경의 축삭 기능을 평가합니다.",
            "CMAP": "복합근육활동전위입니다. 운동신경과 근육 반응을 평가합니다.",
            "MUAP": "운동단위활동전위입니다. 침근전도에서 운동단위의 형태와 동원 양상을 평가합니다.",
            "Giant MUAP": "거대 운동단위활동전위입니다. 만성 재신경지배를 시사할 수 있습니다.",
            "Reduced MU recruitment": "수의수축 시 동원 가능한 운동단위 수가 감소한 상태입니다.",
            "Normal MU recruitment": "수의수축 시 운동단위 동원이 정상적으로 이루어지는 상태입니다.",
            "Silent at rest": "휴식 시 비정상 자발전위가 관찰되지 않는 상태입니다.",
            "fibrillation potential": "탈신경된 근섬유에서 나타날 수 있는 비정상 자발전위입니다.",
            "positive sharp wave": "탈신경 또는 근섬유막 불안정성과 관련된 비정상 자발전위입니다.",
            "Conduction block": "국소 부위에서 신경 자극 전달이 차단되는 소견입니다.",
            "F-wave": "말초신경의 근위부 전도 이상 평가에 도움이 되는 후기 반응입니다.",
            "H-reflex": "S1 반사경로와 척수반사 흥분성 평가에 활용되는 검사입니다.",
            "Blink reflex": "삼차신경, 뇌줄기, 얼굴신경을 포함하는 반사경로 평가입니다.",
        }
    ),
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
        "척추주위근 탈신경": EMG_PARASPINAL_DENERVATION,
        "만성 재신경지배": EMG_CHRONIC_REINNERVATION,
        "활동성 만성": EMG_ACTIVE_CHRONIC,
        "활동성 탈신경과 만성 재신경지배": EMG_ACTIVE_CHRONIC,
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
        "저하",
        "지연",
        "소실",
        "무반응",
        "전도차단",
        "탈신경",
        "재신경지배",
        "동원 불가",
        "항진",
        "증가",
        "Reduced",
        "Delayed",
        "Absent",
        "No response",
        "Conduction block",
        "denervation",
        "reinnervation",
        "hyperactive",
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
