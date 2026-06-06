# data/virtual_reports.py

"""
가상 검사결과표 해석 모드에서 사용하는 데이터와 변환 유틸리티.

역할:
- VIRTUAL_REPORTS 사례 데이터 보관
- 한글 신용어 모드 / 실제 검사결과표 영문 모드 전환
- 검사표 헤더, 섹션명, 행 변환 제공
"""

from data.report_terms import (
    REPORT_LANG_KO,
    REPORT_LANG_EN,
    LANGUAGE_OPTIONS,
    normalize_report_language,
    translate_term,
    translate_row,
    translate_rows,
    get_report_headers,
)


REPORT_TITLE_KO = "가상 검사결과표"
REPORT_TITLE_EN = "Virtual EMG Report"

REPORT_SUBTITLE_KO = "한글 신용어 기본 모드"
REPORT_SUBTITLE_EN = "English mode for actual EMG report"

REPORT_SECTIONS = [
    "sensory",
    "motor",
    "emg",
]


VIRTUAL_REPORTS = {
    "왼쪽 목/어깨 통증 및 팔 저림 (C6 신경뿌리병증 의심)": {
        "info": {
            "age": 45,
            "sex": "남성",
            "symptom": "왼쪽 목 통증 및 무감각, 엄지/검지 손가락 끝 저림, 팔꿉관절 굽힘력 감소",
            "side": "왼쪽",
        },
        "diagnosis": "왼쪽 C6 목 신경뿌리병증",
        "ncs_sensory": [
            ["정중신경 (Median SNAP)", "25 μV", "2.8 ms", "정상 범위"],
            ["자신경 (Ulnar SNAP)", "22 μV", "2.5 ms", "정상 범위"],
        ],
        "ncs_motor": [
            ["정중신경 (Median CMAP)", "손목 자극", "8.5 mV", "3.5 ms", "정상 범위"],
            ["정중신경 (Median CMAP)", "팔꿈치 자극", "8.1 mV", "7.8 ms", "정상 범위"],
        ],
        "emg": [
            [
                "위팔두갈래근 (Biceps brachii)",
                "C5-C6",
                "fibrillation potential, positive sharp wave",
                "Reduced MU recruitment",
                "비정상 (활동성 탈신경)",
            ],
            [
                "긴노쪽손목폄근 (ECRL)",
                "C6-C7",
                "fibrillation potential, positive sharp wave",
                "Giant MUAPs 출현 및 Reduced MU recruitment",
                "비정상 (만성 재신경지배 동반)",
            ],
            [
                "짧은엄지벌림근 (APB)",
                "C8-T1",
                "Silent at rest",
                "Normal MU recruitment",
                "정상 범위",
            ],
            [
                "목 척추주위근 (Cervical paraspinal)",
                "C6",
                "fibrillation potential, positive sharp wave",
                "통증으로 인해 평가불가",
                "비정상 (활동성 탈신경)",
            ],
        ],
        "interpretation": [
            "감각신경활동전위가 정상 범위로 보존되어 병변이 뒤뿌리신경절보다 몸쪽의 신경뿌리 수준에 있음을 시사합니다.",
            "C6 분절 지배 근육과 목 척추주위근에서 활동성 탈신경 소견이 관찰되어 C6 목 신경뿌리병증에 합당합니다.",
        ],
        "emg_meaning": [
            "fibrillation potential, positive sharp wave: 탈신경된 근섬유막의 전기적 불안정성을 의미합니다.",
            "Reduced MU recruitment: 수의수축 시 동원 가능한 운동단위 수가 감소한 상태입니다.",
        ],
        "ddx": "목 디스크 또는 추간공 협착 여부를 확인하기 위해 목 MRI와 임상 진찰 소견을 함께 비교해야 합니다.",
    },

    "오른쪽 1~3번째 손가락 저림 및 야간통 (손목굴증후군 의심)": {
        "info": {
            "age": 52,
            "sex": "여성",
            "symptom": "오른쪽 1, 2, 3번째 손가락 저림, 야간 통증 및 손목 굽힘 시 증상 악화",
            "side": "오른쪽",
        },
        "diagnosis": "오른쪽 손목굴증후군",
        "ncs_sensory": [
            ["정중신경 (Median SNAP)", "8 μV", "4.8 ms", "진폭: 감소 / 잠복기: 지연"],
            ["자신경 (Ulnar SNAP)", "25 μV", "2.6 ms", "정상 범위"],
        ],
        "ncs_motor": [
            ["정중신경 (Median CMAP)", "손목", "3.1 mV", "5.5 ms", "진폭: 감소 / 잠복기: 지연"],
            ["정중신경 (Median CMAP)", "팔꿈치 자극", "2.9 mV", "9.8 ms", "진폭: 감소"],
        ],
        "emg": [
            ["짧은엄지벌림근 (APB)", "C8-T1", "Silent at rest", "Normal MU recruitment", "정상 범위"],
            ["첫째등쪽뼈사이근 (FDI)", "C8-T1", "Silent at rest", "Normal MU recruitment", "정상 범위"],
        ],
        "interpretation": [
            "정중신경 감각 및 운동 전도에서 잠복기 지연이 관찰되어 손목굴 부위 국소 압박성 말이집탈락 병변을 시사합니다.",
            "정중신경 진폭 감소가 동반되어 축삭 손상 가능성도 함께 고려해야 합니다.",
        ],
        "emg_meaning": [
            "Silent at rest: 휴식 시 비정상 자발전위가 관찰되지 않는 상태입니다.",
            "Normal MU recruitment: 수의수축 시 운동단위 동원이 정상적으로 이루어지는 상태입니다.",
        ],
        "ddx": "목 신경뿌리병증과 감별하기 위해 신경학적 진찰, 티넬 징후, 팔렌 검사 등을 함께 확인해야 합니다.",
    },

    "왼쪽 허리 통증 및 엄지발가락 올림 약화 (L5 신경뿌리병증 의심)": {
        "info": {
            "age": 58,
            "sex": "여성",
            "symptom": "왼쪽 허리통증, 종아리 가쪽 및 발등 통증, 발목 등굽힘 약화로 발끝 끌림",
            "side": "왼쪽",
        },
        "diagnosis": "왼쪽 L5 허리 신경뿌리병증",
        "ncs_sensory": [
            ["얕은종아리신경 (Superficial peroneal SNAP)", "12 μV", "2.9 ms", "정상 범위"],
            ["장딴지신경 (Sural SNAP)", "15 μV", "3.1 ms", "정상 범위"],
        ],
        "ncs_motor": [
            ["종아리신경 (Peroneal CMAP)", "발목", "3.5 mV", "4.5 ms", "정상 범위"],
            ["종아리신경 (Peroneal CMAP)", "오금", "3.3 mV", "11.2 ms", "정상 범위"],
        ],
        "emg": [
            ["앞정강근 (Tibialis anterior)", "L4-L5", "fibrillation potential, positive sharp wave", "Reduced MU recruitment", "비정상 (활동성 탈신경)"],
            ["긴종아리근 (Peroneus longus)", "L5-S1", "fibrillation potential, positive sharp wave", "Giant MUAPs 출현 및 Reduced MU recruitment", "비정상 (만성 재신경지배 동반)"],
            ["가자미근 (Soleus)", "S1-S2", "Silent at rest", "Normal MU recruitment", "정상 범위"],
            ["허리 척추주위근 (Lumbar paraspinal)", "L5", "fibrillation potential, positive sharp wave", "통증으로 인해 평가불가", "비정상 (활동성 탈신경)"],
        ],
        "interpretation": [
            "다리의 표재 감각신경활동전위가 보존되어 병변이 뒤뿌리신경절보다 몸쪽의 허리 신경뿌리 수준에 있음을 시사합니다.",
            "L5 지배 근육과 허리 척추주위근에서 탈신경 소견이 동반되어 L5 허리 신경뿌리병증에 합당합니다.",
        ],
        "emg_meaning": [
            "Giant MUAP: 과거 축삭 손상 후 재신경지배가 진행되었음을 시사하는 만성 신경성 변화입니다.",
        ],
        "ddx": "L4-L5 또는 L5-S1 추간판 병변 확인을 위해 허리엉치 MRI와 임상 증상 비교가 필요합니다.",
    },

    "오른쪽 발처짐 및 종아리 가쪽 감각 저하 (온종아리신경 마비 의심)": {
        "info": {
            "age": 32,
            "sex": "남성",
            "symptom": "오랫동안 다리를 꼬고 앉은 뒤 오른쪽 발목 등굽힘 불능 및 보행 시 발처짐",
            "side": "오른쪽",
        },
        "diagnosis": "오른쪽 온종아리신경 마비",
        "ncs_sensory": [
            ["얕은종아리신경 (Superficial peroneal SNAP)", "4 μV", "3.8 ms", "진폭: 감소 / 잠복기: 지연"],
            ["장딴지신경 (Sural SNAP)", "16 μV", "3.0 ms", "정상 범위"],
        ],
        "ncs_motor": [
            ["종아리신경 (Peroneal CMAP)", "발목", "4.5 mV", "4.8 ms", "정상 범위"],
            ["종아리신경 (Peroneal CMAP)", "종아리뼈머리 자극", "1.1 mV", "무반응", "진폭: 감소 (국소 전도차단)"],
        ],
        "emg": [
            ["앞정강근 (Tibialis anterior)", "L4-L5", "Silent at rest", "No MUAPs on volition", "비정상 (전도 완전 마비)"],
            ["긴종아리근 (Peroneus longus)", "L5-S1", "Silent at rest", "Reduced MU recruitment", "비정상 (동원 감소)"],
            ["허리 척추주위근 (Lumbar paraspinal)", "L5", "Silent at rest", "Normal MU recruitment", "정상 범위"],
        ],
        "interpretation": [
            "종아리뼈머리 부위 자극에서 복합근육활동전위 진폭 감소가 관찰되어 국소 전도차단을 시사합니다.",
            "허리 척추주위근이 정상으로 보존되어 L5 신경뿌리병증보다는 말초 온종아리신경 병변에 합당합니다.",
        ],
        "emg_meaning": [
            "Conduction block: 축삭이 완전히 소실되지 않았더라도 국소 압박으로 전기 자극 전달이 차단된 상태입니다.",
        ],
        "ddx": "보행 보조기, 압박 회피, 종아리뼈머리 부위 외부 압박 요인 제거가 중요합니다.",
    },

    "양측 발끝 저림 및 감각 저하 (당뇨병성 다발신경병증 의심)": {
        "info": {
            "age": 68,
            "sex": "남성",
            "symptom": "양 발바닥의 대칭적인 저림, 화끈거림, 무감각",
            "side": "양측",
        },
        "diagnosis": "길이의존성 축삭성 다발신경병증",
        "ncs_sensory": [
            ["장딴지신경 (Sural SNAP) 오른쪽", "무반응", "무반응", "반응 소실"],
            ["정중신경 (Median SNAP) 오른쪽", "18 μV", "3.4 ms", "정상 범위"],
        ],
        "ncs_motor": [
            ["정강신경 (Tibial CMAP) 오른쪽", "발목", "1.5 mV", "6.2 ms", "진폭: 감소 / 잠복기: 지연"],
            ["정강신경 (Tibial CMAP) 오른쪽", "오금", "1.2 mV", "15.2 ms", "진폭: 감소"],
        ],
        "emg": [
            ["앞정강근 (Tibialis anterior)", "L4-L5", "fibrillation potential, positive sharp wave", "Reduced MU recruitment", "비정상 (대칭적 말초 축삭 퇴행)"],
            ["위팔두갈래근 (Biceps brachii)", "C5-C6", "Silent at rest", "Normal MU recruitment", "정상 범위"],
        ],
        "interpretation": [
            "먼쪽 감각신경인 장딴지신경 반응 소실이 관찰되어 길이의존성 축삭 손상을 시사합니다.",
            "상지보다 하지의 먼쪽 신경에서 이상이 두드러져 당뇨병성 다발신경병증 양상에 합당합니다.",
        ],
        "emg_meaning": [
            "Dying-back pattern: 신경 세포체에서 먼 축삭 말단부터 퇴행하는 길이의존성 축삭 손상 양상입니다.",
        ],
        "ddx": "혈당 조절 상태, 당화혈색소, 비타민 결핍, 신장기능 등을 함께 평가해야 합니다.",
    },

    "팔다리 대칭성 근력 저하 (급성 기얭-바레 증후군 의심)": {
        "info": {"age": 41, "sex": "여성", "symptom": "가벼운 장염을 앓고 난 뒤 2주 후부터 대칭적으로 무릎 이하 다리 근력이 빠지고 위쪽으로 상행하는 양상", "side": "양측"},
        "diagnosis": "급성 염증성 탈말이집성 다발신경뿌리병증(Guillain-Barre Syndrome, GBS)",
        "ncs_sensory": [["정중신경 (Median SNAP)", "22 μV", "3.8 ms", "잠복기: 지연"], ["장딴지신경 (Sural SNAP)", "12 μV", "3.4 ms", "정상 범위 (Sural Sparing)"]],
        "ncs_motor": [["종아리신경 (Peroneal CMAP)", "발목", "3.0 mV", "8.5 ms", "잠복기: 지연"], ["종아리신경 (Peroneal CMAP)", "종아리뼈머리 자극", "1.2 mV", "20.1 ms", "잠복기: 지연 / 전도속도 급감"]],
        "emg": [["앞정강근 (Tibialis Anterior)", "L4-L5", "Silent at rest", "Reduced MU recruitment", "비정상 (동원 결손)"], ["허리 척추주위근 (Lumbar Paraspinal)", "L5", "Silent at rest", "통증으로 인해 평가불가", "정상 범위"]],
        "interpretation": [
            "다수의 다리 전도 속도가 폭락하고 전달 잠복기가 130% 이상 대폭 늘어난 대칭 말이집탈락(Demyelination)성 이상 전도를 나타냅니다.",
            "감각신경활동전위(SNAP)는 정상 범위로 생존하면서 오직 운동 신경 복합근육활동전위(CMAP)만 크게 지연되는 기얭-바레 증후군의 전형적인 장딴지 보존(Sural sparing) 양상을 만족합니다."
        ],
        "emg_meaning": [
            "Sural sparing effect: 자가면역 말이집 손상 시 다리 말단 감각인 장딴지 감각신경활동전위 반응이 홀로 정상 유지되는 전형적 기얭-바레 증후군(Guillain-Barre syndrome, GBS) 판독 감별점입니다."
        ],
        "ddx": "급성 상행성 호흡 마비 유무 모니터링을 위해 호흡기 치료 연계 관리가 필수적입니다."
    },
  
    "오른쪽 팔꿈치 통증 및 손가락 힘 빠짐 (C7 신경뿌리병증 의심)": {
        "info": {"age": 49, "sex": "여성", "symptom": "오른쪽 어깨 뒤부터 삼두근 부위를 지나 가운데 손가락으로 전개되는 통증 및 팔꿉관절 폄(Extension) 근력저하", "side": "오른쪽"},
        "diagnosis": "오른쪽 C7 목 신경뿌리병증(Cervical radiculopathy)",
        "ncs_sensory": [["정중신경 (Median SNAP)", "28 μV", "2.9 ms", "정상 범위"], ["자신경 (Ulnar SNAP)", "24 μV", "2.4 ms", "정상 범위"]],
        "ncs_motor": [["정중신경 (Median CMAP)", "손목", "9.2 mV", "3.6 ms", "정상 범위"], ["노신경 (Radial CMAP)", "아래팔", "6.5 mV", "2.8 ms", "정상 범위"]],
        "emg": [
            ["위팔세갈래근 (Triceps brachii)", "C7-C8", "fibrillation potential, positive sharp wave", "Reduced MU recruitment", "비정상 (활동성 탈신경)"],
            ["손목굽힘근 (Flexor carpi radialis)", "C6-C7", "fibrillation potential, positive sharp wave", "Reduced MU recruitment", "비정상 (활동성 탈신경)"],
            ["위팔두갈래근 (Biceps brachii)", "C5-C6", "Silent at rest", "Normal MU recruitment", "정상 범위"],
            ["목 척추주위근 (Cervical Paraspinal)", "C7", "fibrillation potential, positive sharp wave", "통증으로 인해 평가불가", "비정상 (활동성 탈신경)"]
        ],
        "interpretation": [
            "가운데 손가락 저림 부위에도 불구하고 정중신경 감각신경활동전위(SNAP)가 정상 범위인 것은 뒤뿌리신경절보다 몸쪽 목 신경뿌리 부위 병소임을 지지합니다.",
            "C7 지배 운동 영역의 핵심 축을 이루는 복수 근육들 및 제 7 척추 목 수준의 목 척추주위근육에서 일치된 탈신경 비정상 자발전위가 검출되어 C7 목 신경뿌리병증으로 확정됩니다."
        ],
        "emg_meaning": [
            "C7 Myotome mapping: 다른 말초 주행 경로를 가졌으나 오직 C7 분절 신경뿌리를 기원으로 묶이는 복수 표적근에서 동시 탈신경을 의미하는 비정상적인 자발전위가 나오는 기법입니다."
        ],
        "ddx": "위팔세갈래근 반사(Triceps reflex) 감퇴 여부를 검증하고 목 MRI를 통한 제6-7번 목 척추 추간판 유착 확인을 연계합니다."
    },
    
    "S1 신경뿌리병증 의심 사례": {
        "info": {"age": 53, "sex": "남성", "symptom": "왼쪽 허리통증(Lumbago), 왼쪽 볼기에서 허벅지 뒤편을 관통하여 발등 가쪽 및 새끼발가락으로 흐르는 칼로 찌르는 듯한 통증", "side": "왼쪽"},
        "diagnosis": "왼쪽 S1 허리 신경뿌리병증(Lumbar radiculopathy)",
        "ncs_sensory": [["장딴지신경 (Sural SNAP)", "14 μV", "3.0 ms", "정상 범위"], ["얕은종아리신경 (Superficial Peroneal SNAP)", "11 μV", "2.8 ms", "정상 범위"]],
        "ncs_motor": [["정강신경 (Tibial CMAP)", "발목", "5.8 mV", "4.2 ms", "정상 범위"], ["종아리신경 (Peroneal CMAP)", "발목", "4.8 mV", "4.5 ms", "정상 범위"]],
        "emg": [
            ["가자미근 (Soleus)", "S1-S2", "fibrillation potential, positive sharp wave", "Reduced MU recruitment", "비정상 (활동성 탈신경)"],
            ["장딴지근 (Gastrocnemius)", "S1-S2", "fibrillation potential, positive sharp wave", "Reduced MU recruitment", "비정상 (활동성 탈신경)"],
            ["앞정강근 (Tibialis Anterior)", "L4-L5", "Silent at rest", "Normal MU recruitment", "정상 범위"],
            ["허리 척추주위근 (Lumbar Paraspinal)", "S1", "fibrillation potential, positive sharp wave", "통증으로 인해 평가불가", "비정상 (활동성 탈신경)"]
        ],
        "interpretation": [
            "새끼발가락 외측 저림에도 불구하고 장딴지신경 감각신경활동전위(SNAP)가 정상 범위로 완전히 보존되어 병변이 뒤뿌리신경절 몸쪽의 척수 신경뿌리 병변임을 의미합니다.",
            "정강신경 지배 하에 있으면서 S1 지배 하에 있는 가자미근 및 장딴지근에서 탈신경 자발전위가 출현하며, S1 허리 척추주위근육에서 동반 출현하여 S1 허리 신경뿌리병증으로 판독합니다."
        ],
        "emg_meaning": [
            "S1 Myotome pathway: 아킬레스힘줄 반사 경로를 구성하는 가자미근에서 발생하는 비정상적인 자발 활동을 의미합니다."
        ],
        "ddx": "좌골신경통(Sciatica)과의 구분을 위해 바로누운자세 편다리올림검사(SLR test) 물리치료 평가 검사와 허리엉치 MRI 정밀 확인을 권장합니다."
    },
    
    "오른쪽 어깨 통증 및 손 내재근 위축 (가슴문증후군 의심)": {
        "info": {"age": 38, "sex": "여성", "symptom": "오른쪽 어깨 및 빗장뼈(Clavicle) 하부 통증, 새끼손가락 쪽 감각 이상, 짧은엄지벌림근 위축 양상 동반", "side": "오른쪽"},
        "diagnosis": "오른쪽 가슴문증후군(Thoracic outlet syndrome, TOS)",
        "ncs_sensory": [["가쪽아래팔피부신경 (LAC SNAP)", "25 μV", "2.1 ms", "정상 범위"], ["안쪽아래팔피부신경 (MAC SNAP)", "2 μV", "3.9 ms", "진폭: 감소 / 잠복기: 지연"]],
        "ncs_motor": [["정중신경 (Median CMAP)", "손목", "3.8 mV", "4.0 ms", "진폭: 감소"], ["자신경 (Ulnar CMAP)", "손목", "4.1 mV", "3.2 ms", "정상 범위"]],
        "emg": [
            ["짧은엄지벌림근 (APB)", "C8-T1", "Silent at rest", "Giant MUAPs 출현 및 Reduced MU recruitment", "비정상 (손 양상)"],
            ["첫째등쪽뼈사이근 (FDI)", "C8-T1", "Silent at rest", "Giant MUAPs 출현 및 Reduced MU recruitment", "비정상 (손 내재근 위축)"],
            ["위팔두갈래근 (Biceps brachii)", "C5-C6", "Silent at rest", "Normal MU recruitment", "정상 범위"],
            ["목 척추주위근 (C8-T1)", "C8-T1", "Silent at rest", "Normal MU recruitment", "정상 범위"]
        ],
        "interpretation": [
            "위팔신경얼기 하부 신경줄기가 빗장뼈 아래 통로에서 물리 압박을 받는 가슴문증후군 기전입니다. 안쪽아래팔피부신경 감각신경활동전위(SNAP)의 진폭이 극적으로 감소하여 신경얼기 수준의 먼쪽 변성을 가리칩니다.",
            "T1 우세 지배인 짧은엄지벌림근 (APB)과 첫째등쪽뼈사이근 (FDI)에서 만성적인 거대운동단위활동전위(Giant MUAP)가 관찰되는 반면, 목 척추주위근육은 완전 정상이므로 척수 신경뿌리을 배제하고 가슴문 영역의 압박성 마비로 확진합니다."
        ],
        "emg_meaning": [
            "Gilliatt-Sumner hand: 가슴문증후군 장기화로 인해 T1 운동 지배 가지가 소실되어, 짧은엄지벌림근을 중심으로 손 자체기원근육(intrinsic)이 심하게 위축되는 임상적 변성 양상입니다."
        ],
        "ddx": "목갈비근(Scalenus) 단축 긴장을 감별하기 위한 Adson 검사 연계 및 이학적 가슴문 압박 가동 검사가 추천됩니다."
    },
  
    "2주 전쯤 시작된 왼쪽 한쪽 얼굴 마비 (얼굴신경마비 의심)": {
        "info": {
            "age": 29,
            "sex": "남성",
            "symptom": "2주 전쯤부터 발현된 왼쪽 얼굴 전반 마비, 이마 주름 소실, 왼쪽 눈 감김 불능, 입꼬리 비대칭",
            "side": "왼쪽",
        },
        "diagnosis": "왼쪽 특발성 얼굴신경마비",
        "ncs_sensory": [
            ["오른쪽 이마 자극 (V1 분지)", "22 μV", "2.1 ms", "정상 범위"],
            ["왼쪽 이마 자극 (V1 분지)", "21 μV", "2.2 ms", "정상 범위"],
        ],
        "ncs_motor": [
            ["오른쪽 얼굴신경 (Facial CMAP)", "코근", "3.2 mV", "2.8 ms", "정상 범위"],
            ["왼쪽 얼굴신경 (Facial CMAP)", "코근", "1.1 mV", "4.5 ms", "진폭: 감소 / 잠복기: 지연"],
        ],
        "emg": [
            ["눈둘레근 (Orbicularis oculi)", "얼굴신경 지배", "fibrillation potential, positive sharp wave", "Reduced MU recruitment", "비정상 (활동성 탈신경)"],
        ],
        "interpretation": [
            "왼쪽 얼굴신경 자극 시 복합근육활동전위 진폭이 정상측보다 크게 감소(약 66% )하여 말초 얼굴신경 부분적인 운동 축삭 손상을 시사합니다.",
            "침근전도에서 발병 2주 시점에 탈신경성 자발전위(미세섬유전위, positive sharp wave) 가 관찰되는 것은 신경 축삭 손상이 실제로 발생했음을 지지합니다. 또한 운동단위동원 감소(reduced recruitment) 소견은 해당 근육의 운동 단위가 감소했음을 의미합니다.",
            "재생 전위(다극성 MUAP, amplitude 증가 등)는 보통 수주~수개월 후에 관찰되므로 추적 근전도검사로 재생 소견을 확인해야 합니다.",
            "이마 주름 소실과 눈 감김 불능을 동반한 말초성 얼굴마비 양상으로 벨마비에 합당합니다.",
        ],
        "emg_meaning": [
            "발병 2주 시점에서는 탈신경성 자발전위가 이미 나타날 수 있으며, 이는 축삭 손상의 증거입니다.",
            "초기(발병 1주 이내) 검사에서는 자발전위가 없을 수 있으나, 2주 전후에는 탈신경 전위가 관찰되는 경우가 많아 근전도검사가 예후 평가에 도움이됩니다.",
            "얼굴신경 복합근육활동전위는 좌우 진폭 비대칭을 통해 운동 축삭 손상 정도를 추정하는 데 도움이 됩니다.",
        ],
        "ddx": "중추성 얼굴마비는 이마 주름이 비교적 보존될 수 있으므로, 이마 움직임과 다른 신경학적 징후를 함께 확인해야 합니다.",
    },
}


