# data/virtual_reports.py

"""
가상 결과표 판독학습용 데이터베이스 및 영문 변환 모듈.
대한의사협회(KMA) 6.1판 의학용어 원칙을 엄격하게 준수합니다.
"""

ENG_MAP = {
    "검사 신경": "Nerve", "측": "Side", "기록 위치": "Recording Site", "자극 위치": "Stimulation Site",
    "진폭": "Amplitude", "잠복기": "Latency", "전도속도": "Conduction Velocity",
    "기록 근육": "Recording Muscle", "검사 항목": "Test Parameter", "검사 근육": "Muscle",
    "분절": "Segment", "말초신경": "Peripheral Nerve", "휴식 시 반응": "Resting Activity", "자발적 근수축 시 반응": "Voluntary MU Recruitment",
    "오른쪽": "Rt.", "왼쪽": "Lt.", "양측": "Both",
    
    "정중신경 감각신경활동전위(Median SNAP)": "Median SNAP", "자신경 감각신경활동전위(Ulnar SNAP)": "Ulnar SNAP",
    "노신경 표재감각신경활동전위(Superficial radial SNAP)": "Superficial Radial SNAP", "얕은종아리신경 감각신경활동전위(Superficial peroneal SNAP)": "Superficial Peroneal SNAP",
    "장딴지신경 감각신경활동전위(Sural SNAP)": "Sural SNAP", "가쪽아래팔피부신경 감각신경활동전위(Lateral antebrachial cutaneous SNAP)": "Lateral Antebrachial Cutaneous SNAP",
    "정중신경 복합근육활동전위(Median CMAP)": "Median CMAP", "자신경 복합근육활동전위(Ulnar CMAP)": "Ulnar CMAP",
    "노신경 복합근육활동전위(Radial CMAP)": "Radial CMAP", "종아리신경 복합근육활동전위(Peroneal CMAP)": "Peroneal CMAP",
    "정강신경 복합근육활동전위(Tibial CMAP)": "Tibial CMAP", "겨드랑신경 복합근육활동전위(Axillary CMAP)": "Axillary CMAP",
    "근육피부신경 복합근육활동전위(Musculocutaneous CMAP)": "Musculocutaneous CMAP", "얼굴신경 복합근육활동전위(Facial CMAP)": "Facial CMAP",
    
    "정강신경 F파(Tibial F-wave)": "Tibial F-wave", "H-반사(H-reflex)": "H-reflex", "H/M 비율": "H/M Ratio",
    "눈깜빡반사 오른쪽 자극-오른쪽 R1": "Blink Reflex Rt Stim - Rt R1", "눈깜빡반사 오른쪽 자극-오른쪽 R2": "Blink Reflex Rt Stim - Rt R2",
    "눈깜빡반사 오른쪽 자극-왼쪽 R2": "Blink Reflex Rt Stim - Lt R2", "눈깜빡반사 왼쪽 자극-왼쪽 R1": "Blink Reflex Lt Stim - Lt R1",
    "눈깜빡반사 왼쪽 자극-왼쪽 R2": "Blink Reflex Lt Stim - Lt R2", "눈깜빡반사 왼쪽 자극-오른쪽 R2": "Blink Reflex Lt Stim - Rt R2",
    
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
    
    "정중신경": "Median Nerve", "자신경": "Ulnar Nerve", "노신경": "Radial Nerve",
    "근육피부신경": "Musculocutaneous Nerve", "겨드랑신경": "Axillary Nerve",
    "뒤가지(posterior ramus)": "Posterior Ramus", "깊은종아리신경": "Deep Peroneal Nerve",
    "얕은종아리신경": "Superficial Peroneal Nerve", "정강신경": "Tibial Nerve",
    "위볼기신경": "Superior Gluteal Nerve", "넓적다리신경": "Femoral Nerve", "얼굴신경": "Facial Nerve", "삼차신경": "Trigeminal Nerve",
    
    "반응 소실": "No Response", "소실": "Absent", "지연": "Delayed", "감소": "Reduced",
    "정상 범위": "Normal Range", "보존": "Preserved", "통증 및 환자 협조 부족으로 검사 제한": "Limited by Pain/Cooperation",
    "Silent at rest": "Silent at rest", "Reduced MU recruitment": "Reduced MU recruitment", "Normal MU recruitment": "Normal MU recruitment"
}

def translate_value(value, to_english=False):
    if value is None: return ""
    text = str(value).strip()
    return ENG_MAP.get(text, text) if to_english else text

