# data/virtual_reports.py

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
    "위볼기신경": "Superior Gluteal Nerve", "넓적다리신경": "Femoral Nerve", "얼굴신경": "Facial Nerve", "삼차신경": "Trigeminal Nerve",
    
    # Results
    "반응 소실": "No Response", "소실": "Absent", "지연": "Delayed", "감소": "Reduced",
    "정상 범위": "Normal Range", "보존": "Preserved", "통증으로 인한 검사 불가": "Limited by Pain",
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
            {"muscle": "목 척추주위근", "root": "C8-T1", "nerve": "뒤가지(posterior ramus)", "rest": "Silent at rest", "volition": "통증으로 인한 검사 불가"}
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
                "정중신경 지배를 받는 먼쪽 근육인 짧은엄지벌림근에서 휴식 시 비정상 자발전위(섬유성연축 등)가 검출되어 활동성 손상을 확인합니다.",
                "경추 신경뿌리 손상을 대변하는 척추주위근 및 자신경 지배 근육은 전기적으로 조용(Silent at rest)하여 정상입니다."
            ],
            "integration": [
                "▶ 추정 질환: 오른쪽 손목굴증후군(Carpal tunnel syndrome)",
                "▶ 추정 근거: 자신경과 목 척추주위근이 완벽히 정상인 상태에서, 정중신경 지배 영역에 국한된 운동/감각 전도 지연 및 진폭 감소가 도출되었습니다. 침근전도에서 짧은엄지벌림근의 단독 탈신경 소견이 일치하므로 손목굴 부위의 정중신경 포착으로 최종 확진합니다."
            ],
            "differential": [
                "▶ C6 목 신경뿌리병증: 감각신경전도(SNAP)가 정상으로 보존되며, 목 척추주위근 침근전도에서 탈신경 자발전위가 나타나야 합니다."
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
            {"muscle": "목 척추주위근", "root": "C6", "nerve": "뒤가지(posterior ramus)", "rest": "fibrillation potential, positive sharp wave", "volition": "통증으로 인한 검사 불가"}
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
                "▶ 추정 질환: 왼쪽 C6 목 신경뿌리병증(Cervical radiculopathy)",
                "▶ 추정 근거: 감각신경전도의 완전한 보존 소견과 함께, 서로 다른 말초신경의 지배를 받으나 C6 척수 분절을 공유하는 다발 근육군 및 목 척추주위근에 탈신경 현상이 동시 관찰되므로 C6 척수 신경뿌리 병변으로 확진합니다."
            ],
            "differential": [
                "▶ 왼쪽 상부 위팔신경얼기병증(Upper trunk plexopathy): 신경뿌리가 아닌 얼기 수준의 손상이면 말초 감각신경 진폭 감소가 동반되어야 하며, 척추주위근은 정상이어야 합니다."
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
            {"nerve": "얕은종아리신경 감각신경활동전위(Superficial peroneal SNAP)", "recording": "발등", "stimulation": "종아리 가쪽", "side": "왼쪽", "amplitude": "14 μV", "latency": "2.8 ms", "velocity": "48 m/s"},
            {"nerve": "장딴지신경 감각신경활동전위(Sural SNAP)", "recording": "가쪽 발목", "stimulation": "종아리 뒤쪽", "side": "오른쪽", "amplitude": "16 μV", "latency": "3.0 ms", "velocity": "47 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "종아리신경 복합근육활동전위(Peroneal CMAP)", "recording": "짧은발가락폄근", "stimulation": "종아리뼈머리 아래", "side": "오른쪽", "amplitude": "4.4 mV", "latency": "9.1 ms", "velocity": "45 m/s"},
            {"nerve": "종아리신경 복합근육활동전위(Peroneal CMAP)", "recording": "짧은발가락폄근", "stimulation": "종아리뼈머리 위", "side": "오른쪽", "amplitude": "1.5 mV", "latency": "12.8 ms", "velocity": "25 m/s"}
        ],
        "needle_emg": [
            {"muscle": "앞정강근", "root": "L4-L5", "nerve": "깊은종아리신경", "rest": "fibrillation potential, positive sharp wave", "volition": "Reduced MU recruitment"},
            {"muscle": "허리 척추주위근", "root": "L5", "nerve": "뒤가지(posterior ramus)", "rest": "Silent at rest", "volition": "통증으로 인한 검사 불가"}
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
                "▶ 추정 질환: 오른쪽 온종아리신경병증(Common peroneal neuropathy)",
                "▶ 추정 근거: 종아리뼈머리 구간의 명확한 운동 전도차단, 얕은종아리신경 감각 진폭 감소, 요추 척추주위근 정상 소견을 통해 종아리뼈머리 부위의 외부 기계적 압박에 의한 단일 신경 마비임을 확증합니다."
            ],
            "differential": [
                "▶ L5 허리 신경뿌리병증: 얕은종아리신경 감각전도가 정상으로 완벽히 보존되어야 하며, 침근전도에서 허리 척추주위근과 중간볼기근 이상이 동반되어야 합니다."
            ]
        }
    }
}
