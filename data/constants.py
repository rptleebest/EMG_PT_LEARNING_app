# data/constants.py

MODE_CASE = "사례 학습"
MODE_DIRECT = "가상 결과표 판독 학습"

# -------------------------------------------------------------------
# 공통 결과 옵션 (학생 교육용 한글/영문 병기 및 가이드)
# -------------------------------------------------------------------
RESULT_OPTION_NONE = "미선택"
RESULT_NORMAL = "정상 범위(within normal limits)"

# NCS
RESULT_DELAYED = "잠복기 지연 (Delayed latency) - 정상 대비 130% 이상 초과"
RESULT_REDUCED = "진폭 감소 (Reduced amplitude) - 정상 대비 50% 이하 감소"
RESULT_CONDUCTION_BLOCK = "전도차단 (Conduction block) - 근위부/원위부 진폭 50% 이상 감소"
RESULT_ABSENT = "반응 소실 (Absent response) - 전기 자극에 무반응"
RESULT_DELAYED_OR_ABSENT = "잠복기 지연 또는 반응 소실(delayed or absent response)"

# F-wave / Blink / H-reflex
RESULT_F_WAVE_ABN = "F파 최소잠복기 지연 또는 소실(delayed or absent F-wave)"
RESULT_H_REFLEX_HYPER = "H-반사 항진 또는 문턱값 감소(hyperactive H-reflex) - 위운동신경세포 병변 시사"
RESULT_HM_RATIO_INC = "H/M 비율 증가 가능(increased H/M ratio possible)"

# EMG
RESULT_EMG_NORMAL = "휴식 시 Silent at rest (전기적 침묵) / 근수축 시 Normal MU recruitment"
RESULT_EMG_ACTIVE_DENERVATION = "휴식 시 Fibrillation 및 Positive sharp wave 출현 / 근수축 시 Reduced MU recruitment"
RESULT_EMG_CHRONIC_REINNERVATION = "휴식 시 Silent at rest / 근수축 시 Giant MUAPs 출현 및 Reduced MU recruitment"
RESULT_EMG_FASCICULATION = "휴식 시 Fasciculation potentials 출현 / 근수축 시 Reduced MU recruitment"
RESULT_EMG_NO_RESPONSE = "휴식 시 Silent at rest / 근수축 시 No MUAPs on volition (운동단위 동원 불가)"

# 기존 호환용 옵션
RESULT_OPTIONS = [
    RESULT_OPTION_NONE, RESULT_NORMAL, RESULT_DELAYED, RESULT_REDUCED, RESULT_ABSENT,
    RESULT_F_WAVE_ABN, RESULT_H_REFLEX_HYPER, RESULT_HM_RATIO_INC, RESULT_DELAYED_OR_ABSENT,
    RESULT_EMG_NORMAL, RESULT_EMG_ACTIVE_DENERVATION, RESULT_EMG_CHRONIC_REINNERVATION, RESULT_EMG_FASCICULATION, RESULT_EMG_NO_RESPONSE
]

DOMAIN_RESULT_OPTIONS = {
    "sensory": [RESULT_NORMAL, RESULT_DELAYED, RESULT_REDUCED, RESULT_ABSENT],
    "motor": [RESULT_NORMAL, RESULT_DELAYED, RESULT_REDUCED, RESULT_CONDUCTION_BLOCK, RESULT_ABSENT],
    "muscle": [RESULT_EMG_NORMAL, RESULT_EMG_ACTIVE_DENERVATION, RESULT_EMG_CHRONIC_REINNERVATION, RESULT_EMG_FASCICULATION, RESULT_EMG_NO_RESPONSE],
    "h_reflex": [RESULT_NORMAL, RESULT_DELAYED_OR_ABSENT, RESULT_H_REFLEX_HYPER],
    "h_ratio": [RESULT_NORMAL, RESULT_HM_RATIO_INC],
    "f_wave": [RESULT_NORMAL, RESULT_F_WAVE_ABN],
    "blink": [RESULT_NORMAL, RESULT_DELAYED_OR_ABSENT],
}

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