VIRTUAL_REPORTS = {
    "오른쪽 손목굴증후군 의심 결과표": {
        "meta": {
            "age": 52, "sex": "여성", "side": "오른쪽",
            "chief": "최근 3개월간 오른쪽 엄지부터 중지까지 타는 듯한 저림이 발생함. 수면 중 통증으로 자주 깨며, 손목을 굽히고 있으면 저림이 악화됨.",
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
            {"muscle": "목 척추주위근", "root": "C8-T1", "nerve": "뒤가지(posterior ramus)", "rest": "Silent at rest", "volition": "통증 및 환자 협조 부족으로 검사 제한"}
        ],
        "interpretation": {
            "sensory": [
                "오른쪽 정중신경 감각신경 진폭이 정상인 왼쪽(24 μV)에 비해 7 μV로 현저히 감소하였으며, 잠복기가 연장되었습니다. 이는 정중신경 감각 축삭의 손상을 의미합니다.",
                "동일한 손의 자신경 감각신경은 정상 보존되어 전신 다발신경병증이 아님을 확인합니다."
            ],
            "motor": [
                "오른쪽 정중신경 운동검사 시 손목 자극에서 원위잠복기가 5.8 ms로 뚜렷하게 지연되어 손목 구간의 국소 전도 지연(말이집 탈락)을 입증합니다."
            ],
            "emg": [
                "정중신경 지배 먼쪽 근육인 짧은엄지벌림근에서 휴식 시 비정상 자발전위가 검출되어 활동성 손상을 확인합니다.",
                "척수 신경뿌리 손상을 대변하는 척추주위근 및 자신경 지배 근육은 전기적으로 조용하여 정상입니다."
            ],
            "integration": [
                "추정 질환: 오른쪽 손목굴증후군 (Carpal tunnel syndrome)",
                "추정한 이유: 자신경과 목 척추주위근이 완벽히 정상인 상태에서, 정중신경에 국한된 운동/감각 전도 지연 및 진폭 감소가 도출되었습니다. 침근전도에서 짧은엄지벌림근의 단독 탈신경 소견이 일치하므로 손목굴 부위의 정중신경 포착으로 최종 확진합니다."
            ],
            "differential": [
                "C6 목 신경뿌리병증: 감각신경전도(SNAP)가 대개 보존되며, 목 척추주위근 침근전도에서 탈신경 자발전위가 나타나야 합니다."
            ]
        }
    },

    "왼쪽 C6 신경뿌리병증 의심 결과표": {
        "meta": {
            "age": 45, "sex": "남성", "side": "왼쪽",
            "chief": "뒷목부터 왼쪽 어깨를 거쳐 위팔 가쪽 및 엄지/검지로 뻗치는 방사통이 4주간 지속됨. 팔꿉관절을 굽힐 때 힘이 빠지는 느낌을 호소함."
        },
        "sensory_ncs": [
            {"nerve": "정중신경 감각신경활동전위(Median SNAP)", "recording": "검지", "stimulation": "손목", "side": "왼쪽", "amplitude": "26 μV", "latency": "2.9 ms", "velocity": "52 m/s"},
            {"nerve": "노신경 표재감각신경활동전위(Superficial radial SNAP)", "recording": "손등 노쪽", "stimulation": "아래팔", "side": "왼쪽", "amplitude": "21 μV", "latency": "2.5 ms", "velocity": "53 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "정중신경 복합근육활동전위(Median CMAP)", "recording": "짧은엄지벌림근", "stimulation": "손목", "side": "왼쪽", "amplitude": "8.6 mV", "latency": "3.5 ms", "velocity": "-"}
        ],
        "needle_emg": [
            {"muscle": "위팔두갈래근", "root": "C5-C6", "nerve": "근육피부신경", "rest": "fibrillation potential, positive sharp wave", "volition": "Reduced MU recruitment"},
            {"muscle": "노쪽손목폄근", "root": "C6-C7", "nerve": "노신경", "rest": "fibrillation potential, positive sharp wave", "volition": "Reduced MU recruitment"},
            {"muscle": "목 척추주위근", "root": "C6", "nerve": "뒤가지(posterior ramus)", "rest": "fibrillation potential, positive sharp wave", "volition": "통증 및 환자 협조 부족으로 검사 제한"}
        ],
        "interpretation": {
            "sensory": [
                "환자는 뚜렷한 손가락 방사통을 호소하지만, 정중신경과 노신경의 말초 감각신경 진폭 및 잠복기는 대칭적으로 완벽하게 보존되어 있습니다.",
                "이는 병변이 감각신경 세포체(DRG)보다 몸쪽(proximal)인 척수 신경뿌리에 위치함을 입증하는 강력한 생리학적 증거입니다."
            ],
            "emg": [
                "서로 다른 말초신경의 지배를 받으나 'C6 분절'이라는 공통 뿌리를 갖는 위팔두갈래근, 노쪽손목폄근에서 동시 탈신경 소견이 관찰됩니다.",
                "결정적으로 척수 신경뿌리 손상을 직접 대변하는 목 척추주위근(뒤가지)에서도 비정상적인 탈신경 전위가 확인되었습니다."
            ],
            "integration": [
                "추정 질환: 왼쪽 C6 목 신경뿌리병증 (C6 Cervical radiculopathy)",
                "추정한 이유: 말초 감각신경전도의 완전한 보존 소견과 함께, C6 척수 분절을 공유하는 다발 근육군 및 척추주위근에 탈신경 현상이 동시 관찰되므로 C6 척수 신경뿌리 압박 병변으로 확진합니다."
            ],
            "differential": [
                "왼쪽 상부 위팔신경얼기병증: 신경뿌리가 아닌 신경얼기(Plexus) 수준의 파열/손상이면 말초 감각신경 진폭의 감소가 반드시 동반되어야 하며, 목 척추주위근은 온전히 정상이어야 합니다."
            ]
        }
    },

    "오른쪽 온종아리신경병증 의심 결과표": {
        "meta": {
            "age": 41, "sex": "남성", "side": "오른쪽",
            "chief": "정강뼈 골절로 6주간 무릎 아래까지 단단한 석고붕대(Cast)를 유지함. 어제 석고붕대를 제거한 직후 우측 발처짐(Foot drop)과 발등 외측의 감각 둔화를 발견함."
        },
        "sensory_ncs": [
            {"nerve": "얕은종아리신경 감각신경활동전위(Superficial peroneal SNAP)", "recording": "발등", "stimulation": "종아리 가쪽", "side": "오른쪽", "amplitude": "4 μV", "latency": "3.6 ms", "velocity": "36 m/s"},
            {"nerve": "장딴지신경 감각신경활동전위(Sural SNAP)", "recording": "가쪽 발목", "stimulation": "종아리 뒤쪽", "side": "오른쪽", "amplitude": "16 μV", "latency": "3.0 ms", "velocity": "47 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "종아리신경 복합근육활동전위(Peroneal CMAP)", "recording": "짧은발가락폄근", "stimulation": "발목", "side": "오른쪽", "amplitude": "4.4 mV", "latency": "4.1 ms", "velocity": "-"},
            {"nerve": "종아리신경 복합근육활동전위(Peroneal CMAP)", "recording": "짧은발가락폄근", "stimulation": "종아리뼈머리 위", "side": "오른쪽", "amplitude": "1.5 mV", "latency": "12.8 ms", "velocity": "25 m/s"}
        ],
        "needle_emg": [
            {"muscle": "앞정강근", "root": "L4-L5", "nerve": "깊은종아리신경", "rest": "fibrillation potential, positive sharp wave", "volition": "Reduced MU recruitment"},
            {"muscle": "허리 척추주위근", "root": "L5", "nerve": "뒤가지(posterior ramus)", "rest": "Silent at rest", "volition": "통증 및 환자 협조 부족으로 검사 제한"}
        ],
        "interpretation": {
            "sensory": [
                "오른쪽 얕은종아리신경 감각 진폭이 크게 감소하여 먼쪽 말초 감각 축삭 손상을 증명합니다.",
                "인접한 장딴지신경 반응은 완벽히 정상이므로 다발신경병증이나 골반 내 좌골신경 병변 가능성은 배제됩니다."
            ],
            "motor": [
                "종아리신경 운동검사에서 종아리뼈머리 '위' 자극 시 진폭(1.5 mV)이 발목 자극(4.4 mV)보다 크게 급감하였습니다.",
                "이는 피부 얕은 곳을 지나는 종아리뼈머리 가쪽 구간에 가해진 압박(석고붕대)으로 인해 전기 신호가 차단되는 심각한 국소 전도차단(Conduction block) 소견입니다."
            ],
            "emg": [
                "종아리신경 지배 근육인 앞정강근에서 탈신경성 자발전위가 뚜렷하게 관찰됩니다.",
                "반면, 허리 척추주위근은 전기적으로 조용하여 요추 신경뿌리 병변을 완벽하게 감별해 줍니다."
            ],
            "integration": [
                "추정 질환: 오른쪽 온종아리신경병증 (Common peroneal neuropathy)",
                "추정한 이유: 석고붕대 압박 이력, 종아리뼈머리 구간의 명확한 운동 전도차단, 얕은종아리신경 감각 진폭 감소, 요추 척추주위근 정상 소견을 종합하여 외부 기계적 압박에 의한 단일 말초신경 마비로 확진합니다."
            ],
            "differential": [
                "L5 허리 신경뿌리병증: 얕은종아리신경 말초 감각전도가 정상으로 완벽히 보존되어야 하며, 침근전도에서 허리 척추주위근 이상이 반드시 동반되어야 합니다."
            ]
        }
    },

    "왼쪽 L5 신경뿌리병증 의심 결과표": {
        "meta": {
            "age": 58, "sex": "여성", "side": "왼쪽",
            "chief": "한 달 전 무거운 화분을 든 이후 허리에서 좌측 엉치, 종아리 가쪽을 타고 발등까지 뻗치는 방사통. 걸을 때 발끝이 끌리는 발처짐 증상 발생."
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
            {"muscle": "허리 척추주위근", "root": "L5", "nerve": "뒤가지(posterior ramus)", "rest": "fibrillation potential, positive sharp wave", "volition": "통증 및 환자 협조 부족으로 검사 제한"}
        ],
        "interpretation": {
            "sensory": [
                "발등 저림이 있으나 얕은종아리신경과 장딴지신경의 감각신경 전도가 완전히 보존됩니다.",
                "이는 병변이 뒤뿌리신경절(DRG) 상위인 척수 신경뿌리에 위치함을 강력히 지지하는 전형적인 소견입니다."
            ],
            "motor": [
                "종아리신경 운동검사에서 말초 부위 국소 속도 저하 소견이나 전도차단이 발견되지 않아 무릎 주변 포착 마비를 배제합니다."
            ],
            "emg": [
                "허리 척추주위근, 앞정강근, 중간볼기근에서 탈신경 자발전위가 대거 관찰됩니다.",
                "깊은종아리신경과 위볼기신경 등 서로 다른 신경 지배를 받으나 L5 분절을 공유하는 근육들의 동시 탈신경입니다."
            ],
            "integration": [
                "추정 질환: 왼쪽 L5 허리 신경뿌리병증 (L5 Lumbar radiculopathy)",
                "추정한 이유: 말초 감각신경 전도가 정상 보존되고, 침근전도에서 L5 지배 다발 근육 및 핵심적인 요추 척추주위근 침범이 확인되어 척수 신경뿌리 압박으로 확진합니다."
            ],
            "differential": [
                "온종아리신경병증: 얕은종아리신경 감각 진폭이 감소하고, 허리 척추주위근 및 위볼기신경 지배인 중간볼기근은 온전히 정상이어야 합니다."
            ]
        }
    },

    "오른쪽 노신경병증 의심 결과표": {
        "meta": {
            "age": 31, "sex": "남성", "side": "오른쪽",
            "chief": "어제 밤새 만취 상태로 의자 팔걸이에 오른쪽 팔을 걸치고 잠든 후(Saturday night palsy), 아침에 일어나니 오른쪽 손목과 손가락을 전혀 올리지 못함."
        },
        "sensory_ncs": [
            {"nerve": "노신경 표재감각신경활동전위 (Superficial Radial SNAP)", "recording": "손등 노쪽", "stimulation": "아래팔", "side": "오른쪽", "amplitude": "4 μV", "latency": "3.5 ms", "velocity": "42 m/s"},
            {"nerve": "정중신경 감각신경활동전위 (Median SNAP)", "recording": "검지", "stimulation": "손목", "side": "오른쪽", "amplitude": "24 μV", "latency": "2.8 ms", "velocity": "53 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "노신경 복합근육활동전위 (Radial CMAP)", "recording": "손목폄근", "stimulation": "아래팔", "side": "오른쪽", "amplitude": "4.5 mV", "latency": "2.8 ms", "velocity": "-"},
            {"nerve": "노신경 복합근육활동전위 (Radial CMAP)", "recording": "손목폄근", "stimulation": "위팔", "side": "오른쪽", "amplitude": "1.2 mV", "latency": "6.8 ms", "velocity": "38 m/s"}
        ],
        "needle_emg": [
            {"muscle": "노쪽손목폄근", "root": "C6-C7", "nerve": "노신경", "rest": "fibrillation potential, positive sharp wave", "volition": "Reduced MU recruitment"},
            {"muscle": "위팔두갈래근", "root": "C5-C6", "nerve": "근육피부신경", "rest": "Silent at rest", "volition": "Normal MU recruitment"}
        ],
        "interpretation": {
            "sensory": [
                "표재노신경 감각신경 진폭이 크게 감소하여 척수 신경절 먼쪽(distal)에 위치한 말초 노신경 축삭 손상임을 강력히 시사합니다."
            ],
            "motor": [
                "노신경 운동검사 시 아래팔 자극에 비해 '위팔' 자극에서 진폭이 대폭 급감하였습니다. 이는 의자 팔걸이에 눌렸던 나선고랑(Spiral groove) 부위의 심각한 국소 전도차단입니다."
            ],
            "emg": [
                "노쪽손목폄근에 활동성 탈신경 자발전위가 뚜렷하며 자발적 근수축 시 동원이 현저히 감소했습니다."
            ],
            "integration": [
                "추정 질환: 위팔뼈 나선고랑 부위 노신경병증 (Radial neuropathy at spiral groove)",
                "추정한 이유: 특유의 압박 이력(Saturday night palsy), 위팔 부위의 명확한 운동 전도차단, 표재노신경 감각 이상 및 해당 근육군의 단일 탈신경 소견이 압박성 노신경 파열을 확증합니다."
            ],
            "differential": [
                "뒤뼈사이신경병증 (PIN): 순수 운동 분지이므로 표재노신경 피부 감각 소실이 없습니다. 본 환자는 감각 전도 진폭 감소가 뚜렷합니다."
            ]
        }
    },
    # data/virtual_reports.py [Part 4/4]

    "왼쪽 팔꿈치굴증후군 의심 결과표": {
        "meta": {
            "age": 39, "sex": "여성", "side": "왼쪽",
            "chief": "직업이 요리사로, 손목에 힘쓰는 일을 장기간 해옴. 최근 4, 5번째 손가락 저림이 심해지고 새끼손가락 벌림 힘이 빠짐."
        },
        "sensory_ncs": [
            {"nerve": "자신경 감각신경활동전위(Ulnar SNAP)", "recording": "새끼손가락", "stimulation": "손목", "side": "왼쪽", "amplitude": "5 μV", "latency": "3.6 ms", "velocity": "37 m/s"},
            {"nerve": "정중신경 감각신경활동전위(Median SNAP)", "recording": "검지", "stimulation": "손목", "side": "왼쪽", "amplitude": "23 μV", "latency": "2.8 ms", "velocity": "51 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "자신경 복합근육활동전위(Ulnar CMAP)", "recording": "새끼벌림근", "stimulation": "손목", "side": "왼쪽", "amplitude": "7.1 mV", "latency": "2.6 ms", "velocity": "-"},
            {"nerve": "자신경 복합근육활동전위(Ulnar CMAP)", "recording": "새끼벌림근", "stimulation": "팔꿈치 위", "side": "왼쪽", "amplitude": "3.5 mV", "latency": "8.8 ms", "velocity": "34 m/s"}
        ],
        "needle_emg": [
            {"muscle": "새끼벌림근", "root": "C8-T1", "nerve": "자신경", "rest": "fibrillation potential, positive sharp wave", "volition": "Reduced MU recruitment"},
            {"muscle": "짧은엄지벌림근", "root": "C8-T1", "nerve": "정중신경", "rest": "Silent at rest", "volition": "Normal MU recruitment"}
        ],
        "interpretation": {
            "sensory": [
                "자신경 감각신경 진폭이 감소하고 잠복기가 지연되었습니다. 정중신경은 대조적으로 완전히 정상입니다."
            ],
            "motor": [
                "운동신경 전도검사에서 손목 자극에 비해 '팔꿈치 위' 자극 시 진폭이 절반으로 급감하는 명확한 국소 전도차단이 관찰됩니다."
            ],
            "emg": [
                "새끼벌림근에서 휴식 시 비정상 자발전위가 도출되어 자신경 지배 근육의 먼쪽 운동 축삭 변성을 지시합니다."
            ],
            "integration": [
                "추정 질환: 왼쪽 팔꿈치굴증후군 (Cubital tunnel syndrome)",
                "추정한 이유: 4, 5지 감각 이상 병력과 전기생리적으로 팔꿈치 구간에서의 자신경 운동 전도차단 및 해당 근육 침근전도 이상을 융합하여 팔꿈치 주관 포착으로 진단합니다."
            ],
            "differential": [
                "C8-T1 목 신경뿌리병증: 신경뿌리병증은 자신경뿐 아니라 정중신경 근육도 동시 침범되며, 말초 감각신경 전도(SNAP)는 정상으로 보존되어야 합니다."
            ]
        }
    },

    "축삭성 다발신경병증 의심 결과표": {
        "meta": {
            "age": 61, "sex": "여성", "side": "양측",
            "chief": "유방암으로 항암화학치료(Chemotherapy)를 마친 후, 양측 발끝과 손끝이 심하게 저리고 찌르는 듯한 통증이 발생함(항암제 유발 말초신경병증 의심)."
        },
        "sensory_ncs": [
            {"nerve": "장딴지신경 감각신경활동전위(Sural SNAP)", "recording": "가쪽 발목", "stimulation": "종아리 뒤쪽", "side": "양측", "amplitude": "반응 소실", "latency": "반응 소실", "velocity": "반응 소실"},
            {"nerve": "정중신경 감각신경활동전위(Median SNAP)", "recording": "검지", "stimulation": "손목", "side": "양측", "amplitude": "12 μV", "latency": "3.3 ms", "velocity": "46 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "정강신경 복합근육활동전위(Tibial CMAP)", "recording": "엄지벌림근", "stimulation": "발목", "side": "양측", "amplitude": "1.2 mV", "latency": "5.7 ms", "velocity": "-"},
            {"nerve": "정중신경 복합근육활동전위(Median CMAP)", "recording": "짧은엄지벌림근", "stimulation": "손목", "side": "양측", "amplitude": "5.1 mV", "latency": "3.8 ms", "velocity": "-"}
        ],
        "needle_emg": [
            {"muscle": "앞정강근", "root": "L4-L5", "nerve": "깊은종아리신경", "rest": "fibrillation potential, positive sharp wave", "volition": "Reduced MU recruitment"},
            {"muscle": "가쪽넓은근", "root": "L2-L4", "nerve": "넓적다리신경", "rest": "Silent at rest", "volition": "Normal MU recruitment"}
        ],
        "interpretation": {
            "sensory": [
                "다리 가장 먼쪽(distal)인 장딴지신경 감각반응은 완전히 소실되었으나, 상지 감각은 저하되긴 했으나 보존되어 있습니다.",
                "이는 항암 독성에 의해 길이가 가장 긴 발끝 신경 축삭부터 서서히 파괴되는 길이의존성(Length-dependent, dying-back) 패턴입니다."
            ],
            "motor": [
                "하지 운동신경의 CMAP 진폭 역시 대칭적으로 크게 낮아 만성 운동축삭 파괴 상태를 지지합니다."
            ],
            "emg": [
                "다리 먼쪽 근육(앞정강근)에서 탈신경 전위가 대칭적으로 확인되며, 몸쪽(proximal) 근육인 가쪽넓은근은 정상입니다."
            ],
            "integration": [
                "추정 질환: 항암제 유발성 축삭성 다발신경병증 (CIPN)",
                "추정한 이유: 항암치료 병력과 함께 대칭적 장갑-양말형(Glove-stocking) 감각 둔화, 전신 신경 중 긴 신경 말단에서 심한 진폭 감소 및 탈신경 소견이 관찰되어 독성/대사성 축삭 병변임을 확증합니다."
            ],
            "differential": [
                "말이집탈락성 다발신경병증: 진폭 감소보다는 신경 전 구간의 극심한 전도속도 저하 및 잠복기 연장이 먼저 관찰되어야 합니다."
            ]
        }
    },

    "급성 말이집탈락성 다발신경뿌리병증 의심 결과표": {
        "meta": {
            "age": 41, "sex": "여성", "side": "양측",
            "chief": "장염 후 2주 뒤부터 양측 다리의 힘이 빠지기 시작하여 현재는 걷기가 힘든 상행성(ascending) 대칭성 근력 저하 발생. 깊은힘줄반사 완벽 소실."
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
        "interpretation": {
            "sensory": [
                "상지 감각신경 지연에 비해 다리의 장딴지신경(Sural SNAP)이 상대적으로 정상에 가깝게 잘 보존되는 장딴지신경 보존(Sural Sparing) 양상이 관찰되며, 이는 AIDP의 특징적 소견입니다."
            ],
            "motor": [
                "다수 운동신경에서 잠복기가 크게 연장되고 전도속도가 30 m/s 이하로 심각하게 저하되어 다발성 말이집탈락성 마비를 시사합니다."
            ],
            "reflex": [
                "F파가 완전히 소실된 것은 질환이 말초뿐만 아니라 척수 신경뿌리(Root)라는 중추와 가장 가까운 몸쪽 부위까지 침범했음을 증명합니다."
            ],
            "integration": [
                "추정 질환: 급성 염증성 말이집탈락성 다발신경뿌리병증 (AIDP, 길랭-바레증후군)",
                "추정한 이유: 선행 감염력, 상행성 대칭 마비, 심각한 운동 전도속도 저하 및 몸쪽(proximal) 신경뿌리 침범을 대변하는 F파 소실을 근거로 다발성 탈말이집성 병변을 확증합니다."
            ],
            "differential": [
                "축삭성 다발신경병증: 전도속도 저하보다는 진폭 감소가 먼저 명확히 나타나며 F파는 상대적으로 보존되는 경향이 있습니다."
            ]
        }
    },

    "상부 위팔신경얼기병증 의심 결과표": {
        "meta": {
            "age": 28, "sex": "남성", "side": "왼쪽",
            "chief": "며칠 전 교통사고로 목이 심하게 앞뒤로 충격을 받은 이후, 왼쪽 어깨 벌림과 팔꿉관절 굽힘이 약해짐(Rucksack palsy 양상)."
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
            {"muscle": "목 척추주위근", "root": "C5-C6", "nerve": "뒤가지(posterior ramus)", "rest": "Silent at rest", "volition": "통증 및 환자 협조 부족으로 검사 제한"}
        ],
        "interpretation": {
            "sensory": [
                "가쪽아래팔피부신경 감각 진폭이 정상(18 μV) 대비 4 μV로 비정상 저하되었습니다. 이는 병변이 척수 뒤뿌리신경절(DRG)보다 바깥쪽인 위팔신경얼기 수준에 있음을 증명합니다."
            ],
            "motor": [
                "겨드랑신경과 근육피부신경(C5-C6 지배)의 운동 반응 진폭이 소실되어 상부 줄기(Upper trunk) 손상이 확인됩니다."
            ],
            "emg": [
                "어깨 및 위팔 앞쪽 근육들에서 탈신경 전위가 도출되나 척수 신경뿌리 손상을 대변하는 목 척추주위근은 정상으로 유지되어 뿌리(Root) 병변을 배제합니다."
            ],
            "integration": [
                "추정 질환: 왼쪽 상부 위팔신경얼기병증 (Upper trunk brachial plexopathy)",
                "추정한 이유: 배낭 압박 이력, 감각 전도의 뚜렷한 감소, C5-C6 분지를 아우르는 복합 근육 마비, 그러나 목 척추주위근은 완전히 정상인 패턴을 종합해 척수가 아닌 상부 신경얼기 파열/손상으로 확진합니다."
            ],
            "differential": [
                "C5-C6 신경뿌리병증: 신경뿌리 마비 시 말초 감각신경전도는 보존되고 목 척추주위근에 탈신경 이상이 명확하게 관찰되어야 합니다."
            ]
        }
    },

    "눈꺼풀 떨림과 눈 주위 불편감 의심 결과표": {
        "meta": {
            "age": 62, "sex": "여성", "side": "오른쪽",
            "chief": "우측 눈꺼풀에 간헐적인 미세 떨림이 2주 이상 지속됨. 세수할 때 우측 이마와 눈 가쪽을 만지면 내 살 같지 않은 둔한 느낌(감각 저하)을 호소함."
        },
        "late_response": [
            {"test": "눈깜빡반사 오른쪽 자극-오른쪽 R1", "side": "오른쪽", "latency": "지연", "amplitude": "감소"},
            {"test": "눈깜빡반사 오른쪽 자극-오른쪽 R2", "side": "오른쪽", "latency": "소실", "amplitude": "소실"},
            {"test": "눈깜빡반사 오른쪽 자극-왼쪽 R2", "side": "왼쪽", "latency": "소실", "amplitude": "소실"},
            {"test": "눈깜빡반사 왼쪽 자극-왼쪽 R1", "side": "왼쪽", "latency": "정상 범위", "amplitude": "정상 범위"},
            {"test": "눈깜빡반사 왼쪽 자극-왼쪽 R2", "side": "왼쪽", "latency": "정상 범위", "amplitude": "정상 범위"},
            {"test": "눈깜빡반사 왼쪽 자극-오른쪽 R2", "side": "오른쪽", "latency": "정상 범위", "amplitude": "정상 범위"}
        ],
        "interpretation": {
            "reflex": [
                "오른쪽 이마 부위를 자극할 때 연관된 3가지 반사 반응(우측 R1, 우측 R2, 좌측 R2)이 모두 지연되거나 반사 유발이 소실되었습니다.",
                "반면 정상측인 왼쪽을 자극할 때는 동측 반응(좌측 R1, 좌측 R2)뿐 아니라, 건너편인 오른쪽 눈을 감는 반응(우측 R2)도 완전히 정상으로 도출되었습니다.",
                "이는 반응을 만들어내는 얼굴신경(날신경)과 눈꺼풀 근육 자체는 완벽히 정상이지만, 우측 자극을 감지해 뇌줄기로 보내는 삼차신경(들신경) 경로가 손상되었음을 확증합니다."
            ],
            "integration": [
                "추정 질환: 우측 삼차신경 들신경 전도 장애 (Trigeminal afferent pathway dysfunction)",
                "추정한 이유: 얼굴 표정근의 정상적인 운동 기능, 우측 이마 감각 저하 병력, 그리고 눈깜빡반사에서 '우측 자극 시에만' 전체 반응이 차단되는 현상을 논리적으로 결합하여 감각 수용체(삼차신경 V1) 경로 마비로 판독합니다."
            ],
            "differential": [
                "오른쪽 말초성 안면마비(Bell's palsy): 얼굴마비(운동 날신경 병변)라면 어느 쪽을 자극하든 상관없이 우측 눈을 감는 근육 반응(우측 자극 R1/R2 및 좌측 자극 우측 R2)이 모두 소실되어야 하나, 본 환자는 왼쪽 자극 시 오른쪽 눈을 잘 감습니다."
            ]
        }
    },
    
    "오른쪽 말초성 얼굴신경마비 의심 결과표": {
        "meta": {
            "age": 29, "sex": "여성", "side": "오른쪽",
            "chief": "아침에 일어난 후 오른쪽 눈이 감기지 않고 양치할 때 물이 샌다고 호소함. 이마 주름이 안 지어지는 전형적인 우측 안면마비 발생."
        },
        "motor_ncs": [
            {"nerve": "얼굴신경 복합근육활동전위(Facial CMAP)", "recording": "눈둘레근", "stimulation": "귓바퀴 앞", "side": "오른쪽", "amplitude": "0.7 mV", "latency": "4.9 ms", "velocity": "-"},
            {"nerve": "얼굴신경 복합근육활동전위(Facial CMAP)", "recording": "눈둘레근", "stimulation": "귓바퀴 앞", "side": "왼쪽", "amplitude": "3.8 mV", "latency": "3.2 ms", "velocity": "-"}
        ],
        "late_response": [
            {"test": "눈깜빡반사 오른쪽 자극-오른쪽 R1", "side": "오른쪽", "latency": "소실", "amplitude": "소실"},
            {"test": "눈깜빡반사 오른쪽 자극-오른쪽 R2", "side": "오른쪽", "latency": "소실", "amplitude": "소실"},
            {"test": "눈깜빡반사 오른쪽 자극-왼쪽 R2", "side": "왼쪽", "latency": "정상 범위", "amplitude": "보존"},
            {"test": "눈깜빡반사 왼쪽 자극-왼쪽 R1", "side": "왼쪽", "latency": "정상 범위", "amplitude": "보존"},
            {"test": "눈깜빡반사 왼쪽 자극-왼쪽 R2", "side": "왼쪽", "latency": "정상 범위", "amplitude": "보존"},
            {"test": "눈깜빡반사 왼쪽 자극-오른쪽 R2", "side": "오른쪽", "latency": "소실", "amplitude": "소실"}
        ],
        "interpretation": {
            "motor": [
                "오른쪽 얼굴신경 운동 반응 진폭이 대조측 대비 크게 감소하여 얼굴 운동 날신경 축삭의 퇴행 손상을 나타냅니다."
            ],
            "reflex": [
                "어느 쪽(오른쪽 또는 왼쪽)을 자극하든 간에, 오른쪽 눈이 감겨야 하는 근육 반응(오른쪽 자극 Rt R1/R2 및 왼쪽 자극 Rt R2)이 모두 완벽히 소실되었습니다.",
                "이는 자극을 뇌로 전달하는 들신경(삼차신경)은 정상이지만, 최종적으로 우측 눈꺼풀을 수축시켜야 하는 안면신경(날신경)이 완전히 차단되었음을 증명합니다."
            ],
            "integration": [
                "추정 질환: 오른쪽 말초성 얼굴신경마비 (Bell's palsy)",
                "추정한 이유: 이마 주름 소실(말초성 징후)과 함께, 눈깜빡반사에서 우측 눈꺼풀을 닫는 모든 날신경 반응(Efferent response)의 소실을 결합해 뇌신경 7번의 마비로 확진합니다."
            ],
            "differential": [
                "우측 삼차신경 전도 장애: 삼차신경(들신경) 문제라면 왼쪽을 자극했을 때는 오른쪽 반응(Rt R2)이 정상적으로 나타나야 하지만, 본 사례는 소실되었습니다."
            ]
        }
    },

    "뇌졸중 후 경직 정량평가 결과표": {
        "meta": {
            "age": 68, "sex": "남성", "side": "왼쪽",
            "chief": "오른쪽 뇌경색 발병 후 좌측 편마비가 남음. 최근 좌
