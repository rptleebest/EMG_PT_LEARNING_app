# data/report_terms.py

"""
가상 검사결과표의 한글 신용어 모드와 실제 검사결과표 영문 모드 전환을 위한 용어 사전.

이 파일의 역할:
- 검사표 출력 모드 정의
- 한글/영문 헤더 제공
- 표 내부의 짧은 의학 용어를 영문으로 변환
"""

REPORT_LANG_KO = "한글 모드"
REPORT_LANG_EN = "실제 검사결과표 영문 모드"

LANGUAGE_OPTIONS = [
    REPORT_LANG_KO,
    REPORT_LANG_EN,
]


def normalize_report_language(language: str) -> str:
    """
    검사결과표 출력 언어 모드를 표준화합니다.
    """
    if language == REPORT_LANG_EN:
        return REPORT_LANG_EN

    return REPORT_LANG_KO


REPORT_TRANSLATION_PAIRS = [
    # ------------------------------------------------------------
    # 방향/측
    # ------------------------------------------------------------
    ("오른쪽", "Right"),
    ("왼쪽", "Left"),
    ("양측", "Bilateral"),
    ("양쪽", "Bilateral"),

    # ------------------------------------------------------------
    # 신경
    # ------------------------------------------------------------
    ("가쪽아래팔피부신경", "Lateral antebrachial cutaneous nerve"),
    ("안쪽아래팔피부신경", "Medial antebrachial cutaneous nerve"),
    ("얕은종아리신경", "Superficial peroneal nerve"),
    ("장딴지신경", "Sural nerve"),
    ("온종아리신경", "Common peroneal nerve"),
    ("종아리신경", "Peroneal nerve"),
    ("정강신경", "Tibial nerve"),
    ("정중신경", "Median nerve"),
    ("자신경", "Ulnar nerve"),
    ("노신경", "Radial nerve"),
    ("얼굴신경", "Facial nerve"),
    ("겨드랑신경", "Axillary nerve"),
    ("근육피부신경", "Musculocutaneous nerve"),
    ("넓적다리신경", "Femoral nerve"),

    # ------------------------------------------------------------
    # 자극 위치
    # ------------------------------------------------------------
    ("이마 자극", "Forehead stimulation"),
    ("손목 자극", "Wrist stimulation"),
    ("팔꿈치 자극", "Elbow stimulation"),
    ("종아리뼈머리 자극", "Fibular head stimulation"),
    ("손목", "Wrist"),
    ("팔꿈치", "Elbow"),
    ("아래팔", "Forearm"),
    ("발목", "Ankle"),
    ("오금", "Popliteal fossa"),
    ("종아리뼈머리", "Fibular head"),
    ("코근", "Nasalis"),

    # ------------------------------------------------------------
    # 근육
    # ------------------------------------------------------------
    ("위팔두갈래근", "Biceps brachii"),
    ("위팔세갈래근", "Triceps brachii"),
    ("긴노쪽손목폄근", "Extensor carpi radialis longus"),
    ("노쪽손목폄근", "Extensor carpi radialis"),
    ("손목굽힘근", "Flexor carpi radialis"),
    ("짧은엄지벌림근", "Abductor pollicis brevis"),
    ("첫째등쪽뼈사이근", "First dorsal interosseous"),
    ("새끼벌림근", "Abductor digiti minimi"),
    ("집게폄근", "Extensor indicis proprius"),
    ("가시아래근", "Infraspinatus"),
    ("삼각근", "Deltoid"),
    ("앞정강근", "Tibialis anterior"),
    ("긴엄지폄근", "Extensor hallucis longus"),
    ("긴종아리근", "Peroneus longus"),
    ("가쪽넓은근", "Vastus lateralis"),
    ("엉덩허리근", "Iliopsoas"),
    ("중간볼기근", "Gluteus medius"),
    ("가자미근", "Soleus"),
    ("장딴지근", "Gastrocnemius"),
    ("짧은발가락벌림근", "Abductor digiti minimi pedis"),
    ("목 척추주위근", "Cervical paraspinal"),
    ("허리 척추주위근", "Lumbar paraspinal"),
    ("눈둘레근", "Orbicularis oculi"),

    # ------------------------------------------------------------
    # 검사 판정/상태
    # ------------------------------------------------------------
    ("정상 범위", "Within normal limits"),
    ("잠복기: 지연", "Latency: delayed"),
    ("진폭: 감소", "Amplitude: reduced"),
    ("반응 소실", "Absent response"),
    ("무반응", "No response"),
    ("국소 전도차단", "Focal conduction block"),
    ("전도차단", "Conduction block"),
    ("전도속도 급감", "Marked conduction slowing"),
    ("비정상", "Abnormal"),
    ("정상", "Normal"),
    ("활동성 탈신경", "Active denervation"),
    ("만성 재신경지배 동반", "Chronic reinnervation"),
    ("대칭적 말초 축삭 퇴행", "Symmetric distal axonal degeneration"),
    ("손 내재근 위축", "Intrinsic hand muscle atrophy"),
    ("손 양상", "Hand pattern"),
    ("동원 감소", "Reduced recruitment"),
    ("동원 결손", "Recruitment deficit"),
    ("전도 완전 마비", "Complete conduction failure"),
    ("통증으로 인해 평가불가", "Not assessable due to pain"),

    # ------------------------------------------------------------
    # EMG 용어
    # ------------------------------------------------------------
    ("섬유자발전위", "Fibrillation potential"),
    ("미세섬유전위", "Fibrillation potential"),
    ("양성예파", "Positive sharp wave"),
    ("출현", "Present"),
    ("휴식 시", "At rest"),
    ("수의수축", "Volition"),
    ("동원 불가", "No recruitment"),

    # ------------------------------------------------------------
    # 진단명 일부
    # ------------------------------------------------------------
    ("손목굴증후군", "Carpal tunnel syndrome"),
    ("목 신경뿌리병증", "Cervical radiculopathy"),
    ("허리 신경뿌리병증", "Lumbar radiculopathy"),
    ("온종아리신경 마비", "Common peroneal neuropathy"),
    ("다발신경병증", "Polyneuropathy"),
    ("얼굴신경마비", "Facial neuropathy"),
    ("특발성 얼굴신경마비", "Bell palsy"),
    ("가슴문증후군", "Thoracic outlet syndrome"),
]


