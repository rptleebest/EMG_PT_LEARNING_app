# data/anatomy.py

"""
해부학 및 검사 항목 메타데이터.

이 파일은 앱 전체에서 검사 항목을 다음 범주로 분류하기 위해 사용합니다.

domain:
- sensory: 감각신경전도검사
- motor: 운동신경전도검사
- muscle: 침근전도검사 근육
- h_reflex: H-반사
- h_ratio: H/M 비율
- f_wave: F파
- blink: 눈깜빡반사
- other: 기타

주의:
- data.constants.py에서 from data.anatomy import ANATOMY 형태로 불러옵니다.
- 따라서 이 파일이 없으면 ModuleNotFoundError가 발생합니다.
"""


ANATOMY = {
    # ------------------------------------------------------------------
    # 팔 감각신경전도검사
    # ------------------------------------------------------------------
    "정중신경 감각신경활동전위 (Median SNAP)": {
        "domain": "sensory",
        "korean": "정중신경 감각신경활동전위",
        "english": "Median sensory nerve action potential",
        "abbr": "Median SNAP",
        "nerve": "정중신경",
        "roots": "C6-C8",
        "clinical_point": "손목굴증후군, 정중신경병증, 상완신경총병증 감별에 중요합니다.",
    },
    "자신경 감각신경활동전위 (Ulnar SNAP)": {
        "domain": "sensory",
        "korean": "자신경 감각신경활동전위",
        "english": "Ulnar sensory nerve action potential",
        "abbr": "Ulnar SNAP",
        "nerve": "자신경",
        "roots": "C8-T1",
        "clinical_point": "자신경병증, 하부상완신경총병증, C8-T1 병변 감별에 사용합니다.",
    },
    "노신경 표재감각신경활동전위 (Superficial Radial SNAP)": {
        "domain": "sensory",
        "korean": "노신경 표재감각신경활동전위",
        "english": "Superficial radial sensory nerve action potential",
        "abbr": "Superficial radial SNAP",
        "nerve": "노신경 표재감각분지",
        "roots": "C6-C8",
        "clinical_point": "노신경병증, 상완신경총병증, 감각신경 보존 여부 판단에 사용합니다.",
    },
    "가쪽아래팔피부신경 감각신경활동전위 (Lateral Antebrachial Cutaneous SNAP)": {
        "domain": "sensory",
        "korean": "가쪽아래팔피부신경 감각신경활동전위",
        "english": "Lateral antebrachial cutaneous sensory nerve action potential",
        "abbr": "LAC SNAP",
        "nerve": "가쪽아래팔피부신경",
        "roots": "C5-C6",
        "clinical_point": "상부상완신경총병증과 C5-C6 신경뿌리병증 감별에 도움됩니다.",
    },
    "안쪽아래팔피부신경 감각신경활동전위 (Medial Antebrachial Cutaneous SNAP)": {
        "domain": "sensory",
        "korean": "안쪽아래팔피부신경 감각신경활동전위",
        "english": "Medial antebrachial cutaneous sensory nerve action potential",
        "abbr": "MAC SNAP",
        "nerve": "안쪽아래팔피부신경",
        "roots": "C8-T1",
        "clinical_point": "하부상완신경총병증과 C8-T1 신경뿌리병증 감별에 유용합니다.",
    },

    # ------------------------------------------------------------------
    # 팔 운동신경전도검사
    # ------------------------------------------------------------------
    "정중신경 복합근육활동전위 (Median CMAP)": {
        "domain": "motor",
        "korean": "정중신경 복합근육활동전위",
        "english": "Median compound muscle action potential",
        "abbr": "Median CMAP",
        "nerve": "정중신경",
        "roots": "C8-T1",
        "recording_muscle": "짧은엄지벌림근",
        "clinical_point": "손목굴증후군, 정중신경병증, C8-T1 병변 감별에 사용합니다.",
    },
    "자신경 복합근육활동전위 (Ulnar CMAP)": {
        "domain": "motor",
        "korean": "자신경 복합근육활동전위",
        "english": "Ulnar compound muscle action potential",
        "abbr": "Ulnar CMAP",
        "nerve": "자신경",
        "roots": "C8-T1",
        "recording_muscle": "새끼벌림근 또는 첫째등쪽뼈사이근",
        "clinical_point": "팔꿈치굴증후군, 자신경병증, 하부상완신경총병증 감별에 사용합니다.",
    },
    "노신경 복합근육활동전위 (Radial CMAP)": {
        "domain": "motor",
        "korean": "노신경 복합근육활동전위",
        "english": "Radial compound muscle action potential",
        "abbr": "Radial CMAP",
        "nerve": "노신경",
        "roots": "C6-C8",
        "recording_muscle": "손목폄근 또는 집게폄근",
        "clinical_point": "노신경병증, 뒤신경다발 병변, C7 병변 감별에 사용합니다.",
    },
    "겨드랑신경 복합근육활동전위 (Axillary CMAP)": {
        "domain": "motor",
        "korean": "겨드랑신경 복합근육활동전위",
        "english": "Axillary compound muscle action potential",
        "abbr": "Axillary CMAP",
        "nerve": "겨드랑신경",
        "roots": "C5-C6",
        "recording_muscle": "삼각근",
        "clinical_point": "겨드랑신경 손상, 상부상완신경총병증, C5-C6 병변 감별에 사용합니다.",
    },
    "근육피부신경 복합근육활동전위 (Musculocutaneous CMAP)": {
        "domain": "motor",
        "korean": "근육피부신경 복합근육활동전위",
        "english": "Musculocutaneous compound muscle action potential",
        "abbr": "Musculocutaneous CMAP",
        "nerve": "근육피부신경",
        "roots": "C5-C6",
        "recording_muscle": "위팔두갈래근",
        "clinical_point": "근육피부신경병증, C5-C6 신경뿌리병증, 상부상완신경총병증 감별에 사용합니다.",
    },

    # ------------------------------------------------------------------
    # 팔 침근전도검사 근육
    # ------------------------------------------------------------------
    "짧은엄지벌림근 (Abductor Pollicis Brevis, APB)": {
        "domain": "muscle",
        "korean": "짧은엄지벌림근",
        "english": "Abductor pollicis brevis",
        "abbr": "APB",
        "nerve": "정중신경",
        "roots": "C8-T1",
        "clinical_point": "손목굴증후군, 정중신경병증, C8-T1 병변 평가에 중요합니다.",
    },
    "첫째등쪽뼈사이근 (First Dorsal Interosseous, FDI)": {
        "domain": "muscle",
        "korean": "첫째등쪽뼈사이근",
        "english": "First dorsal interosseous",
        "abbr": "FDI",
        "nerve": "자신경",
        "roots": "C8-T1",
        "clinical_point": "자신경병증, 하부상완신경총병증, C8-T1 병변 평가에 사용합니다.",
    },
    "새끼벌림근 (Abductor Digiti Minimi, ADM)": {
        "domain": "muscle",
        "korean": "새끼벌림근",
        "english": "Abductor digiti minimi",
        "abbr": "ADM",
        "nerve": "자신경",
        "roots": "C8-T1",
        "clinical_point": "자신경병증과 하부상완신경총병증 감별에 사용합니다.",
    },
    "집게폄근 (Extensor Indicis Proprius, EIP)": {
        "domain": "muscle",
        "korean": "집게폄근",
        "english": "Extensor indicis proprius",
        "abbr": "EIP",
        "nerve": "뒤뼈사이신경/노신경",
        "roots": "C7-C8",
        "clinical_point": "노신경병증, 뒤뼈사이신경병증, C7-C8 신경뿌리병증 감별에 사용합니다.",
    },
    "노쪽손목폄근 (Extensor Carpi Radialis)": {
        "domain": "muscle",
        "korean": "노쪽손목폄근",
        "english": "Extensor carpi radialis",
        "abbr": "ECR",
        "nerve": "노신경",
        "roots": "C6-C7",
        "clinical_point": "C6-C7 신경뿌리병증과 노신경병증 감별에 사용합니다.",
    },
    "가시아래근 (Infraspinatus)": {
        "domain": "muscle",
        "korean": "가시아래근",
        "english": "Infraspinatus",
        "abbr": "ISP",
        "nerve": "어깨위신경",
        "roots": "C5-C6",
        "clinical_point": "어깨위신경병증, 상부상완신경총병증, C5-C6 병변 감별에 사용합니다.",
    },
    "삼각근 (Deltoid)": {
        "domain": "muscle",
        "korean": "삼각근",
        "english": "Deltoid",
        "abbr": "Deltoid",
        "nerve": "겨드랑신경",
        "roots": "C5-C6",
        "clinical_point": "겨드랑신경병증, C5-C6 신경뿌리병증 감별에 중요합니다.",
    },
    "위팔두갈래근 (Biceps Brachii)": {
        "domain": "muscle",
        "korean": "위팔두갈래근",
        "english": "Biceps brachii",
        "abbr": "Biceps",
        "nerve": "근육피부신경",
        "roots": "C5-C6",
        "clinical_point": "C5-C6 신경뿌리병증과 상부상완신경총병증 감별에 사용합니다.",
    },
    "목 척추주위근 (Cervical Paraspinal)": {
        "domain": "muscle",
        "korean": "목 척추주위근",
        "english": "Cervical paraspinal muscle",
        "abbr": "Cervical paraspinal",
        "nerve": "척수신경 뒤가지",
        "roots": "C5-T1",
        "clinical_point": "이 근육의 이상은 신경뿌리병증을 지지하고, 신경얼기병증과 감별하는 데 중요합니다.",
    },

    # ------------------------------------------------------------------
    # 다리 감각신경전도검사
    # ------------------------------------------------------------------
    "장딴지신경 감각신경활동전위 (Sural SNAP)": {
        "domain": "sensory",
        "korean": "장딴지신경 감각신경활동전위",
        "english": "Sural sensory nerve action potential",
        "abbr": "Sural SNAP",
        "nerve": "장딴지신경",
        "roots": "S1-S2",
        "clinical_point": "다발신경병증, 좌골신경병증, 말초 감각신경 손상 평가에 중요합니다.",
    },
    "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": {
        "domain": "sensory",
        "korean": "얕은종아리신경 감각신경활동전위",
        "english": "Superficial peroneal sensory nerve action potential",
        "abbr": "Superficial peroneal SNAP",
        "nerve": "얕은종아리신경",
        "roots": "L5-S1",
        "clinical_point": "온종아리신경병증과 L5 신경뿌리병증 감별에 중요합니다.",
    },
    "두렁신경 감각신경활동전위 (Saphenous SNAP)": {
        "domain": "sensory",
        "korean": "두렁신경 감각신경활동전위",
        "english": "Saphenous sensory nerve action potential",
        "abbr": "Saphenous SNAP",
        "nerve": "두렁신경",
        "roots": "L3-L4",
        "clinical_point": "넓적다리신경병증, L3-L4 병변 감별에 사용합니다.",
    },

    # ------------------------------------------------------------------
    # 다리 운동신경전도검사
    # ------------------------------------------------------------------
    "종아리신경 복합근육활동전위 (Peroneal CMAP)": {
        "domain": "motor",
        "korean": "종아리신경 복합근육활동전위",
        "english": "Peroneal compound muscle action potential",
        "abbr": "Peroneal CMAP",
        "nerve": "온종아리신경/깊은종아리신경",
        "roots": "L4-L5",
        "recording_muscle": "짧은발가락폄근 또는 앞정강근",
        "clinical_point": "발처짐에서 온종아리신경병증과 L5 신경뿌리병증 감별에 핵심입니다.",
    },
    "정강신경 복합근육활동전위 (Tibial CMAP)": {
        "domain": "motor",
        "korean": "정강신경 복합근육활동전위",
        "english": "Tibial compound muscle action potential",
        "abbr": "Tibial CMAP",
        "nerve": "정강신경",
        "roots": "L5-S2",
        "recording_muscle": "엄지벌림근",
        "clinical_point": "좌골신경병증, 정강신경병증, 다발신경병증 평가에 사용합니다.",
    },
    "넓적다리신경 복합근육활동전위 (Femoral CMAP)": {
        "domain": "motor",
        "korean": "넓적다리신경 복합근육활동전위",
        "english": "Femoral compound muscle action potential",
        "abbr": "Femoral CMAP",
        "nerve": "넓적다리신경",
        "roots": "L2-L4",
        "recording_muscle": "넙다리네갈래근",
        "clinical_point": "넓적다리신경병증, 허리신경얼기병증, L2-L4 병변 평가에 사용합니다.",
    },

    # ------------------------------------------------------------------
    # 다리 침근전도검사 근육
    # ------------------------------------------------------------------
    "앞정강근 (Tibialis Anterior, TA)": {
        "domain": "muscle",
        "korean": "앞정강근",
        "english": "Tibialis anterior",
        "abbr": "TA",
        "nerve": "깊은종아리신경",
        "roots": "L4-L5",
        "clinical_point": "발처짐 평가에서 L5 신경뿌리병증과 종아리신경병증 감별에 중요합니다.",
    },
    "긴엄지폄근 (Extensor Hallucis Longus, EHL)": {
        "domain": "muscle",
        "korean": "긴엄지폄근",
        "english": "Extensor hallucis longus",
        "abbr": "EHL",
        "nerve": "깊은종아리신경",
        "roots": "L5",
        "clinical_point": "L5 신경뿌리병증 평가에 중요한 근육입니다.",
    },
    "긴종아리근 (Peroneus Longus)": {
        "domain": "muscle",
        "korean": "긴종아리근",
        "english": "Peroneus longus",
        "abbr": "PL",
        "nerve": "얕은종아리신경",
        "roots": "L5-S1",
        "clinical_point": "온종아리신경병증, 얕은종아리신경병증, L5-S1 병변 감별에 사용합니다.",
    },
    "가쪽넓은근 (Vastus Lateralis)": {
        "domain": "muscle",
        "korean": "가쪽넓은근",
        "english": "Vastus lateralis",
        "abbr": "VL",
        "nerve": "넓적다리신경",
        "roots": "L2-L4",
        "clinical_point": "넓적다리신경병증, L2-L4 신경뿌리병증 평가에 사용합니다.",
    },
    "엉덩허리근 (Iliopsoas)": {
        "domain": "muscle",
        "korean": "엉덩허리근",
        "english": "Iliopsoas",
        "abbr": "Iliopsoas",
        "nerve": "허리신경얼기 가지",
        "roots": "L1-L3",
        "clinical_point": "허리신경얼기병증과 상위 요추 신경뿌리병증 평가에 사용합니다.",
    },
    "중간볼기근 (Gluteus Medius)": {
        "domain": "muscle",
        "korean": "중간볼기근",
        "english": "Gluteus medius",
        "abbr": "GMED",
        "nerve": "위볼기신경",
        "roots": "L5-S1",
        "clinical_point": "L5 신경뿌리병증과 온종아리신경병증 감별에 매우 중요합니다.",
    },
    "가자미근 (Soleus)": {
        "domain": "muscle",
        "korean": "가자미근",
        "english": "Soleus",
        "abbr": "Soleus",
        "nerve": "정강신경",
        "roots": "S1-S2",
        "clinical_point": "S1 신경뿌리병증, 정강신경병증, 좌골신경병증 평가에 사용합니다.",
    },
    "짧은발가락벌림근 (Abductor Digiti Minimi pedis)": {
        "domain": "muscle",
        "korean": "짧은발가락벌림근",
        "english": "Abductor digiti minimi pedis",
        "abbr": "ADM pedis",
        "nerve": "가쪽발바닥신경",
        "roots": "S1-S2",
        "clinical_point": "원위부 다발신경병증, 정강신경 원위부 병변 평가에 사용합니다.",
    },
    "허리 척추주위근 (Lumbar Paraspinal)": {
        "domain": "muscle",
        "korean": "허리 척추주위근",
        "english": "Lumbar paraspinal muscle",
        "abbr": "Lumbar paraspinal",
        "nerve": "척수신경 뒤가지",
        "roots": "L2-S1",
        "clinical_point": "허리 신경뿌리병증과 말초신경병증/신경얼기병증 감별에 매우 중요합니다.",
    },

    # ------------------------------------------------------------------
    # H반사 / 경직 평가
    # ------------------------------------------------------------------
    "H 반사 (좌)": {
        "domain": "h_reflex",
        "korean": "좌측 H 반사",
        "english": "Left H-reflex",
        "abbr": "Left H-reflex",
        "nerve": "정강신경-가자미근 반사경로",
        "roots": "S1",
        "clinical_point": "S1 반사경로, 말초 신경전도, 척수 반사 흥분성 평가에 사용합니다.",
    },
    "H 반사 (우)": {
        "domain": "h_reflex",
        "korean": "우측 H 반사",
        "english": "Right H-reflex",
        "abbr": "Right H-reflex",
        "nerve": "정강신경-가자미근 반사경로",
        "roots": "S1",
        "clinical_point": "S1 반사경로, 말초 신경전도, 척수 반사 흥분성 평가에 사용합니다.",
    },
    "H/M 비율": {
        "domain": "h_ratio",
        "korean": "H/M 비율",
        "english": "H/M ratio",
        "abbr": "H/M ratio",
        "nerve": "정강신경-가자미근 반사경로",
        "roots": "S1",
        "clinical_point": "경직, 척수 반사 흥분성, 중추신경계 병변 후 변화 평가에 사용합니다.",
    },

    # ------------------------------------------------------------------
    # F파 검사
    # ------------------------------------------------------------------
    "정강/종아리신경 F파 (F-wave)": {
        "domain": "f_wave",
        "korean": "정강/종아리신경 F파",
        "english": "Tibial/Peroneal F-wave",
        "abbr": "F-wave",
        "nerve": "정강신경 또는 종아리신경",
        "roots": "L4-S1",
        "clinical_point": "근위부 전도 이상, 다발신경뿌리병증, Guillain-Barre spectrum 평가에 사용합니다.",
    },

    # ------------------------------------------------------------------
    # 눈깜빡반사검사
    # ------------------------------------------------------------------
    "우측 자극-우측 R1": {
        "domain": "blink",
        "korean": "우측 자극-우측 R1",
        "english": "Right stimulation - right R1",
        "abbr": "Rt stim-Rt R1",
        "nerve": "삼차신경-뇌줄기-얼굴신경 반사경로",
        "roots": "CN V, CN VII",
        "clinical_point": "동측 짧은잠복기 반응으로 얼굴신경과 뇌줄기 반사경로 평가에 사용합니다.",
    },
    "우측 자극-우측 R2": {
        "domain": "blink",
        "korean": "우측 자극-우측 R2",
        "english": "Right stimulation - right R2",
        "abbr": "Rt stim-Rt R2",
        "nerve": "삼차신경-뇌줄기-얼굴신경 반사경로",
        "roots": "CN V, CN VII",
        "clinical_point": "동측 긴잠복기 반응으로 얼굴신경 및 뇌줄기 반사경로 평가에 사용합니다.",
    },
    "우측 자극-좌측 R2": {
        "domain": "blink",
        "korean": "우측 자극-좌측 R2",
        "english": "Right stimulation - left R2",
        "abbr": "Rt stim-Lt R2",
        "nerve": "삼차신경-뇌줄기-얼굴신경 반사경로",
        "roots": "CN V, CN VII",
        "clinical_point": "반대측 긴잠복기 반응으로 양측 뇌줄기 반사경로 평가에 사용합니다.",
    },
    "좌측 자극-좌측 R1": {
        "domain": "blink",
        "korean": "좌측 자극-좌측 R1",
        "english": "Left stimulation - left R1",
        "abbr": "Lt stim-Lt R1",
        "nerve": "삼차신경-뇌줄기-얼굴신경 반사경로",
        "roots": "CN V, CN VII",
        "clinical_point": "동측 짧은잠복기 반응으로 얼굴신경과 뇌줄기 반사경로 평가에 사용합니다.",
    },
    "좌측 자극-좌측 R2": {
        "domain": "blink",
        "korean": "좌측 자극-좌측 R2",
        "english": "Left stimulation - left R2",
        "abbr": "Lt stim-Lt R2",
        "nerve": "삼차신경-뇌줄기-얼굴신경 반사경로",
        "roots": "CN V, CN VII",
        "clinical_point": "동측 긴잠복기 반응으로 얼굴신경 및 뇌줄기 반사경로 평가에 사용합니다.",
    },
    "좌측 자극-우측 R2": {
        "domain": "blink",
        "korean": "좌측 자극-우측 R2",
        "english": "Left stimulation - right R2",
        "abbr": "Lt stim-Rt R2",
        "nerve": "삼차신경-뇌줄기-얼굴신경 반사경로",
        "roots": "CN V, CN VII",
        "clinical_point": "반대측 긴잠복기 반응으로 양측 뇌줄기 반사경로 평가에 사용합니다.",
    },
}


def get_anatomy_meta(item_name):
    """
    검사 항목명으로 해부학 메타데이터를 반환합니다.
    항목이 없으면 기본 other 값을 반환합니다.
    """
    return ANATOMY.get(
        item_name,
        {
            "domain": "other",
            "korean": str(item_name),
            "english": "",
            "abbr": "",
            "nerve": "",
            "roots": "",
            "clinical_point": "",
        },
    )


def get_domain(item_name):
    """
    검사 항목의 domain만 간단히 반환합니다.
    """
    return get_anatomy_meta(item_name).get("domain", "other")
