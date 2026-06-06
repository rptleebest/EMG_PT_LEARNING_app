# data/virtual_reports.py [Part 4/6]

"""
가상 결과표 판독학습용 데이터베이스 및 영문 변환 모듈.
대한의사협회(KMA) 6.1판 의학용어 원칙을 준수합니다.
"""

ENG_MAP = {
    # Headers & UI
    "검사 신경": "Nerve", "측": "Side", "기록 위치": "Recording Site", "자극 위치": "Stimulation Site",
    "진폭": "Amplitude", "잠복기": "Latency", "전도속도": "Conduction Velocity",
    "기록 근육": "Recording Muscle", "검사 항목": "Test Parameter", "검사 근육": "Muscle",
    "분절": "Segment", "말초신경": "Peripheral Nerve", "휴식 시 반응": "Resting Activity", "자발적 근수축 시 반응": "Voluntary MU Recruitment",
    "오른쪽": "Rt.", "왼쪽": "Lt.", "양측": "Both",
    
    # Sensory / Motor Nerves
    "정중신경 감각신경활동전위(Median SNAP)": "Median SNAP", "자신경 감각신경활동전위(Ulnar SNAP)": "Ulnar SNAP",
    "노신경 표재감각신경활동전위(Superficial radial SNAP)": "Superficial Radial SNAP", "얕은종아리신경 감각신경활동전위(Superficial peroneal SNAP)": "Superficial Peroneal SNAP",
    "장딴지신경 감각신경활동전위(Sural SNAP)": "Sural SNAP", "가쪽아래팔피부신경 감각신경활동전위(Lateral antebrachial cutaneous SNAP)": "Lateral Antebrachial Cutaneous SNAP",
    "정중신경 복합근육활동전위(Median CMAP)": "Median CMAP", "자신경 복합근육활동전위(Ulnar CMAP)": "Ulnar CMAP",
    "노신경 복합근육활동전위(Radial CMAP)": "Radial CMAP", "종아리신경 복합근육활동전위(Peroneal CMAP)": "Peroneal CMAP",
    "정강신경 복합근육활동전위(Tibial CMAP)": "Tibial CMAP", "겨드랑신경 복합근육활동전위(Axillary CMAP)": "Axillary CMAP",
    "근육피부신경 복합근육활동전위(Musculocutaneous CMAP)": "Musculocutaneous CMAP", "얼굴신경 복합근육활동전위(Facial CMAP)": "Facial CMAP",
    
    # Late Responses
    "정강신경 F파(Tibial F-wave)": "Tibial F-wave", "H-반사(H-reflex)": "H-reflex", "H/M 비율": "H/M Ratio",
    "눈깜빡반사 오른쪽 자극-오른쪽 R1": "Blink Reflex Rt Stim - Rt R1", "눈깜빡반사 오른쪽 자극-오른쪽 R2": "Blink Reflex Rt Stim - Rt R2",
    "눈깜빡반사 오른쪽 자극-왼쪽 R2": "Blink Reflex Rt Stim - Lt R2", "눈깜빡반사 왼쪽 자극-왼쪽 R1": "Blink Reflex Lt Stim - Lt R1",
    "눈깜빡반사 왼쪽 자극-왼쪽 R2": "Blink Reflex Lt Stim - Lt R2", "눈깜빡반사 왼쪽 자극-오른쪽 R2": "Blink Reflex Lt Stim - Rt R2",
    
    # Sites & Muscles
    "검지": "Index Finger", "새끼손가락": "Little Finger", "손등 노쪽": "Dorsoradial Hand", "발등": "Dorsum of Foot", 
    "가쪽 발목": "Lateral Malleolus", "아래팔 가쪽": "Lateral Forearm", "손목": "Wrist", "팔꿈치": "Elbow", 
    "아래팔": "Forearm", "종아리 가쪽": "Lateral Calf", "종아리 뒤쪽": "Posterior Calf", "발목": "Ankle", 
    "오금": "Popliteal Fossa", "종아리뼈머리": "Fibular Head", "종아리뼈머리 아래": "Below Fibular Head", 
    "종아리뼈머리 위": "Above Fibular Head", "팔꿈치 아래": "Below Elbow", "팔꿈치 위": "Above Elbow", "귓바퀴 앞": "Preauricular",
    
    "짧은엄지벌림근(APB)": "Abductor Pollicis Brevis", "짧은엄지벌림근": "Abductor Pollicis Brevis",
    "첫째등쪽뼈사이근(FDI)": "First Dorsal Interosseous", "첫째등쪽뼈사이근": "First Dorsal Interosseous",
    "목 척추주위근(Cervical paraspinal)": "Cervical Paraspinals", "목 척추주위근": "Cervical Paraspinals",
    "위팔두갈래근(Biceps brachii)": "Biceps Brachii", "위팔두갈래근": "Biceps Brachii",
    "노쪽손목폄근(Extensor carpi radialis)": "Extensor Carpi Radialis", "노쪽손목폄근": "Extensor Carpi Radialis", "손목폄근": "Wrist Extensor",
    "어깨세모근(Deltoid)": "Deltoid", "어깨세모근": "Deltoid",
    "앞정강근(Tibialis anterior)": "Tibialis Anterior", "앞정강근": "Tibialis Anterior",
    "긴종아리근(Peroneus longus)": "Peroneus Longus", "긴종아리근": "Peroneus Longus",
    "가자미근(Soleus)": "Soleus", "가자미근": "Soleus",
    "허리 척추주위근(Lumbar paraspinal)": "Lumbar Paraspinals", "허리 척추주위근": "Lumbar Paraspinals",
    "긴엄지폄근(Extensor hallucis longus)": "Extensor Hallucis Longus", "긴엄지폄근": "Extensor Hallucis Longus",
    "중간볼기근(Gluteus medius)": "Gluteus Medius", "중간볼기근": "Gluteus Medius",
    "가쪽넓은근(Vastus lateralis)": "Vastus Lateralis", "가쪽넓은근": "Vastus Lateralis",
    "새끼벌림근(ADM)": "Abductor Digiti Minimi", "새끼벌림근": "Abductor Digiti Minimi",
    "짧은발가락폄근(EDB)": "Extensor Digitorum Brevis", "짧은발가락폄근": "Extensor Digitorum Brevis",
    "엄지벌림근(AH)": "Abductor Hallucis", "엄지벌림근": "Abductor Hallucis",
    "눈둘레근(Orbicularis oculi)": "Orbicularis Oculi", "눈둘레근": "Orbicularis Oculi",
    "입둘레근(Orbicularis oris)": "Orbicularis Oris", "깨물근(Masseter)": "Masseter", "집게폄근": "Extensor Indicis",
    
    # Nerves in EMG
    "정중신경": "Median Nerve", "자신경": "Ulnar Nerve", "노신경": "Radial Nerve",
    "근육피부신경": "Musculocutaneous Nerve", "겨드랑신경": "Axillary Nerve",
    "뒤가지(posterior ramus)": "Posterior Ramus", "깊은종아리신경": "Deep Peroneal Nerve",
    "얕은종아리신경": "Superficial Peroneal Nerve", "정강신경": "Tibial Nerve",
    "위볼기신경": "Superior Gluteal Nerve", "넓적다리신경": "Femoral Nerve",
    "얼굴신경": "Facial Nerve", "삼차신경": "Trigeminal Nerve",
    
    # Results
    "반응 소실": "No Response", "소실": "Absent", "지연": "Delayed", "감소": "Reduced",
    "정상 범위": "Normal Range", "보존": "Preserved", "통증 및 협조 부족으로 검사 제한": "Limited by Pain",
    "Silent at rest": "Silent at rest",
    "Reduced MU recruitment": "Reduced MU recruitment",
    "Normal MU recruitment": "Normal MU recruitment"
}