def translate_term(value, language: str) -> str:
    """
    단일 문자열을 선택된 검사결과표 언어 모드에 맞게 변환합니다.

    - 한글 모드: 원문 그대로 반환
    - 영문 모드: 표 내부 짧은 용어 중심으로 변환
    """
    language = normalize_report_language(language)
    text = str(value)

    if language == REPORT_LANG_KO:
        return text

    converted = text

    for korean, english in REPORT_TRANSLATION_PAIRS:
        converted = converted.replace(korean, english)

    return converted


def translate_row(row: list, language: str) -> list:
    """
    표의 한 행을 선택 언어에 맞게 변환합니다.
    """
    return [translate_term(item, language) for item in row]


def translate_rows(rows: list, language: str) -> list:
    """
    표 전체 행을 선택 언어에 맞게 변환합니다.
    """
    if not rows:
        return []

    return [translate_row(row, language) for row in rows]


def get_report_headers(section: str, language: str) -> list:
    """
    검사결과표 섹션별 헤더를 반환합니다.
    """
    language = normalize_report_language(language)

    if section == "sensory":
        if language == REPORT_LANG_EN:
            return [
                "Nerve",
                "Amplitude",
                "Latency",
                "Interpretation",
            ]

        return [
            "검사 신경",
            "진폭 수치",
            "잠복기 수치",
            "판단",
        ]

    if section == "motor":
        if language == REPORT_LANG_EN:
            return [
                "Nerve",
                "Stimulation site",
                "Amplitude",
                "Latency",
                "Interpretation",
            ]

        return [
            "검사 신경",
            "자극 위치",
            "진폭 수치",
            "잠복기 수치",
            "판단",
        ]

    if section == "emg":
        if language == REPORT_LANG_EN:
            return [
                "Muscle",
                "Root / Segment",
                "Rest",
                "Volition",
                "Interpretation",
            ]

        return [
            "검사 근육",
            "해당 분절",
            "휴식 시 반응",
            "수의수축 시 반응",
            "판단",
        ]

    return []
