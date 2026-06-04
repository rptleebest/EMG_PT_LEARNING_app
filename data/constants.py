# data/constants.py

"""
앱 전역 상수.

개선 방향:
- constants.py와 anatomy.py에 ANATOMY가 중복 정의되어 있었으므로,
  해부학 정보는 data.anatomy.ANATOMY를 단일 기준으로 사용합니다.
- 사례 학습에서는 결과를 간략화해서 제시하고,
  가상 결과표 판독에서는 수치 기반 결과표를 사용하도록 구분합니다.
"""

from data.anatomy import ANATOMY

MODE_CASE = "사례 학습"
MODE_DIRECT = "가상 결과표 판독 학습"

# -------------------------------------------------------------------
# 공통 결과 옵션
# -------------------------------------------------------------------
RESULT_OPTION_NONE = "미선택"
RESULT_NORMAL = "정상 범위"

# NCS
RESULT_DELAYED = "잠복기 지연"
RESULT_REDUCED = "진폭 감소"
RESULT_CONDUCTION_BLOCK = "전도차단"
RESULT_ABSENT = "반응 소실"
RESULT_DELAYED_OR_ABSENT = "잠복기 지연 또는 반응 소실"

# F-wave / Blink / H-reflex
RESULT_F_WAVE_ABN = "F파 최소잠복기 지연 또는 소실"
RESULT_H_REFLEX_HYPER = "H-반사 항진 또는 문턱값 감소"
RESULT_HM_RATIO_INC = "H/M 비율 증가"

# EMG - 사례 학습용 간략 표기
RESULT_EMG_NORMAL = "정상 반응"
RESULT_EMG_ACTIVE_DENERVATION = "비정상 자발전위 출현 / 운동단위 동원감소"
RESULT_EMG_CHRONIC_REINNERVATION = "만성 재신경지배 소견 / 운동단위 동원감소"
RESULT_EMG_ACTIVE_CHRONIC = "비정상 자발전위 및 만성 재신경지배 소견"
RESULT_EMG_FASCICULATION = "근육다발수축전위 출현"
RESULT_EMG_NO_RESPONSE = "수의수축 시 운동단위 동원 불가"

# EMG - 실제 결과표 학습용 용어 안내
EMG_REST_NORMAL = "Silent at rest"
EMG_REST_ABNORMAL_SPONT = "fibrillation potential, positive sharp wave"
EMG_REST_FASCICULATION = "fasciculation potential"
EMG_VOL_NORMAL = "Normal MU recruitment"
EMG_VOL_REDUCED = "Reduced MU recruitment"
EMG_VOL_GIANT_REDUCED = "Giant MUAPs with reduced recruitment"
EMG_VOL_NO_MUAP = "No MUAPs on volition"

RESULT_OPTIONS = [
    RESULT_OPTION_NONE,
    RESULT_NORMAL,
    RESULT_DELAYED,
    RESULT_REDUCED,
    RESULT_CONDUCTION_BLOCK,
    RESULT_ABSENT,
    RESULT_DELAYED_OR_ABSENT,
    RESULT_F_WAVE_ABN,
    RESULT_H_REFLEX_HYPER,
    RESULT_HM_RATIO_INC,
    RESULT_EMG_NORMAL,
    RESULT_EMG_ACTIVE_DENERVATION,
    RESULT_EMG_CHRONIC_REINNERVATION,
    RESULT_EMG_ACTIVE_CHRONIC,
    RESULT_EMG_FASCICULATION,
    RESULT_EMG_NO_RESPONSE,
]

DOMAIN_RESULT_OPTIONS = {
    "sensory": [
        RESULT_NORMAL,
        RESULT_DELAYED,
        RESULT_REDUCED,
        RESULT_ABSENT,
    ],
    "motor": [
        RESULT_NORMAL,
        RESULT_DELAYED,
        RESULT_REDUCED,
        RESULT_CONDUCTION_BLOCK,
        RESULT_ABSENT,
    ],
    "muscle": [
        RESULT_EMG_NORMAL,
        RESULT_EMG_ACTIVE_DENERVATION,
        RESULT_EMG_CHRONIC_REINNERVATION,
        RESULT_EMG_ACTIVE_CHRONIC,
        RESULT_EMG_FASCICULATION,
        RESULT_EMG_NO_RESPONSE,
    ],
    "h_reflex": [
        RESULT_NORMAL,
        RESULT_DELAYED_OR_ABSENT,
        RESULT_H_REFLEX_HYPER,
    ],
    "h_ratio": [
        RESULT_NORMAL,
        RESULT_HM_RATIO_INC,
    ],
    "f_wave": [
        RESULT_NORMAL,
        RESULT_F_WAVE_ABN,
    ],
    "blink": [
        RESULT_NORMAL,
        RESULT_DELAYED_OR_ABSENT,
    ],
}

