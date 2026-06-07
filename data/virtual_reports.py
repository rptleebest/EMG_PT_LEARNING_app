# data/virtual_reports.py

"""
가상 검사결과표 해석 모드용 실전 데이터.
총 10개의 임상 다빈도 질환에 대한 양측 비교 데이터, 다수 근육 EMG 매핑, 세분화된 해석 및 감별진단이 포함되어 있습니다.
"""

from data.report_terms import (
    REPORT_LANG_KO, REPORT_LANG_EN, LANGUAGE_OPTIONS, normalize_report_language,
    translate_term, translate_rows, get_report_headers
)

REPORT_TITLE_KO = "가상 검사결과표 (양측 비교형)"
REPORT_TITLE_EN = "Virtual EMG Report (Bilateral Comparison)"

VIRTUAL_REPORTS = {
    "왼쪽 목 통증 및 엄지/검지 저림 (C6 신경뿌리병증)": {
        "info": {"age": 45, "sex": "남성", "symptom": "왼쪽 뒷목 통증, 왼쪽 어깨와 엄지/검지로 뻗치는 저림, 팔꿉 굽힘 시 힘 빠짐", "side": "왼쪽"},
        "diagnosis": "왼쪽 C6 목 신경뿌리병증",
        "ncs_sensory": [
            ["정중신경", "오른쪽", "25 μV", "2.8 ms", "정상 범위"],
            ["정중신경", "왼쪽", "24 μV", "2.8 ms", "정상 범위"],
            ["자신경", "오른쪽", "22 μV", "2.5 ms", "정상 범위"],
            ["자신경", "왼쪽", "21 μV", "2.6 ms", "정상 범위"],
        ],
        "ncs_motor": [
            ["정중신경", "손목", "오른쪽", "8.5 mV", "3.5 ms", "정상 범위"],
            ["정중신경", "손목", "왼쪽", "8.2 mV", "3.6 ms", "정상 범위"],
            ["자신경", "손목", "오른쪽", "7.5 mV", "2.8 ms", "정상 범위"],
            ["자신경", "손목", "왼쪽", "7.3 mV", "2.9 ms", "정상 범위"],
        ],
        "emg": [
            ["목 척추주위근", "C6", "왼쪽", "Fibrillation/PSW", "통증으로 평가 불가", "비정상 (활동성 탈신경)"],
            ["어깨세모근", "C5-C6", "왼쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["위팔두갈래근", "C5-C6", "왼쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["원엎침근", "C6-C7", "왼쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["위팔세갈래근", "C7-C8", "왼쪽", "Silent", "Normal recruitment", "정상 범위"],
        ],
        "teaching_diagnosis": {
            "summary": "왼쪽 C6 목 신경뿌리병증",
            "ncs_reason": [
                "정중신경과 자신경의 감각(SNAP)과 운동(CMAP) 전도가 좌오른쪽 모두 대칭적인 정상 범위입니다.",
                "감각신경 진폭이 정상 범위로 보존된 것은 병변이 감각세포체(DRG)보다 중추측인 척수 신경뿌리(Root)에 있음을 명확히 지시합니다."
            ],
            "emg_reason": [
                "위팔두갈래근(근육피부신경 지배)과 원엎침근(정중신경 지배) 등 서로 다른 말초신경 지배를 받는 근육에서 활동성 탈신경 전위가 발견되어 단일 말초신경 병변이 아님을 확인합니다.",
                "C6 척추주위근의 활동성 탈신경 소견은 병변이 척수 신경뿌리에 위치함을 확진하는 가장 강력한 증거입니다."
            ],
            "integration": [
                "NCS 상 정상적인 감각전도 보존 소견과, EMG 상 C6 신경절 지배 다수 말초 근육 및 척추주위근의 침범 소견을 종합하여 C6 목 신경뿌리병증으로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "근육피부신경병증 (Musculocutaneous Neuropathy)",
                "how_to_differentiate": "근육피부신경 단독 마비라면 원엎침근(정중신경 지배)과 목 척추주위근은 반드시 정상이어야 하며 감각 전도가 감소해야 하므로 본 결과와 다릅니다."
            }
        ]
    },

    "오른쪽 1~3번째 손가락 저림 (손목굴증후군)": {
        "info": {"age": 52, "sex": "여성", "symptom": "오른손 엄지~중지 저림, 야간에 통증이 심해 털면 완화됨", "side": "오른쪽"},
        "diagnosis": "오른쪽 손목굴증후군",
        "ncs_sensory": [
            ["정중신경", "왼쪽", "26 μV", "2.7 ms", "정상 범위"],
            ["정중신경", "오른쪽", "11 μV", "4.8 ms", "비정상 (진폭 감소 / 잠복기 지연)"],
            ["자신경", "왼쪽", "25 μV", "2.6 ms", "정상 범위"],
            ["자신경", "오른쪽", "24 μV", "2.5 ms", "정상 범위"],
        ],
        "ncs_motor": [
            ["정중신경", "손목", "왼쪽", "8.1 mV", "3.6 ms", "정상 범위"],
            ["정중신경", "손목", "오른쪽", "4.5 mV", "5.8 ms", "비정상 (진폭 감소 / 잠복기 지연)"],
            ["자신경", "손목", "왼쪽", "7.8 mV", "2.8 ms", "정상 범위"],
            ["자신경", "손목", "오른쪽", "7.6 mV", "2.9 ms", "정상 범위"],
        ],
        "emg": [
            ["짧은엄지벌림근", "C8-T1", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["첫째등쪽뼈사이근", "C8-T1", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["원엎침근", "C6-C7", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
        ],
        "teaching_diagnosis": {
            "summary": "오른쪽 손목굴증후군(Carpal tunnel syndrome)",
            "ncs_reason": [
                "정중신경 감각 및 운동 전도에서만 잠복기가 뚜렷하게 지연되어, 손목굴 통과 부위의 국소 말이집탈락(Demyelination)을 지시합니다.",
                "자신경은 양측 모두 정상 범위를 보여 병변이 정중신경 단일 신경에 국한됨을 증명합니다."
            ],
            "emg_reason": [
                "손목 터널을 통과한 후 지배하는 짧은엄지벌림근에서 탈신경 전위가 없는 것(Silent)은, 아직 축삭이 완전히 손상되거나 마비 단계까지 이르지 않은 상태임을 의미합니다.",
                "손목 상부의 정중신경 지배 근육인 원엎침근이 정상 범위인 것은 신경 압박 위치가 팔꿈치가 아닌 손목 수준임을 확인시켜 줍니다."
            ],
            "integration": [
                "오른쪽 정중신경에 국한된 명확한 말초 잠복기 지연 데이터와, 손목 상위 근육의 정상 소견을 통합하여 손목굴증후군으로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "원엎침근증후군 (Pronator Teres Syndrome)",
                "how_to_differentiate": "원엎침근증후군이라면 손목 부위의 감각/운동 잠복기 지연이 두드러지지 않으며, EMG에서 손목 상부 근육인 원엎침근에 비정상 탈신경 소견이 나타나야 합니다."
            }
        ]
    },

    "왼쪽 허리/엉치 통증 및 발처짐 (L5 신경뿌리병증)": {
        "info": {"age": 58, "sex": "여성", "symptom": "왼쪽 허리통증, 종아리 가쪽/발등 저림, 보행 시 왼쪽 발끝이 걸림", "side": "왼쪽"},
        "diagnosis": "왼쪽 L5 허리 신경뿌리병증",
        "ncs_sensory": [
            ["얕은종아리신경", "오른쪽", "15 μV", "2.8 ms", "정상 범위"],
            ["얕은종아리신경", "왼쪽", "14 μV", "2.9 ms", "정상 범위"],
            ["장딴지신경", "오른쪽", "18 μV", "3.0 ms", "정상 범위"],
            ["장딴지신경", "왼쪽", "17 μV", "3.1 ms", "정상 범위"],
        ],
        "ncs_motor": [
            ["종아리신경", "발목", "오른쪽", "4.8 mV", "4.2 ms", "정상 범위"],
            ["종아리신경", "발목", "왼쪽", "4.5 mV", "4.5 ms", "정상 범위"],
        ],
        "emg": [
            ["허리 척추주위근", "L5", "왼쪽", "Fibrillation/PSW", "통증으로 평가 불가", "비정상 (활동성 탈신경)"],
            ["앞정강근", "L4-L5", "왼쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["긴종아리근", "L5-S1", "왼쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["안쪽장딴지근", "S1-S2", "왼쪽", "Silent", "Normal recruitment", "정상 범위"],
        ],
        "teaching_diagnosis": {
            "summary": "왼쪽 L5 허리 신경뿌리병증",
            "ncs_reason": [
                "발처짐(운동 결손)과 발등 감각 이상이 있음에도 얕은종아리신경 감각 진폭이 양측 대칭적으로 정상 범위입니다.",
                "이는 병변이 감각세포체 몸쪽인 척수 신경뿌리에 위치하여, 말초 감각신경의 퇴행을 유발다리 않았음을 증명합니다."
            ],
            "emg_reason": [
                "깊은종아리신경 지배(앞정강근)와 얕은종아리신경 지배(긴종아리근) 근육 모두에서 활동성 탈신경이 발견되어 말초 단일 마비가 아님을 시사합니다.",
                "L5 허리 척추주위근에 탈신경 자발전위가 나타난 것은 병변 위치가 척수 근위부임을 확진하는 핵심 지표입니다."
            ],
            "integration": [
                "감각전도 보존 현상과, L5 지배 다수 말초 근육 및 척추주위근의 동시 탈신경 출현을 통합하여 L5 허리 신경뿌리병증으로 결론 내립니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "온종아리신경 마비 (Common Peroneal Neuropathy)",
                "how_to_differentiate": "말초 온종아리신경 마비라면 얕은종아리신경의 감각전도(SNAP) 진폭이 감소해야 하며, 허리 척추주위근은 정상 범위로 유지되어야 합니다."
            }
        ]
    },

    "오른쪽 4~5번째 손가락 저림 (팔꿈치굴증후군)": {
        "info": {"age": 42, "sex": "남성", "symptom": "오른손 4~5번째 손가락 저림, 젓가락질이 불편하고 손아귀 힘이 약해짐", "side": "오른쪽"},
        "diagnosis": "오른쪽 팔꿈치굴증후군",
        "ncs_sensory": [
            ["자신경", "왼쪽", "22 μV", "2.5 ms", "정상 범위"],
            ["자신경", "오른쪽", "9 μV", "3.4 ms", "비정상 (진폭 감소 / 잠복기 지연)"],
            ["정중신경", "오른쪽", "24 μV", "2.8 ms", "정상 범위"],
        ],
        "ncs_motor": [
            ["자신경", "팔꿈치 아래", "오른쪽", "7.2 mV", "3.0 ms", "정상 범위"],
            ["자신경", "팔꿈치 위", "오른쪽", "3.1 mV", "8.2 ms", "비정상 (진폭 급감 / 국소 전도차단)"],
        ],
        "emg": [
            ["새끼벌림근", "C8-T1", "오른쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["첫째등쪽뼈사이근", "C8-T1", "오른쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["짧은엄지벌림근", "C8-T1", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["목 척추주위근", "C8-T1", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
        ],
        "teaching_diagnosis": {
            "summary": "오른쪽 팔꿈치굴증후군",
            "ncs_reason": [
                "오른쪽 자신경의 감각전도 지연 및 진폭 감소가 확인됩니다.",
                "팔꿈치 위/아래를 자극했을 때 운동 진폭이 50% 이상 급감하는 '국소 전도차단(Conduction Block)' 현상이 관찰되어 팔꿈치 부위 압박을 확진합니다."
            ],
            "emg_reason": [
                "자신경 지배를 받는 손 내재근에서 활동성 탈신경 전위가 확인되어 압박성 축삭 손상이 동반되었음을 알 수 있습니다.",
                "동일한 C8-T1 분절 지배를 받지만 정중신경 지배인 짧은엄지벌림근과 척추주위근이 완전한 정상 범위인 것은 척수 신경뿌리병증을 배제시킵니다."
            ],
            "integration": [
                "자신경에 국한된 팔꿈치 부위 전도차단 수치와 해당 말초 근육의 선택적 탈신경 데이터를 종합하여 팔꿈치굴증후군으로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "C8 신경뿌리병증 (C8 Radiculopathy)",
                "how_to_differentiate": "C8 신경뿌리병증이라면 정중신경 지배 근육인 짧은엄지벌림근도 함께 약화되며, 감각 전도는 오히려 정상 범위로 보존되어야 합니다."
            }
        ]
    },

    "오른쪽 손목처짐 및 손등 감각 저하 (노신경 마비)": {
        "info": {"age": 34, "sex": "남성", "symptom": "음주 후 의자에서 잔 뒤 발생한 오른쪽 손목처짐 및 손등 저림", "side": "오른쪽"},
        "diagnosis": "오른쪽 노신경 마비",
        "ncs_sensory": [
            ["노신경", "왼쪽", "20 μV", "2.1 ms", "정상 범위"],
            ["노신경", "오른쪽", "8 μV", "3.2 ms", "비정상 (진폭 감소 / 잠복기 지연)"],
            ["정중신경", "오른쪽", "25 μV", "2.8 ms", "정상 범위"],
        ],
        "ncs_motor": [
            ["노신경", "팔꿈치", "오른쪽", "6.8 mV", "2.5 ms", "정상 범위"],
            ["노신경", "나선고랑 위", "오른쪽", "1.5 mV", "7.1 ms", "비정상 (진폭 급감 / 국소 전도차단)"],
        ],
        "emg": [
            ["긴노쪽손목폄근", "C6-C7", "오른쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["손가락폄근", "C7-C8", "오른쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["위팔세갈래근", "C7-C8", "오른쪽", "Silent", "Normal recruitment", "정상 범위 (보존됨)"],
        ],
        "teaching_diagnosis": {
            "summary": "오른쪽 노신경 마비",
            "ncs_reason": [
                "표재노신경 감각전도 진폭 감소와 함께, 나선고랑 상/하부 자극에서 운동 진폭이 급감하는 전도차단 수치가 기록되어 물리적 압박 위치를 지시합니다."
            ],
            "emg_reason": [
                "나선고랑 하부에서 신경 지배를 받는 폄근들은 탈신경 소견을 보입니다.",
                "나선고랑 상부에서 먼저 가지되는 위팔세갈래근이 정상 범위인 것은 신경 병변이 겨드랑이나 목이 아님을 해부학적으로 증명합니다."
            ],
            "integration": [
                "위팔세갈래근의 보존, 나선고랑 부위 국소 전도차단 데이터, 그리고 하부 폄근들의 선택적 마비를 통합하여 노신경 압박 마비로 확진합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "뒤뼈사이신경 마비 (posterior interosseous nerve, PIN Syndrome)",
                "how_to_differentiate": "뒤뼈사이신경 마비는 순수 운동신경 가지 마비이므로 감각 소실이 없으며 표재노신경 감각 전도가 정상 수치로 기록되어야 합니다."
            }
        ]
    },

    "오른쪽 엉치 방사통 및 종아리 약화 (S1 신경뿌리병증)": {
        "info": {"age": 50, "sex": "남성", "symptom": "오른쪽 엉치에서 발바닥으로 당기는 통증, 까치발 걷기가 힘듦", "side": "오른쪽"},
        "diagnosis": "오른쪽 S1 신경뿌리병증",
        "ncs_sensory": [
            ["장딴지신경", "오른쪽", "16 μV", "3.0 ms", "정상 범위"],
            ["장딴지신경", "왼쪽", "17 μV", "2.9 ms", "정상 범위"],
        ],
        "ncs_motor": [
            ["정강신경", "발목", "오른쪽", "6.1 mV", "4.8 ms", "정상 범위"],
            ["종아리신경", "발목", "오른쪽", "5.2 mV", "4.1 ms", "정상 범위"],
        ],
        "emg": [
            ["안쪽장딴지근", "S1-S2", "오른쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["가자미근", "S1-S2", "오른쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["큰볼기근", "S1-S2", "오른쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["앞정강근", "L4-L5", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["허리 척추주위근", "S1", "오른쪽", "Fibrillation/PSW", "통증으로 평가 불가", "비정상 (활동성 탈신경)"],
        ],
        "teaching_diagnosis": {
            "summary": "오른쪽 S1 허리/엉치 신경뿌리병증",
            "ncs_reason": [
                "종아리 뒤쪽 감각 이상이 뚜렷함에도 가장 먼 쪽의 장딴지신경 감각 전도가 양측 모두 정상 범위로 보존되는 전형적인 척수 신경뿌리 병변 양상입니다."
            ],
            "emg_reason": [
                "정강신경 지배(장딴지근)와 하볼기신경 지배(큰볼기근) 등 각기 다른 말초신경의 지배를 받으나 S1 분절을 공유하는 근육들에서 동시 탈신경이 확인됩니다.",
                "S1 레벨 척추주위근의 탈신경 소견은 병변이 말초가 아닌 척수 근위부임을 확진합니다."
            ],
            "integration": [
                "장딴지신경 전도 보존 수치와, S1 분절 우세 말초 근육 및 척추주위근의 탈신경 데이터를 통합하여 S1 신경뿌리병증으로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "궁둥신경병증 (Sciatic Neuropathy)",
                "how_to_differentiate": "말초 궁둥신경이 눌렸다면 장딴지신경 감각 진폭이 유의하게 감소하며, 허리 척추주위근은 정상 범위로 기록되어야 합니다."
            }
        ]
    },

    "왼쪽 발처짐 및 종아리 가쪽 무딤 (온종아리신경 마비)": {
        "info": {"age": 28, "sex": "여성", "symptom": "장기간 동안 압박 압박스타킹을 장시간 착용 후 발생한 왼쪽 발처짐 및 감각 무딤", "side": "왼쪽"},
        "diagnosis": "왼쪽 온종아리신경 마비",
        "ncs_sensory": [
            ["얕은종아리신경", "오른쪽", "16 μV", "2.8 ms", "정상 범위"],
            ["얕은종아리신경", "왼쪽", "6 μV", "4.1 ms", "비정상 (진폭 감소 / 잠복기 지연)"],
            ["장딴지신경", "왼쪽", "18 μV", "3.1 ms", "정상 범위"],
        ],
        "ncs_motor": [
            ["종아리신경", "발목", "왼쪽", "5.1 mV", "4.0 ms", "정상 범위"],
            ["종아리신경", "종아리뼈머리", "왼쪽", "1.2 mV", "8.5 ms", "비정상 (진폭 급감 / 국소 전도차단)"],
        ],
        "emg": [
            ["앞정강근", "L4-L5", "왼쪽", "Silent", "No recruitment", "비정상 (동원 불가)"],
            ["긴종아리근", "L5-S1", "왼쪽", "Silent", "Reduced recruitment", "비정상 (동원 감소)"],
            ["넙다리두갈래근 짧은갈래", "L5-S1", "왼쪽", "Silent", "Normal recruitment", "정상 범위 (보존됨)"],
            ["허리 척추주위근", "L5", "왼쪽", "Silent", "Normal recruitment", "정상 범위"],
        ],
        "teaching_diagnosis": {
            "summary": "왼쪽 온종아리신경 압박 마비",
            "ncs_reason": [
                "얕은종아리신경 감각전도가 저하되었고, 종아리뼈머리 자극에서 운동 진폭이 급감하는 국소 전도차단 수치가 확인되어 병변의 물리적 압박 위치가 특정됩니다."
            ],
            "emg_reason": [
                "종아리뼈머리 하부에 위치한 앞정강근과 긴종아리근은 운동단위 동원이 불가하거나 감소합니다.",
                "무릎 상부에서 갈라져 나오는 신경 가지에 의해 지배되는 넙다리두갈래근(짧은갈래)과 척추주위근이 정상 범위인 것은 궁둥신경이나 척추 뿌리 문제가 아님을 명확히 입증합니다."
            ],
            "integration": [
                "무릎 부위 국소 전도차단 지표와, 무릎 하부 근육들의 선택적 마비 소견을 통합하여 온종아리신경 마비로 확진합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "L5 허리 신경뿌리병증",
                "how_to_differentiate": "L5 병변이라면 감각전도가 양측 대칭적으로 정상이어야 하며, 척추주위근 및 중간볼기근에서 비정상 활동성 탈신경 소견이 나타나야 합니다."
            }
        ]
    },

    "오른쪽 어깨 뻐근함 및 위팔세갈래근 약화 (C7 신경뿌리병증)": {
        "info": {"age": 51, "sex": "여성", "symptom": "오른쪽 날개뼈 안쪽 통증, 팔 뒤쪽부터 가운데 손가락까지 저림, 팔 펴는 힘 빠짐", "side": "오른쪽"},
        "diagnosis": "오른쪽 C7 신경뿌리병증",
        "ncs_sensory": [
            ["정중신경 3지", "오른쪽", "28 μV", "2.7 ms", "정상 범위 (보존됨)"],
            ["정중신경 3지", "왼쪽", "29 μV", "2.6 ms", "정상 범위"],
        ],
        "ncs_motor": [
            ["노신경", "아래팔", "오른쪽", "7.1 mV", "2.5 ms", "정상 범위"],
            ["정중신경", "손목", "오른쪽", "8.8 mV", "3.2 ms", "정상 범위"],
        ],
        "emg": [
            ["목 척추주위근", "C7", "오른쪽", "Fibrillation/PSW", "통증으로 평가 불가", "비정상 (활동성 탈신경)"],
            ["위팔세갈래근", "C7-C8", "오른쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["노쪽손목굽힘근", "C6-C7", "오른쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["손가락폄근", "C7-C8", "오른쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["위팔두갈래근", "C5-C6", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
        ],
        "teaching_diagnosis": {
            "summary": "오른쪽 C7 목 신경뿌리병증",
            "ncs_reason": [
                "가운데 손가락 저림이 뚜렷함에도 정중신경 3번재 손가락 가지의 감각 진폭이 정상 범위로 유지되는 전형적인 근위부 병변입니다."
            ],
            "emg_reason": [
                "C7 분절 지배를 받는 위팔세갈래근(노신경 지배)과 노쪽손목굽힘근(정중신경 지배)에서 동시 탈신경이 확인되어 단일 신경 문제가 아님을 입증합니다.",
                "C7 척추주위근 탈신경 소견과, 인접한 C5-6 지배인 위팔두갈래근의 정상 범위는 병변이 C7 레벨에 특정됨을 확진합니다."
            ],
            "integration": [
                "감각전도 보존 현상과, C7 우세 다수 말초근육의 동시 침범 데이터를 통합하여 C7 신경뿌리병증으로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "노신경 마비 (Radial Neuropathy)",
                "how_to_differentiate": "노신경 마비라면 정중신경 지배를 받는 노쪽손목굽힘근이나 척추주위근은 정상 범위여야 합니다."
            }
        ]
    },

    "왼쪽 갑작스러운 얼굴 마비 (Bell' palsy)": {
        "info": {"age": 35, "sex": "여성", "symptom": "자고 일어난 후 왼쪽 얼굴 전체 마비, 이마 주름 소실 및 눈이 안 감김", "side": "왼쪽"},
        "diagnosis": "왼쪽 특발성 얼굴신경마비",
        "ncs_sensory": [
            ["삼차신경 눈신경가지", "오른쪽", "20 μV", "2.1 ms", "정상 범위"],
            ["삼차신경 눈신경가지", "왼쪽", "21 μV", "2.0 ms", "정상 범위"],
        ],
        "ncs_motor": [
            ["얼굴신경 코근", "오른쪽", "3.5 mV", "2.8 ms", "정상 범위"],
            ["얼굴신경 코근", "왼쪽", "0.8 mV", "4.5 ms", "비정상 (진폭 감소 / 잠복기 지연)"],
        ],
        "emg": [
            ["눈둘레근", "얼굴신경", "왼쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["깨물근", "삼차신경", "왼쪽", "Silent", "Normal recruitment", "정상 범위"],
        ],
        "teaching_diagnosis": {
            "summary": "왼쪽 말초성 얼굴신경마비 (벨마비)",
            "ncs_reason": [
                "감각을 담당하는 삼차신경은 정상이지만, 얼굴신경 운동 진폭이 오른쪽 대비 크게 감소하여 심각한 축삭 변성을 시사합니다."
            ],
            "emg_reason": [
                "시간이 지나 눈둘레근에서 활동성 탈신경 전위가 뚜렷하게 관찰됩니다.",
                "씹기근육(삼차신경 지배)은 정상이므로 복합 뇌신경 마비가 아님을 확인합니다."
            ],
            "integration": [
                "이마 주름 소실, 얼굴신경 단독의 진폭 감소 및 근전도 탈신경 소견을 종합하여 말초성 벨마비로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "중추성 얼굴 마비 (뇌졸중 등)",
                "how_to_differentiate": "뇌졸중 등 중추성 질환은 이마 근육에 양측성 지배가 유지되어 마비측 이마 주름을 잡을 수 있습니다. 벨마비는 이마 주름이 불가능합니다."
            }
        ]
    },

    "양측 발끝 화끈거림 (다발신경병증)": {
        "info": {"age": 68, "sex": "남성", "symptom": "양 발바닥부터 무릎 아래까지 화끈거리는 대칭적 장갑-양말형 저림", "side": "양측"},
        "diagnosis": "대칭성 길이의존성 축삭성 다발신경병증",
        "ncs_sensory": [
            ["장딴지신경", "오른쪽", "무반응", "측정불가", "비정상 (반응 소실)"],
            ["장딴지신경", "왼쪽", "무반응", "측정불가", "비정상 (반응 소실)"],
            ["정중신경", "오른쪽", "16 μV", "3.6 ms", "비정상 (진폭 감소)"],
            ["정중신경", "왼쪽", "15 μV", "3.7 ms", "비정상 (진폭 감소)"],
        ],
        "ncs_motor": [
            ["정강신경", "발목", "오른쪽", "1.8 mV", "6.2 ms", "비정상 (진폭 감소 / 잠복기 지연)"],
            ["정강신경", "발목", "왼쪽", "1.7 mV", "6.4 ms", "비정상 (진폭 감소 / 잠복기 지연)"],
        ],
        "emg": [
            ["앞정강근", "L4-L5", "오른쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["앞정강근", "L4-L5", "왼쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["위팔두갈래근", "C5-C6", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["위팔두갈래근", "C5-C6", "왼쪽", "Silent", "Normal recruitment", "정상 범위"],
        ],
        "teaching_diagnosis": {
            "summary": "길이의존성 축삭성 다발신경병증",
            "ncs_reason": [
                "가장 긴 신경인 다리 장딴지신경 반응이 소실되고, 팔 정중신경도 진폭이 감소한 전형적인 길이의존성 패턴입니다."
            ],
            "emg_reason": [
                "다리 원위부 근육인 양측 앞정강근에서 대칭적인 활동성 탈신경이 확인됩니다.",
                "팔 근위부 근육은 정상 범위인 것을 볼 때, 몸에서 가장 먼 신경 말단부터 서서히 퇴행하는 기전임을 확증합니다."
            ],
            "integration": [
                "양측 전도의 대칭적 소실 데이터와, 원위부 우세 근전도 이상 소견을 통합하여 다발신경병증으로 결론 내립니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "다발성 허리 신경뿌리병증 (Lumbar Canal Stenosis)",
                "how_to_differentiate": "협착증에 의한 다발 뿌리병증은 말초 감각전도가 보존되며, 척추주위근에 양측 탈신경이 도출되어야 합니다. 다발신경병증은 감각 소실이 특징입니다."
            }
        ]
    }
}

def get_report_title(language: str) -> str:
    lang = normalize_report_language(language)
    return REPORT_TITLE_EN if lang == REPORT_LANG_EN else REPORT_TITLE_KO

def get_report_section_name(section: str, language: str) -> str:
    lang = normalize_report_language(language)
    mapping = {
        REPORT_LANG_KO: {"sensory": "감각신경전도검사", "motor": "운동신경전도검사", "emg": "침근전도검사"},
        REPORT_LANG_EN: {"sensory": "Sensory NCS", "motor": "Motor NCS", "emg": "Needle EMG"}
    }
    return mapping.get(lang, mapping[REPORT_LANG_KO]).get(section, section)

def get_available_languages() -> list:
    return list(LANGUAGE_OPTIONS)

def is_report_korean(language: str) -> bool:
    return normalize_report_language(language) == REPORT_LANG_KO

# 영어 모드용 수동 단어 교체 함수
def custom_english_translate(text: str) -> str:
    raw = str(text)
    mapping = {
        "정상 범위": "Within normal limits",
        "비정상 (활동성 탈신경)": "Abnormal (Active denervation)",
        "통증으로 평가 불가": "Incomplete due to pain",
        "진폭 감소 / 잠복기 지연": "Reduced amplitude / Delayed latency",
        "진폭 급감 / 국소 전도차단": "Amplitude drop / Conduction block",
        "비정상 (진폭 감소)": "Abnormal (Reduced amp)",
        "비정상 (진폭 감소 / 잠복기 지연)": "Abnormal (Reduced amp/Delayed)",
        "비정상 (진폭 급감 / 국소 전도차단)": "Abnormal (Conduction block)",
        "비정상 (반응 소실)": "Abnormal (Absent)",
        "비정상 (동원 불가)": "Abnormal (No recruitment)",
        "비정상 (동원 감소)": "Abnormal (Reduced recruitment)",
        "오른쪽": "Rt",
        "왼쪽": "Lt",
        "양측": "Bilateral",
        "정중신경": "Median",
        "자신경": "Ulnar",
        "노신경": "Radial",
        "종아리신경": "Peroneal",
        "얕은종아리신경": "Superficial Peroneal",
        "장딴지신경": "Sural",
        "정강신경": "Tibial",
        "목 척추주위근": "Cervical Paraspinal",
        "허리 척추주위근": "Lumbar Paraspinal",
        "어깨세모근": "Deltoid",
        "위팔두갈래근": "Biceps brachii",
        "위팔세갈래근": "Triceps brachii",
        "원엎침근": "Pronator teres",
        "짧은엄지벌림근": "Abductor pollicis brevis",
        "첫째등쪽뼈사이근": "First dorsal interosseous",
        "앞정강근": "Tibialis anterior",
        "긴종아리근": "Peroneus longus",
        "안쪽장딴지근": "Medial gastrocnemius",
        "가자미근": "Soleus",
        "큰볼기근": "Gluteus maximus",
        "넙다리두갈래근 짧은갈래": "Biceps femoris short head",
        "긴노쪽손목폄근": "Extensor carpi radialis longus",
        "손가락폄근": "Extensor digitorum communis",
        "노쪽손목굽힘근": "Flexor carpi radialis",
        "새끼벌림근": "Abductor digiti minimi",
        "눈둘레근": "Orbicularis oculi",
        "깨물근": "Masseter",
        "얼굴신경 코근": "Facial (Nasalis)",
        "삼차신경 눈신경가지": "Trigeminal (V1)",
        "정중신경 3지": "Median (3rd digit)",
        "손목": "Wrist",
        "아래팔": "Forearm",
        "팔꿈치": "Elbow",
        "팔꿈치 위": "Above elbow",
        "팔꿈치 아래": "Below elbow",
        "나선고랑 위": "Above spiral groove",
        "종아리뼈머리": "Fibular head",
        "발목": "Ankle",
        "무반응": "Absent",
        "측정불가": "N/A"
    }
    for kr, en in mapping.items():
        if kr in raw:
            raw = raw.replace(kr, en)
    return raw