def get_report_title(language: str) -> str:
    language = normalize_report_language(language)

    if language == REPORT_LANG_EN:
        return REPORT_TITLE_EN

    return REPORT_TITLE_KO


def get_report_subtitle(language: str) -> str:
    language = normalize_report_language(language)

    if language == REPORT_LANG_EN:
        return REPORT_SUBTITLE_EN

    return REPORT_SUBTITLE_KO


def get_report_section_name(section: str, language: str) -> str:
    language = normalize_report_language(language)

    mapping = {
        REPORT_LANG_KO: {
            "sensory": "감각신경전도검사",
            "motor": "운동신경전도검사",
            "emg": "침근전도검사",
        },
        REPORT_LANG_EN: {
            "sensory": "Sensory NCS",
            "motor": "Motor NCS",
            "emg": "Needle EMG",
        },
    }

    return mapping.get(language, mapping[REPORT_LANG_KO]).get(section, section)


def get_section_title(section: str, language: str) -> str:
    language = normalize_report_language(language)

    if language == REPORT_LANG_EN:
        mapping = {
            "sensory": "⚡ Sensory NCS",
            "motor": "⚡ Motor NCS",
            "emg": "🪡 Needle EMG",
        }
    else:
        mapping = {
            "sensory": "⚡ 감각신경전도검사",
            "motor": "⚡ 운동신경전도검사",
            "emg": "🪡 침근전도검사",
        }

    return mapping.get(section, section)


def get_table_headers(section: str, language: str) -> list:
    return get_report_headers(section, language)


def convert_rows_for_language(rows: list, language: str) -> list:
    language = normalize_report_language(language)

    if language == REPORT_LANG_KO:
        return rows

    return translate_rows(rows, language)


def convert_text_for_language(text: str, language: str) -> str:
    language = normalize_report_language(language)

    if language == REPORT_LANG_KO:
        return str(text)

    return translate_term(text, language)


def get_available_languages() -> list:
    return list(LANGUAGE_OPTIONS)


def is_report_korean(language: str) -> bool:
    return normalize_report_language(language) == REPORT_LANG_KO


def is_report_english(language: str) -> bool:
    return normalize_report_language(language) == REPORT_LANG_EN
