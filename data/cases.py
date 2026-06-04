# data/cases.py

"""
물리치료학과 학생 교육용 대표 근전도 사례 라이브러리 (총 11개 전체 수록).
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
            "age": 57,
            "sex": "남성",
            "side": "오른쪽",
            "symptoms": [
                "뒷목(Cervical)에서 오른쪽 어깨와 아래팔 노쪽(Radial side), 엄지손가락 쪽으로 뻗치는 통증과 저림이 지속됨",
                "최근 팔꿉관절 굽힘(Flexion) 및 손목관절 폄(Extension) 동작 시 힘이 빠지는 현상 발생"
            ],
            "physical_exam": {
                "감각 검사": [
                    "아래팔 노쪽 및 엄지/검지 쪽 감각 저하. C6 피부분절(Dermatome) 분포와 일치함"
                ],
                "맨손근력검사(MMT)": [
                    "팔꿉관절 굽힘근: Fair (3/5) - 근육피부신경(Musculocutaneous nerve, C5-C6)",
                    "손목관절 폄근: Fair (3/5) - 노신경(Radial nerve, C6-C7)",
                    "팔꿉관절 폄근: Normal (5/5) - 노신경(Radial nerve, C7-C8)"
                ],
                "반사 검사": [
                    "위팔노근 반사(Brachioradialis reflex, C6): 감소(DRT 1+)",
                    "위팔두갈래근 반사(Biceps reflex, C5): 정상(DRT 2+) 또는 경미한 감소",
                    "위팔세갈래근 반사(Triceps reflex, C7): 정상(DRT 2+)"
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
            "summary": "C6 중심의 목 신경뿌리병증(Cervical radiculopathy) 패턴입니다.",
            "ncs_reason": [
                "감각신경활동전위(SNAP)가 정상 범위로 완전히 보존됩니다. 목 신경뿌리병증은 뒤뿌리신경절보다 몸쪽에 병변이 위치하므로, 축삭 손상이 먼쪽 감각신경선까지 진행되지 않아 말초 감각신경전도검사 결과는 정상 범위로 도출되는 생리학적 특성을 지닙니다.",
                "운동신경전도검사의 복합근육활동전위가 정상 범위이므로 말초 신경얼기 혹은 단일 신경병증 가능성은 배제됩니다."
            ],
            "emg_reason": [
                "1) 휴식 시 자발활동 전기생리 판독:",
                "목 척추주위근육, 위팔두갈래근, 노쪽손목폄근에서 휴식 시 섬유자발전위 및 양성예파의 비정상 자발활동전위가 관찰됩니다. 이는 C6 운동신경 축삭 손상으로 지배력을 유실한 먼쪽 근섬유막 전체에 과흥분성 전기적 불안정성이 초래되었음을 뜻하는 활동성 탈신경 지표입니다.",
                "2) 수의수축 시 운동단위 동원 분석:",
                "최대 수의수축 시 위팔두갈래근과 노쪽손목폄근에서 감소된 운동단위동원 양상이 도출되어 동원 가능한 건강한 운동단위 수 자체가 크게 탈락했음을 증명합니다. 목 척추주위근육은 날카로운 통증으로 인해 수의수축 평가가 불가합니다.",
                "목 신경뿌리병증의 생리학적 감별 포인트:",
                "1) 감각 소실 영역이 C5 피부분절이 아닌 C6 피부분절에 명확히 일치합니다.",
                "2) 맨손근력검사 상 C5 지배 어깨세모근의 마비가 없고, C6 및 C7의 중첩 지배를 받는 노쪽손목폄근의 근력이 3/5로 동반 위축되어 있습니다.",
                "3) 반사 검사 상 C5 위주의 위팔두갈래근 반사는 보존되었으나, C6 전형인 위팔노근 반사는 유의미하게 저하되어 최종적으로 C6 목 신경뿌리병증으로 해석하는 것이 전기생리학적으로 부합합니다."
            ],
            "integration": [
                "C6 피부분절 감각 저하, 위팔노근 반사 감소, 손목관절 폄 근력의 저하, 그리고 목 척추주위근육 및 먼쪽 지배 근육의 동시 탈신경 자발활동 출현을 종합하여 C6 목 신경뿌리병증으로 정의합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "노신경병증(Radial neuropathy)",
                "why_consider": "손목관절 폄 근력 약화와 노쪽 감각 이상이 동반되어 목 신경뿌리병증과 혼동될 수 있습니다.",
                "how_to_differentiate": "말초 노신경병증이라면 표재노신경 감각신경활동전위 진폭 감소가 수반되며, 목 척추주위근육 침근전도검사는 완전히 정상 상태를 유지해야 합니다. 본 사례는 감각전도의 완전 보존과 목 척추주위근육의 이상 활동이 공존하여 목 신경뿌리병증으로 정의됩니다.",
                "practical_tip": "손목관절 폄 마비 환자 평가 시, 표재노신경 감각신경활동전위의 보존 여부와 목 척추주위근육의 이상 방전 감별이 임상 판단의 핵심선입니다."
            }
        ]
    },

    "야간 손저림과 엄지 근력 약화": {
        "category": "말초 포착신경병증",
        "difficulty": "초중급",
        "patient": {
            "age": 46,
            "sex": "여성",
            "side": "오른쪽",
            "symptoms": [
                "오른손 1, 2, 3번째 손가락 중심의 저림이 야간에 특히 심함",
                "최근 엄지손가락 벌림(Abduction) 동작 시 힘이 빠지는 현상 발생"
            ],
            "physical_exam": {
                "감각 검사": [
                    "엄지, 검지, 중지 및 반지손가락 노쪽 절반의 손바닥쪽 감각 둔화. 정중신경 피부분절 분포와 일치"
                ],
                "맨손근력검사(MMT)": [
                    "엄지손가락 벌림근: Good (4/5) - 정중신경(Median nerve, C8-T1)"
                ],
                "반사 검사": [
                    "위팔두갈래근 반사(Biceps reflex, C5-C6), 위팔노근 반사(Brachioradialis reflex, C5-C6), 위팔세갈래근 반사(Triceps reflex, C7-C8): 모두 대칭적 정상(DRT 2+)",
                    "특수 검사: 팔렌 검사 양성, 손목 정중신경 주행 부위 티넬 징후 양성"
                ]
            }
        },
        "findings": {
            "정중신경 감각신경활동전위 (Median SNAP)": (NCS_NORMAL, NCS_DELAYED),
            "정중신경 복합근육활동전위 (Median CMAP)": (NCS_NORMAL, NCS_REDUCED),
            "짧은엄지벌림근 (Abductor Pollicis Brevis, APB)": (EMG_NORMAL, EMG_NORMAL)
        },
        "teaching_diagnosis": {
            "summary": "손목굴증후군(Carpal tunnel syndrome)을 시사하는 정중신경 포착병증입니다.",
            "ncs_reason": [
                "정중신경 감각신경활동전위에서 잠복기 지연이 도출되어 손목굴 내 국소 말이집탈락성 전도차단을 지시합니다.",
                "정중신경 복합근육활동전위에서 진폭 감소가 나타나 운동 축삭 손상이 함께 진행되고 있음을 뜻합니다."
            ],
            "emg_reason": [
                "1) 휴식 시 자발활동 전기생리 판독:",
                "짧은엄지벌림근에서 휴식 시 섬유자발전위나 양성예파 등의 이상 자발전위가 검출되지 않는 전기적 침묵의 정상 범위를 보입니다. 이는 정중신경 압박 포착 깊이가 경미하여 아직 먼쪽 축삭 손상 단계까지는 유발되지 않았음을 뜻합니다.",
                "2) 수의수축 시 운동단위 동원 분석:",
                "해당 짧은엄지벌림근의 수의수축 시 정상적인 운동단위동원 동원이 원활하게 일어납니다. 수축을 전달할 수 있는 하위 운동 축삭의 손실이 없어 간섭파형 형성이 온전히 보존되고 있음을 지시합니다."
            ],
            "integration": [
                "야간 통증 저림, 정중신경 분포 영역 감각 저하, 정중신경 전도 지연 및 짧은엄지벌림근 탈신경 전위 관찰을 종합하여 최종 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "몸쪽 정중신경병증(Proximal median neuropathy)",
                "why_consider": "정중신경 지배 영역의 근력 저하 및 손가락 저림이 매우 흡사합니다.",
                "how_to_differentiate": "원엎침근 등 손목 상부의 몸쪽 정중신경 지배 근육들의 침근전도검사 결과가 정상이므로 손목 수준의 포착으로 확진할 수 있습니다.",
                "practical_tip": "포착 신경병증 감별 시, 포착 의심 경계선보다 더 몸쪽에서 기시하는 근육들의 정상 전기활동 보존 여부를 철저히 확인하십시오."
            }
        ]
    },

    "위팔뼈 몸통 골절 후 손목처짐": {
        "category": "말초 포착신경병증",
        "difficulty": "초중급",
        "patient": {
            "age": 34,
            "sex": "남성",
            "side": "오른쪽",
            "symptoms": [
                "위팔뼈 몸통 골절 병력 있음",
                "골절 수술 직후부터 손목과 손가락을 들어 올리지 못하는 손목처짐(Wrist drop) 현상 발생"
            ],
            "physical_exam": {
                "감각 검사": [
                    "손등 노쪽 영역 감각 소실. 표재노신경 지배 영역 분포와 정확히 일치함"
                ],
                "맨손근력검사(MMT)": [
                    "손목관절 폄근: Poor (2/5) - 노신경(Radial nerve, C6-C7)",
                    "손가락 폄근: Poor (2/5) - 뒤뼈사이신경(Posterior interosseous nerve, C7-C8)",
                    "팔꿉관절 폄근: Normal (5/5) - 노신경(Radial nerve, C7-C8)"
                ],
                "반사 검사": [
                    "위팔세갈래근 반사(Triceps reflex, C7-C8): 정상(DRT 2+ - 골절 부위 상단 기시 가지로 보존됨)",
                    "위팔노근 반사(Brachioradialis reflex, C5-C6): 감소(DRT 1+)"
                ]
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
            "summary": "위팔뼈 나선고랑 부위의 노신경병증 마비 패턴입니다.",
            "ncs_reason": [
                "표재노신경 감각신경활동전위 진폭 감소는 병변이 뒤뿌리신경절보다 먼쪽의 혼합 말초신경계 축삭 마비임을 가리킵니다.",
                "노신경 복합근육활동전위 진폭 저하 및 전도 지연은 나선고랑 하부 주행 경로 내 운동 축삭 손상을 대변합니다."
            ],
            "emg_reason": [
                "1) 휴식 시 자발활동 전기생리 판독:",
                "노쪽손목폄근과 집게폄근에서 휴식 시 섬유자발전위 및 양성예파의 탈신경 비정상 자발전위가 관찰됩니다. 이는 나선고랑 통과 구간에서 발생한 기계적 압박에 기인한 먼쪽 축삭 단절 상태를 가리킵니다.",
                "2) 수의수축 시 운동단위 동원 분석:",
                "수의수축 시 노쪽손목폄근과 집게폄근에서 감소된 운동단위동원 패턴 반응이 나타나 폄근 마비를 대변합니다. 반면 목 뒤가지 경로를 대변하는 목 척추주위근육은 휴식 시 전기적 침묵, 수의수축 시 운동단위동원으로 정상을 보여 신경뿌리병증을 배제합니다."
            ],
            "integration": [
                "나선고랑 상단 골절력, 팔꿉관절 폄 기능 보존 대비 먼쪽 손목/손가락 폄 근력의 저하, 표재노신경 SNAP의 진폭 감소, 목 척추주위근육 정상 전기활동을 융합하여 외상성 노신경병증으로 확진합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "뒤뼈사이신경병증(Posterior interosseous neuropathy, PIN)",
                "why_consider": "손가락 및 손목관절 폄 근력 저하가 노신경병증과 유사하게 관찰됩니다.",
                "how_to_differentiate": "뒤뼈사이신경은 노신경의 순수 운동 분지이므로 감각 소실 영역이 없어야 하며, 표재노신경 감각신경활동전위가 완전 정상 범위로 기록되어야 합니다.",
                "practical_tip": "감각신경활동전위의 변성 탈락 유무가 노신경 주간 경로 마비와 먼쪽 심부 운동 분지 마비를 감별하는 핵심 척도입니다."
            }
        ]
    },

    "4, 5번째 손가락 저림과 손가락 근력 약화": {
        "category": "말초 포착신경병증",
        "difficulty": "초중급",
        "patient": {
            "age": 42,
            "sex": "남성",
            "side": "오른쪽",
            "symptoms": [
                "우측 4, 5번째 손가락 감각 이상 및 새끼손가락 가쪽 손날 부위 통증",
                "최근 젓가락질 시 손날 지지력 소실 및 미세한 손가락 동작 약화"
            ],
            "physical_exam": {
                "감각 검사": [
                    "반지손가락 자쪽 절반 및 새끼손가락 감각 저하. 자신경 피부분절 분포 영역에 국한됨"
                ],
                "맨손근력검사(MMT)": [
                    "새끼손가락 벌림근: Fair (3/5) - 자신경(Ulnar nerve, C8-T1)",
                    "손가락 벌림/모음근: Fair (3/5) - 자신경(Ulnar nerve, C8-T1)"
                ],
                "반사 검사": [
                    "위팔두갈래근(C5), 위팔노근(C6), 위팔세갈래근(C7) 반사: 대칭적 정상(DRT 2+)",
                    "특수 검사: 팔꿈치 터널 주행 부위 티넬 징후 양성 및 팔꿉관절 최대 굽힘 유발 검사 양성"
                ]
            }
        },
        "findings": {
            "자신경 감각신경활동전위 (Ulnar SNAP)": (NCS_NORMAL, NCS_DELAYED),
            "자신경 복합근육활동전위 (Ulnar CMAP)": (NCS_NORMAL, NCS_REDUCED),
            "새끼벌림근 (Abductor Digiti Minimi, ADM)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "첫째등쪽뼈사이근 (First Dorsal Interosseous, FDI)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION)
        },
        "teaching_diagnosis": {
            "summary": "팔꿈치터널증후군(Cubital tunnel syndrome)으로 대표되는 팔꿈치 부위 자신경병증입니다.",
            "ncs_reason": [
                "자신경 감각신경활동전위에서 잠복기 지연이 관찰되어 팔꿈치 터널 구간 내의 국소 말이집탈락성 병변을 가리킵니다.",
                "자신경 복합근육활동전위의 진폭 저하는 포착성 신경 마비에 따르는 운동 축삭 손상 단계를 나타냅니다."
            ],
            "emg_reason": [
                "1) 휴식 시 자발활동 전기생리 판독:",
                "새끼벌림근 및 첫째등쪽뼈사이근에서 휴식 시 섬유자발전위 및 양성예파의 탈신경 비정상 자발전위가 도출됩니다. 이는 주관 포착으로 인한 먼쪽 운동 축삭의 변성을 전기생리학적으로 지시합니다.",
                "2) 수의수축 시 운동단위 동원 분석:",
                "수의수축 시 새끼벌림근 및 첫째등쪽뼈사이근에서 동원 가능한 총 결합 단위수 저하 현상에 기인한 감소된 운동단위동원 패턴 반응이 관찰됩니다."
            ],
            "integration": [
                "새끼손가락 감각 이상, 새끼벌림근 및 첫째등쪽뼈사이근 근력 저하, 자신경 잠복기 지연 및 침근전도검사 이상 소견을 융합하여 팔꿈치터널증후군으로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "C8-T1 목 신경뿌리병증(Cervical radiculopathy)",
                "why_consider": "손 내재근 약화 분절이 C8-T1 영역과 일치하여 자신경 분포와 흡사하게 관찰될 수 있습니다.",
                "how_to_differentiate": "목 신경뿌리병증은 정중신경 지배 손가락 근육들도 전반적으로 동시 침범되며, 표재 자신경 감각신경활동전위는 정상 범위로 완벽 보존되는 특징이 있습니다.",
                "practical_tip": "손 자체기원근육 약화 시 정중/자신경의 감각전도를 상호 비교하는 것이 척수 신경뿌리 병변과 말초 단일 포착 병변의 감별 잣대입니다."
            }
        ]
    },

    "허리-다리 통증과 발처짐": {
        "category": "허리 신경뿌리병증(Lumbar radiculopathy)",
        "difficulty": "초중급",
        "patient": {
            "age": 61,
            "sex": "여성",
            "side": "오른쪽",
            "symptoms": [
                "허리에서 우측 엉치, 종아리 가쪽, 발등으로 뻗치는 방사통과 저림",
                "최근 보행 시 발끝이 바닥에 끌려 보행이 어려운 발처짐(Foot drop) 발생"
            ],
            "physical_exam": {
                "감각 검사": [
                    "종아리 가쪽 및 발등 중앙 부위 감각 둔화. L5 피부분절 범위 분포"
                ],
                "맨손근력검사(MMT)": [
                    "발목관절 등굽힘근: Fair (3/5) - 깊은종아리신경(Deep peroneal nerve, L4-L5)",
                    "엄지발가락 폄근: Poor (2/5) - 깊은종아리신경(Deep peroneal nerve, L5)",
                    "엉덩관절 벌림근: Good (4/5) - 위볼기신경(Superior gluteal nerve, L4-S1)"
                ],
                "반사 검사": [
                    "무릎반사(Patellar reflex, L4): 정상(DRT 2+)",
                    "아킬레스힘줄반사(Achilles tendon reflex, S1): 정상(DRT 2+)"
                ]
            }
        },
        "findings": {
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": (NCS_NORMAL, NCS_NORMAL),
            "허리 척추주위근 (Lumbar Paraspinal)": (EMG_NORMAL, EMG_PARASPINAL_DENERVATION),
            "앞정강근 (Tibialis Anterior, TA)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "긴엄지폄근 (Extensor Hallucis Longus, EHL)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "중간볼기근 (Gluteus Medius)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION)
        },
        "teaching_diagnosis": {
            "summary": "발처짐을 동반한 L5 허리 신경뿌리병증 패턴입니다.",
            "ncs_reason": [
                "얕은종아리신경 감각신경활동전위가 대칭성 정상 보존됩니다. 이는 감각 세포체가 위치한 뒤뿌리신경절보다 몸쪽인 요추 척수 내부 신경뿌리 압박 상황을 지지합니다."
            ],
            "emg_reason": [
                "1) 휴식 시 자발활동 전기생리 판독:",
                "허리 척추주위근육, 앞정강근, 긴엄지폄근, 중간볼기근의 바늘 근전도 결과, 휴식 시 섬유자발전위 및 양성예파의 탈신경 자발전위가 대거 관찰됩니다. L5 척수 신경근의 물리적 압박으로 전근 운동 축삭의 퇴행이 진행 중임을 지시합니다.",
                "2) 수의수축 시 운동단위 동원 분석:",
                "수의수축 시 앞정강근, 긴엄지폄근, 중간볼기근에서 동원 가능한 기능적 알파 운동신경원 수의 소실로 인해 감소된 운동단위동원 패턴이 관찰됩니다."
            ],
            "integration": [
                "L5 피부분절 감각 저하, 발처짐 및 중간볼기근 근력 저하, 감각신경활동전위 정상 보존 및 허리 척추주위근육 탈신경 전위 검출을 종합하여 L5 허리 신경뿌리병증으로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "온종아리신경병증(Common peroneal neuropathy)",
                "why_consider": "발목관절 등굽힘근 약화로 보행 시 발처짐 양상이 완전 일치합니다.",
                "how_to_differentiate": "온종아리신경병증은 가쪽 무릎 부위 포착으로 얕은종아리신경 SNAP 및 Peroneal CMAP가 대폭 감소하며, 위볼기신경지배인 중간볼기근 및 척추주위근은 완벽히 정상입니다.",
                "practical_tip": "발처짐 감별 시 엉덩관절 벌림 및 발목 안쪽번짐 근력의 보존 여부를 반드시 연계 확인하십시오."
            }
        ]
    },

    "정강뼈 골절로 석고붕대 후 발처짐과 발등 감각저하": {
        "category": "말초 포착신경병증",
        "difficulty": "초중급",
        "patient": {
            "age": 31,
            "sex": "남성",
            "side": "왼쪽",
            "symptoms": [
                "정강뼈 골절 부위 석고붕대 유지 이력 있음",
                "석고붕대 제거 직후 좌측 발처짐과 발등 감각 소실 발견"
            ],
            "physical_exam": {
                "감각 검사": [
                    "종아리 가쪽 및 발등 부위 감각 소실. 얕은/깊은종아리신경 분포 범위"
                ],
                "맨손근력검사(MMT)": [
                    "발목관절 등굽힘근: Poor (2/5) - 깊은종아리신경(Deep peroneal nerve, L4-L5)",
                    "엄지발가락 폄근: Trace (1/5) - 깊은종아리신경(Deep peroneal nerve, L5)",
                    "발목관절 가쪽번짐근: Poor (2/5) - 얕은종아리신경(Superficial peroneal nerve, L5-S1)",
                    "발목관절 안쪽번짐근: Normal (5/5) - 정강신경(Tibial nerve, L4-S1)"
                ],
                "반사 검사": [
                    "무릎반사(Patellar reflex, L4) 및 아킬레스힘줄반사(Achilles reflex, S1): 모두 대칭적 정상"
                ]
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
            "summary": "종아리뼈머리 부위 압박으로 인한 온종아리신경병증입니다.",
            "ncs_reason": [
                "얕은종아리신경 SNAP 및 Peroneal CMAP의 동시 진폭 감소는 석고붕대에 의한 종아리뼈머리 가쪽에서의 심한 압박 마비 및 축삭 손상을 입증합니다."
            ],
            "emg_reason": [
                "1) 휴식 시 자발활동 전기생리 판독:",
                "좌측 앞정강근과 긴종아리근의 침근전도 소견 상 섬유자발전위, 양성예파의 비정상 탈신경 자발 활동이 관찰됩니다. 석고 캐스트 고정으로 온종아리신경이 직접 압박을 받아 먼쪽 운동축삭 변성이 야기되었음을 가리킵니다.",
                "2) 수의수축 시 운동단위 동원 분석:",
                "해당 앞정강근, 긴종아리근의 수의수축 시 운동단위동원 감소 패턴이 나타나 운동단위 결손을 대변합니다. 반면 허리 척추주위근은 휴식 시 Silent at rest, 수의수축 시 Normal MU recruitment로 매우 조용하여 신경뿌리병증을 완벽히 배제합니다."
            ],
            "integration": [
                "정강뼈 골절 부목 고정력, 정강신경 지배 발목 안쪽번짐 보존 및 종아리 지배 폄근 근력 저하, 감각신경활동전위 감소를 종합하여 압박성 온종아리신경 마비로 정의합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "L5 허리 신경뿌리병증(Lumbar radiculopathy)",
                "why_consider": "발처짐 및 발등 감각 이상 양상이 매우 비슷합니다.",
                "how_to_differentiate": "L5 허리 신경뿌리병증은 감각신경전도가 정상 범위로 유지되며, 척추주위근 침범 비정상적인 자발전위가 뚜렷하게 도출됩니다.",
                "practical_tip": "뒤정강근이 분담하는 안쪽번짐 기능 보존 여부가 L5 뿌리 마비와 말초 온종아리신경 마비를 가르는 임상적 열쇠입니다."
            }
        ]
    },

    "골반 외상 후 다리 전반 근력 약화": {
        "category": "신경얼기병증(Plexopathy)",
        "difficulty": "중급",
        "patient": {
            "age": 45,
            "sex": "여성",
            "side": "왼쪽",
            "symptoms": [
                "골반 골절 수술 후 좌측 다리 전반의 심한 근력 약화 발생",
                "허벅지부터 종아리, 발등까지 광범위한 감각 둔화와 보행장애 호소"
            ],
            "physical_exam": {
                "감각 검사": [
                    "허벅지, 종아리, 발등 등 여러 피부분절을 넘는 광범위 감각 소실"
                ],
                "맨손근력검사(MMT)": [
                    "엉덩관절 굽힘근: Poor (2/5) - 허리신경얼기/넓적다리신경 관련",
                    "무릎관절 폄근: Poor (2/5) - 넓적다리신경(Femoral nerve)",
                    "발목관절 등굽힘근: Trace (1/5) - 깊은종아리신경(Deep peroneal nerve)",
                    "발목관절 발바닥굽힘근: Poor (2/5) - 정강신경(Tibial nerve)"
                ],
                "반사 검사": [
                    "무릎반사(Patellar reflex, L4) 및 아킬레스힘줄반사(Achilles reflex, S1): 좌측 완전 소실(DRT 0)"
                ]
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
            "summary": "외상과 관련된 허리엉치신경얼기병증 패턴입니다.",
            "ncs_reason": [
                "장딴지신경 감각신경활동전위, 넓적다리신경 및 종아리신경 복합근육활동전위 등 복수의 주요 말초 전도에서 진폭 감소가 확인됩니다. 이는 병변이 척수뒤뿌리신경절 먼쪽에 형성된 말초 신경얼기 줄기 장애임을 시사합니다."
            ],
            "emg_reason": [
                "1) 휴식 시 자발활동 전기생리 판독:",
                "좌측 가쪽넓은근과 앞정강근 침근전도 검사에서, 휴식 시 섬유자발전위 및 양성예파의 탈신경 자발 활동전위가 관찰되어, 골반 외상에 수반된 운동축삭 손상 상황을 대변합니다.",
                "2) 수의수축 시 운동단위 동원 분석:",
                "수의수축 시 가쪽넓은근과 앞정강근에서 감소된 운동단위동원 패턴 현상이 도출됩니다. 반면 허리 척추주위근은 휴식 시 전기적 침묵, 수의수축 시 운동단위동원으로 정상을 보여 다발 신경뿌리가 아닌 신경얼기 수준의 파열 손상임을 밝힙니다."
            ],
            "integration": [
                "골반 골절 외상 및 고정 수술력, 다리 다발 신경 영역의 동시 근력 저하, 다발성 감각신경활동전위/복합근육활동전위 감소, 척추주위근 보존을 종합하여 허리엉치신경얼기 마비로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "다발 허리 신경뿌리병증(Lumbar radiculopathy)",
                "why_consider": "복수 척수 분절의 동시 약화와 깊은힘줄 반사 소실이 나타나 혼동하기 쉽습니다.",
                "how_to_differentiate": "다발 허리 신경뿌리병증은 감각신경전도가 정상 범위로 유지되며, 요배부 척추주위근 침근전도에서 다발성 탈신경 활동이 매우 명확하게 나타납니다.",
                "practical_tip": "다리 전반의 광범위 마비 양상 시, 척추주위근 침범과 감각신경활동전위 저하 여부가 감별의 핵심 척도입니다."
            }
        ]
    },

    "양측 발끝 저림과 발가락 약화": {
        "category": "다발신경병증(Polyneuropathy)",
        "difficulty": "초중급",
        "patient": {
            "age": 67,
            "sex": "남성",
            "side": "양쪽",
            "symptoms": [
                "오랜 기간 당뇨병 병력 있음",
                "양쪽 발끝에서 시작해 발목 위로 서서히 올라오는 대칭성 저림과 감각 둔화"
            ],
            "physical_exam": {
                "감각 검사": [
                    "양측 발가락 끝부터 발목 상부까지 대칭적인 장갑-양말형 감각 저하"
                ],
                "맨손근력검사(MMT)": [
                    "양측 엄지발가락 폄근: Good (4/5) - 깊은종아리신경(Deep peroneal nerve, L5)",
                    "양측 발가락 굽힘근: Good (4/5) - 정강신경(Tibial nerve, L5-S2)",
                    "양측 발목관절 등굽힘근: Normal (5/5) - 깊은종아리신경(Deep peroneal nerve)"
                ],
                "반사 검사": [
                    "양측 아킬레스힘줄반사(Achilles reflex, S1): 완전 소실(DRT 0)",
                    "양측 무릎반사(Patellar reflex, L4): 보존 및 경미한 감소"
                ]
            }
        },
        "findings": {
            "장딴지신경 감각신경활동전위 (Sural SNAP)": (NCS_REDUCED, NCS_REDUCED),
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": (NCS_REDUCED, NCS_REDUCED),
            "정강신경 복합근육활동전위 (Tibial CMAP)": (NCS_REDUCED, NCS_REDUCED),
            "앞정강근 (Tibialis Anterior, TA)": (EMG_ACTIVE_CHRONIC, EMG_ACTIVE_CHRONIC)
        },
        "teaching_diagnosis": {
            "summary": "길이 의존성 축삭성 다발신경병증 패턴입니다.",
            "ncs_reason": [
                "양다리 말단의 원위 감각 및 운동 신경들에서 대칭적인 진폭 감소가 두드러지게 관찰되며, 이는 당뇨 등 전신 대사 이상에 따른 말초 축삭 손상 패턴과 정확히 부합합니다."
            ],
            "emg_reason": [
                "1) 휴식 시 자발활동 전기생리 판독:",
                "양측 앞정강근의 침근전도 결과, 휴식 시 섬유자발전위 및 양성예파의 탈신경 비정상 자발전위가 좌우 대칭 분포로 유도됩니다. 대사성 축삭 병변으로 인해 긴 말단 축삭 가지부터 대칭 손상해 들어오는 dying-back 기전의 세포학적 단서입니다.",
                "2) 수의수축 시 운동단위 동원 분석:",
                "해당 앞정강근 근육들의 수의수축 시, 운동단위 소실 및 잔여 축삭 발아에 기초하여 거대운동단위활동전위 출현 및 감소된 운동단위동원 양상이 좌우 대칭적으로 발생하여 만성 축삭 파괴 상태를 지지합니다."
            ],
            "integration": [
                "장기 당뇨병 병력, 대칭성 먼쪽 장갑-양말 감각 저하, 아킬레스 반사 소실 및 다리 감각신경활동전위/복합근육활동전위 진폭 감소를 연결하여 최종 확진합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "말이집탈락성 다발신경병증(Demyelinating polyneuropathy)",
                "why_consider": "상하 대칭적인 다발성 신경 침범 양상이 매우 유사합니다.",
                "how_to_differentiate": "말이집탈락성은 진폭 보존 하에 극심한 전도 잠복기 지연, 전도속도 저하, 후기반응 소실이 선행 지표로 검출됩니다.",
                "practical_tip": "다발성 다리 마비 환자의 판독 시 진폭 감소가 우선인지, 잠복기 지연이 우선인지 구분하십시오."
            }
        ]
    },

    "대칭성 팔다리 근력저하와 보행 저하": {
        "category": "다발신경병증(Polyneuropathy)",
        "difficulty": "중급",
        "patient": {
            "age": 55,
            "sex": "여성",
            "side": "양쪽",
            "symptoms": [
                "몇 달간 양쪽 손과 발이 대칭적으로 저리고 둔함",
                "계단 오르기와 발목 움직임 모두에서 진행성 근력 약화 호소"
            ],
            "physical_exam": {
                "감각 검사": [
                    "양측 팔과 다리 먼쪽의 대칭적인 감각 탈락"
                ],
                "맨손근력검사(MMT)": [
                    "양측 어깨관절 벌림근: Fair (3/5) - 겨드랑신경(Axillary nerve, C5-C6)",
                    "양측 엉덩관절 굽힘근: Fair (3/5) - 허리신경얼기/넓적다리신경 관련",
                    "양측 손목관절 폄근: Fair (3/5) - 노신경(Radial nerve, C6-C7)",
                    "양측 발목관절 등굽힘근: Fair (3/5) - 깊은종아리신경(Deep peroneal nerve, L4-L5)"
                ],
                "반사 검사": [
                    "전신 깊은힘줄 반사(C5, C6, C7, L4, S1): 완벽한 소실(DRT 0)"
                ]
            }
        },
        "findings": {
            "정중신경 감각신경활동전위 (Median SNAP)": (NCS_DELAYED, NCS_DELAYED),
            "자신경 감각신경활동전위 (Ulnar SNAP)": (NCS_DELAYED, NCS_DELAYED),
            "정중신경 복합근육활동전위 (Median CMAP)": (NCS_DELAYED, NCS_DELAYED),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": (NCS_DELAYED, NCS_DELAYED),
            "정강/종아리신경 F파 (F-wave)": (FWAVE_DELAYED_ABSENT, FWAVE_DELAYED_ABSENT),
            "앞정강근 (Tibialis Anterior, TA)": (EMG_NORMAL, EMG_NORMAL)
        },
        "teaching_diagnosis": {
            "summary": "만성 염증성 말이집탈락성 다발신경병증 양상입니다.",
            "ncs_reason": [
                "다수의 운동 및 감각 전도에서 광범위한 잠복기 지연이 대칭 도출되는 것은 다발성 말이집 탈락성 변화를 강하게 입증합니다.",
                "F파 전도 속도의 유의미한 지연 및 소실은 척수 신경근과 가장 가까운 근위 전도부의 말이집 손상을 직접 시사합니다."
            ],
            "emg_reason": [
                "1) 휴식 시 자발활동 전기생리 판독:",
                "양측 앞정강근의 침근전도 결과, 휴식 시 자발 활동이 전혀 관찰되지 않는 전기적 침묵이 나타나 정상 소견을 보입니다. 축삭 손상이 동반되지 않은 탈말이집 상태임을 생리학적으로 입증합니다.",
                "2) 수의수축 시 운동단위 동원 분석:",
                "해당 앞정강근 근육의 수의수축 시 정상적인 운동단위동원 양상이 나타납니다. 축삭 단절에 의한 지배 유실이 없으므로 수의수축 시 간섭파형 동원은 완벽히 유발 보존되고 있음을 지시합니다."
            ],
            "integration": [
                "근위/먼쪽 동시 마비, 전신 무반사, 다발성 잠복기 지연 및 F파 지연 소실을 종합하여 만성 염증성 말이집탈락성 다발신경병증으로 판단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "근육병증(Myopathy)",
                "why_consider": "어깨 및 엉덩관절 등 몸쪽 약화 기전이 유사하여 혼동을 초래합니다.",
                "how_to_differentiate": "근육병증은 말단 감각 소실이 없으며 전신 깊은힘줄 반사도가 비교적 정상적으로 유지되는 경향을 띱니다.",
                "practical_tip": "감각의 보존 여부와 전신 무반사 대조가 신경병과 근육병 감별의 기준선입니다."
            }
        ]
    },

    "눈꺼풀 떨림과 눈 주위 불편감 지속": {
        "category": "뇌신경/반사경로",
        "difficulty": "중급",
        "patient": {
            "age": 62,
            "sex": "여성",
            "side": "오른쪽",
            "symptoms": [
                "우측 눈꺼풀 주변의 간헐적인 미세 떨림과 가벼운 경련이 2주간 발생함",
                "우측 눈 가쪽의 가벼운 촉각 저하 및 이물감이 동반됨"
            ],
            "physical_exam": {
                "얼굴 표정근 관찰": [
                    "이마 주름잡기(이마근-얼굴신경): 양측 대칭성 정상 범위 보존",
                    "눈 꽉 감기(눈둘레근-얼굴신경): 양측 대칭성 정상 범위 보존",
                    "입꼬리 올리기(큰광대근-얼굴신경): 양측 대칭성 정상 범위 보존"
                ],
                "뇌신경 감각 검사": [
                    "우측 이마 및 눈 주변 영역[CN V1 분지]의 촉각 감각 감소"
                ],
                "반사 검사": [
                    "우측 각막반사(Corneal reflex): 임상적 저하 관찰"
                ]
            }
        },
        "findings": {
            "우측 자극-우측 R1": (BLINK_DELAYED, "14.8 ms"),
            "우측 자극-우측 R2": (BLINK_DELAYED_ABSENT, "48.5 ms"),
            "우측 자극-좌측 R2": (BLINK_DELAYED_ABSENT, "49.1 ms"),
            "좌측 자극-좌측 R1": (NCS_NORMAL, "10.4 ms"),
            "좌측 자극-좌측 R2": (NCS_NORMAL, "32.1 ms"),
            "좌측 자극-우측 R2": (NCS_NORMAL, "31.8 ms"),
            "눈둘레근 (Orbicularis Oculi)": (EMG_NORMAL, EMG_NORMAL)
        },
        "teaching_diagnosis": {
            "summary": "우측 삼차신경의 들신경 경로 손상입니다.",
            "ncs_reason": [
                "우측 자극 시 우측 R1, 우측 R2, 좌측 R2가 모두 정상측 대비 지연되거나 반사 유발이 소실됩니다.",
                "반면 좌측 자극 시에는 동측 R1, R2뿐만 아니라 우측 R2 반사 반응까지 완전히 정상 범위로 도출됩니다.",
                "이는 얼굴마비를 일으키는 얼굴신경은 정상이나, 자극을 수용하여 뇌줄기로 보내는 삼차신경의 우측 가지에 전도 장애가 발생했음을 생리학적으로 확증합니다."
            ],
            "emg_reason": [
                "1) 검사 선택의 전기생리학적 근거:",
                "본 사례는 삼차-얼굴신경 반사궁 회로의 회로 전도 결손만을 정밀 평가하는 증례로, 먼쪽 운동 단절이나 변성이 수반되지 않아 침근전도 검사는 임상 프로토콜 상 전면 제외되었습니다."
            ],
            "integration": [
                "우측 삼차신경 지배 가지의 촉각 저하, 우측 각막반사 감소 및 우측 자극 시 양측 수축 반응의 전기적 지연 소실을 종합하여 우측 삼차신경 전도 장애로 최종 판독합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "우측 얼굴신경병증 (얼굴마비)",
                "why_consider": "눈 감기 불편감과 얼굴 불편감이 얼굴마비 초기와 혼동될 수 있습니다.",
                "how_to_differentiate": "우측 얼굴신경 병변이라면 좌측 자극 시에도 우측 반응인 우측 R2가 소실되며, 본 환자는 좌측 자극 시 우측 R2가 정상입니다.",
                "practical_tip": "눈깜빡반사 판독 시 전기 자극을 준 쪽이 문제인지(들신경), 반응을 하는 눈꺼풀 근육 쪽이 문제인지(날신경) 비교해서 확인하세요."
            }
        ]
    },

    "뇌졸중 환자 발목 경직 평가": {
        "category": "중추성 반사이상",
        "difficulty": "중급",
        "patient": {
            "age": 68,
            "sex": "남성",
            "side": "오른쪽",
            "symptoms": [
                "뇌졸중 후 편마비 상태이며 우측 발목 발바닥굽힘근의 중증 경직 발생",
                "보행에 극심한 지장을 받아, 일정기간 물리치료 전/후 경직 완화 효과를 정량적으로 모니터링함"
            ],
            "physical_exam": {
                "근긴장도 검사 (MAS)": [
                    "우측 발목 발바닥굽힘근 수정된 애쉬워스 척도(MAS): 3등급 (물리치료 적용 전)",
                    "우측 발목 발바닥굽힘근 수정된 애쉬워스 척도(MAS): 2등급 (물리치료 적용 후)"
                ],
                "깊은힘줄 및 병적반사 검사": [
                    "아킬레스힘줄반사(Achilles tendon reflex, S1): 우측 비정상적 항진 (DRT 4+)",
                    "우측 발목간대경련(Ankle clonus): 3-5회 지속적 관찰"
                ]
            }
        },
        "findings": {
            "우측 가자미근 H-반사 최대 진폭 (물리치료 전)": (H_REFLEX_HYPERACTIVE, "7.2 mV"),
            "우측 가자미근 H-반사 최대 진폭 (물리치료 후)": (NCS_NORMAL, "5.1 mV"),
            "우측 가자미근 H/M ratio 비율 (물리치료 전)": (H_M_RATIO_INCREASED, "65%"),
            "우측 가자미근 H/M ratio 비율 (물리치료 후)": (NCS_NORMAL, "55%")
        },
        "teaching_diagnosis": {
            "summary": "물리치료 중재 적용 후 우측 가자미근의 척수반사 흥분성 감소 및 경직 완화 효과가 일부 나타난 것으로 평가됩니다.",
            "ncs_reason": [
                "물리치료 적용 전 H/M 비율이 65%로 매우 높게 나타난 것은 대뇌-척수 상부 억제계 상실로 우측 가자미근 알파운동신경세포의 흥분성이 정상 범위를 초과해 극도로 비정상 항진되어 있었음을 의미합니다.",
                "스트레칭 및 대항근 전기자극 적용 후, H/M ratio가 55%로 소폭 감소하여 척수 반사회로의 과흥분성이 일부 완화된 것으로 평가됩니다."
            ],
            "emg_reason": [
                "1) 치료 효과 검증을 위한 H-반사 단독 평가:",
                "본 사례는 편마비 환자의 경직 정량적 중재 평가를 목적으로 후기반응인 H 반사만을 단독 추적 관찰했습니다."
            ],
            "integration": [
                "MAS 3등급의 보행 불능 환자에게 물리치료를 적용한 후, H-반사의 진폭 감소 및 H/M 비율의 정량적 회복을 통해 위운동신경세포 증후군 환자의 소폭 경직 완화 효과를 검증한 임상 사례입니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "말초 S1 신경뿌리병증",
                "why_consider": "아킬레스 힘줄과 S1 반사 경로를 공유하므로 유사하게 해석될 여지가 있습니다.",
                "how_to_differentiate": "말초 신경 손상(신경뿌리병증) 시에는 H-반사의 지연 및 유발 소실이 수반되지만, 중추성 마비에 의한 경직 시에는 H-반사 진폭이 크게 항진되고 H/M 비율이 증가합니다.",
                "practical_tip": "H/M 비율의 양적 감소 수치는 중추성 신경 손상 환자의 물리치료적 경직 중재 수준을 평가하는 정량적인 근거로 활용될 수 있습니다."
            }
        ]
    }
}
