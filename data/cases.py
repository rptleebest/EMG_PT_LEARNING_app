# data/cases.py

"""
물리치료학과 학생 교육용 대표 근전도 사례 라이브러리 (총 6개 핵심 사례 최적화).
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
        "patient": {
            "age": 57, "sex": "남성", "side": "오른쪽",
            "symptoms": [
                "뒷목부터 오른쪽 위팔 가쪽을 지나 엄지손가락까지 타는 듯한 통증이 방사됨.",
                "머리를 뒤로 젖히면 통증이 심해지며, 최근 팔꿉관절 굽힘 시 힘이 빠짐."
            ],
            "physical_exam": {
                "감각 검사": ["아래팔 노쪽 및 엄지/검지 부위 촉각 저하 (C6 피부분절)"],
                "맨손근력검사(MMT)": [
                    "팔꿉관절 굽힘근: Fair (3/5) - 근육피부신경 지배",
                    "손목관절 폄근: Fair (3/5) - 노신경 지배"
                ],
                "반사 검사": [
                    "위팔노근 깊은힘줄반사(C6): 비정상 감소 (DRT 1+)",
                    "위팔세갈래근 반사(C7): 대칭적 정상 보존 (DRT 2+)"
                ]
            }
        },
        "findings": {
            "노신경 표재감각신경활동전위 (Superficial Radial SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "근육피부신경 복합근육활동전위 (Musculocutaneous CMAP)": (NCS_NORMAL, NCS_NORMAL),
            "목 척추주위근 (Cervical Paraspinals)": (EMG_NORMAL, EMG_PARASPINAL_DENERVATION),
            "위팔두갈래근 (Biceps Brachii)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "노쪽손목폄근 (Extensor Carpi Radialis)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION)
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "감각 둔화 호소에도 불구하고 말초 감각신경전도(SNAP)가 대칭적으로 정상 보존됩니다. 이는 감각 세포체가 위치한 뒤뿌리신경절(DRG)보다 몸쪽(proximal)에 위치한 신경뿌리 압박 병변임을 뜻하는 전형적 소견입니다."
            ],
            "emg_reason": [
                "목 척추주위근, 위팔두갈래근, 노쪽손목폄근에서 휴식 시 비정상 자발활동전위가 관찰되어 먼쪽(distal) 근육까지 이르는 축삭 탈신경 상태를 의미합니다.",
                "이 근육들은 말초신경 갈래는 다르지만 모두 C6 척수 분절을 공유하므로 단일 뿌리 손상을 지시합니다."
            ],
            "integration": [
                "▶ 추정 질환: 오른쪽 C6 목 신경뿌리병증(Cervical radiculopathy)",
                "▶ 추정 근거: C6 피부분절 감각 저하, 위팔노근 반사 감소, 그리고 침근전도에서 목 척추주위근과 C6 지배 먼쪽 근육군의 동시 탈신경을 종합하여 C6 신경뿌리 마비로 확진합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "▶ 노신경병증(Radial neuropathy)",
                "how_to_differentiate": "손목관절 폄 약화로 혼동할 수 있으나, 말초 노신경 마비라면 표재노신경 감각 진폭 감소가 나타나며 목 척추주위근육은 완전 정상이어야 합니다."
            }
        ]
    },

    "허리-다리 통증과 발처짐": {
        "patient": {
            "age": 61, "sex": "여성", "side": "오른쪽",
            "symptoms": [
                "오른쪽 허리에서 엉치, 종아리 가쪽을 타고 발등까지 찌릿한 방사통이 심함.",
                "보행 시 오른쪽 발끝이 바닥에 끌려 넘어질 뻔한 발처짐(Foot drop) 현상 발생."
            ],
            "physical_exam": {
                "감각 검사": ["종아리 가쪽 및 발등 중앙 부위 감각 둔화 (L5 피부분절)"],
                "맨손근력검사(MMT)": [
                    "발목관절 등굽힘근: Poor (2/5) - 깊은종아리신경",
                    "엉덩관절 벌림근: Fair (3/5) - 위볼기신경"
                ],
                "반사 검사": ["아킬레스힘줄반사(S1) 및 무릎반사(L4): 모두 정상 보존"]
            }
        },
        "findings": {
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": (NCS_NORMAL, NCS_NORMAL),
            "허리 척추주위근 (Lumbar Paraspinals)": (EMG_NORMAL, EMG_PARASPINAL_DENERVATION),
            "앞정강근 (Tibialis Anterior)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "중간볼기근 (Gluteus Medius)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION)
        },
        "teaching_diagnosis": {
            "ncs_reason": [
                "얕은종아리신경 감각 진폭이 정상으로 보존되어, 요추 뒤뿌리신경절보다 몸쪽(proximal)에 위치한 중추 신경뿌리 압박임을 지지합니다."
            ],
            "emg_reason": [
                "허리 척추주위근, 앞정강근, 중간볼기근에서 탈신경 자발전위가 뚜렷합니다. 이는 서로 다른 말초신경 지배를 받으나 L5 분절을 공유하는 근육들의 동시 탈신경입니다."
            ],
            "integration": [
                "▶ 추정 질환: 오른쪽 L5 허리 신경뿌리병증(Lumbar radiculopathy)",
                "▶ 추정 근거: 얕은종아리신경 감각전도 보존, 허리 척추주위근 및 중간볼기근 탈신경 동반, 발처짐 양상을 통해 허리디스크 등에 의한 L5 신경뿌리 마비로 확진합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "▶ 온종아리신경병증(Common peroneal neuropathy)",
                "how_to_differentiate": "발목 등굽힘근 약화로 발처짐이 생기는 점은 일치하나, 온종아리 마비는 얕은종아리 감각 진폭이 급감하고 척추주위근 및 중간볼기근은 완벽히 정상입니다."
            }
        ]
    },

    "눈꺼풀 떨림과 눈 주위 불편감 지속": {
        "patient": {
            "age": 62, "sex": "여성", "side": "오른쪽",
            "symptoms": [
                "오른쪽 눈꺼풀 주변에 간헐적인 미세 떨림이 2주간 지속됨.",
                "우측 이마와 눈 가쪽을 만졌을 때 둔한 감각과 이물감이 동반됨."
            ],
            "physical_exam": {
                "얼굴 표정근 관찰": ["이마 주름잡기, 눈 꽉 감기, 입꼬리 올리기 대칭적 정상 범위 보존"],
                "뇌신경 감각 검사": ["오른쪽 이마/눈 주변(삼차신경 V1 분지) 촉각 감소"],
                "반사 검사": ["오른쪽 각막반사 유발 시 지연 및 약화 관찰"]
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
                "본 사례는 먼쪽(distal) 운동 단절이 수반되지 않은 반사궁 전도 결손이므로 침근전도는 실시되지 않았습니다."
            ],
            "integration": [
                "▶ 추정 질환: 오른쪽 삼차신경 전도 장애(Trigeminal afferent pathway dysfunction)",
                "▶ 추정 근거: 오른쪽 삼차신경 지배 피부분절의 감각 저하, 우측 각막반사 감소 및 우측 전기 자극 시 양측 수축 반응의 지연/소실을 종합하여 수용체 경로 마비로 판독합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "▶ 오른쪽 말초성 얼굴마비(Bell's palsy)",
                "how_to_differentiate": "얼굴마비(운동 날신경 병변)라면 왼쪽을 자극했을 때도 오른쪽 눈을 감는 반응(Rt R2)이 소실되어야 하나, 이 환자는 왼쪽 자극 시 오른쪽 반응을 잘 수행합니다."
            }
        ]
    },

    "뇌졸중 환자 발목 경직 평가": {
        "patient": {
            "age": 68, "sex": "남성", "side": "왼쪽",
            "symptoms": [
                "오른쪽 대뇌 뇌졸중 후 편마비 상태이며, 최근 왼쪽 발목에 강한 강직이 발생함.",
                "보행 시 첨족(toe walking) 양상이 심해 물리치료 전/후 효과를 객관적으로 평가하고자 함."
            ],
            "physical_exam": {
                "근긴장도 검사 (MAS)": ["왼쪽 발목 발바닥굽힘근 수정된 애쉬워스 척도(MAS): 3등급"],
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
                "물리치료 적용 전 H/M 비율이 왼쪽에서 65%(정상 우측 25%)로 매우 높게 나타납니다.",
                "이는 대뇌-척수 상부 억제계 상실로 왼쪽 가자미근 알파운동신경세포의 흥분성이 정상 범위를 초과해 비정상 항진된 위운동신경세포(UMN) 양상을 의미합니다."
            ],
            "emg_reason": [
                "말초 손상이 아니며 중추성 경직 정량화를 목적으로 하였으므로 침근전도는 실시하지 않습니다."
            ],
            "integration": [
                "▶ 추정 질환: 위운동신경세포 증후군에 의한 왼쪽 하지 경직(Spasticity)",
                "▶ 추정 근거: MAS 3등급 임상 소견과 비정상적 H-반사 항진, 높은 H/M 비율을 매칭시켜 중추성 척수 억제 상실로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "▶ 말초성 S1 신경뿌리병증",
                "how_to_differentiate": "동일한 S1 반사 회로를 이용하지만, 말초 신경 뿌리 손상 시에는 H-반사 진폭이 항진되는 것이 아니라 지연되거나 완전히 소실됩니다."
            }
        ]
    }
}
