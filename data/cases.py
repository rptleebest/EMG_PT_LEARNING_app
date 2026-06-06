# data/cases.py

"""
물리치료학과 학생 교육용 대표 근전도 사례 라이브러리.
의협 6.1판 신용어 엄격 적용 및 검사/해석의 의학적 정합성 완비.
"""

EMG_NORMAL = "emg_normal"
EMG_ACTIVE_DENERVATION = "emg_active_denervation"
EMG_PARASPINAL_DENERVATION = "emg_paraspinal_denervation"
EMG_CHRONIC_REINNERVATION = "emg_chronic_reinnervation"
EMG_ACTIVE_CHRONIC = "emg_active_chronic"

NCS_NORMAL = "ncs_normal"
NCS_DELAYED = "ncs_delayed"
NCS_REDUCED = "ncs_reduced"
NCS_ABSENT = "ncs_absent"

FWAVE_DELAYED_ABSENT = "fwave_delayed_absent"
H_REFLEX_HYPERACTIVE = "h_reflex_hyperactive"
H_M_RATIO_INCREASED = "h_m_ratio_increased"
BLINK_DELAYED = "blink_delayed"
BLINK_DELAYED_ABSENT = "blink_delayed_absent"

CASE_LIBRARY = {
    "목-팔 통증 증상과 팔 근력 약화": {
        "category": "C6 목 신경뿌리병증",
        "difficulty": "초중급",
        "patient": {
            "age": 57, "sex": "남성", "side": "왼쪽",
            "symptoms": [
                "2개월 전부터 뒷목에서 시작하여 왼쪽 어깨, 아래팔의 노쪽(바깥쪽)을 지나 엄지와 검지손가락까지 전기가 통하듯 뻗치는 극심한 방사통을 호소함.",
                "고개를 뒤로 젖히거나 왼쪽으로 돌릴 때 통증이 악화되며, 최근 물건을 쥘 때 손목에 힘이 빠지는 증상이 발생함."
            ],
            "physical_exam": {
                "감각 검사": ["왼쪽 아래팔 노쪽 및 엄지/검지 쪽 촉각 둔화 (C6 피부분절 분포 일치)"],
                "맨손근력검사(MMT)": [
                    "팔꿉관절 굽힘근(Biceps): Fair (3/5) - 근육피부신경 (C5-C6)",
                    "손목관절 폄근(ECR): Fair (3/5) - 노신경 (C6-C7)",
                    "팔꿉관절 폄근(Triceps): Normal (5/5) - 노신경 (C7 보존)"
                ],
                "반사 검사": [
                    "위팔노근 깊은힘줄반사(Brachioradialis DTR, C6): 비정상 감소",
                    "위팔두갈래근(C5) 및 위팔세갈래근(C7) 깊은힘줄반사: 정상 대칭"
                ]
            }
        },
        "findings": {
            "노신경 표재감각신경활동전위 (Superficial Radial SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "정중신경 감각신경활동전위 (Median SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "노신경 복합근육활동전위 (Radial CMAP) - 먼쪽 자극": (NCS_NORMAL, NCS_NORMAL),
            "목 척추주위근 (Cervical Paraspinal)": (EMG_PARASPINAL_DENERVATION, EMG_NORMAL),
            "위팔두갈래근 (Biceps Brachii)": (EMG_ACTIVE_DENERVATION, EMG_NORMAL),
            "노쪽손목폄근 (Extensor Carpi Radialis)": (EMG_ACTIVE_DENERVATION, EMG_NORMAL)
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "감각신경활동전위(SNAP)가 대칭적으로 정상 범위로 완전히 보존됩니다. 신경뿌리병증은 감각신경 세포체가 있는 뒤뿌리신경절(DRG)보다 몸쪽(proximal) 척수 신경뿌리에서 발생하므로, 말초 감각신경은 손상되지 않고 정상으로 측정되는 특징을 가집니다."
            ],
            "emg_reason": [
                "1) 휴식 시 비정상 자발활동",
                "목 척추주위근을 포함하여, 서로 다른 말초신경의 지배를 받지만 C6 척수 분절을 공유하는 위팔두갈래근과 노쪽손목폄근에서 활동성 탈신경 전위가 동시 관찰됩니다.",
                "2) 자발적 근수축 시 운동단위 동원",
                "최대 수축 시 위팔두갈래근과 노쪽손목폄근에서 운동단위 동원이 대폭 감소하여 실제 운동 축삭의 심각한 소실이 확인됩니다."
            ],
            "integration": [
                "🎯 C6 목 신경뿌리병증 (C6 Cervical Radiculopathy)",
                "💡 추정한 이유: 임상적으로 C6 피부분절의 감각 저하와 위팔노근 반사 감소가 명확합니다. 전기생리학적으로 말초 감각 전도는 보존되나, 침근전도에서 목 척추주위근을 포함한 C6 지배 여러 근육들에 다발성 탈신경이 확인되어 말초신경 포착이 아닌 척수 신경뿌리의 압박 병변으로 확진합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "⚖️ 노신경병증 (Radial neuropathy)",
                "how_to_differentiate": "손목 폄 약화로 인해 말초 노신경병증으로 오인할 수 있으나, 말초 마비라면 표재노신경 감각 전도 진폭이 감소해야 합니다. 또한 목 척추주위근과 위팔두갈래근은 완전히 정상이어야 하므로 감별됩니다."
            }
        ]
    },

    "야간 손저림과 엄지 근력 약화": {
        "category": "정중신경 포착병증",
        "difficulty": "초중급",
        "patient": {
            "age": 46, "sex": "여성", "side": "오른쪽",
            "symptoms": [
                "6개월 전부터 오른쪽 엄지, 검지, 중지 손가락에 타는 듯한 저림이 발생함.",
                "수면 중 야간에 통증이 극심해져 잠에서 깨어 손을 터는 행동을 반복함.",
                "최근 병뚜껑을 열거나 열쇠를 돌릴 때 엄지손가락 쪽의 힘이 빠지는 느낌을 호소함."
            ],
            "physical_exam": {
                "감각 검사": ["엄지, 검지, 중지의 손바닥 면 감각 둔화 (정중신경 분포 영역)"],
                "맨손근력검사(MMT)": ["짧은엄지벌림근: Good (4/5) - 엄지두덩 근육 경미한 위축 관찰됨"],
                "특수 검사": ["팔렌 검사(Phalen test) 양성, 손목터널 부위 티넬 징후 뚜렷한 양성"]
            }
        },
        "findings": {
            "정중신경 감각신경활동전위 (Median SNAP)": (NCS_NORMAL, NCS_DELAYED),
            "자신경 감각신경활동전위 (Ulnar SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "정중신경 복합근육활동전위 (Median CMAP) - 손목 자극": (NCS_NORMAL, NCS_REDUCED),
            "정중신경 복합근육활동전위 (Median CMAP) - 팔꿈치 자극": (NCS_NORMAL, NCS_REDUCED),
            "짧은엄지벌림근 (Abductor Pollicis Brevis)": (EMG_NORMAL, EMG_NORMAL)
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "정중신경 감각신경에서만 선택적으로 잠복기 지연이 도출되어, 손목굴(Carpal tunnel) 내 국소 말이집탈락성 전도차단 현상을 지시합니다.",
                "손목과 팔꿈치 자극 모두에서 운동신경 진폭 감소가 나타나 축삭의 변성도 일부 동반되고 있음을 뜻합니다. 인접한 자신경 전도는 정상이므로 다발성 신경병증을 배제합니다."
            ],
            "emg_reason": [
                "짧은엄지벌림근에서 비정상 자발전위가 검출되지 않고 자발적 근수축 시 동원 양상이 원활합니다. 이는 압박이 아직 근섬유막의 광범위한 탈신경을 유발할 정도의 비가역적 단계는 아님을 의미합니다."
            ],
            "integration": [
                "🎯 오른쪽 손목굴증후군 (Carpal tunnel syndrome)",
                "💡 추정한 이유: 야간 통증 및 손털기 증상, 정중신경 영역에 국한된 임상적 감각 둔화 징후가 명확합니다. 검사 결과 정중신경 먼쪽(distal) 구간의 잠복기 지연이 뚜렷하여 손목 부위 정중신경의 포착성 병변으로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "⚖️ 몸쪽 정중신경병증 (원엎침근 증후군)",
                "how_to_differentiate": "팔꿈치 아래 몸쪽(proximal) 정중신경 지배 근육들의 침근전도가 정상이며, 감각 및 운동 지연이 '손목' 구간에서만 뚜렷하게 나타나므로 몸쪽 포착과 명확히 구분됩니다."
            }
        ]
    },

    "위팔뼈 몸통 골절 후 손목처짐": {
        "category": "노신경 포착/손상",
        "difficulty": "초중급",
        "patient": {
            "age": 34, "sex": "남성", "side": "오른쪽",
            "symptoms": [
                "교통사고로 인한 오른쪽 위팔뼈 몸통(Humeral shaft) 나선형 골절로 금속판 고정 수술을 시행 받음.",
                "수술 직후 마취에서 깬 후부터 오른쪽 손목과 손가락을 전혀 위로 젖히지 못하는 손목처짐(Wrist drop) 현상이 지속됨."
            ],
            "physical_exam": {
                "감각 검사": ["오른쪽 손등 노쪽 영역(엄지와 검지 사이 웹 공간)의 감각 완전 소실"],
                "맨손근력검사(MMT)": [
                    "팔꿉관절 폄근(Triceps): Normal (5/5) - 손상 부위보다 몸쪽 분지로 기능 보존됨",
                    "손목관절 폄근(ECR): Poor (2/5) - 손목처짐 뚜렷함",
                    "손가락 폄근(EDC): Poor (2/5)"
                ],
                "반사 검사": ["위팔세갈래근 깊은힘줄반사 정상, 위팔노근 반사 비정상 감소"]
            }
        },
        "findings": {
            "노신경 표재감각신경활동전위 (Superficial Radial SNAP)": (NCS_NORMAL, NCS_REDUCED),
            "노신경 복합근육활동전위 (Radial CMAP) - 아래팔 자극": (NCS_NORMAL, NCS_REDUCED),
            "노신경 복합근육활동전위 (Radial CMAP) - 위팔 자극": (NCS_NORMAL, NCS_REDUCED),
            "노쪽손목폄근 (Extensor Carpi Radialis)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "집게폄근 (Extensor Indicis)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "목 척추주위근 (Cervical Paraspinal)": (EMG_NORMAL, EMG_NORMAL)
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "표재노신경 감각신경의 진폭 감소는 병변이 척수 신경절(DRG)보다 먼쪽(distal)에 위치한 말초신경계 축삭 손상임을 강력히 시사합니다."
            ],
            "emg_reason": [
                "위팔뼈 나선고랑 아래에서 분지하는 노쪽손목폄근과 집게폄근에 활동성 탈신경 자발전위가 뚜렷하며, 자발적 근수축 시 운동단위 동원이 현저히 감소했습니다.",
                "목 척추주위근은 정상으로 유지되어 경추 신경뿌리 질환을 완벽히 감별해 줍니다."
            ],
            "integration": [
                "🎯 나선고랑 부위 노신경병증 (Radial neuropathy at spiral groove)",
                "💡 추정한 이유: 팔꿉관절 폄 기능은 보존되었으나 먼쪽 손목과 손가락 폄근 마비가 뚜렷하며, 표재노신경 감각 이상 및 해당 근육군의 탈신경 소견이 위팔뼈 몸통 부위의 외상성 노신경 파열/손상을 확증합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "⚖️ 뒤뼈사이신경병증 (Posterior interosseous neuropathy, PIN)",
                "how_to_differentiate": "PIN은 노신경의 순수 운동 분지이므로 피부 감각 소실이 없습니다. 본 환자는 감각 전도 진폭 감소가 뚜렷하여 주간(Main trunk) 노신경 마비로 감별됩니다."
            }
        ]
    },

    "4, 5번째 손가락 저림과 손가락 근력 약화": {
        "category": "자신경 포착병증",
        "difficulty": "초중급",
        "patient": {
            "age": 42, "sex": "남성", "side": "오른쪽",
            "symptoms": [
                "3개월 전부터 오른쪽 새끼손가락과 반지손가락 절반 부위에 찌릿한 저림과 가쪽 손날 부위 통증이 발생함.",
                "최근 젓가락질을 하거나 단추를 채울 때 손가락 사이의 미세한 지지력이 떨어져 불편함을 심하게 호소함."
            ],
            "physical_exam": {
                "감각 검사": ["반지손가락 자쪽 절반 및 새끼손가락 감각 둔화 (자신경 피부분절 일치)"],
                "맨손근력검사(MMT)": [
                    "새끼손가락 벌림근(ADM): Fair (3/5)",
                    "손가락 벌림/모음근(Interossei): Fair (3/5) - 갈퀴손 변형 징후 의심됨"
                ],
                "특수 검사": ["팔꿈치 터널 주행 부위 티넬 징후 양성, 팔꿉관절 최대 굽힘 시 저림 증상 재현됨"]
            }
        },
        "findings": {
            "자신경 감각신경활동전위 (Ulnar SNAP)": (NCS_NORMAL, NCS_DELAYED),
            "정중신경 감각신경활동전위 (Median SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "자신경 복합근육활동전위 (Ulnar CMAP) - 팔목 자극": (NCS_NORMAL, NCS_NORMAL),
            "자신경 복합근육활동전위 (Ulnar CMAP) - 팔꿈치 위 자극": (NCS_NORMAL, NCS_REDUCED),
            "새끼벌림근 (Abductor Digiti Minimi)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "첫째등쪽뼈사이근 (First Dorsal Interosseous)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION)
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "자신경 감각신경 잠복기 지연이 나타나며, 운동신경 전도검사에서 손목 자극에 비해 '팔꿈치 위' 자극 시 진폭이 급감하는 국소 전도차단이 명확히 관찰됩니다.",
                "정중신경은 대조적으로 완전히 정상 수치를 보입니다."
            ],
            "emg_reason": [
                "새끼벌림근 및 첫째등쪽뼈사이근에서 휴식 시 비정상 자발전위가 도출되어 자신경 지배 근육의 먼쪽 운동 축삭 변성을 지시합니다."
            ],
            "integration": [
                "🎯 팔꿈치굴증후군 (Cubital tunnel syndrome)",
                "💡 추정한 이유: 4, 5지 감각 이상과 손 내재근 약화 증상이 있으며, 전기생리적으로 팔꿈치 구간에서의 자신경 운동 전도차단 및 해당 근육의 침근전도 이상을 융합하여 팔꿈치 주관 포착으로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "⚖️ C8-T1 목 신경뿌리병증",
                "how_to_differentiate": "목 신경뿌리병증은 자신경뿐 아니라 정중신경 근육도 동시 침범되며, 말초 감각신경 전도(SNAP)는 몸쪽 병변이므로 정상으로 보존되어야 합니다."
            }
        ]
    },

    "허리-다리 통증과 발처짐": {
        "category": "L5 허리 신경뿌리병증",
        "difficulty": "초중급",
        "patient": {
            "age": 61, "sex": "여성", "side": "오른쪽",
            "symptoms": [
                "한 달 전 무거운 화분을 든 이후 허리에서 우측 엉치, 종아리 가쪽을 타고 발등까지 전기가 통하듯 뻗치는 방사통이 시작됨.",
                "최근 걸을 때 우측 발끝이 바닥에 자꾸 걸려 넘어질 뻔한 발처짐(Foot drop) 증상이 심해짐."
            ],
            "physical_exam": {
                "감각 검사": ["우측 종아리 가쪽 및 발등 중앙 부위 감각 둔화 (L5 피부분절)"],
                "맨손근력검사(MMT)": [
                    "발목관절 등굽힘근(TA): Poor (2/5) - 깊은종아리신경",
                    "엄지발가락 폄근(EHL): Poor (2/5)",
                    "엉덩관절 벌림근(Gluteus medius): Fair (3/5) - 위볼기신경"
                ],
                "반사 검사": ["양측 무릎반사(L4) 및 아킬레스힘줄반사(S1): 정상 대칭"]
            }
        },
        "findings": {
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "장딴지신경 감각신경활동전위 (Sural SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "종아리신경 복합근육활동전위 (Peroneal CMAP) - 발목 자극": (NCS_NORMAL, NCS_NORMAL),
            "종아리신경 복합근육활동전위 (Peroneal CMAP) - 종아리뼈 자극": (NCS_NORMAL, NCS_NORMAL),
            "허리 척추주위근 (Lumbar Paraspinal)": (EMG_NORMAL, EMG_PARASPINAL_DENERVATION),
            "앞정강근 (Tibialis Anterior)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "중간볼기근 (Gluteus Medius)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION)
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "다리 감각을 담당하는 얕은종아리신경과 장딴지신경의 감각신경 전도가 완전히 보존됩니다. 이는 질환 부위가 감각 세포체가 위치한 뒤뿌리신경절(DRG)보다 몸쪽인 척수 신경뿌리 압박임을 강력히 지지합니다.",
                "운동신경 검사에서 종아리뼈머리 부위의 전도차단이 없어 말초 압박을 배제합니다."
            ],
            "emg_reason": [
                "허리 척추주위근, 앞정강근, 중간볼기근에서 탈신경 자발전위가 대거 관찰됩니다. 서로 다른 말초신경 지배를 받으나 L5 분절을 공유하는 근육들의 동시 탈신경을 의미합니다."
            ],
            "integration": [
                "🎯 L5 허리 신경뿌리병증 (L5 Lumbar radiculopathy)",
                "💡 추정한 이유: 말초 감각신경 전도가 정상 보존되고, 말초 운동 전도차단이 없으며, 침근전도에서 L5 지배 다발 근육 및 핵심적인 요추 척추주위근 침범이 확인되어 추간판 탈출 등에 의한 신경뿌리 압박으로 확진합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "⚖️ 온종아리신경병증 (Common peroneal neuropathy)",
                "how_to_differentiate": "온종아리 마비는 얕은종아리신경 감각 전도 진폭이 대폭 감소하며, 종아리뼈머리 자극 시 뚜렷한 운동 전도차단이 나타납니다. 또한 위볼기신경이 지배하는 중간볼기근과 척추주위근은 완벽히 정상으로 유지됩니다."
            }
        ]
    },
    # data/cases.py [Part 2/5]

    "정강뼈 골절로 석고붕대 후 발처짐과 발등 감각저하": {
        "category": "온종아리신경 포착병증",
        "difficulty": "초중급",
        "patient": {
            "age": 31, "sex": "남성", "side": "왼쪽",
            "symptoms": [
                "한 달 전 스키를 타다 좌측 정강뼈 몸쪽 골절을 입어 무릎 아래까지 석고붕대를 단단히 유지하였음.",
                "어제 석고붕대를 제거한 직후, 좌측 발목을 위로 들어 올리지 못하는 심한 발처짐과 발등 감각이 전혀 느껴지지 않는 증상을 호소함."
            ],
            "physical_exam": {
                "감각 검사": ["좌측 종아리 가쪽 및 발등 부위 감각 완전 소실"],
                "맨손근력검사(MMT)": [
                    "발목관절 등굽힘근(TA): Poor (2/5) - 깊은종아리신경 지배",
                    "발목관절 가쪽번짐근(Peroneus): Poor (2/5) - 얕은종아리신경 지배",
                    "발목관절 안쪽번짐근(Tibialis posterior): Normal (5/5) - 정강신경 기능 완벽히 보존됨"
                ],
                "반사 검사": ["양측 무릎반사 및 아킬레스힘줄반사 대칭적 정상"]
            }
        },
        "findings": {
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": (NCS_REDUCED, NCS_NORMAL),
            "종아리신경 복합근육활동전위 (Peroneal CMAP) - 발목 자극": (NCS_NORMAL, NCS_NORMAL),
            "종아리신경 복합근육활동전위 (Peroneal CMAP) - 종아리뼈머리 위 자극": (NCS_REDUCED, NCS_NORMAL),
            "앞정강근 (Tibialis Anterior)": (EMG_ACTIVE_DENERVATION, EMG_NORMAL),
            "긴종아리근 (Peroneus Longus)": (EMG_ACTIVE_DENERVATION, EMG_NORMAL),
            "허리 척추주위근 (Lumbar Paraspinal)": (EMG_NORMAL, EMG_NORMAL)
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "얕은종아리신경 SNAP 진폭 감소는 병변이 척수 신경절 먼쪽(distal)임을 의미하며, 종아리뼈머리 '위' 자극 시 운동신경 진폭이 크게 떨어지는 것은 피부와 가까운 종아리뼈머리 부위에서 발생한 외부 압박성 마비(전도차단)를 명확히 입증합니다."
            ],
            "emg_reason": [
                "종아리신경 분지가 지배하는 앞정강근과 긴종아리근에서 자발적 근수축 시 동원 감소 및 비정상 탈신경 전위가 뚜렷합니다. 그러나 허리 척추주위근은 조용하여 신경뿌리 병변을 완벽히 배제합니다."
            ],
            "integration": [
                "🎯 온종아리신경병증 (Common peroneal neuropathy)",
                "💡 추정한 이유: 정강뼈 부목에 의한 기계적 압박 이력, 정강신경 지배 근육(안쪽번짐)의 보존, 그리고 감각신경 전도 저하와 종아리뼈머리에서의 국소 전도차단을 종합하여 말초 신경 포착으로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "⚖️ L5 허리 신경뿌리병증",
                "how_to_differentiate": "신경뿌리 마비 시 감각 전도가 정상 수준으로 유지되며, 허리 척추주위근 및 중간볼기근(위볼기신경) 침범이 뚜렷하게 도출됩니다."
            }
        ]
    },

    "골반 외상 후 다리 전반 근력 약화": {
        "category": "신경얼기병증(Plexopathy)",
        "difficulty": "중급",
        "patient": {
            "age": 45, "sex": "여성", "side": "왼쪽",
            "symptoms": [
                "심한 골반 골절 및 고관절 탈구 수술 이후, 좌측 다리 전체를 움직이기 힘든 광범위한 근력 약화가 발생함.",
                "허벅지 앞쪽부터 종아리, 발바닥까지 전체적으로 내 살 같지 않은 감각 둔화와 심한 보행장애를 호소함."
            ],
            "physical_exam": {
                "감각 검사": ["좌측 허벅지, 종아리, 발등 등 다중 피부분절을 넘나드는 광범위 감각 소실"],
                "맨손근력검사(MMT)": [
                    "엉덩관절 굽힘근, 무릎관절 폄근(넓적다리신경): Poor (2/5)",
                    "발목관절 등굽힘근(종아리신경), 발바닥굽힘근(정강신경): Poor (2/5)"
                ],
                "반사 검사": ["무릎반사(L4) 및 아킬레스힘줄반사(S1) 좌측 완전 소실"]
            }
        },
        "findings": {
            "허리 척추주위근 (Lumbar Paraspinal)": (EMG_NORMAL, EMG_NORMAL),
            "장딴지신경 감각신경활동전위 (Sural SNAP)": (NCS_REDUCED, NCS_NORMAL),
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": (NCS_REDUCED, NCS_NORMAL),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": (NCS_REDUCED, NCS_NORMAL),
            "가쪽넓은근 (Vastus Lateralis)": (EMG_ACTIVE_DENERVATION, EMG_NORMAL),
            "앞정강근 (Tibialis Anterior)": (EMG_ACTIVE_DENERVATION, EMG_NORMAL)
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "넓적다리신경계열 및 좌골신경계열의 다수 말초 감각/운동 전도에서 진폭 감소가 일제히 확인되어 척수신경절 바깥 영역인 '신경얼기(Plexus)'의 거대 파열 장애를 시사합니다."
            ],
            "emg_reason": [
                "가쪽넓은근, 앞정강근 등 앞뒤 다리 근육의 광범위한 탈신경 침범이 있으나, 허리 척추주위근은 정상으로 유지되어 다발 신경뿌리 파열은 아님을 밝힙니다."
            ],
            "integration": [
                "🎯 허리엉치신경얼기병증 (Lumbosacral plexopathy)",
                "💡 추정한 이유: 대형 골반 외상 이력, 다리에 분포하는 여러 신경 네트워크의 동시 마비, 다발 감각신경 진폭 감소 및 척추주위근 보존 패턴을 결합하여 복합 신경얼기 손상으로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "⚖️ 다발 허리 신경뿌리병증",
                "how_to_differentiate": "신경뿌리병증은 말초 감각 전도가 정상으로 유지되며, 허리 척추주위근 침범이 매우 명확하게 관찰됩니다."
            }
        ]
    },

    "양측 발끝 저림과 발가락 약화": {
        "category": "다발신경병증(Polyneuropathy)",
        "difficulty": "초중급",
        "patient": {
            "age": 67, "sex": "남성", "side": "양쪽",
            "symptoms": [
                "20년 이상의 당뇨병 병력이 있으며 혈당 조절이 불량한 환자임.",
                "몇 년 전부터 양쪽 발끝에서 시작된 저림과 화끈거림이 점차 발목 위로 올라오고 있으며, 최근에는 걷을 때 발바닥 감각이 무뎌 구름 위를 걷는 것 같다고 호소함."
            ],
            "physical_exam": {
                "감각 검사": ["양측 발가락 끝부터 발목 상부까지 대칭적인 장갑-양말형(Glove-stocking) 감각 저하"],
                "맨손근력검사(MMT)": ["양측 발가락 폄근 및 굽힘근 등 신체 가장 먼쪽(Distal) 근육 위주 약화"],
                "반사 검사": ["양측 아킬레스힘줄반사(S1) 대칭적 완전 소실"]
            }
        },
        "findings": {
            "장딴지신경 감각신경활동전위 (Sural SNAP)": (NCS_REDUCED, NCS_REDUCED),
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": (NCS_REDUCED, NCS_REDUCED),
            "정강신경 복합근육활동전위 (Tibial CMAP)": (NCS_REDUCED, NCS_REDUCED),
            "앞정강근 (Tibialis Anterior)": (EMG_ACTIVE_CHRONIC, EMG_ACTIVE_CHRONIC)
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "다리 끝에 위치한 감각 및 운동 신경들에서 대칭적인 진폭 감소가 두드러집니다. 이는 당뇨 등 대사성 원인에 의해 길이가 가장 긴 신경 축삭 말단부터 죽어 들어가는 길이의존성(Dying-back) 양상과 부합합니다."
            ],
            "emg_reason": [
                "양측 앞정강근 등 먼쪽 근육에서 만성적인 탈신경 자발전위와 자발적 근수축 시 운동단위 동원 감소가 대칭 분포로 나타납니다."
            ],
            "integration": [
                "🎯 길이 의존성 축삭성 다발신경병증 (Length-dependent axonal polyneuropathy)",
                "💡 추정한 이유: 만성 당뇨 병력, 먼쪽 중심의 장갑-양말형 감각 저하, 먼쪽 깊은힘줄반사 소실 및 대칭성 진폭 감소 수치를 연결하여 전신적 축삭 손상으로 확진합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "⚖️ 말이집탈락성 다발신경병증",
                "how_to_differentiate": "말이집탈락성은 진폭 감소보다 전 구간의 극심한 전도 잠복기 지연 및 속도 저하가 주된 지표로 나타납니다."
            }
        ]
    },

    "상부 위팔신경얼기병증 의심": {
        "category": "신경얼기병증(Plexopathy)",
        "difficulty": "중급",
        "patient": {
            "age": 37, "sex": "여성", "side": "왼쪽",
            "symptoms": [
                "오토바이 사고로 어깨가 심하게 꺾인 직후 심한 왼쪽 어깨 통증 발생함.",
                "이후 왼쪽 어깨 벌림과 팔꿉관절 굽힘이 전혀 안 되는 뚜렷한 근력 약화를 호소함."
            ],
            "physical_exam": {
                "감각 검사": ["왼쪽 어깨 바깥쪽 및 아래팔 가쪽 감각 소실 (C5-C6 피부분절)"],
                "맨손근력검사(MMT)": [
                    "어깨세모근(Deltoid): Poor (2/5) - 겨드랑신경",
                    "위팔두갈래근(Biceps): Poor (2/5) - 근육피부신경"
                ],
                "반사 검사": ["위팔두갈래근 깊은힘줄반사 좌측 소실"]
            }
        },
        "findings": {
            "가쪽아래팔피부신경 감각신경활동전위 (Lateral antebrachial cutaneous SNAP)": (NCS_REDUCED, NCS_NORMAL),
            "겨드랑신경 복합근육활동전위 (Axillary CMAP)": (NCS_REDUCED, NCS_NORMAL),
            "근육피부신경 복합근육활동전위 (Musculocutaneous CMAP)": (NCS_REDUCED, NCS_NORMAL),
            "어깨세모근 (Deltoid)": (EMG_ACTIVE_DENERVATION, EMG_NORMAL),
            "목 척추주위근 (Cervical Paraspinal)": (EMG_NORMAL, EMG_NORMAL)
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "가쪽아래팔피부신경 감각 진폭이 비정상으로 저하되어, 병변이 뒤뿌리신경절(DRG)보다 바깥쪽인 위팔신경얼기 수준에 있음을 증명합니다.",
                "겨드랑신경과 근육피부신경(C5-C6 지배)의 운동 반응이 대폭 소실되어 상부 줄기(Upper trunk) 손상이 확인됩니다."
            ],
            "emg_reason": [
                "어깨 및 위팔 앞쪽 근육들에서 탈신경 전위가 도출되나 척수 신경뿌리 손상을 대변하는 목 척추주위근은 정상으로 유지되어 뿌리(Root) 병변을 배제합니다."
            ],
            "integration": [
                "🎯 왼쪽 상부 위팔신경얼기병증 (Upper trunk brachial plexopathy)",
                "💡 추정한 이유: 감각 전도의 뚜렷한 감소, C5-C6 분지를 아우르는 복합 근육 마비, 그러나 목 척추주위근은 완전히 정상인 패턴을 종합해 척수가 아닌 상부 신경얼기 파열/손상으로 확진합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "⚖️ C5-C6 신경뿌리병증",
                "how_to_differentiate": "신경뿌리 마비 시 말초 감각신경전도는 보존되고 목 척추주위근에 탈신경 이상이 명확하게 관찰되어야 합니다."
            }
        ]
    },

    "대칭성 팔다리 근력저하와 보행 저하": {
        "category": "다발신경병증(Polyneuropathy)",
        "difficulty": "중급",
        "patient": {
            "age": 55, "sex": "여성", "side": "양쪽",
            "symptoms": [
                "최근 수주에 걸쳐 양쪽 손과 발이 대칭적으로 저리며 보행 및 팔 사용 시 진행성 근력 약화를 호소함.",
                "다리가 무거워 계단 오르기가 특히 힘들다고 말함."
            ],
            "physical_exam": {
                "감각 검사": ["양측 팔다리 대칭적 감각 탈락"],
                "맨손근력검사(MMT)": ["어깨, 엉덩관절, 손목, 발목 모두 전반적 Fair (3/5) 약화"],
                "반사 검사": ["전신 깊은힘줄반사 완벽한 소실"]
            }
        },
        "findings": {
            "정중신경 감각신경활동전위 (Median SNAP)": (NCS_DELAYED, NCS_DELAYED),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": (NCS_DELAYED, NCS_DELAYED),
            "정강/종아리신경 F파 (F-wave)": (FWAVE_DELAYED_ABSENT, FWAVE_DELAYED_ABSENT),
            "앞정강근 (Tibialis Anterior)": (EMG_NORMAL, EMG_NORMAL)
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "광범위한 운동/감각 신경의 잠복기 지연과 F파 소실은 신경뿌리를 포함한 다발성 말이집 탈락성 변화를 강하게 입증합니다."
            ],
            "emg_reason": [
                "침근전도에서 축삭 손상을 대변하는 비정상 자발전위가 없어 단순 말이집 손상 상태임을 지시합니다."
            ],
            "integration": [
                "🎯 만성 염증성 말이집탈락성 다발신경병증 (CIDP)",
                "💡 추정한 이유: 몸쪽/먼쪽 전신 대칭 마비, 전신 무반사, 다발 잠복기 지연 및 F파 소실을 통해 염증성 말이집 탈락 질환으로 판단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "⚖️ 근육병증(Myopathy)",
                "how_to_differentiate": "근육병증은 말단 감각 소실이 없으며 전신 반사도가 어느 정도 보존됩니다."
            }
        ]
    },
