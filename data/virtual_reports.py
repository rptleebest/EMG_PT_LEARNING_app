# data/virtual_reports.py

"""
가상 결과표 판독학습용 데이터베이스 및 영문 변환 모듈.
"""

ENG_MAP = {
    # Headers
    "검사 신경": "Nerve", "측": "Side", "기록 위치": "Recording Site", "자극 위치": "Stimulation Site",
    "진폭": "Amplitude", "잠복기": "Latency", "전도속도": "Conduction Velocity",
    "기록 근육": "Recording Muscle", "검사 항목": "Test Parameter", "검사 근육": "Muscle",
    "분절": "Segment", "말초신경": "Peripheral Nerve", "휴식 시 반응": "Resting Activity", "수의수축 시 반응": "Voluntary MU Recruitment",
    # Side
    "오른쪽": "Rt.", "왼쪽": "Lt.", "양측": "Both",
    # Sensory / Motor Nerves
    "정중신경 감각신경활동전위(Median SNAP)": "Median SNAP",
    "자신경 감각신경활동전위(Ulnar SNAP)": "Ulnar SNAP",
    "노신경 표재감각신경활동전위(Superficial radial SNAP)": "Superficial Radial SNAP",
    "얕은종아리신경 감각신경활동전위(Superficial peroneal SNAP)": "Superficial Peroneal SNAP",
    "장딴지신경 감각신경활동전위(Sural SNAP)": "Sural SNAP",
    "가쪽아래팔피부신경 감각신경활동전위(Lateral antebrachial cutaneous SNAP)": "Lateral Antebrachial Cutaneous SNAP",
    "정중신경 복합근육활동전위(Median CMAP)": "Median CMAP",
    "자신경 복합근육활동전위(Ulnar CMAP)": "Ulnar CMAP",
    "노신경 복합근육활동전위(Radial CMAP)": "Radial CMAP",
    "종아리신경 복합근육활동전위(Peroneal CMAP)": "Peroneal CMAP",
    "정강신경 복합근육활동전위(Tibial CMAP)": "Tibial CMAP",
    "겨드랑신경 복합근육활동전위(Axillary CMAP)": "Axillary CMAP",
    "근육피부신경 복합근육활동전위(Musculocutaneous CMAP)": "Musculocutaneous CMAP",
    "얼굴신경 복합근육활동전위(Facial CMAP)": "Facial CMAP",
    # Late Responses
    "정강신경 F파(Tibial F-wave)": "Tibial F-wave",
    "H-반사(H-reflex)": "H-reflex",
    "H/M 비율": "H/M Ratio",
    "눈깜빡반사 오른쪽 자극-오른쪽 R1": "Blink Reflex Rt Stim - Rt R1",
    "눈깜빡반사 오른쪽 자극-오른쪽 R2": "Blink Reflex Rt Stim - Rt R2",
    "눈깜빡반사 오른쪽 자극-왼쪽 R2": "Blink Reflex Rt Stim - Lt R2",
    "눈깜빡반사 왼쪽 자극-왼쪽 R1": "Blink Reflex Lt Stim - Lt R1",
    "눈깜빡반사 왼쪽 자극-왼쪽 R2": "Blink Reflex Lt Stim - Lt R2",
    "눈깜빡반사 왼쪽 자극-오른쪽 R2": "Blink Reflex Lt Stim - Rt R2",
    # Sites & Muscles
    "검지": "Index Finger", "새끼손가락": "Little Finger", "손등 노쪽": "Dorsoradial Hand",
    "발등": "Dorsum of Foot", "가쪽 발목": "Lateral Malleolus", "아래팔 가쪽": "Lateral Forearm",
    "손목": "Wrist", "팔꿈치": "Elbow", "아래팔": "Forearm", "종아리 가쪽": "Lateral Calf",
    "종아리 뒤쪽": "Posterior Calf", "발목": "Ankle", "오금": "Popliteal Fossa",
    "종아리뼈머리": "Fibular Head", "종아리뼈머리 아래": "Below Fibular Head", "종아리뼈머리 위": "Above Fibular Head",
    "팔꿈치 아래": "Below Elbow", "팔꿈치 위": "Above Elbow", "팔꿈치 근처": "Near Elbow",
    "Erb's point": "Erb's Point", "귓바퀴 앞": "Preauricular",
    "짧은엄지벌림근(APB)": "Abductor Pollicis Brevis (APB)", "첫째등쪽뼈사이근(FDI)": "First Dorsal Interosseous (FDI)",
    "목 척추주위근(Cervical paraspinal)": "Cervical Paraspinals", "위팔두갈래근(Biceps brachii)": "Biceps Brachii",
    "노쪽손목폄근(Extensor carpi radialis)": "Extensor Carpi Radialis", "어깨세모근(Deltoid)": "Deltoid",
    "앞정강근(Tibialis anterior)": "Tibialis Anterior", "긴종아리근(Peroneus longus)": "Peroneus Longus",
    "가자미근(Soleus)": "Soleus", "허리 척추주위근(Lumbar paraspinal)": "Lumbar Paraspinals",
    "긴엄지폄근(Extensor hallucis longus)": "Extensor Hallucis Longus", "중간볼기근(Gluteus medius)": "Gluteus Medius",
    "짧은발가락벌림근(Abductor digiti minimi pedis)": "Abductor Digiti Minimi (pedis)",
    "가쪽넓은근(Vastus lateralis)": "Vastus Lateralis", "짧은발가락폄근(EDB)": "Extensor Digitorum Brevis (EDB)",
    "엄지벌림근(AH)": "Abductor Hallucis (AH)", "새끼벌림근(ADM)": "Abductor Digiti Minimi (ADM)",
    "가시아래근(Infraspinatus)": "Infraspinatus", "눈둘레근(Orbicularis oculi)": "Orbicularis Oculi",
    "입둘레근(Orbicularis oris)": "Orbicularis Oris", "깨물근(Masseter)": "Masseter",
    # Nerves in EMG
    "정중신경": "Median Nerve", "자신경": "Ulnar Nerve", "노신경": "Radial Nerve",
    "근육피부신경": "Musculocutaneous Nerve", "겨드랑신경": "Axillary Nerve",
    "뒤가지(posterior ramus)": "Posterior Ramus", "깊은종아리신경": "Deep Peroneal Nerve",
    "얕은종아리신경": "Superficial Peroneal Nerve", "정강신경": "Tibial Nerve",
    "위볼기신경": "Superior Gluteal Nerve", "발바닥신경": "Plantar Nerve",
    "넓적다리신경": "Femoral Nerve", "어깨위신경": "Suprascapular Nerve",
    "얼굴신경": "Facial Nerve", "삼차신경": "Trigeminal Nerve",
    # Results
    "반응 소실": "No Response", "소실": "Absent", "지연": "Delayed", "감소": "Reduced",
    "정상 범위": "Normal Range", "보존": "Preserved", "평가 제한": "Limited Evaluation",
    "Silent at rest": "Silent at rest",
    "Reduced MU recruitment": "Reduced MU recruitment",
    "Normal MU recruitment": "Normal MU recruitment",
    "Giant MUAPs with reduced recruitment": "Giant MUAPs with reduced recruitment",
    "Markedly reduced MU recruitment": "Markedly reduced MU recruitment"
}

