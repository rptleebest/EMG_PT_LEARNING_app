# data/cases.py

"""
물리치료학과 학생 교육용 대표 근전도 사례 라이브러리 (총 11개 사례 완벽 복원).
의협 6.1판 신용어 엄격 적용 및 임상 추론 구조 최적화
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
                "환자는 2개월 전부터 뒷목에서 시작하여 오른쪽 어깨, 아래팔의 노쪽(바깥쪽)을 지나 엄지와 검지손가락까지 전기가 통하듯 뻗치는 극심한 방사통을 호소합니다.",
                "고개를 뒤로 젖히거나 오른쪽으로 돌릴 때 통증이 악화되며, 최근에는 물건을 쥘 때 손목에 힘이 빠지는 증상을 경험했습니다."
            ],
            "physical_exam": {
                "감각 검사": ["아래팔 노쪽 및 엄지/검지 쪽 감각 둔화 (C6 피부분절 분포와 정확히 일치)"],
                "맨손근력검사(MMT)": [
                    "팔꿉관절 굽힘근(Biceps): Fair (3/5) - 근육피부신경 (C5-C6)",
                    "손목관절 폄근(ECR): Fair (3/5) - 노신경 (C6-C7)",
                    "팔꿉관절 폄근(Triceps): Normal (5/5) - 노신경 (C7-C8)"
                ],
                "반사 검사": [
                    "위팔노근 깊은힘줄반사(Brachioradialis DTR, C6): 감소",
                    "위팔두갈래근(C5) 및 위팔세갈래근(C7) 반사: 정상"
                ]
            }
        },
        "findings": {
            "노신경 표재감각신경활동전위 (Superficial Radial SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "정중신경 감각신경활동전위 (Median SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "근육피부신경 복합근육활동전위 (Musculocutaneous CMAP)": (NCS_NORMAL, NCS_NORMAL),
            "목 척추주위근 (Cervical Paraspinal)": (EMG_NORMAL, EMG_PARASPINAL_DENERVATION),
            "위팔두갈래근 (Biceps Brachii)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "노쪽손목폄근 (Extensor Carpi Radialis)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION)
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "감각신경활동전위(SNAP)가 대칭적으로 정상 범위로 완전히 보존됩니다. 신경뿌리병증은 감각신경 세포체가 있는 뒤뿌리신경절(DRG)보다 몸쪽(Proximal)에서 발생하므로, 말초 감각신경은 손상되지 않고 정상으로 측정되는 특징을 가집니다."
            ],
            "emg_reason": [
                "목 척추주위근을 포함하여, 서로 다른 말초신경의 지배를 받지만 C6 척수 분절을 공유하는 위팔두갈래근, 노쪽손목폄근에서 활동성 탈신경(Active denervation) 전위가 동시 관찰됩니다.",
                "최대 수축 시 위팔두갈래근과 노쪽손목폄근에서 운동단위 동원이 감소하여 실제 운동 축삭의 소실이 확인됩니다."
            ],
            "integration": [
                "▶ 추정 질환: C6 목 신경뿌리병증 (C6 Cervical Radiculopathy)",
                "▶ 추정 근거: 임상적으로 C6 피부분절의 감각 저하와 위팔노근 반사 감소가 관찰됩니다. 전기생리학적으로 말초 감각 전도는 보존되나, 침근전도에서 척추주위근을 포함한 C6 지배 근육들에 다발성 탈신경이 확인되어 말초신경이 아닌 척수 신경뿌리의 압박 병변으로 확진할 수 있습니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "▶ 노신경병증 (Radial neuropathy)",
                "how_to_differentiate": "말초 노신경병증이라면 표재노신경 감각 전도 진폭이 감소해야 하며, 목 척추주위근과 근육피부신경 지배인 위팔두갈래근은 완전히 정상이어야 합니다."
            }
        ]
    },

    "야간 손저림과 엄지 근력 약화": {
        "category": "말초 포착신경병증",
        "difficulty": "초중급",
        "patient": {
            "age": 46, "sex": "여성", "side": "오른쪽",
            "symptoms": [
                "환자는 6개월 전부터 오른쪽 엄지, 검지, 중지 손가락에 타는 듯한 저림을 호소합니다. 이 증상은 수면 중 야간에 극심해져 잠에서 깨어 손을 터는 행동을 반복합니다.",
                "최근에는 병뚜껑을 열거나 열쇠를 돌릴 때 엄지손가락 쪽의 힘이 빠지는 느낌을 받고 있습니다."
            ],
            "physical_exam": {
                "감각 검사": ["엄지, 검지, 중지의 손바닥 면 감각 둔화 (정중신경 분포 영역)"],
                "맨손근력검사(MMT)": ["짧은엄지벌림근: Good (4/5) - 엄지두덩(Thenar) 근육 경미한 위축"],
                "특수 검사": ["팔렌 검사(Phalen test) 양성, 손목터널 부위 티넬 징후(Tinel's sign) 양성"]
            }
        },
        "findings": {
            "정중신경 감각신경활동전위 (Median SNAP)": (NCS_NORMAL, NCS_DELAYED),
            "자신경 감각신경활동전위 (Ulnar SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "정중신경 복합근육활동전위 (Median CMAP)": (NCS_NORMAL, NCS_REDUCED),
            "짧은엄지벌림근 (Abductor Pollicis Brevis, APB)": (EMG_NORMAL, EMG_NORMAL)
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "정중신경 감각신경에서만 선택적으로 잠복기 지연이 도출되어, 손목굴(Carpal tunnel) 내 국소 말이집탈락성 전도차단을 지시합니다.",
                "인접한 자신경 전도는 정상으로 측정되어 다발성 질환을 배제합니다."
            ],
            "emg_reason": [
                "짧은엄지벌림근(APB)에서 비정상 자발전위가 검출되지 않고 자발적 근수축이 원활합니다. 이는 압박이 감각신경 위주로 발생했으며, 아직 근섬유의 비가역적 축삭 변성 단계로는 진입하지 않았음을 의미합니다."
            ],
            "integration": [
                "▶ 추정 질환: 오른쪽 손목굴증후군 (Carpal tunnel syndrome)",
                "▶ 추정 근거: 야간 통증 및 손털기 증상, 정중신경 영역에 국한된 임상적 마비 징후가 있으며, 검사 결과 정중신경 먼쪽(Distal) 구간의 잠복기 지연이 명확하여 손목 부위 정중신경 포착으로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "▶ 원엎침근 증후군 (Pronator teres syndrome)",
                "how_to_differentiate": "원엎침근 등 팔꿈치 아래 몸쪽(Proximal) 정중신경 지배 근육들의 근전도가 정상이며, 감각 지연이 손목 구간에서 뚜렷하게 나타나므로 몸쪽 포착과 구분됩니다."
            }
        ]
    },

    "위팔뼈 몸통 골절 후 손목처짐": {
        "category": "말초 포착신경병증",
        "difficulty": "초중급",
        "patient": {
            "age": 34, "sex": "남성", "side": "오른쪽",
            "symptoms": [
                "교통사고로 인한 오른쪽 위팔뼈 몸통(Humeral shaft) 나선형 골절로 금속판 고정 수술을 받았습니다.",
                "수술 직후 마취에서 깬 후부터 오른쪽 손목과 손가락을 전혀 위로 젖히지 못하는 손목처짐(Wrist drop) 현상이 지속되고 있습니다."
            ],
            "physical_exam": {
                "감각 검사": ["오른쪽 손등 노쪽 영역(엄지와 검지 사이 웹 공간)의 감각 완전 소실"],
                "맨손근력검사(MMT)": [
                    "팔꿉관절 폄근(Triceps): Normal (5/5) - 손상 부위보다 몸쪽 분지",
                    "손목관절 폄근(ECR): Poor (2/5) - 손목처짐 뚜렷",
                    "손가락 폄근(EDC): Poor (2/5)"
                ],
                "반사 검사": ["위팔세갈래근 반사 정상, 위팔노근 반사 감소"]
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
                "표재노신경 감각신경의 진폭 감소는 병변이 척수 신경절보다 먼쪽(Distal)에 위치한 말초신경계 축삭 손상임을 강력히 시사합니다."
            ],
            "emg_reason": [
                "위팔뼈 나선고랑 아래에서 분지하는 노쪽손목폄근과 집게폄근에 비정상 자발전위(활동성 탈신경)가 뚜렷합니다.",
                "목 척추주위근은 정상으로 유지되어 경추부 질환을 감별해 줍니다."
            ],
            "integration": [
                "▶ 추정 질환: 나선고랑 부위 노신경병증 (Radial neuropathy at spiral groove)",
                "▶ 추정 근거: 팔꿉관절 폄 기능은 보존되었으나 먼쪽 손목과 손가락 폄근 마비가 뚜렷하며, 표재노신경 감각 이상 및 해당 근육 탈신경 소견이 위팔뼈 몸통 부위의 외상성 노신경 파열/손상을 확증합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "▶ 뒤뼈사이신경병증 (Posterior interosseous neuropathy, PIN)",
                "how_to_differentiate": "PIN은 노신경의 순수 운동 분지이므로 감각 소실이 없습니다. 본 환자는 감각 전도 진폭 감소가 뚜렷하여 주간(Main trunk) 노신경 마비로 감별됩니다."
            }
        ]
    },
    # data/cases.py [Part 2/6]

    "4, 5번째 손가락 저림과 손가락 근력 약화": {
        "category": "말초 포착신경병증",
        "difficulty": "초중급",
        "patient": {
            "age": 42, "sex": "남성", "side": "오른쪽",
            "symptoms": [
                "환자는 3개월 전부터 우측 새끼손가락과 반지손가락의 절반 부위에 찌릿한 저림과 가쪽 손날 부위 통증을 호소합니다.",
                "최근 젓가락질을 하거나 단추를 채울 때 손가락 사이의 미세한 지지력이 떨어져 불편함을 겪고 있습니다."
            ],
            "physical_exam": {
                "감각 검사": ["반지손가락 자쪽 절반 및 새끼손가락 감각 둔화 (자신경 피부분절)"],
                "맨손근력검사(MMT)": [
                    "새끼손가락 벌림근(ADM): Fair (3/5)",
                    "손가락 벌림/모음근(Interossei): Fair (3/5) - 갈퀴손(Claw hand) 징후 의심"
                ],
                "특수 검사": ["팔꿈치 터널 주행 부위 티넬 징후 양성, 팔꿉관절 최대 굽힘 시 증상 재현"]
            }
        },
        "findings": {
            "자신경 감각신경활동전위 (Ulnar SNAP)": (NCS_NORMAL, NCS_DELAYED),
            "정중신경 감각신경활동전위 (Median SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "자신경 복합근육활동전위 (Ulnar CMAP)": (NCS_NORMAL, NCS_REDUCED),
            "새끼벌림근 (Abductor Digiti Minimi, ADM)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "첫째등쪽뼈사이근 (First Dorsal Interosseous, FDI)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION)
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "자신경 감각신경 잠복기 지연 및 복합근육활동전위 진폭 저하는 팔꿈치 구간 국소 말이집탈락 및 축삭 손상을 나타냅니다.",
                "정중신경은 대조적으로 완전히 정상입니다."
            ],
            "emg_reason": [
                "새끼벌림근 및 첫째등쪽뼈사이근에서 휴식 시 비정상 자발전위가 도출되어 자신경 지배 근육의 먼쪽(Distal) 운동 축삭 변성을 지시합니다."
            ],
            "integration": [
                "▶ 추정 질환: 팔꿈치굴증후군 (Cubital tunnel syndrome)",
                "▶ 추정 근거: 4, 5지 감각 이상과 손 내재근 약화 증상이 있으며, 전기생리적으로 자신경에 국한된 잠복기 지연 및 침근전도 이상을 융합하여 팔꿈치 주관 포착으로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "▶ C8-T1 목 신경뿌리병증",
                "how_to_differentiate": "목 신경뿌리병증은 자신경뿐 아니라 정중신경 근육도 동시 침범되며, 말초 감각신경 전도는 몸쪽 병변이므로 정상으로 보존됩니다."
            }
        ]
    },

    "허리-다리 통증과 발처짐": {
        "category": "허리 신경뿌리병증(Lumbar radiculopathy)",
        "difficulty": "초중급",
        "patient": {
            "age": 61, "sex": "여성", "side": "오른쪽",
            "symptoms": [
                "한 달 전 무거운 화분을 든 이후 허리에서 우측 엉치, 종아리 가쪽을 타고 발등까지 전기가 통하듯 뻗치는 방사통이 시작되었습니다.",
                "최근 걸을 때 우측 발끝이 바닥에 자꾸 걸려 넘어질 뻔한 발처짐(Foot drop) 증상이 생겼습니다."
            ],
            "physical_exam": {
                "감각 검사": ["우측 종아리 가쪽 및 발등 중앙 부위 감각 둔화 (L5 피부분절)"],
                "맨손근력검사(MMT)": [
                    "발목관절 등굽힘근(TA): Fair (3/5)",
                    "엄지발가락 폄근(EHL): Poor (2/5)",
                    "엉덩관절 벌림근(Gluteus medius): Good (4/5)"
                ],
                "반사 검사": ["양측 무릎반사(L4) 및 아킬레스힘줄반사(S1): 정상 대칭"]
            }
        },
        "findings": {
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "장딴지신경 감각신경활동전위 (Sural SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": (NCS_NORMAL, NCS_NORMAL),
            "허리 척추주위근 (Lumbar Paraspinal)": (EMG_NORMAL, EMG_PARASPINAL_DENERVATION),
            "앞정강근 (Tibialis Anterior, TA)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "중간볼기근 (Gluteus Medius)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION)
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "다리 감각을 담당하는 얕은종아리신경과 장딴지신경의 감각신경 전도가 완전히 보존됩니다. 이는 뒤뿌리신경절(DRG) 상위인 신경뿌리의 압박을 강력히 지지합니다."
            ],
            "emg_reason": [
                "허리 척추주위근, 앞정강근, 중간볼기근에서 탈신경 자발전위가 대거 관찰됩니다. 깊은종아리신경(TA)과 위볼기신경(Gluteus) 등 서로 다른 신경 지배를 받으나 L5 분절을 공유하는 근육들의 동시 탈신경입니다."
            ],
            "integration": [
                "▶ 추정 질환: L5 허리 신경뿌리병증 (L5 Lumbar radiculopathy)",
                "▶ 추정 근거: 말초 감각신경 전도가 정상 보존되고, 침근전도에서 L5 지배 다발 근육 및 핵심적인 요추 척추주위근 침범이 확인되어 척수 신경뿌리 압박으로 확진합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "▶ 온종아리신경병증 (Common peroneal neuropathy)",
                "how_to_differentiate": "온종아리 마비는 얕은종아리신경 감각 전도 진폭이 대폭 감소하며, 위볼기신경이 지배하는 중간볼기근과 척추주위근은 완벽히 정상으로 유지됩니다."
            }
        ]
    },

    "정강뼈 골절로 석고붕대 후 발처짐과 발등 감각저하": {
        "category": "말초 포착신경병증",
        "difficulty": "초중급",
        "patient": {
            "age": 31, "sex": "남성", "side": "왼쪽",
            "symptoms": [
                "환자는 한 달 전 스키를 타다 좌측 정강뼈 몸쪽 골절을 입어 무릎 아래까지 깁스(Cast)를 유지했습니다.",
                "어제 깁스를 제거한 직후, 좌측 발목을 위로 들어 올리지 못하는 발처짐과 발등의 감각이 전혀 느껴지지 않는 증상을 발견했습니다."
            ],
            "physical_exam": {
                "감각 검사": ["좌측 종아리 가쪽 및 발등 부위 감각 완전 소실"],
                "맨손근력검사(MMT)": [
                    "발목관절 등굽힘근(TA): Poor (2/5)",
                    "발목관절 가쪽번짐근(Peroneus): Poor (2/5)",
                    "발목관절 안쪽번짐근(Tibialis posterior): Normal (5/5) (정강신경 기능 보존)"
                ],
                "반사 검사": ["양측 무릎반사 및 아킬레스힘줄반사 정상"]
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
                "얕은종아리신경 SNAP 및 Peroneal CMAP의 동시 진폭 감소는 석고붕대에 의해 피부와 가까운 종아리뼈머리 부위에서 발생한 외부 압박성 마비(축삭 손상 동반)를 입증합니다."
            ],
            "emg_reason": [
                "종아리신경 분지가 지배하는 앞정강근과 긴종아리근에서 비정상 탈신경 전위가 뚜렷합니다. 그러나 허리 척추주위근은 조용(Silent)하여 신경뿌리 병변을 완벽히 배제합니다."
            ],
            "integration": [
                "▶ 추정 질환: 온종아리신경병증 (Common peroneal neuropathy)",
                "▶ 추정 근거: 정강뼈 부목에 의한 기계적 압박 이력, 정강신경 지배 근육(안쪽번짐)의 보존, 그리고 감각신경 전도 저하와 종아리 지배 근육군 약화를 종합하여 말초 신경 포착으로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "▶ L5 허리 신경뿌리병증",
                "how_to_differentiate": "신경뿌리 마비 시 감각 전도가 정상 수준으로 유지되며, 허리 척추주위근 및 중간볼기근 침범이 뚜렷하게 도출됩니다."
            }
        ]
    },
    # data/cases.py [Part 3/6]

    "골반 외상 후 다리 전반 근력 약화": {
        "category": "신경얼기병증(Plexopathy)",
        "difficulty": "중급",
        "patient": {
            "age": 45, "sex": "여성", "side": "왼쪽",
            "symptoms": [
                "심한 골반 골절 및 고관절 탈구 수술 이후, 좌측 다리 전체를 움직이기 힘든 광범위한 근력 약화가 발생했습니다.",
                "허벅지 앞쪽부터 종아리, 발바닥까지 전체적으로 내 살 같지 않은 감각 둔화와 심한 보행장애를 호소합니다."
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
            "앞정강근 (Tibialis Anterior, TA)": (EMG_ACTIVE_DENERVATION, EMG_NORMAL)
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "넓적다리신경계열 및 좌골신경계열의 다수 말초 감각/운동 전도에서 진폭 감소가 일제히 확인되어 척수신경절 바깥 영역인 '신경얼기'의 거대 파열 장애를 시사합니다."
            ],
            "emg_reason": [
                "가쪽넓은근, 앞정강근 등 앞뒤 다리 근육의 광범위한 탈신경 침범이 있으나, 허리 척추주위근은 정상으로 유지되어 다발 신경뿌리 파열은 아님을 밝힙니다."
            ],
            "integration": [
                "▶ 추정 질환: 허리엉치신경얼기병증 (Lumbosacral plexopathy)",
                "▶ 추정 근거: 대형 골반 외상 이력, 다리에 분포하는 여러 신경 네트워크의 동시 마비, 다발 감각신경 진폭 감소 및 척추주위근 보존 패턴을 결합하여 복합 신경얼기 손상으로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "▶ 다발 허리 신경뿌리병증",
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
                "20년 이상의 당뇨병 병력이 있으며 혈당 조절이 불량한 환자입니다.",
                "몇 년 전부터 양쪽 발끝에서 시작된 저림과 화끈거림이 점차 발목 위로 올라오고 있으며, 최근에는 걷을 때 발바닥 감각이 무뎌 구름 위를 걷는 것 같다고 합니다."
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
            "앞정강근 (Tibialis Anterior, TA)": (EMG_ACTIVE_CHRONIC, EMG_ACTIVE_CHRONIC)
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "다리 끝에 위치한 감각 및 운동 신경들에서 대칭적인 진폭 감소가 두드러집니다. 이는 당뇨 등 대사성 원인에 의해 길이가 가장 긴 신경 축삭 말단부터 죽어 들어가는 Dying-back 양상과 부합합니다."
            ],
            "emg_reason": [
                "양측 앞정강근 등 먼쪽 근육에서 만성적인 탈신경 자발전위와 운동단위 동원 감소가 대칭 분포로 나타납니다."
            ],
            "integration": [
                "▶ 추정 질환: 길이 의존성 축삭성 다발신경병증 (Length-dependent axonal polyneuropathy)",
                "▶ 추정 근거: 만성 당뇨 병력, 먼쪽 중심의 장갑-양말형 감각 저하, 먼쪽 반사 소실 및 대칭성 진폭 감소 수치를 연결하여 전신적 축삭 손상으로 확진합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "▶ 말이집탈락성 다발신경병증",
                "how_to_differentiate": "말이집탈락성은 진폭 감소보다 전 구간의 극심한 전도 잠복기 지연 및 속도 저하가 주된 지표로 나타납니다."
            }
        ]
    },

    "대칭성 팔다리 근력저하와 보행 저하": {
        "category": "다발신경병증(Polyneuropathy)",
        "difficulty": "중급",
        "patient": {
            "age": 55, "sex": "여성", "side": "양쪽",
            "symptoms": [
                "최근 수주에 걸쳐 양쪽 손과 발이 대칭적으로 저리며 보행 및 팔 사용 시 진행성 근력 약화를 호소합니다.",
                "다리가 무거워 계단 오르기가 특히 힘들다고 말합니다."
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
                "▶ 추정 질환: 만성 염증성 말이집탈락성 다발신경병증 (CIDP)",
                "▶ 추정 근거: 몸쪽/먼쪽 전신 대칭 마비, 전신 무반사, 다발 잠복기 지연 및 F파 소실을 통해 염증성 말이집 탈락 질환으로 판단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "▶ 근육병증(Myopathy)",
                "how_to_differentiate": "근육병증은 말단 감각 소실이 없으며 전신 반사도가 어느 정도 보존됩니다."
            }
        ]
    },

    "눈꺼풀 떨림과 눈 주위 불편감 지속": {
        "category": "뇌신경/반사경로",
        "difficulty": "중급",
        "patient": {
            "age": 62, "sex": "여성", "side": "오른쪽",
            "symptoms": [
                "우측 눈꺼풀과 그 주변에 간헐적인 미세 떨림이 2주간 지속되고 있습니다.",
                "거울을 볼 때 얼굴이 비뚤어지지는 않았으나, 우측 이마와 눈 가쪽을 만질 때 내 살 같지 않은 둔한 느낌이 듭니다."
            ],
            "physical_exam": {
                "얼굴 표정근 관찰": ["이마 주름잡기, 눈 꽉 감기, 입꼬리 올리기 모두 양측 대칭 및 정상 (얼굴마비 배제)"],
                "뇌신경 감각 검사": ["우측 이마 및 눈 주변(삼차신경 V1 분지) 촉각 감소"],
                "반사 검사": ["우측 각막반사(Corneal reflex) 유발 시 지연 및 약화 관찰"]
            }
        },
        "findings": {
            "눈깜빡반사 오른쪽 자극-오른쪽 R1": (BLINK_DELAYED, "14.8 ms"),
            "눈깜빡반사 오른쪽 자극-오른쪽 R2": (BLINK_DELAYED_ABSENT, "48.5 ms"),
            "눈깜빡반사 오른쪽 자극-왼쪽 R2": (BLINK_DELAYED_ABSENT, "49.1 ms"),
            "눈깜빡반사 왼쪽 자극-왼쪽 R1": (NCS_NORMAL, "10.4 ms"),
            "눈깜빡반사 왼쪽 자극-왼쪽 R2": (NCS_NORMAL, "32.1 ms"),
            "눈깜빡반사 왼쪽 자극-오른쪽 R2": (NCS_NORMAL, "31.8 ms")
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "오른쪽 자극 시 관련된 반사 반응(Rt R1, Rt R2, Lt R2)이 모두 지연되거나 반사 유발이 소실되었습니다.",
                "반면 왼쪽 자극 시에는 동측 반응뿐 아니라 건너편 오른쪽 반응(Rt R2)도 완전히 정상 도출되었습니다.",
                "이는 반응을 만들어내는 얼굴신경(날신경)은 정상이지만, 자극을 감지해 뇌줄기로 보내는 삼차신경(들신경) 오른쪽 가지에 전도 장애가 있음을 확증합니다."
            ],
            "emg_reason": [
                "본 사례는 운동 단절이 수반되지 않은 반사궁 전도 결손이므로 침근전도는 실시되지 않았습니다."
            ],
            "integration": [
                "▶ 추정 질환: 오른쪽 삼차신경 전도 장애 (Trigeminal afferent pathway dysfunction)",
                "▶ 추정 근거: 얼굴 표정근의 정상 기능, 우측 이마 감각 저하, 그리고 눈깜빡반사에서 자극 측에 따른 반응 차이를 결합하여 삼차신경(V1) 손상으로 판독합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "▶ 오른쪽 말초성 얼굴마비 (Bell's palsy)",
                "how_to_differentiate": "얼굴마비(날신경 병변)라면 왼쪽을 자극했을 때도 오른쪽 눈을 감는 반응(Rt R2)이 소실되어야 하나, 이 환자는 왼쪽 자극 시 오른쪽 반응을 잘 수행합니다."
            }
        ]
    },

    "뇌졸중 환자 발목 경직 평가": {
        "category": "중추성 반사이상",
        "difficulty": "중급",
        "patient": {
            "age": 68, "sex": "남성", "side": "왼쪽",
            "symptoms": [
                "1년 전 오른쪽 대뇌 반구 뇌졸중 발병 후, 좌측 편마비가 남은 환자입니다.",
                "좌측 발목 장딴지 근육의 뻣뻣한 강직이 심해져 보행 시 발끝으로 걷는 첨족(Toe walking) 현상이 심해 물리치료실에 내원했습니다."
            ],
            "physical_exam": {
                "근긴장도 검사 (MAS)": ["왼쪽 발목 발바닥굽힘근(가자미근) MAS 3등급 (심한 경직)"],
                "반사 검사": [
                    "왼쪽 아킬레스힘줄반사: 비정상적 항진 (DRT 4+)",
                    "왼쪽 발목간대경련(Ankle clonus): 지속적 관찰"
                ]
            }
        },
        "findings": {
            "가자미근 H-반사 (H-reflex)": (H_REFLEX_HYPERACTIVE, NCS_NORMAL),
            "가자미근 H/M 비율 (H/M Ratio)": (H_M_RATIO_INCREASED, "25%")
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "H-반사는 척수 반사회로의 흥분성을 평가하는 특수 검사입니다.",
                "정상측(우측) H/M 비율은 25%이나, 편마비측(좌측) H/M 비율이 65%로 폭발적으로 항진되었습니다. 이는 뇌 피질에서 척수를 눌러주던 상위 억제 시스템이 파괴되어 척수 알파운동신경원 세포가 과흥분 상태에 빠졌음을 수치로 입증합니다."
            ],
            "emg_reason": [
                "말초 손상이 아니며 중추성 경직 정량화를 목적으로 하였으므로 침근전도는 실시하지 않습니다."
            ],
            "integration": [
                "▶ 추정 질환: 위운동신경세포 증후군에 의한 왼쪽 하지 경직 (Spasticity from UMN syndrome)",
                "▶ 추정 근거: MAS 3등급 임상 소견과 비정상적 H-반사 항진, 높은 H/M 비율을 매칭시켜 중추성 척수 억제 상실로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "▶ 말초성 S1 신경뿌리병증",
                "how_to_differentiate": "S1 신경뿌리가 파괴되는 말초 질환이라면 반사 경로가 끊겨 H-반사 진폭이 커지는 것이 아니라 반대로 완전히 소실되거나 지연됩니다."
            }
        ]
    }
}
