# data/cases.py (Part 1)
CASE_LIBRARY = {
    "목-팔 통증 증상과 팔 근력 약화": {
        "category": "C6 목 신경뿌리병증",
        "difficulty": "초중급",
        "patient": {
            "age": 57, "sex": "남성", "side": "왼쪽",
            "symptoms": ["2개월 전부터 뒷목에서 왼쪽 어깨, 엄지까지 뻗치는 방사통", "손목 힘이 빠짐"],
            "physical_exam": {"감각": ["C6 피부분절 촉각 둔화"], "MMT": ["Biceps 3/5", "ECR 3/5"], "반사": ["Brachioradialis DTR 감소"]}
        },
        "findings": {
            "노신경 표재감각신경활동전위 (SNAP)": "normal",
            "정중신경 감각신경활동전위 (SNAP)": "normal",
            "노신경 복합근육활동전위 (CMAP)": "normal",
            "목 척추주위근 (Cervical Paraspinal)": "paraspinal_denervation",
            "위팔두갈래근 (Biceps Brachii)": "active_denervation",
            "노쪽손목폄근 (ECR)": "active_denervation"
        },
        "teaching_diagnosis": {
            "sensory_reason": ["감각신경활동전위(SNAP)가 정상 범위로 보존됩니다. 이는 병변이 뒤뿌리신경절보다 몸쪽(척수 신경뿌리)임을 시사합니다."],
            "motor_reason": ["말초 운동신경전도(CMAP)에서 전도차단이나 지연이 없어 말초 포착 마비를 배제합니다."],
            "emg_reason": ["목 척추주위근과 C6 지배 근육들에서 비정상적 자발전위가 동시 출현하며 운동단위 동원이 감소되었습니다."],
            "integration": ["🎯 C6 목 신경뿌리병증: 임상 증상과 침근전도 탈신경 소견을 종합하여 신경뿌리 압박으로 확진합니다."]
        },
        "differential_diagnosis": [{"name": "⚖️ 노신경병증", "how_to_differentiate": "말초 노신경 손상 시 SNAP 진폭이 감소하며 척추주위근은 정상입니다."}]
    },
    "야간 손저림과 엄지 근력 약화": {
        "category": "정중신경 포착병증",
        "difficulty": "초중급",
        "patient": {
            "age": 46, "sex": "여성", "side": "오른쪽",
            "symptoms": ["오른쪽 엄지~중지 타는 듯한 저림", "야간 통증으로 잠에서 깸"],
            "physical_exam": {"감각": ["정중신경 영역 둔화"], "MMT": ["APB 4/5"], "특수": ["Phalen test 양성"]}
        },
        "findings": {
            "정중신경 감각신경활동전위 (SNAP)": "delayed",
            "자신경 감각신경활동전위 (SNAP)": "normal",
            "정중신경 복합근육활동전위 (CMAP)": "reduced",
            "짧은엄지벌림근 (APB)": "emg_normal"
        },
        "teaching_diagnosis": {
            "sensory_reason": ["정중신경 감각 잠복기가 지연되었습니다. 이는 손목굴 부위의 국소적 말이집 손상을 의미합니다."],
            "motor_reason": ["운동신경 진폭이 감소한 것은 장기화된 압박으로 인해 일부 축삭 변성이 일어났음을 뜻합니다."],
            "emg_reason": ["짧은엄지벌림근은 정상 반응이나, 이는 아직 근육의 완전한 탈신경까지는 진행되지 않았음을 보여줍니다."],
            "integration": ["🎯 오른쪽 손목굴증후군: 정중신경에 국한된 전도 지연 및 진폭 감소를 근거로 진단합니다."]
        },
        "differential_diagnosis": [{"name": "⚖️ C6 신경뿌리병증", "how_to_differentiate": "신경뿌리 질환은 말초 감각전도(SNAP)가 정상으로 유지됩니다."}]
    },
    "위팔뼈 몸통 골절 후 손목처짐": {
        "category": "노신경 포착/손상",
        "difficulty": "초중급",
        "patient": {
            "age": 34, "sex": "남성", "side": "오른쪽",
            "symptoms": ["위팔뼈 골절 수술 후 손목과 손가락을 전혀 올리지 못함"],
            "physical_exam": {"감각": ["손등 노쪽 감각 소실"], "MMT": ["ECR 2/5", "EDC 2/5"], "반사": ["위팔노근 반사 소실"]}
        },
        "findings": {
            "노신경 표재감각신경활동전위 (SNAP)": "reduced",
            "노신경 복합근육활동전위 (CMAP)": "reduced",
            "노쪽손목폄근 (ECR)": "active_denervation",
            "집게폄근 (Extensor Indicis)": "active_denervation",
            "목 척추주위근 (Cervical Paraspinal)": "emg_normal"
        },
        "teaching_diagnosis": {
            "sensory_reason": ["노신경 감각 진폭이 감소되었습니다. 이는 병변이 말초 신경 축삭 수준임을 입증합니다."],
            "motor_reason": ["운동신경 진폭 감소는 위팔뼈 골절 부위에서의 운동 축삭 손상을 뒷받침합니다."],
            "emg_reason": ["노신경 지배 근육에서 비정상 자발전위가 뚜렷하나, 목 척추주위근은 정상입니다."],
            "integration": ["🎯 나선고랑 노신경병증: 외상 이력과 합치되는 말초 축삭 손상 소견으로 확진합니다."]
        },
        "differential_diagnosis": [{"name": "⚖️ C7 신경뿌리병증", "how_to_differentiate": "신경뿌리병증은 SNAP이 정상이며 척추주위근에 이상이 나타납니다."}]
    },
    "4, 5번째 손가락 저림과 손가락 근력 약화": {
        "category": "자신경 포착병증",
        "difficulty": "초중급",
        "patient": {
            "age": 42, "sex": "남성", "side": "오른쪽",
            "symptoms": ["새끼손가락 저림과 손날 통증", "젓가락질 힘이 빠짐"],
            "physical_exam": {"감각": ["자신경 영역 감각 저하"], "MMT": ["ADM 3/5", "FDI 3/5"], "특수": ["팔꿈치 티넬 징후 양성"]}
        },
        "findings": {
            "자신경 감각신경활동전위 (SNAP)": "delayed",
            "정중신경 감각신경활동전위 (SNAP)": "normal",
            "자신경 복합근육활동전위 (CMAP) - 팔꿈치 상/하 비교": "reduced",
            "새끼벌림근 (ADM)": "active_denervation"
        },
        "teaching_diagnosis": {
            "sensory_reason": ["자신경 감각 잠복기 지연은 팔꿈치 부위의 전도 장애를 시사합니다."],
            "motor_reason": ["팔꿈치 위/아래 비교 시 진폭이 급감하는 국소 전도차단이 확인됩니다."],
            "emg_reason": ["자신경 지배 손 내재근에서 비정상 자발전위와 운동단위 동원 감소가 관찰됩니다."],
            "integration": ["🎯 팔꿈치굴증후군: 팔꿈치 구간의 국소 전도차단 및 탈신경 소견을 근거로 진단합니다."]
        },
        "differential_diagnosis": [{"name": "⚖️ C8 신경뿌리병증", "how_to_differentiate": "신경뿌리 질환은 SNAP이 보존되며 정중신경 지배 근육(APB)도 함께 침범될 수 있습니다."}]
    },
    "허리-다리 통증과 발처짐": {
        "category": "L5 허리 신경뿌리병증",
        "difficulty": "초중급",
        "patient": {
            "age": 61, "sex": "여성", "side": "오른쪽",
            "symptoms": ["요통과 함께 오른쪽 종아리~발등 방사통", "발끝이 끌리는 발처짐"],
            "physical_exam": {"감각": ["L5 피부분절 감각 둔화"], "MMT": ["TA 2/5", "EHL 2/5", "Gluteus Medius 3/5"]}
        },
        "findings": {
            "얕은종아리신경 감각신경활동전위 (SNAP)": "normal",
            "장딴지신경 감각신경활동전위 (SNAP)": "normal",
            "종아리신경 복합근육활동전위 (CMAP)": "normal",
            "허리 척추주위근 (Lumbar Paraspinal)": "paraspinal_denervation",
            "앞정강근 (Tibialis Anterior)": "active_denervation",
            "중간볼기근 (Gluteus Medius)": "active_denervation"
        },
        "teaching_diagnosis": {
            "sensory_reason": ["하지 말초 감각전도가 완전히 정상입니다. 이는 병변 위치가 뒤뿌리신경절보다 몸쪽임을 강력히 시사합니다."],
            "motor_reason": ["말초 운동신경 전도는 정상이며, 무릎 주변의 압박 징후(속도 저하 등)가 없습니다."],
            "emg_reason": ["허리 척추주위근 및 L5 지배 근육군(중간볼기근 포함)에서 동시 탈신경이 확인됩니다."],
            "integration": ["🎯 L5 허리 신경뿌리병증: 감각전도 보존과 다발 근육 및 척추주위근 침범을 근거로 진단합니다."]
        },
        "differential_diagnosis": [{"name": "⚖️ 온종아리신경병증", "how_to_differentiate": "말초 신경병증은 SNAP 진폭이 감소하며 중간볼기근과 척추주위근은 정상입니다."}]
    },
    "온종아리신경 외상성 손상 의심": {
        "category": "온종아리신경 포착/외상",
        "difficulty": "초중급",
        "patient": {
            "age": 25, "sex": "남성", "side": "왼쪽",
            "symptoms": ["축구 경기 중 무릎 바깥쪽 강한 타박상 후 발처짐 발생"],
            "physical_exam": {"감각": ["발등 감각 소실"], "MMT": ["TA 2/5", "Peroneus 2/5"], "반사": ["양측 무릎반사 정상"]}
        },
        "findings": {
            "얕은종아리신경 감각신경활동전위 (SNAP)": "reduced",
            "종아리신경 복합근육활동전위 (CMAP) - 종아리뼈머리 자극": "reduced",
            "앞정강근 (Tibialis Anterior)": "active_denervation",
            "긴종아리근 (Peroneus Longus)": "active_denervation",
            "허리 척추주위근 (Lumbar Paraspinal)": "emg_normal"
        },
        "teaching_diagnosis": {
            "sensory_reason": ["얕은종아리신경 진폭 감소는 말초 축삭 손상을 입증합니다."],
            "motor_reason": ["종아리뼈머리 부위 자극 시 진폭 급감은 직접적인 타격에 의한 전도차단을 뒷받침합니다."],
            "emg_reason": ["해당 신경 지배 근육에서 탈신경 소견이 뚜렷하며 척추주위근은 정상입니다."],
            "integration": ["🎯 온종아리신경병증: 외상 이력과 일치하는 단일 말초신경 마비로 확진합니다."]
        },
        "differential_diagnosis": [{"name": "⚖️ L5 신경뿌리병증", "how_to_differentiate": "신경뿌리병증은 SNAP이 정상이며 중간볼기근과 척추주위근 이상이 동반됩니다."}]
    }
}
# data/cases.py (Part 2: 사례 7~12 완결)
CASE_LIBRARY.update({
    "골반 외상 후 다리 전반 근력 약화": {
        "category": "신경얼기병증(Plexopathy)",
        "difficulty": "중급",
        "patient": {
            "age": 45, "sex": "여성", "side": "왼쪽",
            "symptoms": ["심한 골반 골절 수술 후 다리 전체 근력 저하", "다리 광범위한 영역의 감각 둔화"],
            "physical_exam": {"감각": ["L2-S1 피부분절 전반적 저하"], "MMT": ["Hip flexor 2/5", "Ankle dorsiflexor 2/5"], "반사": ["양측 무릎/아킬레스 반사 소실"]}
        },
        "findings": {
            "장딴지신경 감각신경활동전위 (SNAP)": "reduced",
            "얕은종아리신경 감각신경활동전위 (SNAP)": "reduced",
            "종아리신경 복합근육활동전위 (CMAP)": "reduced",
            "가쪽넓은근 (Vastus Lateralis)": "active_denervation",
            "앞정강근 (Tibialis Anterior)": "active_denervation",
            "허리 척추주위근 (Lumbar Paraspinal)": "emg_normal"
        },
        "teaching_diagnosis": {
            "sensory_reason": ["다수의 말초 감각신경(SNAP) 진폭이 감소되었습니다. 이는 병변이 뒤뿌리신경절보다 먼쪽임을 의미합니다."],
            "motor_reason": ["여러 운동신경(CMAP)에서 진폭 감소가 도출되어 신경얼기 수준의 다발성 축삭 손상을 증명합니다."],
            "emg_reason": ["다리 전면과 후면 근육에서 광범위한 탈신경이 관찰되나, 척추주위근은 정상입니다."],
            "integration": ["🎯 허리엉치신경얼기병증: 외상 이력과 감각전도 감소, 척추주위근 보존 패턴을 결합하여 확진합니다."]
        },
        "differential_diagnosis": [{"name": "⚖️ 다발 신경뿌리병증", "how_to_differentiate": "신경뿌리병증은 SNAP이 보존되며 척추주위근 탈신경이 반드시 동반됩니다."}]
    },
    "양측 발끝 저림과 발가락 약화": {
        "category": "다발신경병증(Polyneuropathy)",
        "difficulty": "초중급",
        "patient": {
            "age": 67, "sex": "남성", "side": "양쪽",
            "symptoms": ["만성 당뇨 병력", "양쪽 발끝에서 시작해 발목으로 올라오는 저림과 화끈거림"],
            "physical_exam": {"감각": ["장갑-양말형 감각 저하"], "MMT": ["발가락 폄근 4/5"], "반사": ["양측 아킬레스 반사 소실"]}
        },
        "findings": {
            "장딴지신경 감각신경활동전위 (SNAP)": "reduced",
            "얕은종아리신경 감각신경활동전위 (SNAP)": "reduced",
            "정강신경 복합근육활동전위 (CMAP)": "reduced",
            "앞정강근 (Tibialis Anterior)": "active_chronic"
        },
        "teaching_diagnosis": {
            "sensory_reason": ["양측 하지 먼쪽 감각신경 진폭이 대칭적으로 감소했습니다. 이는 전신적 축삭 손상을 시사합니다."],
            "motor_reason": ["운동신경 진폭 또한 대칭적으로 감소하여 길이의존성(Dying-back) 양상을 뒷받침합니다."],
            "emg_reason": ["양측 앞정강근에서 만성적 탈신경 자발전위와 재신경지배 소견이 대칭적으로 관찰됩니다."],
            "integration": ["🎯 길이 의존성 축삭성 다발신경병증: 당뇨 병력과 대칭적 진폭 감소를 근거로 진단합니다."]
        },
        "differential_diagnosis": [{"name": "⚖️ 말이집탈락성 다발신경병증", "how_to_differentiate": "말이집탈락성은 진폭 감소보다 전 구간의 잠복기 지연과 속도 저하가 주된 소견입니다."}]
    },
    "상부 위팔신경얼기병증 의심": {
        "category": "신경얼기병증(Plexopathy)",
        "difficulty": "중급",
        "patient": {
            "age": 37, "sex": "여성", "side": "왼쪽",
            "symptoms": ["사고 후 어깨 벌림과 팔꿉관절 굽힘 불가", "어깨 바깥쪽 감각 소실"],
            "physical_exam": {"감각": ["C5-C6 영역 감각 소실"], "MMT": ["Deltoid 2/5", "Biceps 2/5"], "반사": ["Biceps 반사 소실"]}
        },
        "findings": {
            "가쪽아래팔피부신경 감각전도 (SNAP)": "reduced",
            "겨드랑신경 복합근육활동전위 (CMAP)": "reduced",
            "근육피부신경 복합근육활동전위 (CMAP)": "reduced",
            "어깨세모근 (Deltoid)": "active_denervation",
            "목 척추주위근 (Cervical Paraspinal)": "emg_normal"
        },
        "teaching_diagnosis": {
            "sensory_reason": ["가쪽아래팔피부신경 SNAP 진폭이 감소되었습니다. 이는 병변이 신경얼기 수준에 있음을 증명합니다."],
            "motor_reason": ["C5-C6 지배 운동신경 반응이 소실되어 상부 줄기(Upper trunk)의 심각한 축삭 손상을 나타냅니다."],
            "emg_reason": ["어깨 및 위팔 근육들에서 탈신경 전위가 뚜렷하나 척추주위근은 정상입니다."],
            "integration": ["🎯 상부 위팔신경얼기병증: SNAP 감소와 척추주위근 보존 패턴을 통해 신경뿌리 질환과 감별합니다."]
        },
        "differential_diagnosis": [{"name": "⚖️ C5-C6 신경뿌리병증", "how_to_differentiate": "신경뿌리병증은 말초 SNAP이 보존되며 목 척추주위근 이상이 동반됩니다."}]
    },
    "대칭성 팔다리 근력저하와 보행 저하": {
        "category": "다발신경병증(Polyneuropathy)",
        "difficulty": "중급",
        "patient": {
            "age": 55, "sex": "여성", "side": "양쪽",
            "symptoms": ["최근 수주간 진행된 대칭적 근력 약화", "손발 저림과 보행 장애"],
            "physical_exam": {"감각": ["전신 대칭적 감각 탈락"], "MMT": ["사지 근력 Fair(3/5)"], "반사": ["전신 깊은힘줄반사 완벽 소실"]}
        },
        "findings": {
            "정중신경 감각신경활동전위 (SNAP)": "delayed",
            "종아리신경 복합근육활동전위 (CMAP)": "delayed",
            "정강/종아리신경 F파": "fwave_delayed_absent",
            "앞정강근 (Tibialis Anterior)": "emg_normal"
        },
        "teaching_diagnosis": {
            "sensory_reason": ["광범위한 감각신경 잠복기 지연은 다발성 말이집 탈락성 변화를 입증합니다."],
            "motor_reason": ["운동신경 잠복기 지연 및 F파 소실은 신경뿌리를 포함한 다발성 전도 지연을 의미합니다."],
            "emg_reason": ["침근전도에서 축삭 손상을 대변하는 자발전위가 없어 현재 말이집 손상 위주의 단계임을 지시합니다."],
            "integration": ["🎯 만성 염증성 말이집탈락성 다발신경병증(CIDP): 전신 무반사와 전도 지연을 근거로 진단합니다."]
        },
        "differential_diagnosis": [{"name": "⚖️ 근육병증", "how_to_differentiate": "근육병증은 말단 감각 소실이 없으며 전신 반사가 어느 정도 보존됩니다."}]
    },
    "눈꺼풀 떨림과 눈 주위 불편감 지속": {
        "category": "뇌신경 들신경 장애",
        "difficulty": "중급",
        "patient": {
            "age": 62, "sex": "여성", "side": "오른쪽",
            "symptoms": ["우측 눈꺼풀 미세 떨림", "우측 이마와 눈 주변 감각 둔화"],
            "physical_exam": {"표정근": ["양측 대칭 정상"], "감각": ["우측 삼차신경 V1 영역 저하"], "반사": ["우측 각막반사 지연"]}
        },
        "findings": {
            "눈깜빡반사 우측 자극-우측 R1": "blink_delayed",
            "눈깜빡반사 우측 자극-우측 R2": "blink_delayed_absent",
            "눈깜빡반사 우측 자극-좌측 R2": "blink_delayed_absent",
            "눈깜빡반사 좌측 자극-좌측 R1": "normal"
        },
        "teaching_diagnosis": {
            "reflex_reason": ["우측 자극 시 연관된 모든 반사 반응이 지연/소실되었습니다. 반면 좌측 자극 시에는 양측 반응이 모두 정상입니다.", "이는 안면신경은 정상이지만 우측 삼차신경(들신경) 경로가 손상되었음을 확증합니다."],
            "integration": ["🎯 우측 삼차신경 전도 장애: 얼굴 운동 기능은 정상이나 우측 자극 시에만 반사가 차단되는 현상을 결합해 진단합니다."]
        },
        "differential_diagnosis": [{"name": "⚖️ 말초성 얼굴마비", "how_to_differentiate": "얼굴마비라면 어느 쪽을 자극하든 상관없이 병변측 눈을 감는 반응(R2)이 소실되어야 합니다."}]
    },
    "뇌졸중 환자 발목 경직 평가": {
        "category": "경직(Spasticity) 정량 평가",
        "difficulty": "중급",
        "patient": {
            "age": 68, "sex": "남성", "side": "왼쪽",
            "symptoms": ["뇌졸중 발병 1년 후 좌측 편마비", "발목 장딴지 근육 경직으로 보행 시 첨족 양상"],
            "physical_exam": {"근긴장도": ["좌측 발목 MAS 3등급"], "반사": ["좌측 아킬레스 반사 항진(4+)", "Ankle clonus 관찰"]}
        },
        "findings": {
            "가자미근 H-반사 진폭": "h_reflex_hyperactive",
            "가자미근 H/M 비율 (치료 전)": "h_m_ratio_increased",
            "가자미근 H/M 비율 (치료 후)": "normal"
        },
        "teaching_diagnosis": {
            "reflex_reason": ["H-반사 항진과 높은 H/M 비율은 상위 조절 시스템의 파괴로 인한 척수 반사 회로의 과흥분 상태를 정량적으로 입증합니다.", "치료 후 비율 감소는 물리치료 중재에 의해 경직이 완화되었음을 보여주는 객관적 지표입니다."],
            "integration": ["🎯 위운동신경세포 증후군에 의한 하지 경직: 비정상적 H-반사 항진을 통해 중추성 억제 상실 상태를 확증합니다."]
        },
        "differential_diagnosis": []
    }
})