ANATOMY = {
    "정중신경 감각신경활동전위 (Median SNAP)": {"nerve": "정중신경", "level": "C6-T1", "domain": "sensory", "region": "arm"},
    "자신경 감각신경활동전위 (Ulnar SNAP)": {"nerve": "자신경", "level": "C8-T1", "domain": "sensory", "region": "arm"},
    "노신경 표재감각신경활동전위 (Superficial Radial SNAP)": {"nerve": "표재노신경", "level": "C6-C8", "domain": "sensory", "region": "arm"},
    "가쪽아래팔피부신경 감각신경활동전위 (Lateral Antebrachial Cutaneous SNAP)": {"nerve": "가쪽아래팔피부신경", "level": "C5-C6", "domain": "sensory", "region": "arm"},
    "정중신경 복합근육활동전위 (Median CMAP)": {"nerve": "정중신경", "level": "C8-T1", "domain": "motor", "region": "arm"},
    "자신경 복합근육활동전위 (Ulnar CMAP)": {"nerve": "자신경", "level": "C8-T1", "domain": "motor", "region": "arm"},
    "노신경 복합근육활동전위 (Radial CMAP)": {"nerve": "노신경", "level": "C6-C8", "domain": "motor", "region": "arm"},
    "겨드랑신경 복합근육활동전위 (Axillary CMAP)": {"nerve": "겨드랑신경", "level": "C5-C6", "domain": "motor", "region": "arm"},
    "근육피부신경 복합근육활동전위 (Musculocutaneous CMAP)": {"nerve": "근육피부신경", "level": "C5-C6", "domain": "motor", "region": "arm"},
    "짧은엄지벌림근 (Abductor Pollicis Brevis, APB)": {"nerve": "정중신경", "level": "C8-T1", "domain": "muscle", "region": "arm"},
    "첫째등쪽뼈사이근 (First Dorsal Interosseous, FDI)": {"nerve": "자신경", "level": "C8-T1", "domain": "muscle", "region": "arm"},
    "새끼벌림근 (Abductor Digiti Minimi, ADM)": {"nerve": "자신경", "level": "C8-T1", "domain": "muscle", "region": "arm"},
    "집게폄근 (Extensor Indicis Proprius, EIP)": {"nerve": "노신경", "level": "C7-C8", "domain": "muscle", "region": "arm"},
    "노쪽손목폄근 (Extensor Carpi Radialis)": {"nerve": "노신경", "level": "C6-C7", "domain": "muscle", "region": "arm"},
    "가시아래근 (Infraspinatus)": {"nerve": "어깨위신경", "level": "C5-C6", "domain": "muscle", "region": "arm"},
    "삼각근 (Deltoid)": {"nerve": "겨드랑신경", "level": "C5-C6", "domain": "muscle", "region": "arm"},
    "위팔두갈래근 (Biceps Brachii)": {"nerve": "근육피부신경", "level": "C5-C6", "domain": "muscle", "region": "arm"},
    "목 척추주위근 (Cervical Paraspinal)": {"nerve": "후지", "level": "경추 신경뿌리 수준", "domain": "muscle", "region": "arm"},
    "장딴지신경 감각신경활동전위 (Sural SNAP)": {"nerve": "장딴지신경", "level": "S1-S2", "domain": "sensory", "region": "leg"},
    "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": {"nerve": "얕은종아리신경", "level": "L5-S1", "domain": "sensory", "region": "leg"},
    "두렁신경 감각신경활동전위 (Saphenous SNAP)": {"nerve": "두렁신경", "level": "L3-L4", "domain": "sensory", "region": "leg"},
    "종아리신경 복합근육활동전위 (Peroneal CMAP)": {"nerve": "종아리신경", "level": "L4-S1", "domain": "motor", "region": "leg"},
    "정강신경 복합근육활동전위 (Tibial CMAP)": {"nerve": "정강신경", "level": "L4-S3", "domain": "motor", "region": "leg"},
    "넓적다리신경 복합근육활동전위 (Femoral CMAP)": {"nerve": "넓적다리신경", "level": "L2-L4", "domain": "motor", "region": "leg"},
    "앞정강근 (Tibialis Anterior, TA)": {"nerve": "깊은종아리신경", "level": "L4-L5", "domain": "muscle", "region": "leg"},
    "긴엄지폄근 (Extensor Hallucis Longus, EHL)": {"nerve": "깊은종아리신경", "level": "L5", "domain": "muscle", "region": "leg"},
    "긴종아리근 (Peroneus Longus)": {"nerve": "얕은종아리신경", "level": "L5-S1", "domain": "muscle", "region": "leg"},
    "가쪽넓은근 (Vastus Lateralis)": {"nerve": "넓적다리신경", "level": "L2-L4", "domain": "muscle", "region": "leg"},
    "엉덩허리근 (Iliopsoas)": {"nerve": "요신경얼기/넓적다리신경 관련", "level": "L2-L3", "domain": "muscle", "region": "leg"},
    "중간볼기근 (Gluteus Medius)": {"nerve": "위볼기신경", "level": "L5 우세", "domain": "muscle", "region": "leg"},
    "가자미근 (Soleus)": {"nerve": "정강신경", "level": "S1-S2", "domain": "muscle", "region": "leg"},
    "짧은발가락벌림근 (Abductor Digiti Minimi pedis)": {"nerve": "발바닥신경", "level": "S1-S2", "domain": "muscle", "region": "leg"},
    "허리 척추주위근 (Lumbar Paraspinal)": {"nerve": "후지", "level": "요추 신경뿌리 수준", "domain": "muscle", "region": "leg"},
    "H 반사 (좌)": {"nerve": "정강신경-S1 반사고리", "level": "S1", "domain": "h_reflex", "region": "leg"},
    "H 반사 (우)": {"nerve": "정강신경-S1 반사고리", "level": "S1", "domain": "h_reflex", "region": "leg"},
    "H/M 비율": {"nerve": "척수 반사 흥분성", "level": "척수 반사", "domain": "h_ratio", "region": "leg"},
    "정강/종아리신경 F파 (F-wave)": {"nerve": "근위부 운동신경/신경뿌리", "level": "근위부 전도", "domain": "f_wave", "region": "leg"},
    "우측 자극-우측 R1": {"nerve": "삼차-뇌줄기-안면신경 반사경로", "level": "blink reflex", "domain": "blink", "region": "face"},
    "우측 자극-우측 R2": {"nerve": "삼차-뇌줄기-안면신경 반사경로", "level": "blink reflex", "domain": "blink", "region": "face"},
    "우측 자극-좌측 R2": {"nerve": "삼차-뇌줄기-안면신경 반사경로", "level": "blink reflex", "domain": "blink", "region": "face"},
    "좌측 자극-좌측 R1": {"nerve": "삼차-뇌줄기-안면신경 반사경로", "level": "blink reflex", "domain": "blink", "region": "face"},
    "좌측 자극-좌측 R2": {"nerve": "삼차-뇌줄기-안면신경 반사경로", "level": "blink reflex", "domain": "blink", "region": "face"},
    "좌측 자극-우측 R2": {"nerve": "삼차-뇌줄기-안면신경 반사경로", "level": "blink reflex", "domain": "blink", "region": "face"},
}

