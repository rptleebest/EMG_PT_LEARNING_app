# data/cases.py [Part 1/2]

"""
물리치료학과 학생 교육용 대표 근전도 사례 라이브러리.
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
        "category": "목 신경뿌리병증(Cervical radiculopathy)",
        "difficulty": "초중급",
        "patient": {
            "age": 57, "sex": "남성", "side": "오른쪽",
            "symptoms": [
                "뒷목(Cervical)에서 오른쪽 어깨와 아래팔 노쪽(Radial side), 엄지손가락 쪽으로 뻗치는 통증과 저림이 지속됨",
                "최근 팔꿉관절 굽힘(Flexion) 및 손목관절 폄(Extension) 동작 시 힘이 빠지는 현상 발생"
            ],
            "physical_exam": {
                "감각 검사": ["아래팔 노쪽 및 엄지/검지 쪽 감각 저하. C6 피부분절(Dermatome) 분포와 일치함"],
                "맨손근력검사(MMT)": [
                    "팔꿉관절 굽힘근: Fair (3/5) - 근육피부신경(Musculocutaneous nerve, C5-C6)",
                    "손목관절 폄근: Fair (3/5) - 노신경(Radial nerve, C6-C7)"
                ],
                "반사 검사": [
                    "위팔노근 반사(Brachioradialis reflex, C6): 감소(DRT 1+)",
                    "위팔두갈래근 반사(Biceps reflex, C5): 정상(DRT 2+) 또는 경미한 감소"
                ]
            }
        },
        "findings": {
            "노신경 표재감각신경활동전위 (Superficial Radial SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "가쪽아래팔피부신경 감각신경활동전위 (Lateral Antebrachial Cutaneous SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "근육피부신경 복합근육활동전위 (Musculocutaneous CMAP)": (NCS_NORMAL, NCS_NORMAL),
            "노신경 복합근육활동전위 (Radial CMAP)": (NCS_NORMAL, NCS_NORMAL),
            "목 척추주위근 (Cervical Paraspinal)": (EMG_NORMAL, EMG_PARASPINAL_DENERVATION),
            "위팔두갈래근 (Biceps Brachii)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "노쪽손목폄근 (Extensor Carpi Radialis)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION)
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "감각신경활동전위(SNAP)가 정상 범위로 완전히 보존됩니다. 뒤뿌리신경절(DRG)보다 몸쪽(Proximal) 병변이므로 말초 감각신경전도는 정상 범위로 도출되는 생리학적 특성을 지닙니다."
            ],
            "emg_reason": [
                "1) 휴식 시 자발활동 전기생리 판독:",
                "목 척추주위근, 위팔두갈래근, 노쪽손목폄근에서 휴식 시 비정상 자발활동전위가 관찰되어 활동성 탈신경(Active denervation)을 의미합니다.",
                "2) 수의수축 시 운동단위 동원 분석:",
                "최대 수의수축 시 위팔두갈래근과 노쪽손목폄근에서 감소된 운동단위동원 양상이 도출되어 축삭 손상을 증명합니다."
            ],
            "integration": [
                "[추정 질환] C6 중심의 목 신경뿌리병증(Cervical radiculopathy)",
                "C6 피부분절 감각 저하, 위팔노근 반사 감소, 손목관절 폄 근력 저하, 그리고 목 척추주위근육 및 먼쪽(Distal) 지배 근육의 동시 탈신경을 종합하여 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "노신경병증(Radial neuropathy)",
                "why_consider": "손목관절 폄 근력 약화와 노쪽 감각 이상이 동반되어 혼동될 수 있습니다.",
                "how_to_differentiate": "말초 노신경병증이라면 표재노신경 감각신경전도 진폭 감소가 수반되며, 목 척추주위근육 침근전도는 완전히 정상이어야 합니다."
            }
        ]
    },

    "야간 손저림과 엄지 근력 약화": {
        "category": "말초 포착신경병증",
        "difficulty": "초중급",
        "patient": {
            "age": 46, "sex": "여성", "side": "오른쪽",
            "symptoms": [
                "오른손 1, 2, 3번째 손가락 중심의 저림이 야간에 특히 심함",
                "최근 엄지손가락 벌림(Abduction) 동작 시 힘이 빠지는 현상 발생"
            ],
            "physical_exam": {
                "감각 검사": ["엄지, 검지, 중지 노쪽 절반의 손바닥 감각 둔화"],
                "맨손근력검사(MMT)": ["엄지손가락 벌림근: Good (4/5)"],
                "반사 검사": ["팔렌 검사(Phalen test) 양성, 손목 정중신경 티넬 징후(Tinel's sign) 양성"]
            }
        },
        "findings": {
            "정중신경 감각신경활동전위 (Median SNAP)": (NCS_NORMAL, NCS_DELAYED),
            "정중신경 복합근육활동전위 (Median CMAP)": (NCS_NORMAL, NCS_REDUCED),
            "짧은엄지벌림근 (Abductor Pollicis Brevis, APB)": (EMG_NORMAL, EMG_NORMAL)
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "정중신경 감각신경활동전위(SNAP)에서 잠복기 지연이 도출되어 국소 말이집탈락성 전도차단을 지시합니다.",
                "정중신경 복합근육활동전위(CMAP)에서 진폭 감소가 나타나 축삭 손상이 동반되고 있음을 뜻합니다."
            ],
            "emg_reason": [
                "1) 휴식 시 자발활동 전기생리 판독:",
                "짧은엄지벌림근(APB)에서 이상 자발전위가 검출되지 않는 전기적 침묵을 보입니다. 압박이 아직 근섬유막 탈신경을 유발할 정도는 아님을 뜻합니다."
            ],
            "integration": [
                "[추정 질환] 손목굴증후군(Carpal tunnel syndrome)",
                "야간 통증, 정중신경 전도 지연 및 손목 부위 국소 마비 징후를 종합하여 정중신경 포착 병변으로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "몸쪽 정중신경병증(Proximal median neuropathy)",
                "why_consider": "정중신경 지배 영역 근력 저하 및 저림이 흡사합니다.",
                "how_to_differentiate": "원엎침근 등 손목 상부 근육들의 침근전도검사가 정상이므로 손목 수준 포착으로 확진합니다."
            }
        ]
    },

    "위팔뼈 몸통 골절 후 손목처짐": {
        "category": "말초 포착신경병증",
        "difficulty": "초중급",
        "patient": {
            "age": 34, "sex": "남성", "side": "오른쪽",
            "symptoms": [
                "위팔뼈 몸통 골절 병력 있음",
                "골절 수술 직후 손목과 손가락을 들어 올리지 못하는 손목처짐 발생"
            ],
            "physical_exam": {
                "감각 검사": ["손등 노쪽 영역 감각 소실"],
                "맨손근력검사(MMT)": [
                    "손목관절 폄근: Poor (2/5)",
                    "손가락 폄근: Poor (2/5)"
                ],
                "반사 검사": ["위팔세갈래근 반사(Triceps reflex): 정상 (골절 상단 분지 보존)"]
            }
        },
        "findings": {
            "노신경 표재감각신경활동전위 (Superficial Radial SNAP)": (NCS_NORMAL, NCS_REDUCED),
            "노신경 복합근육활동전위 (Radial CMAP)": (NCS_NORMAL, NCS_REDUCED),
            "노쪽손목폄근 (Extensor Carpi Radialis)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "집게폄근 (Extensor Indicis Proprius, EIP)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "목 척추주위근 (Cervical Paraspinal)": (EMG_NORMAL, EMG_NORMAL)
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "표재노신경 감각신경활동전위 진폭 감소는 뒤뿌리신경절 먼쪽의 말초신경계 축삭 마비를 가리킵니다."
            ],
            "emg_reason": [
                "1) 휴식 시 자발활동 전기생리 판독:",
                "노쪽손목폄근(ECR)과 집게폄근(EIP)에서 섬유자발전위 등 탈신경이 관찰되어 압박에 기인한 축삭 단절 상태를 가리킵니다. 목 척추주위근은 정상입니다."
            ],
            "integration": [
                "[추정 질환] 위팔뼈 나선고랑 부위의 노신경병증(Radial neuropathy)",
                "팔꿉관절 폄 기능은 보존되나 먼쪽 손목 폄이 안 되고 표재노신경 이상이 동반되어 외상성 노신경 마비로 확진합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "뒤뼈사이신경병증(PIN)",
                "why_consider": "손가락 및 손목관절 폄 약화가 노신경병증과 유사합니다.",
                "how_to_differentiate": "뒤뼈사이신경은 순수 운동 분지이므로 감각 소실이 없어야 합니다. 감각 전도 변성이 있다면 주간 노신경 마비입니다."
            }
        ]
    },

    "4, 5번째 손가락 저림과 손가락 근력 약화": {
        "category": "말초 포착신경병증",
        "difficulty": "초중급",
        "patient": {
            "age": 42, "sex": "남성", "side": "오른쪽",
            "symptoms": [
                "우측 4, 5번째 손가락 감각 이상 및 새끼손가락 가쪽 통증",
                "최근 젓가락질 시 지지력 소실"
            ],
            "physical_exam": {
                "감각 검사": ["반지손가락 자쪽 절반 및 새끼손가락 감각 저하"],
                "맨손근력검사(MMT)": ["새끼손가락 벌림근: Fair (3/5)"],
                "반사 검사": ["팔꿈치 터널 주행 부위 티넬 징후 양성"]
            }
        },
        "findings": {
            "자신경 감각신경활동전위 (Ulnar SNAP)": (NCS_NORMAL, NCS_DELAYED),
            "자신경 복합근육활동전위 (Ulnar CMAP)": (NCS_NORMAL, NCS_REDUCED),
            "새끼벌림근 (Abductor Digiti Minimi, ADM)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "첫째등쪽뼈사이근 (First Dorsal Interosseous, FDI)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION)
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "자신경 감각신경 잠복기 지연 및 복합근육활동전위 진폭 저하는 팔꿈치 구간 국소 말이집탈락 및 축삭 손상을 나타냅니다."
            ],
            "emg_reason": [
                "새끼벌림근 및 첫째등쪽뼈사이근에서 휴식 시 섬유자발전위가 도출되어 자신경 지배 근육의 먼쪽 운동 축삭 변성을 지시합니다."
            ],
            "integration": [
                "[추정 질환] 팔꿈치터널증후군(Cubital tunnel syndrome)",
                "새끼손가락 감각 이상, 자신경 전도 지연 및 침근전도 이상을 융합하여 주관 포착으로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "C8-T1 목 신경뿌리병증",
                "why_consider": "손 내재근 약화가 흡사하게 관찰될 수 있습니다.",
                "how_to_differentiate": "목 신경뿌리병증은 정중신경 근육도 동시 침범되며, 표재 자신경 감각신경활동전위는 정상으로 보존됩니다."
            }
        ]
    },
    # data/cases.py [Part 2/2]

    "허리-다리 통증과 발처짐": {
        "category": "허리 신경뿌리병증(Lumbar radiculopathy)",
        "difficulty": "초중급",
        "patient": {
            "age": 61, "sex": "여성", "side": "오른쪽",
            "symptoms": [
                "허리에서 종아리 가쪽, 발등으로 뻗치는 방사통",
                "보행 시 발끝이 끌리는 발처짐(Foot drop) 발생"
            ],
            "physical_exam": {
                "감각 검사": ["종아리 가쪽 및 발등 중앙 부위 감각 둔화"],
                "맨손근력검사(MMT)": [
                    "발목관절 등굽힘근: Fair (3/5)",
                    "엉덩관절 벌림근: Good (4/5)"
                ],
                "반사 검사": ["아킬레스힘줄반사 및 무릎반사: 정상"]
            }
        },
        "findings": {
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": (NCS_NORMAL, NCS_NORMAL),
            "허리 척추주위근 (Lumbar Paraspinal)": (EMG_NORMAL, EMG_PARASPINAL_DENERVATION),
            "앞정강근 (Tibialis Anterior, TA)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "중간볼기근 (Gluteus Medius)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION)
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "얕은종아리신경 감각신경활동전위가 대칭성 정상 보존됩니다. 이는 감각 세포체가 위치한 뒤뿌리신경절보다 몸쪽인 신경뿌리 압박을 지지합니다."
            ],
            "emg_reason": [
                "허리 척추주위근, 앞정강근, 중간볼기근에서 탈신경 자발전위가 관찰됩니다. 서로 다른 신경 지배를 받으나 L5 분절을 공유하는 근육들의 동시 탈신경입니다."
            ],
            "integration": [
                "[추정 질환] L5 허리 신경뿌리병증(Lumbar radiculopathy)",
                "감각신경 보존, 요추 척추주위근 침범 및 발처짐을 통해 신경뿌리 마비로 확진합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "온종아리신경병증",
                "why_consider": "발목 등굽힘근 약화로 발처짐이 일치합니다.",
                "how_to_differentiate": "온종아리 마비는 얕은종아리신경 감각전도가 대폭 감소하며 척추주위근/중간볼기근은 완벽히 정상입니다."
            }
        ]
    },

    "정강뼈 골절로 석고붕대 후 발처짐과 발등 감각저하": {
        "category": "말초 포착신경병증",
        "difficulty": "초중급",
        "patient": {
            "age": 31, "sex": "남성", "side": "왼쪽",
            "symptoms": [
                "정강뼈 골절 석고붕대 제거 후 발처짐과 발등 감각 소실 발견"
            ],
            "physical_exam": {
                "감각 검사": ["종아리 가쪽 및 발등 부위 감각 소실"],
                "맨손근력검사(MMT)": [
                    "발목관절 등굽힘근: Poor (2/5)",
                    "발목관절 안쪽번짐근: Normal (5/5) (정강신경)"
                ],
                "반사 검사": ["무릎반사 및 아킬레스힘줄반사 정상"]
            }
        },
        "findings": {
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": (NCS_REDUCED, NCS_NORMAL),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": (NCS_REDUCED, NCS_NORMAL),
            "앞정강근 (Tibialis Anterior, TA)": (EMG_ACTIVE_DENERVATION, EMG_NORMAL),
            "긴종아리근 (Peroneus Longus)": (EMG_ACTIVE_DENERVATION, EMG_NORMAL),
            "허리 척추주위근 (Lumbar Paraspinal)": (EMG_NORMAL, EMG_NORMAL)
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "얕은종아리신경 SNAP 및 Peroneal CMAP의 동시 감소는 석고붕대에 의한 종아리뼈머리 부위의 말초 압박 마비를 입증합니다."
            ],
            "emg_reason": [
                "종아리신경이 지배하는 앞정강근 등에서 비정상 탈신경이 관찰되나 허리 척추주위근은 정상으로 신경뿌리 병변을 배제합니다."
            ],
            "integration": [
                "[추정 질환] 온종아리신경병증(Common peroneal neuropathy)",
                "정강뼈 골절 부목에 의한 압박과 종아리 지배 마비를 종합하여 말초 신경 포착으로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "L5 허리 신경뿌리병증",
                "why_consider": "발처짐 및 발등 감각 이상 양상이 비슷합니다.",
                "how_to_differentiate": "신경뿌리 마비 시 감각 전도가 정상 유지되며, 척추주위근 침범이 뚜렷하게 도출됩니다."
            }
        ]
    },

    "골반 외상 후 다리 전반 근력 약화": {
        "category": "신경얼기병증(Plexopathy)",
        "difficulty": "중급",
        "patient": {
            "age": 45, "sex": "여성", "side": "왼쪽",
            "symptoms": [
                "골반 골절 수술 후 좌측 다리 전반의 심한 근력 약화 발생"
            ],
            "physical_exam": {
                "감각 검사": ["허벅지, 종아리, 발등 등 광범위 감각 소실"],
                "맨손근력검사(MMT)": [
                    "엉덩관절 굽힘근, 무릎 폄근, 발목 굽힘근 전반: Poor (2/5)"
                ],
                "반사 검사": ["무릎 및 아킬레스힘줄반사 좌측 완전 소실"]
            }
        },
        "findings": {
            "허리 척추주위근 (Lumbar Paraspinal)": (EMG_NORMAL, EMG_NORMAL),
            "장딴지신경 감각신경활동전위 (Sural SNAP)": (NCS_REDUCED, NCS_NORMAL),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": (NCS_REDUCED, NCS_NORMAL),
            "넓적다리신경 복합근육활동전위 (Femoral CMAP)": (NCS_REDUCED, NCS_NORMAL),
            "가쪽넓은근 (Vastus Lateralis)": (EMG_ACTIVE_DENERVATION, EMG_NORMAL),
            "앞정강근 (Tibialis Anterior, TA)": (EMG_ACTIVE_DENERVATION, EMG_NORMAL)
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "다수의 주요 다리 말초 감각/운동 전도에서 진폭 감소가 확인되어 척수신경절 밖 신경얼기 장애를 시사합니다."
            ],
            "emg_reason": [
                "가쪽넓은근과 앞정강근 등 광범위한 침범이 있으나 허리 척추주위근은 정상으로 신경뿌리 파열은 아님을 밝힙니다."
            ],
            "integration": [
                "[추정 질환] 허리엉치신경얼기병증(Lumbosacral plexopathy)",
                "골반 외상 이력, 다발 감각/운동 마비, 척추주위근 보존을 결합하여 신경얼기 마비로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "다발 허리 신경뿌리병증",
                "why_consider": "복수 척수 분절의 동시 약화가 나타나 혼동하기 쉽습니다.",
                "how_to_differentiate": "신경뿌리병증은 감각 전도가 정상 유지되며, 척추주위근 침범이 매우 명확히 나타납니다."
            }
        ]
    },

    "양측 발끝 저림과 발가락 약화": {
        "category": "다발신경병증(Polyneuropathy)",
        "difficulty": "초중급",
        "patient": {
            "age": 67, "sex": "남성", "side": "양쪽",
            "symptoms": [
                "당뇨병 병력 하 양쪽 발끝에서 서서히 올라오는 대칭성 저림"
            ],
            "physical_exam": {
                "감각 검사": ["양측 발가락 끝부터 발목까지 대칭적 장갑-양말형 감각 저하"],
                "맨손근력검사(MMT)": ["양측 엄지발가락 폄근 등 먼쪽 근육 경미한 약화"],
                "반사 검사": ["양측 아킬레스힘줄반사 완전 소실"]
            }
        },
        "findings": {
            "장딴지신경 감각신경활동전위 (Sural SNAP)": (NCS_REDUCED, NCS_REDUCED),
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": (NCS_REDUCED, NCS_REDUCED),
            "정강신경 복합근육활동전위 (Tibial CMAP)": (NCS_REDUCED, NCS_REDUCED),
            "앞정강근 (Tibialis Anterior, TA)": (EMG_ACTIVE_CHRONIC, EMG_ACTIVE_CHRONIC)
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "양다리 말단 감각 및 운동 신경들에서 대칭적인 진폭 감소가 두드러지게 관찰되며 당뇨성 말초 축삭 손상과 부합합니다."
            ],
            "emg_reason": [
                "양측 다리 먼쪽 근육(앞정강근)에서 탈신경 자발전위가 대칭 분포로 유도되어 dying-back 만성 파괴를 지지합니다."
            ],
            "integration": [
                "[추정 질환] 길이 의존성 축삭성 다발신경병증(Axonal polyneuropathy)",
                "당뇨 병력, 먼쪽 장갑-양말 감각 저하, 아킬레스 반사 소실을 연결하여 축삭성 다발신경 손상으로 확진합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "말이집탈락성 다발신경병증",
                "why_consider": "상하 대칭적인 다발성 침범 양상이 유사합니다.",
                "how_to_differentiate": "말이집탈락성은 진폭 감소보다 극심한 전도 잠복기 지연 및 속도 저하가 주된 지표입니다."
            }
        ]
    },

    "대칭성 팔다리 근력저하와 보행 저하": {
        "category": "다발신경병증(Polyneuropathy)",
        "difficulty": "중급",
        "patient": {
            "age": 55, "sex": "여성", "side": "양쪽",
            "symptoms": [
                "양쪽 손과 발이 대칭적으로 저리며 보행 및 팔 사용 진행성 근력 약화"
            ],
            "physical_exam": {
                "감각 검사": ["양측 팔다리 대칭적 감각 탈락"],
                "맨손근력검사(MMT)": ["어깨, 엉덩관절, 손목, 발목 모두 전반적 Fair (3/5) 약화"],
                "반사 검사": ["전신 깊은힘줄 반사 완벽한 소실"]
            }
        },
        "findings": {
            "정중신경 감각신경활동전위 (Median SNAP)": (NCS_DELAYED, NCS_DELAYED),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": (NCS_DELAYED, NCS_DELAYED),
            "정강/종아리신경 F파 (F-wave)": (FWAVE_DELAYED_ABSENT, FWAVE_DELAYED_ABSENT),
            "앞정강근 (Tibialis Anterior, TA)": (EMG_NORMAL, EMG_NORMAL)
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "광범위한 운동/감각 신경의 잠복기 지연과 F파 소실은 신경뿌리를 포함한 다발성 말이집 탈락성 변화를 강하게 입증합니다."
            ],
            "emg_reason": [
                "침근전도에서 축삭 손상을 대변하는 비정상 자발전위가 없어 단순 말이집 손상 상태임을 지시합니다."
            ],
            "integration": [
                "[추정 질환] 만성 염증성 말이집탈락성 다발신경병증(CIDP/AIDP 계열)",
                "근위/먼쪽 전신 대칭 마비, 전신 무반사, 다발 잠복기 지연을 통해 염증성 말이집 탈락 질환으로 판단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "근육병증(Myopathy)",
                "why_consider": "어깨/엉덩이 등 몸쪽 근력 약화가 유사합니다.",
                "how_to_differentiate": "근육병증은 말단 감각 소실이 없으며 전신 반사도가 어느 정도 보존됩니다."
            }
        ]
    },

    "눈꺼풀 떨림과 눈 주위 불편감 지속": {
        "category": "뇌신경/반사경로",
        "difficulty": "중급",
        "patient": {
            "age": 62, "sex": "여성", "side": "오른쪽",
            "symptoms": ["우측 눈꺼풀 주변 간헐적 미세 떨림, 눈 가쪽 감각 저하"],
            "physical_exam": {
                "얼굴 표정근 관찰": ["이마 주름잡기, 눈 감기, 입꼬리 올리기 모두 양측 정상"],
                "뇌신경 감각 검사": ["우측 이마/눈 주변(CN V1) 감각 감소"],
                "반사 검사": ["우측 각막반사 저하"]
            }
        },
        "findings": {
            "우측 자극-우측 R1": (BLINK_DELAYED, "14.8 ms"),
            "우측 자극-우측 R2": (BLINK_DELAYED_ABSENT, "48.5 ms"),
            "우측 자극-좌측 R2": (BLINK_DELAYED_ABSENT, "49.1 ms"),
            "좌측 자극-좌측 R1": (NCS_NORMAL, "10.4 ms"),
            "좌측 자극-우측 R2": (NCS_NORMAL, "31.8 ms")
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "우측 자극 시 관련된 반사 반응이 모두 지연/소실되지만 좌측 자극 시 우측 반응이 정상이므로 삼차신경(들신경) 전도 장애를 확증합니다."
            ],
            "emg_reason": [
                "운동 단절이 아니므로 침근전도는 배제되었습니다."
            ],
            "integration": [
                "[추정 질환] 우측 삼차신경 전도 장애(Afferent trunk dysfunction)",
                "감각 저하 및 자극 시의 반사 차단을 결합하여 수용체 경로 마비로 판독합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "오른쪽 말초성 얼굴마비",
                "why_consider": "눈 감기 불편감이 얼굴마비와 혼동될 수 있습니다.",
                "how_to_differentiate": "얼굴마비(날신경 병변)라면 좌측 자극 시에도 우측 반응이 소실되어야 하나, 이 환자는 반응을 잘 수행합니다."
            }
        ]
    },

    "뇌졸중 환자 발목 경직 평가": {
        "category": "중추성 반사이상",
        "difficulty": "중급",
        "patient": {
            "age": 68, "sex": "남성", "side": "오른쪽",
            "symptoms": ["우측 뇌졸중 후 좌측 발목 경직 증가 및 첨족 보행"],
            "physical_exam": {
                "근긴장도 검사 (MAS)": ["좌측 발바닥굽힘근 MAS 3등급"],
                "반사 검사": ["좌측 아킬레스힘줄반사 항진, 발목간대경련 관찰"]
            }
        },
        "findings": {
            "좌측 가자미근 H-반사 진폭": (H_REFLEX_HYPERACTIVE, "7.2 mV"),
            "우측 가자미근 H-반사 진폭": (NCS_NORMAL, "2.1 mV"),
            "좌측 가자미근 H/M ratio 비율": (H_M_RATIO_INCREASED, "65%"),
            "우측 가자미근 H/M ratio 비율": (NCS_NORMAL, "25%")
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "H/M 비율이 좌측에서 65%로 크게 항진되어 대뇌 상위운동신경원(UMN) 손상으로 인한 척수 알파운동신경 세포의 과흥분 상태를 객관적으로 증명합니다."
            ],
            "emg_reason": [
                "말초 손상이 아니므로 침근전도는 실시하지 않았습니다."
            ],
            "integration": [
                "[추정 질환] 뇌졸중 후 좌측 하지 경직(Spasticity)",
                "MAS 3등급 임상 소견과 비정상적 H-반사 항진을 매칭시켜 중추성 척수 억제 상실로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "말초성 S1 신경뿌리병증",
                "why_consider": "동일 반사경로를 사용합니다.",
                "how_to_differentiate": "말초 신경 손상 시에는 H-반사 진폭이 커지는 것이 아니라 소실되거나 지연됩니다."
            }
        ]
    }
}