def translate_value(value, to_english=False):
    if value is None: return ""
    text = str(value).strip()
    return ENG_MAP.get(text, text) if to_english else text

VIRTUAL_REPORTS = {
    "오른쪽 손목굴증후군 의심": {
        "meta": {
            "age": 52, "sex": "여성", "side": "오른쪽",
            "chief": "최근 3개월간 오른쪽 엄지부터 중지까지 타는 듯한 저림이 발생했으며, 수면 중 통증으로 자주 깸. 손목을 굽히고 있으면 저림이 더욱 악화됨.",
        },
        "sensory_ncs": [
            {"nerve": "정중신경 감각신경활동전위(Median SNAP)", "recording": "검지", "stimulation": "손목", "side": "오른쪽", "amplitude": "7 μV", "latency": "4.6 ms", "velocity": "32 m/s"},
            {"nerve": "정중신경 감각신경활동전위(Median SNAP)", "recording": "검지", "stimulation": "손목", "side": "왼쪽", "amplitude": "24 μV", "latency": "2.8 ms", "velocity": "51 m/s"},
            {"nerve": "자신경 감각신경활동전위(Ulnar SNAP)", "recording": "새끼손가락", "stimulation": "손목", "side": "오른쪽", "amplitude": "23 μV", "latency": "2.6 ms", "velocity": "54 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "정중신경 복합근육활동전위(Median CMAP)", "recording": "짧은엄지벌림근", "stimulation": "손목", "side": "오른쪽", "amplitude": "3.0 mV", "latency": "5.8 ms", "velocity": "-"},
            {"nerve": "정중신경 복합근육활동전위(Median CMAP)", "recording": "짧은엄지벌림근", "stimulation": "팔꿈치", "side": "오른쪽", "amplitude": "2.8 mV", "latency": "10.2 ms", "velocity": "48 m/s"},
            {"nerve": "자신경 복합근육활동전위(Ulnar CMAP)", "recording": "새끼벌림근", "stimulation": "손목", "side": "오른쪽", "amplitude": "8.8 mV", "latency": "2.7 ms", "velocity": "-"}
        ],
        "needle_emg": [
            {"muscle": "짧은엄지벌림근", "root": "C8-T1", "nerve": "정중신경", "rest": "fibrillation potential, positive sharp wave", "volition": "Reduced MU recruitment"},
            {"muscle": "첫째등쪽뼈사이근", "root": "C8-T1", "nerve": "자신경", "rest": "Silent at rest", "volition": "Normal MU recruitment"},
            {"muscle": "목 척추주위근", "root": "C8-T1", "nerve": "뒤가지(posterior ramus)", "rest": "Silent at rest", "volition": "통증 및 협조 부족으로 검사 제한"}
        ],
        "interpretation": {
            "sensory": [
                "오른쪽 정중신경 감각신경 진폭이 정상인 왼쪽(24 μV)에 비해 7 μV로 현저히 감소하였으며, 잠복기가 연장되었습니다. 이는 정중신경의 감각 축삭 손상을 의미합니다.",
                "동일한 손의 자신경 감각신경은 정상 보존되어, 전신 다발신경병증이 아닌 정중신경에 국한된 말초성 포착 병변임을 확증합니다."
            ],
            "motor": [
                "오른쪽 정중신경 운동검사 시 손목 자극에서 원위잠복기가 5.8 ms로 뚜렷하게 지연되어 손목 구간의 국소 전도 지연(말이집 탈락)을 입증합니다.",
                "진폭(3.0 mV) 또한 저하되어 있어 단순 압박을 넘어 운동 신경의 먼쪽(distal) 축삭 파괴가 동반되었음을 지시합니다."
            ],
            "emg": [
                "정중신경 지배를 받는 먼쪽 근육인 짧은엄지벌림근에서 휴식 시 비정상 자발전위가 검출되어 활동성 손상을 확인합니다.",
                "경추 신경뿌리 손상을 대변하는 척추주위근 및 자신경 지배 근육은 전기적으로 조용(Silent at rest)하여 정상입니다."
            ],
            "integration": [
                "▶ 추정 질환: 오른쪽 손목굴증후군 (Carpal tunnel syndrome)",
                "▶ 추정한 이유: 자신경과 목 척추주위근이 완벽히 정상인 상태에서, 정중신경 지배 영역에 국한된 운동/감각 전도 지연 및 진폭 감소가 도출되었습니다. 침근전도에서 짧은엄지벌림근의 단독 탈신경 소견이 일치하므로 손목굴 부위의 정중신경 포착으로 최종 확진합니다."
            ],
            "differential": [
                "▶ C6 목 신경뿌리병증: 감각신경전도(SNAP)가 대개 보존되며, 목 척추주위근 침근전도에서 탈신경 자발전위가 나타나야 합니다."
            ]
        }
    },

    "왼쪽 C6 신경뿌리병증 의심": {
        "meta": {
            "age": 45, "sex": "남성", "side": "왼쪽",
            "chief": "뒷목부터 왼쪽 어깨를 거쳐 위팔 가쪽 및 엄지/검지로 뻗치는 방사통이 4주간 지속됨. 머리를 감거나 팔꿉관절을 굽힐 때 힘이 빠지는 느낌을 호소함."
        },
        "sensory_ncs": [
            {"nerve": "정중신경 감각신경활동전위(Median SNAP)", "recording": "검지", "stimulation": "손목", "side": "왼쪽", "amplitude": "26 μV", "latency": "2.9 ms", "velocity": "52 m/s"},
            {"nerve": "노신경 표재감각신경활동전위(Superficial radial SNAP)", "recording": "손등 노쪽", "stimulation": "아래팔", "side": "왼쪽", "amplitude": "21 μV", "latency": "2.5 ms", "velocity": "53 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "정중신경 복합근육활동전위(Median CMAP)", "recording": "짧은엄지벌림근", "stimulation": "손목", "side": "왼쪽", "amplitude": "8.6 mV", "latency": "3.5 ms", "velocity": "-"},
            {"nerve": "노신경 복합근육활동전위(Radial CMAP)", "recording": "손목폄근", "stimulation": "아래팔", "side": "왼쪽", "amplitude": "6.7 mV", "latency": "2.9 ms", "velocity": "-"}
        ],
        "needle_emg": [
            {"muscle": "위팔두갈래근", "root": "C5-C6", "nerve": "근육피부신경", "rest": "fibrillation potential, positive sharp wave", "volition": "Reduced MU recruitment"},
            {"muscle": "노쪽손목폄근", "root": "C6-C7", "nerve": "노신경", "rest": "fibrillation potential, positive sharp wave", "volition": "Giant MUAPs with reduced recruitment"},
            {"muscle": "목 척추주위근", "root": "C6", "nerve": "뒤가지(posterior ramus)", "rest": "fibrillation potential, positive sharp wave", "volition": "통증 및 협조 부족으로 검사 제한"}
        ],
        "interpretation": {
            "sensory": [
                "환자는 뚜렷한 손가락 방사통을 호소하지만, 정중신경과 노신경의 말초 감각신경 진폭 및 잠복기는 대칭적으로 완벽하게 보존되어 정상 수치를 보입니다.",
                "감각 기능은 떨어지나 신경전도가 정상이라는 것은, 병변이 감각신경 세포체(DRG)보다 중추 쪽인 신경뿌리(Root)에 위치함을 입증하는 생리학적 증거입니다."
            ],
            "motor": [
                "말초 운동신경전도검사에서 전도차단이나 원위잠복기 지연이 전혀 관찰되지 않아 말초 포착성 병변(예: 손목굴증후군)을 배제합니다."
            ],
            "emg": [
                "근육피부신경 지배(위팔두갈래근)와 노신경 지배(노쪽손목폄근)라는 전혀 다른 말초신경계 근육에서 동시 탈신경 소견이 보입니다. 이들은 'C6 분절'이라는 공통 뿌리를 갖습니다.",
                "결정적으로 척수 신경뿌리 손상을 직접 대변하는 목 척추주위근(뒤가지)에서도 비정상적인 자발전위가 도출되었습니다."
            ],
            "integration": [
                "▶ 추정 질환: 왼쪽 C6 목 신경뿌리병증 (C6 Cervical radiculopathy)",
                "▶ 추정한 이유: 감각신경전도의 완전한 보존 소견과 함께, 서로 다른 말초신경의 지배를 받으나 C6 척수 분절을 공유하는 다발 근육군 및 목 척추주위근에 탈신경 현상이 동시 관찰되므로 C6 척수 신경뿌리 병변으로 확진합니다."
            ],
            "differential": [
                "▶ 왼쪽 상부 위팔신경얼기병증: 신경뿌리가 아닌 얼기 수준의 손상이면 말초 감각신경 진폭 감소가 동반되어야 하며, 척추주위근은 정상이어야 합니다."
            ]
        }
    },

    "오른쪽 온종아리신경병증 의심": {
        "meta": {
            "age": 32, "sex": "남성", "side": "오른쪽",
            "chief": "장시간 다리를 꼬고 앉아 업무를 본 뒤 우측 발목을 위로 들어올리지 못하는 발처짐(Foot drop)이 발생함. 발등 외측의 감각 둔화 동반."
        },
        "sensory_ncs": [
            {"nerve": "얕은종아리신경 감각신경활동전위(Superficial peroneal SNAP)", "recording": "발등", "stimulation": "종아리 가쪽", "side": "오른쪽", "amplitude": "4 μV", "latency": "3.6 ms", "velocity": "36 m/s"},
            {"nerve": "장딴지신경 감각신경활동전위(Sural SNAP)", "recording": "가쪽 발목", "stimulation": "종아리 뒤쪽", "side": "오른쪽", "amplitude": "16 μV", "latency": "3.0 ms", "velocity": "47 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "종아리신경 복합근육활동전위(Peroneal CMAP)", "recording": "짧은발가락폄근", "stimulation": "종아리뼈머리 아래", "side": "오른쪽", "amplitude": "4.4 mV", "latency": "9.1 ms", "velocity": "45 m/s"},
            {"nerve": "종아리신경 복합근육활동전위(Peroneal CMAP)", "recording": "짧은발가락폄근", "stimulation": "종아리뼈머리 위", "side": "오른쪽", "amplitude": "1.5 mV", "latency": "12.8 ms", "velocity": "25 m/s"}
        ],
        "needle_emg": [
            {"muscle": "앞정강근", "root": "L4-L5", "nerve": "깊은종아리신경", "rest": "fibrillation potential, positive sharp wave", "volition": "Reduced MU recruitment"},
            {"muscle": "허리 척추주위근", "root": "L5", "nerve": "뒤가지(posterior ramus)", "rest": "Silent at rest", "volition": "통증 및 협조 부족으로 검사 제한"}
        ],
        "interpretation": {
            "sensory": [
                "오른쪽 얕은종아리신경 감각 진폭이 정상(14 μV) 대비 4 μV로 크게 감소하여 먼쪽(distal) 말초 감각 축삭 손상을 증명합니다.",
                "인접한 장딴지신경 반응은 완벽히 정상이므로 광범위 다발신경병증이나 골반 내 좌골신경 병변 가능성은 배제됩니다."
            ],
            "motor": [
                "종아리신경 운동검사에서 '종아리뼈머리 위(몸쪽)' 자극 시 진폭(1.5 mV)이 '아래(먼쪽)' 자극(4.4 mV)보다 절반 이상 급감하였습니다.",
                "이는 종아리뼈머리 가쪽 구간을 지날 때 전기 신호가 차단되는 심각한 국소 전도차단(Conduction block)의 전형적 소견입니다."
            ],
            "emg": [
                "깊은종아리신경 지배 근육인 앞정강근에서 탈신경성 자발전위가 뚜렷하게 관찰됩니다.",
                "반면, 허리 척추주위근은 전기적으로 조용하여 요추 신경뿌리 병변을 완벽하게 감별해 줍니다."
            ],
            "integration": [
                "▶ 추정 질환: 오른쪽 온종아리신경병증 (Common peroneal neuropathy)",
                "▶ 추정한 이유: 종아리뼈머리 구간의 명확한 운동 전도차단, 얕은종아리신경 감각 진폭 감소, 요추 척추주위근 정상 소견을 통해 종아리뼈머리 부위의 외부 기계적 압박에 의한 단일 신경 마비임을 확증합니다."
            ],
            "differential": [
                "▶ L5 허리 신경뿌리병증: 얕은종아리신경 감각전도가 정상으로 완벽히 보존되어야 하며, 침근전도에서 허리 척추주위근과 중간볼기근 이상이 동반되어야 합니다."
            ]
        }
    },

    "왼쪽 L5 신경뿌리병증 의심": {
        "meta": {
            "age": 58, "sex": "여성", "side": "왼쪽",
            "chief": "한 달 전 무거운 화분을 든 이후 허리에서 좌측 엉치, 종아리 가쪽을 타고 발등까지 전기가 통하듯 뻗치는 방사통. 발처짐 증상 발생."
        },
        "sensory_ncs": [
            {"nerve": "얕은종아리신경 감각신경활동전위(Superficial peroneal SNAP)", "recording": "발등", "stimulation": "종아리 가쪽", "side": "왼쪽", "amplitude": "13 μV", "latency": "2.9 ms", "velocity": "47 m/s"},
            {"nerve": "장딴지신경 감각신경활동전위(Sural SNAP)", "recording": "가쪽 발목", "stimulation": "종아리 뒤쪽", "side": "왼쪽", "amplitude": "15 μV", "latency": "3.1 ms", "velocity": "46 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "종아리신경 복합근육활동전위(Peroneal CMAP)", "recording": "짧은발가락폄근", "stimulation": "발목", "side": "왼쪽", "amplitude": "3.9 mV", "latency": "4.5 ms", "velocity": "-"},
            {"nerve": "정강신경 복합근육활동전위(Tibial CMAP)", "recording": "엄지벌림근", "stimulation": "발목", "side": "왼쪽", "amplitude": "7.4 mV", "latency": "4.2 ms", "velocity": "-"}
        ],
        "needle_emg": [
            {"muscle": "앞정강근", "root": "L4-L5", "nerve": "깊은종아리신경", "rest": "fibrillation potential, positive sharp wave", "volition": "Reduced MU recruitment"},
            {"muscle": "중간볼기근", "root": "L5", "nerve": "위볼기신경", "rest": "fibrillation potential, positive sharp wave", "volition": "Reduced MU recruitment"},
            {"muscle": "허리 척추주위근", "root": "L5", "nerve": "뒤가지(posterior ramus)", "rest": "fibrillation potential, positive sharp wave", "volition": "통증 및 협조 부족으로 검사 제한"}
        ],
        "interpretation": {
            "sensory": [
                "다리 감각을 담당하는 얕은종아리신경과 장딴지신경의 감각신경 전도가 완전히 보존됩니다.",
                "이는 뒤뿌리신경절(DRG) 상위인 신경뿌리의 압박을 강력히 지지하는 전형적인 소견입니다."
            ],
            "motor": [
                "종아리신경 운동검사에서 말초 부위 전도차단이나 국소 속도 저하 소견이 발견되지 않아 무릎 주변 포착 마비를 배제합니다."
            ],
            "emg": [
                "허리 척추주위근, 앞정강근, 중간볼기근에서 탈신경 자발전위가 대거 관찰됩니다.",
                "깊은종아리신경과 위볼기신경 등 서로 다른 신경 지배를 받으나 L5 분절을 공유하는 근육들의 동시 탈신경입니다."
            ],
            "integration": [
                "▶ 추정 질환: 왼쪽 L5 허리 신경뿌리병증 (L5 Lumbar radiculopathy)",
                "▶ 추정한 이유: 말초 감각신경 전도가 대칭적으로 정상 보존되고, 침근전도에서 L5 지배 다발 근육 및 핵심적인 요추 척추주위근 침범이 확인되어 척수 신경뿌리 압박으로 확진합니다."
            ],
            "differential": [
                "▶ 온종아리신경병증: 얕은종아리신경 감각 진폭이 감소하고, 허리 척추주위근 및 위볼기신경 지배인 중간볼기근은 정상이어야 합니다."
            ]
        }
    },
# data/virtual_reports.py [Part 5/6]

    "축삭성 다발신경병증 의심": {
        "meta": {
            "age": 68, "sex": "남성", "side": "양측",
            "chief": "20년 이상의 당뇨병 병력. 몇 년 전부터 양쪽 발끝에서 시작된 대칭성 저림과 화끈거림이 점차 발목 위로 올라오며 수면을 방해함."
        },
        "sensory_ncs": [
            {"nerve": "장딴지신경 감각신경활동전위(Sural SNAP)", "recording": "가쪽 발목", "stimulation": "종아리 뒤쪽", "side": "오른쪽", "amplitude": "반응 소실", "latency": "반응 소실", "velocity": "반응 소실"},
            {"nerve": "얕은종아리신경 감각신경활동전위(Superficial peroneal SNAP)", "recording": "발등", "stimulation": "종아리 가쪽", "side": "오른쪽", "amplitude": "3 μV", "latency": "3.9 ms", "velocity": "33 m/s"},
            {"nerve": "정중신경 감각신경활동전위(Median SNAP)", "recording": "검지", "stimulation": "손목", "side": "오른쪽", "amplitude": "18 μV", "latency": "3.2 ms", "velocity": "48 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "정강신경 복합근육활동전위(Tibial CMAP)", "recording": "엄지벌림근", "stimulation": "발목", "side": "오른쪽", "amplitude": "1.4 mV", "latency": "5.9 ms", "velocity": "-"},
            {"nerve": "정중신경 복합근육활동전위(Median CMAP)", "recording": "짧은엄지벌림근", "stimulation": "손목", "side": "오른쪽", "amplitude": "7.6 mV", "latency": "3.8 ms", "velocity": "-"}
        ],
        "needle_emg": [
            {"muscle": "앞정강근", "root": "L4-L5", "nerve": "깊은종아리신경", "rest": "fibrillation potential, positive sharp wave", "volition": "Reduced MU recruitment"},
            {"muscle": "가쪽넓은근", "root": "L2-L4", "nerve": "넓적다리신경", "rest": "Silent at rest", "volition": "Normal MU recruitment"}
        ],
        "interpretation": {
            "sensory": [
                "다리 가장 먼쪽(distal)인 장딴지신경 감각반응은 완전히 소실되었으나, 상지인 정중신경 감각은 어느 정도 보존되어 있습니다.",
                "이는 신경 길이가 긴 발끝 축삭부터 서서히 퇴행하는 길이의존성(Length-dependent, dying-back) 패턴입니다."
            ],
            "motor": [
                "하지 운동신경의 CMAP 진폭 역시 대칭적으로 크게 낮아, 광범위한 만성 운동축삭 파괴 상태를 지지합니다."
            ],
            "emg": [
                "다리 먼쪽 근육(앞정강근)에서 탈신경 전위가 확인되며, 몸쪽(proximal) 근육인 가쪽넓은근은 정상으로 말단 중심 손상을 뒷받침합니다."
            ],
            "integration": [
                "▶ 추정 질환: 길이의존성 축삭성 다발신경병증 (Axonal polyneuropathy)",
                "▶ 추정한 이유: 양측 대칭적 장갑-양말형(Glove-stocking) 감각 둔화와 함께, 전신 신경 중 긴 신경 말단에서 가장 심한 진폭 감소 및 탈신경 소견이 관찰되어 만성 축삭성 대사성/염증성 병변임을 확증합니다."
            ],
            "differential": [
                "▶ 말이집탈락성 다발신경병증: 진폭 감소보다는 신경 전 구간의 극심한 전도속도 저하 및 잠복기 연장이 먼저 관찰됩니다."
            ]
        }
    },

    "급성 말이집탈락성 다발신경뿌리병증 의심": {
        "meta": {
            "age": 41, "sex": "여성", "side": "양측",
            "chief": "장염 후 2주 뒤부터 양측 다리의 힘이 빠지기 시작하여 현재는 걷기가 힘든 상행성(ascending) 근력 저하 발생. 깊은힘줄반사(DTR) 완벽 소실."
        },
        "sensory_ncs": [
            {"nerve": "정중신경 감각신경활동전위(Median SNAP)", "recording": "검지", "stimulation": "손목", "side": "오른쪽", "amplitude": "18 μV", "latency": "3.8 ms", "velocity": "39 m/s"},
            {"nerve": "장딴지신경 감각신경활동전위(Sural SNAP)", "recording": "가쪽 발목", "stimulation": "종아리 뒤쪽", "side": "오른쪽", "amplitude": "14 μV", "latency": "3.2 ms", "velocity": "45 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "종아리신경 복합근육활동전위(Peroneal CMAP)", "recording": "짧은발가락폄근", "stimulation": "종아리뼈머리", "side": "오른쪽", "amplitude": "2.4 mV", "latency": "18.9 ms", "velocity": "28 m/s"},
            {"nerve": "정강신경 복합근육활동전위(Tibial CMAP)", "recording": "엄지벌림근", "stimulation": "발목", "side": "오른쪽", "amplitude": "3.5 mV", "latency": "7.2 ms", "velocity": "-"}
        ],
        "late_response": [
            {"test": "정강신경 F파(Tibial F-wave)", "side": "오른쪽", "latency": "소실", "amplitude": "-"}
        ],
        "needle_emg": [
            {"muscle": "앞정강근", "root": "L4-L5", "nerve": "깊은종아리신경", "rest": "Silent at rest", "volition": "Reduced MU recruitment"}
        ],
        "interpretation": {
            "sensory": [
                "상지 감각신경 지연에 비해 다리의 장딴지신경(Sural SNAP)이 상대적으로 정상에 가깝게 잘 보존되는 장딴지신경 보존(Sural Sparing) 양상이 관찰되며, 이는 AIDP의 특징적 소견입니다."
            ],
            "motor": [
                "다수 운동신경에서 잠복기가 크게 연장되고 전도속도가 30 m/s 이하로 저하되어 다발성 말이집탈락성 마비를 시사합니다."
            ],
            "emg": [
                "발병 2주 이내의 급성기이므로 휴식 시 비정상 자발전위(섬유성연축 등)는 아직 나타나지 않으며, 신경 전도 차단으로 인한 자발적 근수축 동원 감소만 보입니다."
            ],
            "integration": [
                "▶ 추정 질환: 급성 염증성 말이집탈락성 다발신경뿌리병증 (AIDP, 기얭-바레증후군)",
                "▶ 추정한 이유: 선행 감염력, 상행성 대칭 마비, 심각한 운동 전도속도 저하 및 몸쪽(proximal) 신경뿌리 침범을 대변하는 F파 소실을 근거로 다발성 탈말이집성 병변을 확증합니다."
            ],
            "differential": [
                "▶ 축삭성 다발신경병증: 전도속도 저하보다는 진폭 감소가 먼저 명확히 나타나며 F파는 상대적으로 보존되는 경향이 있습니다."
            ]
        }
    },

    "오른쪽 팔꿈치굴증후군 의심": {
        "meta": {
            "age": 49, "sex": "남성", "side": "오른쪽",
            "chief": "최근 젓가락질을 하거나 단추를 채울 때 손가락 지지력이 떨어지며, 오른쪽 새끼손가락과 약지 자쪽의 저림이 심함. 팔꿈치를 오래 굽히면 악화됨."
        },
        "sensory_ncs": [
            {"nerve": "자신경 감각신경활동전위(Ulnar SNAP)", "recording": "새끼손가락", "stimulation": "손목", "side": "오른쪽", "amplitude": "6 μV", "latency": "3.5 ms", "velocity": "38 m/s"},
            {"nerve": "정중신경 감각신경활동전위(Median SNAP)", "recording": "검지", "stimulation": "손목", "side": "오른쪽", "amplitude": "25 μV", "latency": "2.9 ms", "velocity": "52 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "자신경 복합근육활동전위(Ulnar CMAP)", "recording": "새끼벌림근", "stimulation": "팔꿈치 아래", "side": "오른쪽", "amplitude": "6.8 mV", "latency": "6.4 ms", "velocity": "49 m/s"},
            {"nerve": "자신경 복합근육활동전위(Ulnar CMAP)", "recording": "새끼벌림근", "stimulation": "팔꿈치 위", "side": "오른쪽", "amplitude": "3.1 mV", "latency": "10.9 ms", "velocity": "28 m/s"}
        ],
        "needle_emg": [
            {"muscle": "첫째등쪽뼈사이근", "root": "C8-T1", "nerve": "자신경", "rest": "fibrillation potential, positive sharp wave", "volition": "Reduced MU recruitment"},
            {"muscle": "짧은엄지벌림근", "root": "C8-T1", "nerve": "정중신경", "rest": "Silent at rest", "volition": "Normal MU recruitment"}
        ],
        "interpretation": {
            "sensory": [
                "오른쪽 자신경 감각신경 진폭이 대폭 감소하였으나, 동일한 손의 정중신경 반응은 완벽히 정상으로 자신경에 국한된 문제임을 지시합니다."
            ],
            "motor": [
                "운동검사 시 팔꿈치 위 자극에서 팔꿈치 아래 자극에 비해 진폭이 절반 이하(6.8 -> 3.1)로 급감하고 속도가 느려져, 팔꿈치 관절 부위의 심각한 국소 전도차단을 강력히 증명합니다."
            ],
            "emg": [
                "자신경 지배 손가락 근육에서 뚜렷한 탈신경 자발전위가 보이며, 정중신경 지배 근육은 깨끗합니다."
            ],
            "integration": [
                "▶ 추정 질환: 오른쪽 팔꿈치굴증후군 (Cubital tunnel syndrome)",
                "▶ 추정한 이유: 팔꿈치 터널 구간에서의 명확한 운동 전도차단과 자신경 분포 내 국소 탈신경을 근거로 팔꿈치 주관 포착 마비로 확진합니다."
            ],
            "differential": [
                "▶ C8-T1 목 신경뿌리병증: 감각신경전도가 대개 정상 보존되고, 목 척추주위근 방전이 동반됩니다."
            ]
        }
    },

    "왼쪽 상부위팔신경얼기병증 의심": {
        "meta": {
            "age": 37, "sex": "여성", "side": "왼쪽",
            "chief": "오토바이 사고로 어깨가 꺾인 직후 심한 왼쪽 어깨 통증 발생. 이후 어깨 벌림과 팔꿉관절 굽힘이 전혀 안 되는 뚜렷한 근력 약화 호소."
        },
        "sensory_ncs": [
            {"nerve": "가쪽아래팔피부신경 감각신경활동전위(Lateral antebrachial cutaneous SNAP)", "recording": "아래팔 가쪽", "stimulation": "팔꿈치 근처", "side": "왼쪽", "amplitude": "4 μV", "latency": "3.3 ms", "velocity": "35 m/s"},
            {"nerve": "가쪽아래팔피부신경 감각신경활동전위(Lateral antebrachial cutaneous SNAP)", "recording": "아래팔 가쪽", "stimulation": "팔꿈치 근처", "side": "오른쪽", "amplitude": "18 μV", "latency": "2.4 ms", "velocity": "52 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "겨드랑신경 복합근육활동전위(Axillary CMAP)", "recording": "어깨세모근", "stimulation": "Erb's point", "side": "왼쪽", "amplitude": "1.8 mV", "latency": "5.1 ms", "velocity": "-"},
            {"nerve": "근육피부신경 복합근육활동전위(Musculocutaneous CMAP)", "recording": "위팔두갈래근", "stimulation": "Erb's point", "side": "왼쪽", "amplitude": "2.0 mV", "latency": "4.8 ms", "velocity": "-"}
        ],
        "needle_emg": [
            {"muscle": "어깨세모근", "root": "C5-C6", "nerve": "겨드랑신경", "rest": "fibrillation potential, positive sharp wave", "volition": "Reduced MU recruitment"},
            {"muscle": "목 척추주위근", "root": "C5-C6", "nerve": "뒤가지(posterior ramus)", "rest": "Silent at rest", "volition": "통증 및 협조 부족으로 검사 제한"}
        ],
        "interpretation": {
            "sensory": [
                "가쪽아래팔피부신경 감각 진폭이 정상(18 μV) 대비 4 μV로 비정상 저하되었습니다. 이는 병변이 척수 뒤뿌리신경절(DRG)보다 바깥쪽인 위팔신경얼기 수준에 있음을 증명합니다."
            ],
            "motor": [
                "겨드랑신경과 근육피부신경(C5-C6 지배)의 운동 반응이 대폭 소실되어 상부 줄기(Upper trunk) 손상이 확인됩니다."
            ],
            "emg": [
                "어깨 및 위팔 앞쪽 근육들에서 탈신경 전위가 도출되나 척수 신경뿌리 손상을 대변하는 목 척추주위근은 정상으로 유지되어 뿌리(Root) 병변을 배제합니다."
            ],
            "integration": [
                "▶ 추정 질환: 왼쪽 상부 위팔신경얼기병증 (Upper trunk brachial plexopathy)",
                "▶ 추정한 이유: 감각 전도의 뚜렷한 감소, C5-C6 분지를 아우르는 복합 근육 마비, 그러나 목 척추주위근은 완전히 정상인 패턴을 종합해 척수가 아닌 상부 신경얼기 파열/손상으로 확진합니다."
            ],
            "differential": [
                "▶ C5-C6 신경뿌리병증: 감각신경전도는 보존되고 목 척추주위근에 탈신경 이상이 명확하게 관찰되어야 합니다."
            ]
        }
    },

    "오른쪽 말초성 얼굴신경마비 의심": {
        "meta": {
            "age": 29, "sex": "여성", "side": "오른쪽",
            "chief": "아침에 일어난 후 오른쪽 눈이 감기지 않고 양치할 때 물이 샘. 이마 주름이 안 지어지는 우측 안면마비 발생(발병 10일째)."
        },
        "sensory_ncs": [],
        "motor_ncs": [
            {"nerve": "얼굴신경 복합근육활동전위(Facial CMAP)", "recording": "눈둘레근", "stimulation": "귓바퀴 앞", "side": "오른쪽", "amplitude": "0.7 mV", "latency": "4.9 ms", "velocity": "-"},
            {"nerve": "얼굴신경 복합근육활동전위(Facial CMAP)", "recording": "눈둘레근", "stimulation": "귓바퀴 앞", "side": "왼쪽", "amplitude": "3.8 mV", "latency": "3.2 ms", "velocity": "-"}
        ],
        "late_response": [
            {"test": "눈깜빡반사 오른쪽 자극-오른쪽 R1", "side": "오른쪽", "latency": "소실", "amplitude": "-"},
            {"test": "눈깜빡반사 오른쪽 자극-왼쪽 R2", "side": "왼쪽", "latency": "정상 범위", "amplitude": "보존"},
            {"test": "눈깜빡반사 왼쪽 자극-왼쪽 R1", "side": "왼쪽", "latency": "정상 범위", "amplitude": "보존"},
            {"test": "눈깜빡반사 왼쪽 자극-오른쪽 R2", "side": "오른쪽", "latency": "소실", "amplitude": "-"}
        ],
        "needle_emg": [],
        "interpretation": {
            "sensory": [
                "얼굴신경 마비는 일반 사지 감각신경전도가 아닌 눈깜빡반사(Blink Reflex)와 안면 운동신경검사(Facial CMAP)를 주로 활용해 평가합니다."
            ],
            "motor": [
                "오른쪽 얼굴신경 운동 반응 진폭이 왼쪽 대비 20% 미만으로 크게 감소하여 얼굴 운동 날신경 축삭의 심한 퇴행 손상을 나타냅니다."
            ],
            "emg": [
                "얼굴 근육 침근전도는 발병 2~3주 경과 후 예후 및 변성 정도를 정밀히 볼 때 수행하며, 초기 진단에서는 반사와 전도검사가 핵심입니다."
            ],
            "integration": [
                "▶ 추정 질환: 오른쪽 말초성 안면신경마비 (Bell's palsy)",
                "▶ 추정한 이유: 이마 주름 소실(말초성 징후), 안면 운동 진폭 급감 및 우측 얼굴 근육이 반응해야 하는 모든 눈깜빡반사(Rt R1, Lt 자극 Rt R2)의 차단을 결합해 뇌신경 7번의 말초 날신경 가지 손상으로 진단합니다."
            ],
            "differential": [
                "▶ 중추성 안면마비: 대뇌 지배 특성 상 이마 주름은 양측이 모두 보존되며 마비가 입 주위에만 국한되어 나타납니다."
            ]
        }
    },

    "뇌졸중 후 경직 H-반사 평가": {
        "meta": {
            "age": 63, "sex": "남성", "side": "왼쪽",
            "chief": "1년 전 오른쪽 뇌경색 후 좌측 편마비 상태임. 좌측 발목 장딴지 근육의 뻣뻣한 강직이 심해져 보행 시 첨족(toe walking)이 심각함."
        },
        "sensory_ncs": [],
        "motor_ncs": [],
        "late_response": [
            {"test": "H-반사(H-reflex)", "side": "왼쪽", "latency": "정상 범위", "amplitude": "증가"},
            {"test": "H-반사(H-reflex)", "side": "오른쪽", "latency": "정상 범위", "amplitude": "정상 범위"},
            {"test": "H/M 비율", "side": "왼쪽", "latency": "-", "amplitude": "0.62 (62%)"},
            {"test": "H/M 비율", "side": "오른쪽", "latency": "-", "amplitude": "0.28 (28%)"}
        ],
        "needle_emg": [],
        "interpretation": {
            "sensory": [
                "이 사례는 말초신경계 파괴 질환 판독이 아니므로 일반 말초 감각신경검사를 루틴으로 시행하지 않습니다."
            ],
            "motor": [
                "대뇌 상위운동신경원(UMN) 손상 환자에서 척수 반사회로의 경직(Spasticity)을 정량적으로 평가하기 위해 H-반사를 집중 활용합니다."
            ],
            "emg": [
                "척수 단일 시냅스 반사회로를 대변하는 H/M 비율이 편마비측(왼쪽)에서 0.62로 대조측(0.28)보다 월등히 높습니다.",
                "이는 뇌 피질에서 척수를 눌러주던 상위 억제 시스템이 상실되어 알파 운동신경원의 흥분성이 비정상적으로 치솟은 '과흥분 상태'를 명확히 입증합니다."
            ],
            "integration": [
                "▶ 추정 질환: 위운동신경세포 증후군에 의한 왼쪽 하지 경직 (Spasticity from UMN syndrome)",
                "▶ 추정한 이유: 비정상적인 발목간대경련 임상 소견과 비정상적 H-반사 항진, 극도로 높은 H/M 비율은 상위운동신경원 병변으로 인한 척수 억제 상실의 객관적 증거가 됩니다."
            ],
            "differential": [
                "▶ 말초 S1 신경뿌리병증: H-반사 진폭이 커지는 것이 아니라 지연되거나 아예 소실되는 양상으로 정반대의 결과를 냅니다."
            ]
        }
    }
}
