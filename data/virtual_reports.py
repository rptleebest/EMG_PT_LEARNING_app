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
REPORT_SUBTITLE_KO = "물리치료 임상 다빈도 10대 질환 기반 실전 데이터"
REPORT_SUBTITLE_EN = "10 Common Clinical Cases for Physical Therapy"

REPORT_SECTIONS = ["sensory", "motor", "emg"]

VIRTUAL_REPORTS = {
    "1. 왼쪽 목 통증 및 엄지/검지 저림 (C6 신경뿌리병증)": {
        "info": {"age": 45, "sex": "남성", "symptom": "왼쪽 뒷목 통증, 왼쪽 어깨와 엄지/검지로 뻗치는 저림, 팔꿉 굽힘 시 힘 빠짐", "side": "왼쪽(Lt)"},
        "diagnosis": "왼쪽 C6 목 신경뿌리병증 (Cervical Radiculopathy)",
        "ncs_sensory": [
            ["정중신경(Median)", "오른쪽(Rt)", "25 μV", "2.8 ms", "정상"],
            ["정중신경(Median)", "왼쪽(Lt)", "24 μV", "2.8 ms", "정상"],
            ["자신경(Ulnar)", "오른쪽(Rt)", "22 μV", "2.5 ms", "정상"],
            ["자신경(Ulnar)", "왼쪽(Lt)", "21 μV", "2.6 ms", "정상"],
        ],
        "ncs_motor": [
            ["정중신경(Median)", "손목(Wrist)", "오른쪽(Rt)", "8.5 mV", "3.5 ms", "정상"],
            ["정중신경(Median)", "손목(Wrist)", "왼쪽(Lt)", "8.2 mV", "3.6 ms", "정상"],
            ["자신경(Ulnar)", "손목(Wrist)", "오른쪽(Rt)", "7.5 mV", "2.8 ms", "정상"],
            ["자신경(Ulnar)", "손목(Wrist)", "왼쪽(Lt)", "7.3 mV", "2.9 ms", "정상"],
        ],
        "emg": [
            ["목 척추주위근 (Cerv. Paraspinal)", "C6", "왼쪽(Lt)", "Fibrillation/PSW", "통증으로 평가불가", "비정상 (탈신경)"],
            ["어깨세모근 (Deltoid)", "C5-C6", "왼쪽(Lt)", "Silent", "Normal recruitment", "정상"],
            ["위팔두갈래근 (Biceps brachii)", "C5-C6", "왼쪽(Lt)", "Fibrillation/PSW", "Reduced recruitment", "비정상 (탈신경)"],
            ["원엎침근 (Pronator teres)", "C6-C7", "왼쪽(Lt)", "Fibrillation/PSW", "Reduced recruitment", "비정상 (탈신경)"],
            ["위팔세갈래근 (Triceps brachii)", "C7-C8", "왼쪽(Lt)", "Silent", "Normal recruitment", "정상"],
        ],
        "teaching_diagnosis": {
            "summary": "왼쪽 C6 목 신경뿌리병증",
            "ncs_reason": [
                "정중신경과 자신경의 감각(SNAP)과 운동(CMAP) 전도가 좌우측 모두 대칭적인 정상 범위입니다.",
                "감각신경 진폭이 보존된 것은 병변이 감각세포체(DRG)보다 중추측인 척수 신경뿌리(Root)에 있음을 명확히 지시합니다."
            ],
            "emg_reason": [
                "위팔두갈래근(근육피부신경 지배)과 원엎침근(정중신경 지배) 등 서로 다른 말초신경 지배를 받는 근육에서 활동성 탈신경 전위가 발견되어 단일 말초신경 병변이 아님을 확인합니다.",
                "C6 척추주위근의 활동성 탈신경 소견은 병변이 척수 신경뿌리에 위치함을 확진하는 가장 강력한 증거입니다."
            ],
            "integration": [
                "NCS 상 정상적인 감각전도와, EMG 상 C6 신경절 지배 다수 근육 및 척추주위근의 침범 소견을 통합하여 C6 목 신경뿌리병증으로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "근육피부신경병증 (Musculocutaneous Neuropathy)",
                "why_consider": "위팔두갈래근 약화와 엄지/검지 쪽 감각 이상이 C6 신경뿌리병증의 양상과 매우 유사합니다.",
                "how_to_differentiate": "근육피부신경 단독 마비라면 원엎침근(정중신경 지배)과 목 척추주위근은 정상이어야 하며, 감각 전도가 감소해야 합니다."
            }
        ]
    },

    "2. 오른쪽 1~3번째 손가락 저림 (손목굴증후군)": {
        "info": {"age": 52, "sex": "여성", "symptom": "오른손 엄지~중지 저림, 야간에 통증이 심해 털면 완화됨", "side": "오른쪽(Rt)"},
        "diagnosis": "오른쪽 손목굴증후군 (Carpal Tunnel Syndrome)",
        "ncs_sensory": [
            ["정중신경(Median)", "왼쪽(Lt)", "26 μV", "2.7 ms", "정상"],
            ["정중신경(Median)", "오른쪽(Rt)", "11 μV", "4.8 ms", "비정상 (지연/진폭감소)"],
            ["자신경(Ulnar)", "왼쪽(Lt)", "25 μV", "2.6 ms", "정상"],
            ["자신경(Ulnar)", "오른쪽(Rt)", "24 μV", "2.5 ms", "정상"],
        ],
        "ncs_motor": [
            ["정중신경(Median)", "손목(Wrist)", "왼쪽(Lt)", "8.1 mV", "3.6 ms", "정상"],
            ["정중신경(Median)", "손목(Wrist)", "오른쪽(Rt)", "4.5 mV", "5.8 ms", "비정상 (지연/진폭감소)"],
            ["자신경(Ulnar)", "손목(Wrist)", "왼쪽(Lt)", "7.8 mV", "2.8 ms", "정상"],
            ["자신경(Ulnar)", "손목(Wrist)", "오른쪽(Rt)", "7.6 mV", "2.9 ms", "정상"],
        ],
        "emg": [
            ["짧은엄지벌림근 (APB)", "C8-T1 (정중)", "오른쪽(Rt)", "Silent", "Normal recruitment", "정상"],
            ["첫째등쪽뼈사이근 (FDI)", "C8-T1 (자신경)", "오른쪽(Rt)", "Silent", "Normal recruitment", "정상"],
            ["원엎침근 (Pronator teres)", "C6-C7 (정중)", "오른쪽(Rt)", "Silent", "Normal recruitment", "정상"],
        ],
        "teaching_diagnosis": {
            "summary": "오른쪽 손목굴증후군 (손목 부위 정중신경 포착)",
            "ncs_reason": [
                "정중신경 감각 및 운동 전도에서만 잠복기가 정상측 대비 뚜렷하게 지연되어, 손목굴 통과 부위의 국소 말이집탈락(Demyelination)을 지시합니다.",
                "자신경은 양측 모두 정상 수치를 보여 병변이 정중신경 단일 신경에 국한됨을 증명합니다."
            ],
            "emg_reason": [
                "손목 터널을 통과한 후 지배하는 APB 근육에서 탈신경 전위가 없는 것(Silent)은, 심각한 축삭 손상이나 마비 단계까지는 이르지 않은 상태임을 의미합니다.",
                "손목 상부의 정중신경 지배 근육인 원엎침근(PT)이 정상인 것은 신경 압박 위치가 팔꿈치가 아닌 손목 수준임을 확인시켜 줍니다."
            ],
            "integration": [
                "오른쪽 정중신경에 국한된 명확한 말초 잠복기 지연 데이터와, 손목 상위 근육의 정상 소견을 통합하여 손목굴증후군으로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "원엎침근증후군 (Pronator Teres Syndrome)",
                "why_consider": "1~3번째 손가락 저림 증상이 손목굴증후군과 완전히 겹칩니다.",
                "how_to_differentiate": "원엎침근증후군이라면 손목 부위의 감각/운동 잠복기 지연이 두드러지지 않으며, EMG에서 손목 상부 근육인 원엎침근에 비정상 탈신경 소견이 나타나야 합니다."
            }
        ]
    },

    "3. 왼쪽 허리/엉치 통증 및 발처짐 (L5 신경뿌리병증)": {
        "info": {"age": 58, "sex": "여성", "symptom": "왼쪽 허리통증, 종아리 가쪽/발등 저림, 보행 시 왼쪽 발끝이 걸림", "side": "왼쪽(Lt)"},
        "diagnosis": "왼쪽 L5 허리 신경뿌리병증 (Lumbar Radiculopathy)",
        "ncs_sensory": [
            ["얕은종아리신경(Sup. Peroneal)", "오른쪽(Rt)", "15 μV", "2.8 ms", "정상"],
            ["얕은종아리신경(Sup. Peroneal)", "왼쪽(Lt)", "14 μV", "2.9 ms", "정상"],
            ["장딴지신경(Sural)", "오른쪽(Rt)", "18 μV", "3.0 ms", "정상"],
            ["장딴지신경(Sural)", "왼쪽(Lt)", "17 μV", "3.1 ms", "정상"],
        ],
        "ncs_motor": [
            ["종아리신경(Peroneal)", "발목(Ankle)", "오른쪽(Rt)", "4.8 mV", "4.2 ms", "정상"],
            ["종아리신경(Peroneal)", "발목(Ankle)", "왼쪽(Lt)", "4.5 mV", "4.5 ms", "정상"],
        ],
        "emg": [
            ["허리 척추주위근 (Lumb. Paraspinal)", "L5", "왼쪽(Lt)", "Fibrillation/PSW", "통증으로 평가불가", "비정상 (활동성 탈신경)"],
            ["앞정강근 (Tibialis anterior)", "L4-L5", "왼쪽(Lt)", "Fibrillation/PSW", "Reduced recruitment", "비정상 (탈신경)"],
            ["긴종아리근 (Peroneus longus)", "L5-S1", "왼쪽(Lt)", "Fibrillation/PSW", "Reduced recruitment", "비정상 (탈신경)"],
            ["안쪽장딴지근 (Med. Gastrocnemius)", "S1-S2", "왼쪽(Lt)", "Silent", "Normal recruitment", "정상"],
        ],
        "teaching_diagnosis": {
            "summary": "왼쪽 L5 허리 신경뿌리병증",
            "ncs_reason": [
                "발처짐(운동 결손)과 발등 감각 이상이 있음에도 얕은종아리신경 SNAP 진폭이 양측 모두 대칭적으로 정상입니다.",
                "이는 병변이 뒤뿌리신경절(DRG) 몸쪽인 L5 척수 신경뿌리에 위치하여, 말초 감각신경의 축삭 퇴행을 유발하지 않았음을 생리학적으로 증명합니다."
            ],
            "emg_reason": [
                "깊은종아리신경 지배(앞정강근)와 얕은종아리신경 지배(긴종아리근) 근육 모두에서 활동성 탈신경 전위가 발견되어 특정 말초신경의 단일 마비가 아님을 시사합니다.",
                "L5 허리 척추주위근에 탈신경 자발전위가 나타난 것은 병변 위치가 말초가 아닌 척수 근위부임을 확진하는 핵심 지표입니다."
            ],
            "integration": [
                "감각전도 보존 현상과, L5 지배를 받는 다수 말초 근육 및 척추주위근의 동시 탈신경 전위 출현을 통합하여 L5 허리 신경뿌리병증으로 결론 내립니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "온종아리신경 마비 (Common Peroneal Neuropathy)",
                "why_consider": "발처짐(Foot drop)과 종아리 가쪽 감각 저하 증상이 L5 신경뿌리병증과 거의 동일하게 나타납니다.",
                "how_to_differentiate": "말초 온종아리신경 마비라면 얕은종아리신경의 감각전도(SNAP) 진폭이 감소하며, 허리 척추주위근 EMG는 반드시 정상이어야 합니다."
            }
        ]
    },

    "4. 오른쪽 4~5번째 손가락 저림 (팔꿈치굴증후군)": {
        "info": {"age": 42, "sex": "남성", "symptom": "오른손 4~5번째 손가락 저림, 젓가락질이 불편하고 손아귀 힘이 약해짐", "side": "오른쪽(Rt)"},
        "diagnosis": "오른쪽 팔꿈치굴증후군 (Cubital Tunnel Syndrome)",
        "ncs_sensory": [
            ["자신경(Ulnar)", "왼쪽(Lt)", "22 μV", "2.5 ms", "정상"],
            ["자신경(Ulnar)", "오른쪽(Rt)", "9 μV", "3.4 ms", "비정상 (진폭감소/지연)"],
            ["정중신경(Median)", "오른쪽(Rt)", "24 μV", "2.8 ms", "정상"],
        ],
        "ncs_motor": [
            ["자신경(Ulnar)", "팔꿈치 아래(Below)", "오른쪽(Rt)", "7.2 mV", "3.0 ms", "정상"],
            ["자신경(Ulnar)", "팔꿈치 위(Above)", "오른쪽(Rt)", "3.1 mV", "8.2 ms", "비정상 (국소 전도차단)"],
        ],
        "emg": [
            ["새끼벌림근 (ADM)", "C8-T1 (자신경)", "오른쪽(Rt)", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["첫째등쪽뼈사이근 (FDI)", "C8-T1 (자신경)", "오른쪽(Rt)", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["짧은엄지벌림근 (APB)", "C8-T1 (정중)", "오른쪽(Rt)", "Silent", "Normal recruitment", "정상"],
            ["목 척추주위근 (Cerv. Paraspinal)", "C8-T1", "오른쪽(Rt)", "Silent", "Normal recruitment", "정상"],
        ],
        "teaching_diagnosis": {
            "summary": "오른쪽 자신경 팔꿈치 부위 포착 (팔꿈치굴증후군)",
            "ncs_reason": [
                "오른쪽 자신경의 감각전도 지연 및 진폭 감소가 뚜렷하게 확인됩니다.",
                "특히 팔꿈치 위/아래를 자극했을 때 운동 진폭이 50% 이상 급감하는 '전도차단(Conduction Block)' 현상이 관찰되어 팔꿈치 부위의 직접적인 압박을 확진합니다."
            ],
            "emg_reason": [
                "자신경 지배를 받는 손 내재근(ADM, FDI)에서 활동성 탈신경 전위가 확인되어, 단순 압박을 넘어 축삭 손상이 동반되었음을 알 수 있습니다.",
                "동일한 C8-T1 분절 지배를 받지만 정중신경 지배인 APB와 목 척추주위근이 완전히 정상인 것은 척수 신경뿌리병증을 배제시킵니다."
            ],
            "integration": [
                "자신경에 국한된 팔꿈치 부위 전도차단 수치와 해당 말초 근육의 선택적 축삭 손상 데이터를 종합하여 팔꿈치굴증후군으로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "C8 신경뿌리병증 (C8 Radiculopathy)",
                "why_consider": "손 내재근(아귀힘) 약화 및 손날 부위 저림이 매우 유사하여 혼동을 줍니다.",
                "how_to_differentiate": "C8 신경뿌리병증이라면 정중신경 지배 근육(APB)도 함께 탈신경되며, 감각 전도(SNAP)는 오히려 정상으로 보존되어야 합니다."
            }
        ]
    },

    "5. 오른쪽 손목처짐 및 손등 감각 저하 (요골신경 마비)": {
        "info": {"age": 34, "sex": "남성", "symptom": "음주 후 의자에서 잔 뒤 발생한 우측 손목처짐(Wrist drop) 및 손등 저림", "side": "오른쪽(Rt)"},
        "diagnosis": "오른쪽 요골신경 마비 (Saturday Night Palsy)",
        "ncs_sensory": [
            ["노신경(Radial)", "왼쪽(Lt)", "20 μV", "2.1 ms", "정상"],
            ["노신경(Radial)", "오른쪽(Rt)", "8 μV", "3.2 ms", "비정상 (진폭감소/지연)"],
            ["정중신경(Median)", "오른쪽(Rt)", "25 μV", "2.8 ms", "정상"],
        ],
        "ncs_motor": [
            ["노신경(Radial)", "팔꿈치(Elbow)", "오른쪽(Rt)", "6.8 mV", "2.5 ms", "정상"],
            ["노신경(Radial)", "나선고랑 위(Spiral G.)", "오른쪽(Rt)", "1.5 mV", "7.1 ms", "비정상 (국소 전도차단)"],
        ],
        "emg": [
            ["긴노쪽손목폄근 (ECRL)", "C6-C7 (노신경)", "오른쪽(Rt)", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["손가락폄근 (EDC)", "C7-C8 (노신경)", "오른쪽(Rt)", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["위팔세갈래근 (Triceps)", "C7-C8 (노신경)", "오른쪽(Rt)", "Silent", "Normal recruitment", "정상 (보존됨)"],
        ],
        "teaching_diagnosis": {
            "summary": "위팔 나선고랑(Spiral groove) 부위의 오른쪽 요골신경 압박 마비",
            "ncs_reason": [
                "표재노신경 감각전도 진폭 감소와 함께, 운동신경 자극 시 나선고랑 상하부 사이에서 심한 전도차단(Conduction Block) 수치가 기록되어 물리적 압박 위치를 지시합니다."
            ],
            "emg_reason": [
                "나선고랑 하부에서 신경 지배를 받는 손목폄근과 손가락폄근은 탈신경 소견을 보입니다.",
                "나선고랑 상부에서 먼저 분지되는 위팔세갈래근(Triceps)이 정상인 것은 신경 병변이 겨드랑이나 목이 아님을 해부학적으로 증명합니다."
            ],
            "integration": [
                "위팔세갈래근의 보존, 나선고랑 부위 전도차단 데이터, 그리고 하부 폄근들의 선택적 마비 소견을 통합하여 나선고랑 부위 요골신경 마비로 확진합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "후골간신경 마비 (PIN Syndrome)",
                "why_consider": "손가락과 손목 폄이 안 되는 증상이 매우 유사합니다.",
                "how_to_differentiate": "후골간신경 마비는 순수 운동신경의 분지 마비이므로 감각 소실이 없으며 표재노신경 SNAP이 정상 수치로 기록되어야 합니다."
            }
        ]
    },

    "6. 오른쪽 엉치 방사통 및 종아리 약화 (S1 신경뿌리병증)": {
        "info": {"age": 50, "sex": "남성", "symptom": "우측 엉치에서 발바닥으로 당기는 통증, 까치발 걷기가 힘듦", "side": "오른쪽(Rt)"},
        "diagnosis": "오른쪽 S1 허리/엉치 신경뿌리병증 (Lumbosacral Radiculopathy)",
        "ncs_sensory": [
            ["장딴지신경(Sural)", "오른쪽(Rt)", "16 μV", "3.0 ms", "정상"],
            ["장딴지신경(Sural)", "왼쪽(Lt)", "17 μV", "2.9 ms", "정상"],
        ],
        "ncs_motor": [
            ["정강신경(Tibial)", "발목(Ankle)", "오른쪽(Rt)", "6.1 mV", "4.8 ms", "정상"],
            ["종아리신경(Peroneal)", "발목(Ankle)", "오른쪽(Rt)", "5.2 mV", "4.1 ms", "정상"],
        ],
        "emg": [
            ["안쪽장딴지근 (Med. Gastrocnemius)", "S1-S2", "오른쪽(Rt)", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["가자미근 (Soleus)", "S1-S2", "오른쪽(Rt)", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["큰볼기근 (Gluteus maximus)", "S1-S2", "오른쪽(Rt)", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["앞정강근 (Tibialis anterior)", "L4-L5", "오른쪽(Rt)", "Silent", "Normal recruitment", "정상"],
            ["허리 척추주위근 (Lumb. Paraspinal)", "S1", "오른쪽(Rt)", "Fibrillation/PSW", "통증으로 평가불가", "비정상 (탈신경)"],
        ],
        "teaching_diagnosis": {
            "summary": "오른쪽 S1 허리/엉치 신경뿌리병증",
            "ncs_reason": [
                "종아리 뒤쪽 및 발바닥 감각 이상이 뚜렷함에도 장딴지신경(Sural) SNAP가 양측 모두 정상으로 보존되는 전형적인 척수 신경뿌리(DRG 몸쪽) 병변 양상입니다."
            ],
            "emg_reason": [
                "정강신경 지배(장딴지근, 가자미근)와 하볼기신경 지배(큰볼기근) 등 각기 다른 말초신경의 지배를 받으나 S1 분절을 공유하는 근육들에서 동시 탈신경이 확인됩니다.",
                "S1 레벨 척추주위근의 탈신경 소견은 병변이 말초가 아닌 척수 근위부임을 확진합니다."
            ],
            "integration": [
                "장딴지신경 전도 보존 수치와, S1 분절 우세 말초 근육 및 척추주위근의 탈신경 전위 데이터를 통합하여 S1 신경뿌리병증으로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "궁둥신경병증 (Sciatic Neuropathy)",
                "why_consider": "다리 뒤쪽 통증과 종아리 근육 약화가 S1 증상과 완벽히 겹칩니다.",
                "how_to_differentiate": "말초 궁둥신경이 눌렸다면 장딴지신경 감각전도 진폭이 유의하게 감소하며, 허리 척추주위근 EMG는 반드시 정상이어야 합니다."
            }
        ]
    },

    "7. 왼쪽 발처짐 및 종아리 가쪽 무딤 (온종아리신경 마비)": {
        "info": {"age": 28, "sex": "여성", "symptom": "다리를 꼬고 오래 앉은 후 발생한 좌측 발처짐(Foot drop)과 종아리 감각 무딤", "side": "왼쪽(Lt)"},
        "diagnosis": "왼쪽 온종아리신경 마비 (Common Peroneal Neuropathy)",
        "ncs_sensory": [
            ["얕은종아리신경(Sup. Peroneal)", "오른쪽(Rt)", "16 μV", "2.8 ms", "정상"],
            ["얕은종아리신경(Sup. Peroneal)", "왼쪽(Lt)", "6 μV", "4.1 ms", "비정상 (진폭감소/지연)"],
            ["장딴지신경(Sural)", "왼쪽(Lt)", "18 μV", "3.1 ms", "정상"],
        ],
        "ncs_motor": [
            ["종아리신경(Peroneal)", "발목(Ankle)", "왼쪽(Lt)", "5.1 mV", "4.0 ms", "정상"],
            ["종아리신경(Peroneal)", "종아리뼈머리(Fib. Head)", "왼쪽(Lt)", "1.2 mV", "8.5 ms", "비정상 (국소 전도차단)"],
        ],
        "emg": [
            ["앞정강근 (Tibialis anterior)", "L4-L5 (깊은종아리)", "왼쪽(Lt)", "Silent", "No recruitment", "비정상 (동원불가/완전마비)"],
            ["긴종아리근 (Peroneus longus)", "L5-S1 (얕은종아리)", "왼쪽(Lt)", "Silent", "Reduced recruitment", "비정상 (동원감소)"],
            ["넙다리두갈래근 짧은갈래 (Biceps femoris)", "L5-S1 (궁둥)", "왼쪽(Lt)", "Silent", "Normal recruitment", "정상 (보존됨)"],
            ["허리 척추주위근 (Lumb. Paraspinal)", "L5", "왼쪽(Lt)", "Silent", "Normal recruitment", "정상"],
        ],
        "teaching_diagnosis": {
            "summary": "종아리뼈머리 부위의 왼쪽 온종아리신경 압박 마비",
            "ncs_reason": [
                "얕은종아리신경 감각전도가 저하되었고, 운동전도 검사에서 종아리뼈머리를 지날 때 급격한 진폭 감소(전도차단)가 수치로 확인되어 물리적 압박 위치가 특정됩니다."
            ],
            "emg_reason": [
                "종아리뼈머리 아래에 위치한 앞정강근과 긴종아리근은 운동단위 동원이 안되거나 대폭 감소합니다.",
                "무릎 위쪽에서 분지되는 넙다리두갈래근(짧은갈래)과 허리 척추주위근이 정상인 것은 궁둥신경이나 척추 뿌리 문제가 아님을 해부학적으로 명확히 입증합니다."
            ],
            "integration": [
                "무릎 부위 국소 전도차단 지표와, 무릎 하부 폄근/벌림근의 선택적 마비 및 상부 근육 정상 보존을 통합하여 온종아리신경 마비로 확진합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "L5 허리 신경뿌리병증",
                "why_consider": "발처짐과 발등 감각 이상 양상이 거의 동일합니다.",
                "how_to_differentiate": "L5 병변이라면 감각전도(SNAP)가 양측 대칭적으로 정상이어야 하며, 무릎 위의 근육(중둔근 등)과 척추주위근에서 비정상 소견이 나타나야 합니다."
            }
        ]
    },

    "8. 오른쪽 어깨/팔 뻐근함 및 삼두근 약화 (C7 신경뿌리병증)": {
        "info": {"age": 51, "sex": "여성", "symptom": "우측 날개뼈 안쪽 통증, 팔 뒤쪽부터 가운데 손가락까지 저림, 삼두근 힘 빠짐", "side": "오른쪽(Rt)"},
        "diagnosis": "오른쪽 C7 목 신경뿌리병증 (Cervical Radiculopathy)",
        "ncs_sensory": [
            ["정중신경 3지(Median 3rd D.)", "오른쪽(Rt)", "28 μV", "2.7 ms", "정상 (보존됨)"],
            ["정중신경 3지(Median 3rd D.)", "왼쪽(Lt)", "29 μV", "2.6 ms", "정상"],
        ],
        "ncs_motor": [
            ["노신경(Radial)", "아래팔(Forearm)", "오른쪽(Rt)", "7.1 mV", "2.5 ms", "정상"],
            ["정중신경(Median)", "손목(Wrist)", "오른쪽(Rt)", "8.8 mV", "3.2 ms", "정상"],
        ],
        "emg": [
            ["목 척추주위근 (Cerv. Paraspinal)", "C7", "오른쪽(Rt)", "Fibrillation/PSW", "통증으로 평가불가", "비정상 (활동성 탈신경)"],
            ["위팔세갈래근 (Triceps brachii)", "C7-C8 (노신경)", "오른쪽(Rt)", "Fibrillation/PSW", "Reduced recruitment", "비정상 (탈신경)"],
            ["노쪽손목굽힘근 (FCR)", "C6-C7 (정중신경)", "오른쪽(Rt)", "Fibrillation/PSW", "Reduced recruitment", "비정상 (탈신경)"],
            ["손가락폄근 (EDC)", "C7-C8 (노신경)", "오른쪽(Rt)", "Fibrillation/PSW", "Reduced recruitment", "비정상 (탈신경)"],
            ["위팔두갈래근 (Biceps brachii)", "C5-C6", "오른쪽(Rt)", "Silent", "Normal recruitment", "정상"],
        ],
        "teaching_diagnosis": {
            "summary": "오른쪽 C7 목 신경뿌리병증",
            "ncs_reason": [
                "가운데 손가락 저림이 뚜렷함에도 정중신경 3지 SNAP 진폭이 양측 모두 정상으로 유지되는 전형적인 척수 신경뿌리(근위부) 병변입니다."
            ],
            "emg_reason": [
                "C7 분절의 주요 지배를 받는 위팔세갈래근(노신경 지배)과 노쪽손목굽힘근(정중신경 지배)에서 동시 탈신경이 확인되어 말초 단일 신경 문제가 아님을 입증합니다.",
                "C7 척추주위근 탈신경 소견과, C5-6 지배인 위팔두갈래근의 정상 소견은 병변이 C7 레벨에 특정되어 있음을 확진합니다."
            ],
            "integration": [
                "감각전도 보존 현상과, C7 우세 다수 말초근육의 동시 침범, 척추주위근 침범을 통합하여 C7 신경뿌리병증으로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "요골신경 마비 (Radial Neuropathy)",
                "why_consider": "삼두근(팔꿉 폄) 약화 및 손가락 폄근 약화가 요골신경 마비 증상과 같습니다.",
                "how_to_differentiate": "요골신경 마비라면 정중신경 지배를 받는 노쪽손목굽힘근(FCR)이나 척추주위근은 정상이어야 합니다."
            }
        ]
    },

    "9. 왼쪽 갑작스러운 안면 마비 (벨마비)": {
        "info": {"age": 35, "sex": "여성", "symptom": "자고 일어난 후 좌측 얼굴 전체 마비, 이마 주름 소실 및 눈이 안 감김", "side": "왼쪽(Lt)"},
        "diagnosis": "왼쪽 특발성 얼굴신경마비 (Bell's Palsy)",
        "ncs_sensory": [
            ["삼차신경 눈신경가지(V1)", "오른쪽(Rt)", "20 μV", "2.1 ms", "정상"],
            ["삼차신경 눈신경가지(V1)", "왼쪽(Lt)", "21 μV", "2.0 ms", "정상"],
        ],
        "ncs_motor": [
            ["얼굴신경(Facial) - 코근", "오른쪽(Rt)", "3.5 mV", "2.8 ms", "정상"],
            ["얼굴신경(Facial) - 코근", "왼쪽(Lt)", "0.8 mV", "4.5 ms", "비정상 (진폭급감/지연)"],
        ],
        "emg": [
            ["눈둘레근 (Orbicularis oculi)", "얼굴신경(CN VII)", "왼쪽(Lt)", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["깨물근 (Masseter)", "삼차신경(CN V)", "왼쪽(Lt)", "Silent", "Normal recruitment", "정상"],
        ],
        "teaching_diagnosis": {
            "summary": "왼쪽 말초성 얼굴신경마비 (벨마비)",
            "ncs_reason": [
                "감각을 담당하는 삼차신경(V1)은 정상이나, 안면 근육의 운동을 담당하는 얼굴신경 CMAP 진폭이 건측(오른쪽) 대비 25% 이하로 급감하여 심각한 축삭 변성을 수치로 시사합니다."
            ],
            "emg_reason": [
                "발병 후 충분한 시간(약 2~3주)이 지나 눈둘레근에서 비정상 자발전위(활동성 탈신경)가 뚜렷하게 관찰됩니다.",
                "저작근(삼차신경 지배)은 정상이므로 뇌줄기 등 중추성 복합 뇌신경 마비가 아님을 확인합니다."
            ],
            "integration": [
                "얼굴신경 단독의 심한 진폭 감소 및 근전도 탈신경 소견을 통합하여 전형적인 말초성 벨마비로 확진합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "중추성 안면 마비 (뇌졸중 등)",
                "why_consider": "입이 돌아가고 얼굴이 비대칭인 겉모습이 매우 유사합니다.",
                "how_to_differentiate": "대뇌 피질은 이마 근육에 양측성으로 지배를 내리므로, 뇌졸중 환자는 마비측 이마에 주름을 잡을 수 있습니다. 반면 벨마비(말초성)는 이마 주름조차 짓지 못합니다."
            }
        ]
    },

    "10. 양측 발끝 저림 및 감각 소실 (다발신경병증)": {
        "info": {"age": 68, "sex": "남성", "symptom": "양 발바닥부터 무릎 아래까지 화끈거리는 대칭적 장갑-양말형 저림", "side": "양쪽(Both)"},
        "diagnosis": "대칭성 길이의존성 축삭성 다발신경병증 (Polyneuropathy)",
        "ncs_sensory": [
            ["장딴지신경(Sural)", "오른쪽(Rt)", "무반응", "측정불가", "비정상 (반응소실)"],
            ["장딴지신경(Sural)", "왼쪽(Lt)", "무반응", "측정불가", "비정상 (반응소실)"],
            ["정중신경(Median)", "오른쪽(Rt)", "16 μV", "3.6 ms", "비정상 (진폭감소)"],
            ["정중신경(Median)", "왼쪽(Lt)", "15 μV", "3.7 ms", "비정상 (진폭감소)"],
        ],
        "ncs_motor": [
            ["정강신경(Tibial)", "발목(Ankle)", "오른쪽(Rt)", "1.8 mV", "6.2 ms", "비정상 (진폭감소/지연)"],
            ["정강신경(Tibial)", "발목(Ankle)", "왼쪽(Lt)", "1.7 mV", "6.4 ms", "비정상 (진폭감소/지연)"],
        ],
        "emg": [
            ["앞정강근 (Tibialis ant.)", "L4-L5", "오른쪽(Rt)", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["앞정강근 (Tibialis ant.)", "L4-L5", "왼쪽(Lt)", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["위팔두갈래근 (Biceps)", "C5-C6", "오른쪽(Rt)", "Silent", "Normal recruitment", "정상"],
            ["위팔두갈래근 (Biceps)", "C5-C6", "왼쪽(Lt)", "Silent", "Normal recruitment", "정상"],
        ],
        "teaching_diagnosis": {
            "summary": "길이의존성 축삭성 다발신경병증 (Dying-back Polyneuropathy)",
            "ncs_reason": [
                "가장 긴 신경인 양측 다리 장딴지신경(Sural)에서 반응이 완전히 소실되고, 상대적으로 짧은 상지 정중신경은 반응이 남아있으나 진폭이 감소한 전형적인 길이의존성 패턴입니다.",
                "대칭적인 광범위 진폭 감소는 전신적인 대사성/독성 원인에 의한 축삭 퇴행을 의미합니다."
            ],
            "emg_reason": [
                "다리 원위부 근육인 양측 앞정강근에서 대칭적인 활동성 탈신경 전위가 확인됩니다.",
                "상지 근위부 근육인 위팔두갈래근은 정상인 것을 볼 때, 몸에서 가장 먼 신경 말단부터 서서히 퇴행(Dying-back)하는 기전임을 확증합니다."
            ],
            "integration": [
                "양측 다리 감각/운동 전도의 대칭적 소실 데이터와, 원위부 우세 EMG 이상 소견을 통합하여 전신성 다발신경병증으로 결론 내립니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "다발성 허리 신경뿌리병증 (Lumbar Canal Stenosis)",
                "why_consider": "양쪽 다리가 대칭적으로 저리고 힘이 빠지는 증상 때문에 척추관 협착증과 헷갈리기 쉽습니다.",
                "how_to_differentiate": "협착증에 의한 다발 뿌리병증은 말초 감각전도(SNAP)가 대부분 보존되며, EMG 상 허리 척추주위근에 양측성 탈신경 소견이 뚜렷하게 도출되어야 합니다. 반면 다발신경병증은 SNAP 소실이 핵심입니다."
            }
        ]
    }
}

def get_report_title(language: str) -> str:
    return REPORT_TITLE_EN if normalize_report_language(language) == REPORT_LANG_EN else REPORT_TITLE_KO

def get_report_subtitle(language: str) -> str:
    return REPORT_SUBTITLE_EN if normalize_report_language(language) == REPORT_LANG_EN else REPORT_SUBTITLE_KO

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