SECTION_HINTS = {
    "팔 감각신경전도검사 (arm sensory NCS)": "감각신경전도 보존 여부는 신경뿌리병증과 말초신경병증 감별에 중요합니다.",
    "팔 운동신경전도검사 (arm motor NCS)": "CMAP 진폭 감소는 운동축삭 손상 가능성을 시사할 수 있습니다.",
    "팔 침근전도검사 근육 (arm needle EMG muscles)": "서로 다른 말초신경이지만 같은 분절을 공유하는 근육의 동시 침범 여부를 보세요.",
    "다리 감각신경전도검사 (leg sensory NCS)": "발처짐이나 다리 저림에서 SNAP 보존 여부는 L5 root와 종아리신경병증 감별에 유용합니다.",
    "다리 운동신경전도검사 (leg motor NCS)": "운동신경전도 이상은 원위부 말초신경 침범 여부를 판단하는 데 도움됩니다.",
    "다리 침근전도검사 근육 (leg needle EMG muscles)": "척추주위근과 중간볼기근 등 근위부 근육 침범 여부를 함께 보세요.",
    "H반사 / 경직 평가": "반사 저하/소실은 S1 근위부 경로 이상, 항진은 중추성 반사 흥분성 증가 해석에 도움됩니다.",
    "F파 검사 (F-wave study)": "원위부 전도가 비교적 보존되어도 F파 이상은 근위부 전도 이상을 시사할 수 있습니다.",
    "눈깜빡반사검사 (Blink reflex)": "자극측과 반응측을 분리해 삼차신경-뇌줄기-얼굴신경 반사경로를 해석합니다.",
}

def get_result_options_for_item(item_name: str):
    meta = ANATOMY.get(item_name, {})
    domain = meta.get("domain")
    return DOMAIN_RESULT_OPTIONS.get(domain, RESULT_OPTIONS)