def translate_value(value, to_english=False):
    if value is None:
        return ""
    text = str(value).strip()
    if not to_english:
        return text
    return ENG_MAP.get(text, text)


VIRTUAL_REPORTS = {
    "오른쪽 손목굴증후군 의심": {
        "meta": {
            "age": 52, "sex": "여성", "side": "오른쪽",
            "chief": "오른쪽 엄지, 검지, 중지 저림과 야간 통증. 손목 굽힘 시 증상 악화.",
            "clinical_hint": "정중신경 분포 감각 이상과 엄지두덩 약화가 의심되는 사례입니다."
        },
        "diagnosis": "오른쪽 손목굴증후군(Carpal tunnel syndrome), 정중신경 손목 부위 포착성 신경병증",
        "lesion": "오른쪽 손목굴 부위의 정중신경 먼쪽(distal) 감각 및 운동섬유",
        "sensory_ncs": [
            {"nerve": "정중신경 감각신경활동전위(Median SNAP)", "recording": "검지", "stimulation": "손목", "side": "오른쪽", "amplitude": "7 μV", "latency": "4.6 ms", "velocity": "32 m/s"},
            {"nerve": "정중신경 감각신경활동전위(Median SNAP)", "recording": "검지", "stimulation": "손목", "side": "왼쪽", "amplitude": "24 μV", "latency": "2.8 ms", "velocity": "51 m/s"},
            {"nerve": "자신경 감각신경활동전위(Ulnar SNAP)", "recording": "새끼손가락", "stimulation": "손목", "side": "오른쪽", "amplitude": "23 μV", "latency": "2.6 ms", "velocity": "54 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "정중신경 복합근육활동전위(Median CMAP)", "recording": "짧은엄지벌림근(APB)", "stimulation": "손목", "side": "오른쪽", "amplitude": "3.0 mV", "latency": "5.8 ms", "velocity": "-"},
            {"nerve": "정중신경 복합근육활동전위(Median CMAP)", "recording": "짧은엄지벌림근(APB)", "stimulation": "팔꿈치", "side": "오른쪽", "amplitude": "2.8 mV", "latency": "10.2 ms", "velocity": "48 m/s"},
            {"nerve": "정중신경 복합근육활동전위(Median CMAP)", "recording": "짧은엄지벌림근(APB)", "stimulation": "손목", "side": "왼쪽", "amplitude": "8.4 mV", "latency": "3.4 ms", "velocity": "-"},
            {"nerve": "자신경 복합근육활동전위(Ulnar CMAP)", "recording": "새끼벌림근(ADM)", "stimulation": "손목", "side": "오른쪽", "amplitude": "8.8 mV", "latency": "2.7 ms", "velocity": "-"}
        ],
        "needle_emg": [
            {"muscle": "짧은엄지벌림근(APB)", "root": "C8-T1", "nerve": "정중신경", "rest": "fibrillation potential, positive sharp wave", "volition": "Reduced MU recruitment"},
            {"muscle": "첫째등쪽뼈사이근(FDI)", "root": "C8-T1", "nerve": "자신경", "rest": "Silent at rest", "volition": "Normal MU recruitment"},
            {"muscle": "목 척추주위근(Cervical paraspinal)", "root": "C8-T1", "nerve": "뒤가지(posterior ramus)", "rest": "Silent at rest", "volition": "평가 제한"}
        ],
        "interpretation": {
            "sensory": [
                "오른쪽 정중신경 감각신경활동전위는 정상측인 왼쪽에 비해 진폭이 크게 낮고 잠복기가 길며 전도속도가 느립니다.",
                "반면 오른쪽 자신경 감각신경활동전위는 비교적 보존되어 있어, 다발성 신경병증이 아닌 정중신경 국소 병변을 의심합니다."
            ],
            "motor": [
                "오른쪽 정중신경 운동반응은 손목 자극에서 원위잠복기가 뚜렷하게 지연되어 있습니다.",
                "오른쪽 정중신경 복합근육활동전위(CMAP) 진폭도 정상측보다 낮아 탈말이집성 지연뿐 아니라 운동축삭 손상 가능성이 동반됩니다."
            ],
            "emg": [
                "짧은엄지벌림근에서 휴식 시 자발활동전위가 관찰되어 정중신경 지배 근육의 활동성 탈신경을 시사합니다.",
                "첫째등쪽뼈사이근과 목 척추주위근은 보존되어 있어 신경뿌리병증 가능성은 낮아집니다."
            ],
            "integration": [
                "증상 분포, 정중신경 전도 지연, 짧은엄지벌림근의 탈신경 소견을 종합하면 오른쪽 손목굴증후군이 가장 타당합니다."
            ],
            "differential": [
                "C6 또는 C8 신경뿌리병증: 감각신경전도가 주로 정상으로 유지되고 척추주위근 이상이 동반됩니다."
            ],
            "additional": [
                "야간 보조기 적용, 손목 과굴곡 피하기, 정중신경 활주운동을 물리치료 중재로 적용합니다."
            ]
        }
    },

    "왼쪽 C6 신경뿌리병증 의심": {
        "meta": {
            "age": 45, "sex": "남성", "side": "왼쪽",
            "chief": "왼쪽 목 통증, 어깨와 위팔 가쪽 통증, 엄지와 검지 저림. 팔꿉관절 굽힘 약화.",
            "clinical_hint": "감각신경전도는 보존되지만 C6 분절 근육 침근전도 이상이 관찰되는 사례입니다."
        },
        "diagnosis": "왼쪽 C6 목 신경뿌리병증(C6 cervical radiculopathy)",
        "lesion": "왼쪽 C6 신경뿌리, 뒤뿌리신경절보다 몸쪽 병변",
        "sensory_ncs": [
            {"nerve": "정중신경 감각신경활동전위(Median SNAP)", "recording": "검지", "stimulation": "손목", "side": "왼쪽", "amplitude": "26 μV", "latency": "2.9 ms", "velocity": "52 m/s"},
            {"nerve": "노신경 표재감각신경활동전위(Superficial radial SNAP)", "recording": "손등 노쪽", "stimulation": "아래팔", "side": "왼쪽", "amplitude": "21 μV", "latency": "2.5 ms", "velocity": "53 m/s"},
            {"nerve": "자신경 감각신경활동전위(Ulnar SNAP)", "recording": "새끼손가락", "stimulation": "손목", "side": "왼쪽", "amplitude": "24 μV", "latency": "2.6 ms", "velocity": "55 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "정중신경 복합근육활동전위(Median CMAP)", "recording": "짧은엄지벌림근(APB)", "stimulation": "손목", "side": "왼쪽", "amplitude": "8.6 mV", "latency": "3.5 ms", "velocity": "-"},
            {"nerve": "정중신경 복합근육활동전위(Median CMAP)", "recording": "짧은엄지벌림근(APB)", "stimulation": "팔꿈치", "side": "왼쪽", "amplitude": "8.1 mV", "latency": "7.7 ms", "velocity": "54 m/s"}
        ],
        "needle_emg": [
            {"muscle": "위팔두갈래근(Biceps brachii)", "root": "C5-C6", "nerve": "근육피부신경", "rest": "fibrillation potential, positive sharp wave", "volition": "Reduced MU recruitment"},
            {"muscle": "노쪽손목폄근(Extensor carpi radialis)", "root": "C6-C7", "nerve": "노신경", "rest": "fibrillation potential, positive sharp wave", "volition": "Giant MUAPs with reduced recruitment"},
            {"muscle": "목 척추주위근(Cervical paraspinal)", "root": "C6", "nerve": "뒤가지(posterior ramus)", "rest": "fibrillation potential, positive sharp wave", "volition": "평가 제한"}
        ],
        "interpretation": {
            "sensory": [
                "환자는 감각 둔화를 호소하지만 모든 감각신경활동전위(SNAP)가 대칭적으로 정상 보존됩니다.",
                "이는 병변이 감각신경 세포체(DRG)보다 몸쪽인 신경뿌리 수준에 있음을 강력히 시사합니다."
            ],
            "motor": [
                "운동신경전도검사에서 말초신경의 전도차단이나 원위잠복기 지연이 관찰되지 않습니다."
            ],
            "emg": [
                "서로 다른 말초신경 지배를 받으나 C6 분절을 공유하는 위팔두갈래근, 노쪽손목폄근, 그리고 목 척추주위근에서 다발성 탈신경 소견이 나타납니다."
            ],
            "integration": [
                "감각전도 보존 및 C6 지배 근육/척추주위근의 동시성 탈신경 소견을 근거로 왼쪽 C6 목 신경뿌리병증으로 확진합니다."
            ],
            "differential": [
                "상완신경총(위팔신경얼기)병증: 감각신경 진폭 감소가 동반되며 목 척추주위근은 대개 보존됩니다."
            ],
            "additional": [
                "목 MRI를 통해 추간판 탈출 여부를 확인하고 목 견인치료(Traction) 등을 적용합니다."
            ]
        }
    },

    "오른쪽 온종아리신경병증 의심": {
        "meta": {
            "age": 32, "sex": "남성", "side": "오른쪽",
            "chief": "다리를 오래 꼬고 앉은 뒤 오른쪽 발처짐 발생. 발등 감각 저하."
        },
        "diagnosis": "오른쪽 온종아리신경병증(Common peroneal neuropathy)",
        "lesion": "오른쪽 종아리뼈머리(Fibular head) 주변 온종아리신경",
        "sensory_ncs": [
            {"nerve": "얕은종아리신경 감각신경활동전위(Superficial peroneal SNAP)", "recording": "발등", "stimulation": "종아리 가쪽", "side": "오른쪽", "amplitude": "4 μV", "latency": "3.6 ms", "velocity": "36 m/s"},
            {"nerve": "얕은종아리신경 감각신경활동전위(Superficial peroneal SNAP)", "recording": "발등", "stimulation": "종아리 가쪽", "side": "왼쪽", "amplitude": "14 μV", "latency": "2.8 ms", "velocity": "48 m/s"},
            {"nerve": "장딴지신경 감각신경활동전위(Sural SNAP)", "recording": "가쪽 발목", "stimulation": "종아리 뒤쪽", "side": "오른쪽", "amplitude": "16 μV", "latency": "3.0 ms", "velocity": "47 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "종아리신경 복합근육활동전위(Peroneal CMAP)", "recording": "짧은발가락폄근(EDB)", "stimulation": "종아리뼈머리 아래", "side": "오른쪽", "amplitude": "4.4 mV", "latency": "9.1 ms", "velocity": "45 m/s"},
            {"nerve": "종아리신경 복합근육활동전위(Peroneal CMAP)", "recording": "짧은발가락폄근(EDB)", "stimulation": "종아리뼈머리 위", "side": "오른쪽", "amplitude": "1.5 mV", "latency": "12.8 ms", "velocity": "25 m/s"},
            {"nerve": "정강신경 복합근육활동전위(Tibial CMAP)", "recording": "엄지벌림근(AH)", "stimulation": "발목", "side": "오른쪽", "amplitude": "8.1 mV", "latency": "4.1 ms", "velocity": "-"}
        ],
        "needle_emg": [
            {"muscle": "앞정강근(Tibialis anterior)", "root": "L4-L5", "nerve": "깊은종아리신경", "rest": "fibrillation potential, positive sharp wave", "volition": "Reduced MU recruitment"},
            {"muscle": "긴종아리근(Peroneus longus)", "root": "L5-S1", "nerve": "얕은종아리신경", "rest": "fibrillation potential, positive sharp wave", "volition": "Reduced MU recruitment"},
            {"muscle": "허리 척추주위근(Lumbar paraspinal)", "root": "L5", "nerve": "뒤가지(posterior ramus)", "rest": "Silent at rest", "volition": "평가 제한"}
        ],
        "interpretation": {
            "sensory": [
                "얕은종아리신경 감각반응 진폭이 정상측 대비 크게 감소하여 말초 감각신경 손상을 확인합니다.",
                "장딴지신경 반응은 정상이므로 좌골신경이나 다발신경병증의 가능성은 낮습니다."
            ],
            "motor": [
                "종아리신경 운동검사에서 '종아리뼈머리 위' 자극 시 '아래' 자극보다 진폭이 50% 이상 급감하는 국소 전도차단(Conduction block)을 확인했습니다."
            ],
            "emg": [
                "종아리신경이 지배하는 앞정강근 등에서 탈신경 소견이 확인되나, 요추 척추주위근은 정상입니다."
            ],
            "integration": [
                "종아리뼈머리 부위의 뚜렷한 전도차단 및 관련 근육군 탈신경을 종합하여 '오른쪽 온종아리신경 마비'로 진단합니다."
            ],
            "differential": [
                "L5 허리 신경뿌리병증: 얕은종아리신경 감각전도가 정상이고, 침근전도에서 허리 척추주위근 이상이 관찰되어야 합니다."
            ],
            "additional": [
                "다리 꼬기 습관 교정 및 발목 등굽힘 보조기(AFO) 착용을 고려합니다."
            ]
        }
    },
        "왼쪽 L5 신경뿌리병증 의심": {
        "meta": {
            "age": 58, "sex": "여성", "side": "왼쪽",
            "chief": "왼쪽 허리 통증과 발등 저림. 엄지발가락 폄과 발목 등굽힘 약화."
        },
        "diagnosis": "왼쪽 L5 허리 신경뿌리병증(L5 lumbar radiculopathy)",
        "lesion": "왼쪽 L5 신경뿌리, 뒤뿌리신경절보다 몸쪽 병변",
        "sensory_ncs": [
            {"nerve": "얕은종아리신경 감각신경활동전위(Superficial peroneal SNAP)", "recording": "발등", "stimulation": "종아리 가쪽", "side": "왼쪽", "amplitude": "13 μV", "latency": "2.9 ms", "velocity": "47 m/s"},
            {"nerve": "장딴지신경 감각신경활동전위(Sural SNAP)", "recording": "가쪽 발목", "stimulation": "종아리 뒤쪽", "side": "왼쪽", "amplitude": "15 μV", "latency": "3.1 ms", "velocity": "46 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "종아리신경 복합근육활동전위(Peroneal CMAP)", "recording": "짧은발가락폄근(EDB)", "stimulation": "발목", "side": "왼쪽", "amplitude": "3.9 mV", "latency": "4.5 ms", "velocity": "-"},
            {"nerve": "정강신경 복합근육활동전위(Tibial CMAP)", "recording": "엄지벌림근(AH)", "stimulation": "발목", "side": "왼쪽", "amplitude": "7.4 mV", "latency": "4.2 ms", "velocity": "-"}
        ],
        "needle_emg": [
            {"muscle": "앞정강근(Tibialis anterior)", "root": "L4-L5", "nerve": "깊은종아리신경", "rest": "fibrillation potential, positive sharp wave", "volition": "Reduced MU recruitment"},
            {"muscle": "중간볼기근(Gluteus medius)", "root": "L5", "nerve": "위볼기신경", "rest": "fibrillation potential, positive sharp wave", "volition": "Reduced MU recruitment"},
            {"muscle": "허리 척추주위근(Lumbar paraspinal)", "root": "L5", "nerve": "뒤가지(posterior ramus)", "rest": "fibrillation potential, positive sharp wave", "volition": "평가 제한"}
        ],
        "interpretation": {
            "sensory": [
                "발등 저림이 있으나 다리 감각신경활동전위가 양측 정상 보존되어, 병변이 뒤뿌리신경절 상위(신경뿌리)임을 의미합니다."
            ],
            "motor": [
                "종아리신경 운동검사에서 말초 부위 전도차단이나 국소 속도 저하 소견이 발견되지 않습니다."
            ],
            "emg": [
                "L5 분절을 공유하는 앞정강근, 중간볼기근과 허리 척추주위근에서 뚜렷한 동시 탈신경 활동이 포착됩니다."
            ],
            "integration": [
                "감각 전도 보존 및 L5 다발 근육 및 척추주위근 침근전도 이상을 종합하여 '왼쪽 L5 허리 신경뿌리병증'으로 진단합니다."
            ],
            "differential": [
                "온종아리신경병증: 감각신경 진폭이 감소하고, 허리 척추주위근 및 중간볼기근은 정상이어야 합니다."
            ],
            "additional": [
                "요추 MRI로 L4-L5 추간판 탈출 여부를 살피고 코어 안정화 및 윌리엄/맥켄지 운동을 선별 적용합니다."
            ]
        }
    },

    "축삭성 다발신경병증 의심": {
        "meta": {
            "age": 68, "sex": "남성", "side": "양측",
            "chief": "양측 발끝부터 시작된 저림과 화끈거림. 밤에 악화."
        },
        "diagnosis": "길이의존성 축삭성 감각운동 다발신경병증(Length-dependent axonal sensorimotor polyneuropathy)",
        "lesion": "양측 다리 먼쪽(distal) 말초신경 축삭",
        "sensory_ncs": [
            {"nerve": "장딴지신경 감각신경활동전위(Sural SNAP)", "recording": "가쪽 발목", "stimulation": "종아리 뒤쪽", "side": "오른쪽", "amplitude": "반응 소실", "latency": "반응 소실", "velocity": "반응 소실"},
            {"nerve": "장딴지신경 감각신경활동전위(Sural SNAP)", "recording": "가쪽 발목", "stimulation": "종아리 뒤쪽", "side": "왼쪽", "amplitude": "반응 소실", "latency": "반응 소실", "velocity": "반응 소실"},
            {"nerve": "정중신경 감각신경활동전위(Median SNAP)", "recording": "검지", "stimulation": "손목", "side": "오른쪽", "amplitude": "18 μV", "latency": "3.2 ms", "velocity": "48 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "정강신경 복합근육활동전위(Tibial CMAP)", "recording": "엄지벌림근(AH)", "stimulation": "발목", "side": "오른쪽", "amplitude": "1.4 mV", "latency": "5.9 ms", "velocity": "-"},
            {"nerve": "정중신경 복합근육활동전위(Median CMAP)", "recording": "짧은엄지벌림근(APB)", "stimulation": "손목", "side": "오른쪽", "amplitude": "7.6 mV", "latency": "3.8 ms", "velocity": "-"}
        ],
        "needle_emg": [
            {"muscle": "앞정강근(Tibialis anterior)", "root": "L4-L5", "nerve": "깊은종아리신경", "rest": "fibrillation potential, positive sharp wave", "volition": "Reduced MU recruitment"},
            {"muscle": "가쪽넓은근(Vastus lateralis)", "root": "L2-L4", "nerve": "넓적다리신경", "rest": "Silent at rest", "volition": "Normal MU recruitment"}
        ],
        "interpretation": {
            "sensory": [
                "다리 말단인 장딴지신경 감각반응이 완전 소실되었으나, 팔 정중신경 반응은 보존되어 있어 '길이의존성(Dying-back)' 마비 패턴과 일치합니다."
            ],
            "motor": [
                "하지 운동신경(정강신경 등)의 복합근육활동전위 진폭이 대칭적으로 크게 낮아 다발성 만성 운동축삭 파괴 상태를 지지합니다."
            ],
            "emg": [
                "다리 말단 근육에서 탈신경 전위가 확인되며 근위부 허벅지 근육(가쪽넓은근)은 정상입니다."
            ],
            "integration": [
                "대칭적 장갑-양말형 감각 둔화, 말단 중심 진폭 감소를 통해 '길이의존성 축삭성 다발신경병증'으로 진단합니다."
            ],
            "differential": [
                "말이집탈락성 다발신경병증: 진폭 감소보다는 심각한 전도속도 저하 및 잠복기 연장이 먼저 관찰됩니다."
            ],
            "additional": [
                "당뇨(HbA1c), 음주력 등 대사적 원인을 파악하고 발 보건 교육(화상 방지 등)을 최우선 지도합니다."
            ]
        }
    },

    "급성 말이집탈락성 다발신경뿌리병증 의심": {
        "meta": {
            "age": 41, "sex": "여성", "side": "양측",
            "chief": "장염 후 2주 뒤부터 양측 다리 근력저하가 상행. 심부건반사 저하."
        },
        "diagnosis": "급성 염증성 말이집탈락성 다발신경뿌리병증(AIDP, Guillain-Barre syndrome spectrum)",
        "lesion": "다발 말초신경 및 몸쪽(proximal) 신경뿌리의 말이집탈락성 병변",
        "sensory_ncs": [
            {"nerve": "정중신경 감각신경활동전위(Median SNAP)", "recording": "검지", "stimulation": "손목", "side": "오른쪽", "amplitude": "18 μV", "latency": "3.8 ms", "velocity": "39 m/s"},
            {"nerve": "장딴지신경 감각신경활동전위(Sural SNAP)", "recording": "가쪽 발목", "stimulation": "종아리 뒤쪽", "side": "오른쪽", "amplitude": "14 μV", "latency": "3.2 ms", "velocity": "45 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "종아리신경 복합근육활동전위(Peroneal CMAP)", "recording": "짧은발가락폄근(EDB)", "stimulation": "종아리뼈머리", "side": "오른쪽", "amplitude": "2.4 mV", "latency": "18.9 ms", "velocity": "28 m/s"},
            {"nerve": "정강신경 복합근육활동전위(Tibial CMAP)", "recording": "엄지벌림근(AH)", "stimulation": "발목", "side": "오른쪽", "amplitude": "3.5 mV", "latency": "7.2 ms", "velocity": "-"}
        ],
        "late_response": [
            {"test": "정강신경 F파(Tibial F-wave)", "side": "오른쪽", "latency": "소실", "amplitude": "-"}
        ],
        "needle_emg": [
            {"muscle": "앞정강근(Tibialis anterior)", "root": "L4-L5", "nerve": "깊은종아리신경", "rest": "Silent at rest", "volition": "Reduced MU recruitment"}
        ],
        "interpretation": {
            "sensory": [
                "팔 감각신경 지연에 비해 다리의 장딴지신경(Sural SNAP)이 상대적으로 잘 보존되는(Sural Sparing) 양상이 관찰되며, 이는 AIDP의 특징적 소견입니다."
            ],
            "motor": [
                "다수 운동신경에서 잠복기가 크게 연장되고 전도속도가 30 m/s 이하로 저하되어 말이집탈락성 마비를 시사합니다."
            ],
            "emg": [
                "발병 2주 이내의 초기이므로 휴식 시 자발전위는 나타나지 않으며, 전도 차단으로 인한 수의 수축 동원 감소만 보입니다."
            ],
            "integration": [
                "선행 감염력, 상행성 마비, 심각한 운동 전도속도 저하 및 근위부 신경뿌리를 대변하는 F파 소실을 근거로 '급성 염증성 말이집탈락성 다발신경뿌리병증(기얭-바레)'으로 진단합니다."
            ],
            "differential": [
                "축삭성 다발신경병증: 전도속도 저하보다는 진폭 감소가 먼저 명확히 나타나며 F파는 상대적으로 보존됩니다."
            ],
            "additional": [
                "급성 호흡근 마비 대비 폐활량(VC) 모니터링이 필수이며, 피로를 피하는 수동 관절가동운동을 실시합니다."
            ]
        }
    },

    "오른쪽 팔꿈치굴증후군 의심": {
        "meta": {
            "age": 49, "sex": "남성", "side": "오른쪽",
            "chief": "오른쪽 새끼손가락과 약지 자쪽 저림. 팔꿈치를 오래 굽히면 증상 악화."
        },
        "diagnosis": "오른쪽 팔꿈치굴증후군, 팔꿈치 부위 자신경병증(Ulnar neuropathy at the elbow)",
        "lesion": "오른쪽 팔꿈치굴(Cubital tunnel) 또는 팔꿈치 주변 자신경",
        "sensory_ncs": [
            {"nerve": "자신경 감각신경활동전위(Ulnar SNAP)", "recording": "새끼손가락", "stimulation": "손목", "side": "오른쪽", "amplitude": "6 μV", "latency": "3.5 ms", "velocity": "38 m/s"},
            {"nerve": "정중신경 감각신경활동전위(Median SNAP)", "recording": "검지", "stimulation": "손목", "side": "오른쪽", "amplitude": "25 μV", "latency": "2.9 ms", "velocity": "52 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "자신경 복합근육활동전위(Ulnar CMAP)", "recording": "새끼벌림근(ADM)", "stimulation": "팔꿈치 아래", "side": "오른쪽", "amplitude": "6.8 mV", "latency": "6.4 ms", "velocity": "49 m/s"},
            {"nerve": "자신경 복합근육활동전위(Ulnar CMAP)", "recording": "새끼벌림근(ADM)", "stimulation": "팔꿈치 위", "side": "오른쪽", "amplitude": "3.1 mV", "latency": "10.9 ms", "velocity": "28 m/s"}
        ],
        "needle_emg": [
            {"muscle": "첫째등쪽뼈사이근(FDI)", "root": "C8-T1", "nerve": "자신경", "rest": "fibrillation potential, positive sharp wave", "volition": "Reduced MU recruitment"},
            {"muscle": "짧은엄지벌림근(APB)", "root": "C8-T1", "nerve": "정중신경", "rest": "Silent at rest", "volition": "Normal MU recruitment"}
        ],
        "interpretation": {
            "sensory": [
                "오른쪽 자신경 감각신경 진폭이 대폭 감소하였으나, 정중신경 반응은 정상으로 자신경에 국한된 문제임을 지시합니다."
            ],
            "motor": [
                "팔꿈치 위 자극 시 팔꿈치 아래 자극에 비해 진폭이 절반 이하로 급감하고 속도가 느려져, 팔꿈치 관절 부위의 국소 전도차단을 강력히 증명합니다."
            ],
            "emg": [
                "자신경 지배 손가락 근육에서 탈신경 소견이 보이며, 정중신경 근육은 깨끗합니다."
            ],
            "integration": [
                "팔꿈치 터널 구간에서의 명확한 전도 이상과 자신경 국소 침범을 근거로 '오른쪽 팔꿈치굴증후군'으로 확진합니다."
            ],
            "differential": [
                "C8-T1 목 신경뿌리병증: 감각신경전도가 정상 보존되고, 목 척추주위근 방전이 동반됩니다."
            ],
            "additional": [
                "야간 팔꿈치 신전 보조기를 착용하고 컴퓨터 작업 시 팔꿈치 압박 회피 자세를 지도합니다."
            ]
        }
    },
        "왼쪽 상부위팔신경얼기병증 의심": {
        "meta": {
            "age": 37, "sex": "여성", "side": "왼쪽",
            "chief": "갑작스러운 왼쪽 어깨 통증 이후 어깨 벌림과 팔꿉관절 굽힘 약화."
        },
        "diagnosis": "왼쪽 위쪽 위팔신경얼기병증(Upper trunk brachial plexopathy)",
        "lesion": "왼쪽 위팔신경얼기 상부줄기, 주로 C5-C6 섬유",
        "sensory_ncs": [
            {"nerve": "가쪽아래팔피부신경 감각신경활동전위(Lateral antebrachial cutaneous SNAP)", "recording": "아래팔 가쪽", "stimulation": "팔꿈치 근처", "side": "왼쪽", "amplitude": "4 μV", "latency": "3.3 ms", "velocity": "35 m/s"},
            {"nerve": "가쪽아래팔피부신경 감각신경활동전위(Lateral antebrachial cutaneous SNAP)", "recording": "아래팔 가쪽", "stimulation": "팔꿈치 근처", "side": "오른쪽", "amplitude": "18 μV", "latency": "2.4 ms", "velocity": "52 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "겨드랑신경 복합근육활동전위(Axillary CMAP)", "recording": "어깨세모근", "stimulation": "Erb's point", "side": "왼쪽", "amplitude": "1.8 mV", "latency": "5.1 ms", "velocity": "-"},
            {"nerve": "근육피부신경 복합근육활동전위(Musculocutaneous CMAP)", "recording": "위팔두갈래근", "stimulation": "Erb's point", "side": "왼쪽", "amplitude": "2.0 mV", "latency": "4.8 ms", "velocity": "-"}
        ],
        "needle_emg": [
            {"muscle": "어깨세모근(Deltoid)", "root": "C5-C6", "nerve": "겨드랑신경", "rest": "fibrillation potential, positive sharp wave", "volition": "Reduced MU recruitment"},
            {"muscle": "목 척추주위근(Cervical paraspinal)", "root": "C5-C6", "nerve": "뒤가지(posterior ramus)", "rest": "Silent at rest", "volition": "평가 제한"}
        ],
        "interpretation": {
            "sensory": [
                "가쪽아래팔피부신경 감각 진폭이 비정상으로 저하되어, 병변이 뒤뿌리신경절(DRG)보다 바깥쪽인 위팔신경얼기 수준에 있음을 증명합니다."
            ],
            "motor": [
                "겨드랑신경과 근육피부신경(C5-C6)의 운동 반응이 소실되어 상부 줄기(Upper trunk) 손상이 확인됩니다."
            ],
            "emg": [
                "어깨 및 위팔 앞쪽 근육들에서 탈신경 전위가 도출되나 목 척추주위근은 정상으로 유지되어 척수 뿌리(Root) 병변을 배제합니다."
            ],
            "integration": [
                "감각 감퇴, 복합 근육 마비, 목 척추주위근 정상 패턴을 종합해 '왼쪽 위쪽 위팔신경얼기병증'으로 진단합니다."
            ],
            "differential": [
                "C5-C6 신경뿌리병증: 감각신경전도는 보존되고 목 척추주위근에 탈신경 이상이 관찰되어야 합니다."
            ],
            "additional": [
                "Erb's point 주변 신경초음파 확인 및 어깨 아탈구 방지용 슬링(Sling) 착용을 권장합니다."
            ]
        }
    },

    "오른쪽 말초성 얼굴신경마비 의심": {
        "meta": {
            "age": 29, "sex": "여성", "side": "오른쪽",
            "chief": "오른쪽 눈 감기 어려움, 입꼬리 처짐, 이마 주름 감소. 발병 10일째."
        },
        "diagnosis": "오른쪽 말초성 얼굴신경마비(Bell's palsy)",
        "lesion": "오른쪽 얼굴신경 말초부(CN VII) 운동 가지",
        "sensory_ncs": [],
        "motor_ncs": [
            {"nerve": "얼굴신경 복합근육활동전위(Facial CMAP)", "recording": "눈둘레근(Orbicularis oculi)", "stimulation": "귓바퀴 앞", "side": "오른쪽", "amplitude": "0.7 mV", "latency": "4.9 ms", "velocity": "-"},
            {"nerve": "얼굴신경 복합근육활동전위(Facial CMAP)", "recording": "눈둘레근(Orbicularis oculi)", "stimulation": "귓바퀴 앞", "side": "왼쪽", "amplitude": "3.8 mV", "latency": "3.2 ms", "velocity": "-"}
        ],
        "late_response": [
            {"test": "눈깜빡반사 오른쪽 자극-오른쪽 R1", "side": "오른쪽", "latency": "소실", "amplitude": "-"},
            {"test": "눈깜빡반사 오른쪽 자극-왼쪽 R2", "side": "왼쪽", "latency": "정상 범위", "amplitude": "보존"},
            {"test": "눈깜빡반사 왼쪽 자극-왼쪽 R1", "side": "왼쪽", "latency": "정상 범위", "amplitude": "보존"}
        ],
        "needle_emg": [],
        "interpretation": {
            "sensory": [
                "얼굴신경 마비는 일반 사지 감각신경전도가 아닌 눈깜빡반사(Blink Reflex)와 안면 운동신경검사(Facial CMAP)를 주로 활용해 평가합니다."
            ],
            "motor": [
                "오른쪽 얼굴신경 운동 반응 진폭이 왼쪽 대비 20% 미만으로 크게 감소하여 얼굴 운동축삭의 심한 퇴행 손상을 나타냅니다."
            ],
            "emg": [
                "얼굴 근육 침근전도는 발병 2~3주 경과 후 예후 및 변성 정도를 정밀히 볼 때 수행하며, 초기 진단에서는 반사와 전도검사가 핵심입니다."
            ],
            "integration": [
                "이마 주름 소실(말초성 징후), 안면 운동 진폭 급감 및 우측 자극 시의 반사 차단을 결합해 '오른쪽 말초성 안면신경마비(Bell's palsy)'로 진단합니다."
            ],
            "differential": [
                "중추성 안면마비: 이마 주름은 양측 대뇌 지배로 보존되며 주로 입 주위에만 마비가 국한되어 나타납니다."
            ],
            "additional": [
                "안구 건조 및 각막 궤양 예방(안대, 인공눈물 적용)과 바이오피드백 표정근 운동 물리치료가 필요합니다."
            ]
        }
    },

    "뇌졸중 후 경직 H-반사 평가": {
        "meta": {
            "age": 63, "sex": "남성", "side": "왼쪽",
            "chief": "오른쪽 대뇌 뇌졸중 후 왼쪽 발목 저측굴곡 강직 증가. 보행 시 첨족(toe walking) 양상."
        },
        "diagnosis": "중추성 상위운동신경원 증후군에 의한 왼쪽 하지 경직(Spasticity)",
        "lesion": "오른쪽 뇌 피질척수로 손상에 의한 왼쪽 척수 분절 억제 기전 상실",
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
                "이 사례는 말초신경계 질환 판독이 아니므로 일반 말초 감각신경검사를 루틴으로 시행하지 않습니다."
            ],
            "motor": [
                "대뇌 상위운동신경원(UMN) 손상 환자에서 척수 반사회로의 경직(Spasticity) 정량적 평가를 위해 H-반사를 집중 활용합니다."
            ],
            "emg": [
                "척수 단일 시냅스 반사회로를 대변하는 H/M 비율이 왼쪽(환측)에서 0.62로 대조측(0.28)보다 월등히 높습니다.",
                "이는 상위 중추의 억제 시스템이 상실되어 알파 운동신경원의 흥분성이 비정상적으로 치솟은 '과흥분 상태'를 명확히 입증합니다."
            ],
            "integration": [
                "비정상적 H-반사 항진 및 높은 H/M 비율은 '뇌졸중 유발 상위운동신경원(UMN) 병변으로 인한 좌측 가자미근 강직'의 객관적 증거가 됩니다."
            ],
            "differential": [
                "말초 S1 신경뿌리병증: H-반사 진폭이 커지는 것이 아니라 지연되거나 아예 소실되는 양상으로 정반대의 결과를 냅니다."
            ],
            "additional": [
                "MAS(Modified Ashworth Scale) 평가, 종아리 스트레칭, 대항근인 앞정강근에 FES 자극을 가하는 상호억제 물리치료를 권장합니다."
            ]
        }
    }
}