# -------------------------------------------------------------------
# 검사 섹션
# -------------------------------------------------------------------
SECTIONS = {
    "팔 감각신경전도검사 (arm sensory NCS)": [
        "정중신경 감각신경활동전위 (Median SNAP)",
        "자신경 감각신경활동전위 (Ulnar SNAP)",
        "노신경 표재감각신경활동전위 (Superficial Radial SNAP)",
        "가쪽아래팔피부신경 감각신경활동전위 (Lateral Antebrachial Cutaneous SNAP)",
    ],
    "팔 운동신경전도검사 (arm motor NCS)": [
        "정중신경 복합근육활동전위 (Median CMAP)",
        "자신경 복합근육활동전위 (Ulnar CMAP)",
        "노신경 복합근육활동전위 (Radial CMAP)",
        "겨드랑신경 복합근육활동전위 (Axillary CMAP)",
        "근육피부신경 복합근육활동전위 (Musculocutaneous CMAP)",
    ],
    "팔 침근전도검사 근육 (arm needle EMG muscles)": [
        "짧은엄지벌림근 (Abductor Pollicis Brevis, APB)",
        "첫째등쪽뼈사이근 (First Dorsal Interosseous, FDI)",
        "새끼벌림근 (Abductor Digiti Minimi, ADM)",
        "집게폄근 (Extensor Indicis Proprius, EIP)",
        "노쪽손목폄근 (Extensor Carpi Radialis)",
        "가시아래근 (Infraspinatus)",
        "삼각근 (Deltoid)",
        "위팔두갈래근 (Biceps Brachii)",
        "목 척추주위근 (Cervical Paraspinal)",
    ],
    "다리 감각신경전도검사 (leg sensory NCS)": [
        "장딴지신경 감각신경활동전위 (Sural SNAP)",
        "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)",
        "두렁신경 감각신경활동전위 (Saphenous SNAP)",
    ],
    "다리 운동신경전도검사 (leg motor NCS)": [
        "종아리신경 복합근육활동전위 (Peroneal CMAP)",
        "정강신경 복합근육활동전위 (Tibial CMAP)",
        "넓적다리신경 복합근육활동전위 (Femoral CMAP)",
    ],
    "다리 침근전도검사 근육 (leg needle EMG muscles)": [
        "앞정강근 (Tibialis Anterior, TA)",
        "긴엄지폄근 (Extensor Hallucis Longus, EHL)",
        "긴종아리근 (Peroneus Longus)",
        "가쪽넓은근 (Vastus Lateralis)",
        "엉덩허리근 (Iliopsoas)",
        "중간볼기근 (Gluteus Medius)",
        "가자미근 (Soleus)",
        "짧은발가락벌림근 (Abductor Digiti Minimi pedis)",
        "허리 척추주위근 (Lumbar Paraspinal)",
    ],
    "H반사 / 경직 평가": [
        "H 반사 (좌)",
        "H 반사 (우)",
        "H/M 비율",
    ],
    "F파 검사 (F-wave study)": [
        "정강/종아리신경 F파 (F-wave)",
    ],
    "눈깜빡반사검사 (Blink reflex)": [
        "우측 자극-우측 R1",
        "우측 자극-우측 R2",
        "우측 자극-좌측 R2",
        "좌측 자극-좌측 R1",
        "좌측 자극-좌측 R2",
        "좌측 자극-우측 R2",
    ],
}

SECTION_HINTS = {
    "팔 감각신경전도검사 (arm sensory NCS)": "감각신경전도 보존 여부는 신경뿌리병증과 말초신경병증 감별에 중요합니다.",
    "팔 운동신경전도검사 (arm motor NCS)": "CMAP 진폭 감소는 운동축삭 손상 가능성을 시사합니다.",
    "팔 침근전도검사 근육 (arm needle EMG muscles)": "서로 다른 말초신경이지만 같은 척수 분절을 공유하는 근육의 동시 침범 여부를 확인합니다.",
    "다리 감각신경전도검사 (leg sensory NCS)": "발처짐 또는 다리 저림에서 SNAP 보존 여부는 L5 신경뿌리병증과 종아리신경병증 감별에 유용합니다.",
    "다리 운동신경전도검사 (leg motor NCS)": "운동신경전도 이상은 원위부 말초신경 침범 여부 판단에 도움됩니다.",
    "다리 침근전도검사 근육 (leg needle EMG muscles)": "척추주위근과 근위부 근육 침범 여부를 함께 보면 신경뿌리병증 감별이 쉬워집니다.",
    "H반사 / 경직 평가": "H-반사 지연/소실은 말초 S1 경로 이상, 항진은 중추성 반사 흥분성 증가 해석에 도움됩니다.",
    "F파 검사 (F-wave study)": "원위부 전도가 보존되어도 F파 이상은 근위부 전도 이상을 시사할 수 있습니다.",
    "눈깜빡반사검사 (Blink reflex)": "자극측과 반응측을 분리해 삼차신경-뇌줄기-얼굴신경 반사경로를 해석합니다.",
}


def get_result_options_for_item(item_name: str):
    meta = ANATOMY.get(item_name, {})
    domain = meta.get("domain")
    return DOMAIN_RESULT_OPTIONS.get(domain, RESULT_OPTIONS)
