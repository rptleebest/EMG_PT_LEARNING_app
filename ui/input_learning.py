import streamlit as st
from ui.navigation import render_bottom_navigation

VIRTUAL_REPORTS = {
    "왼쪽 목/어깨 통증 및 팔 저림 (C6 신경뿌리병증 의심)": {
        "info": {"age": 45, "sex": "남성", "symptom": "왼쪽 목(Cervical) 통증 및 무감각, 엄지/검지 손가락 끝 저림, 팔꿉관절 굽힘(Flexion)력 감소", "side": "왼쪽"},
        "diagnosis": "왼쪽 C6 목 신경뿌리병증(Cervical radiculopathy)",
        "ncs_sensory": [
            ["정중신경 (Median SNAP)", "25 μV", "2.8 ms", "정상 범위"],
            ["자신경 (Ulnar SNAP)", "22 μV", "2.5 ms", "정상 범위"]
        ],
        "ncs_motor": [
            ["정중신경 (Median CMAP)", "손목(Wrist)", "8.5 mV", "3.5 ms", "정상 범위"],
            ["정중신경 (Median CMAP)", "팔꿈치(Elbow)", "8.1 mV", "7.8 ms", "정상 범위"]
        ],
        "emg": [
            ["위팔두갈래근 (Biceps brachii)", "C5-C6", "fibrillation potential, positive sharp wave", "Reduced MU recruitment", "비정상 (활동성 탈신경)"],
            ["긴노쪽손목폄근 (ECRL)", "C6-C7", "fibrillation potential, positive sharp wave", "Giant MUAPs 출현 및 Reduced MU recruitment", "비정상 (만성 재신경지배 동반)"],
            ["짧은엄지벌림근 (APB)", "C8-T1", "Silent at rest", "Normal MU recruitment", "정상 범위"],
            ["목 척추주위근 (Cervical Paraspinal)", "C6", "fibrillation potential, positive sharp wave", "통증으로 인해 평가불가", "비정상 (활동성 탈신경)"]
        ],
        "interpretation": [
            "감각신경활동전위(Sensory Nerve Action Potential, SNAP)가 정상 범위로 보존됩니다. 이는 감각 세포체가 위치한 뒤뿌리신경절(Dorsal Root Ganglion, DRG)보다 몸쪽(Proximal)에서 목(Cervical) 신경뿌리 압박 병변이 일어났음을 생리학적으로 입증합니다.",
            "침근전도검사(Needle EMG)에서 동일한 C6 신경 분절 지배를 공유하는 복수 근육들 및 목 척추주위근육(Cervical paraspinal muscle)에서 활동성 탈신경(Active denervation) 자발전위가 검출되어 최종적으로 C6 목 신경뿌리병증(Cervical radiculopathy)으로 확진합니다."
        ],
        "emg_meaning": [
            "fibrillation potential, positive sharp wave: 신경 지배를 탈락한 개별 근섬유막의 전기적 불안정성을 고발하는 이상 자발전위입니다.",
            "Reduced MU recruitment: 수의수축(Volition) 시 동원 및 결합되는 운동단위(Motor Unit, MU) 개수의 정량적 감소 상태를 뜻합니다."
        ],
        "ddx": "목(Cervical) 디스크 협착 병변을 감별하기 위해 목 MRI 정밀 영상 검사와의 대조 분석이 요구됩니다."
    },

    "오른쪽 1~3번째 손가락 저림 및 야간통 (손목굴증후군 의심)": {
        "info": {"age": 52, "sex": "여성", "symptom": "오른쪽 1, 2, 3번째 손가락 노쪽(Radial) 분포 영역 저림, 야간 통증 및 손목관절 굽힘(Flexion) 시 통증 악화", "side": "오른쪽"},
        "diagnosis": "오른쪽 손목굴증후군(Carpal tunnel syndrome)",
        "ncs_sensory": [
            ["정중신경 (Median SNAP)", "8 μV", "4.8 ms", "진폭: 감소 / 잠복기: 지연"],
            ["자신경 (Ulnar SNAP)", "25 μV", "2.6 ms", "정상 범위"]
        ],
        "ncs_motor": [
            ["정중신경 (Median CMAP)", "손목(Wrist)", "3.1 mV", "5.5 ms", "진폭: 감소 / 잠복기: 지연"],
            ["정중신경 (Median CMAP)", "팔꿈치(Elbow)", "2.9 mV", "9.8 ms", "진폭: 감소"]
        ],
        "emg": [
            ["짧은엄지벌림근 (APB)", "C8-T1", "Silent at rest", "Normal MU recruitment", "정상 범위"],
            ["첫째등쪽뼈사이근 (FDI)", "C8-T1", "Silent at rest", "Normal MU recruitment", "정상 범위"]
        ],
        "interpretation": [
            "정중신경(Median nerve) 감각전도 SNAP과 운동전도 복합근육활동전위(CMAP)의 잠복기 지연이 나타나 손목 영역의 국소 말이집탈락(Demyelination)성 압박 상태를 고시합니다.",
            "정중신경(Median nerve) 진폭의 유의미한 감소가 관찰되어, 단순 말이집탈락을 넘어 운동 축삭 손상(Axonal loss)이 함께 전개되고 있음을 의미합니다."
        ],
        "emg_meaning": [
            "Silent at rest: 휴식 시 어떠한 비정상 전위 자발방전도 유발되지 않는 생리적 침묵 상태입니다.",
            "Normal MU recruitment: 등척성/등장성 수의수축 요구도에 맞추어 하위 운동 단위들이 조화롭게 동원되는 양상입니다."
        ],
        "ddx": "목(Cervical) 신경뿌리 장애와의 감별을 위해 이학적 반사 검사 및 손목 정중신경 주행 부위 티넬 징후(Tinel's sign) 확인이 동반되어야 합니다."
    },

    "왼쪽 허리 통증 및 엄지발가락 올림 약화 (L5 신경뿌리병증 의심)": {
        "info": {"age": 58, "sex": "여성", "symptom": "왼쪽 허리통증(Lumbago)-종아리 가쪽 및 발등 통증, 보행 시 발목관절 등굽힘(Dorsiflexion) 근력 약화로 발끝 끌림", "side": "왼쪽"},
        "diagnosis": "왼쪽 L5 허리 신경뿌리병증(Lumbar radiculopathy)",
        "ncs_sensory": [
            ["얕은종아리신경 (Superficial Peroneal SNAP)", "12 μV", "2.9 ms", "정상 범위"],
            ["장딴지신경 (Sural SNAP)", "15 μV", "3.1 ms", "정상 범위"]
        ],
        "ncs_motor": [
            ["종아리신경 (Peroneal CMAP)", "발목(Ankle)", "3.5 mV", "4.5 ms", "정상 범위"],
            ["종아리신경 (Peroneal CMAP)", "오금(Popliteal)", "3.3 mV", "11.2 ms", "정상 범위"]
        ],
        "emg": [
            ["앞정강근 (Tibialis Anterior)", "L4-L5", "fibrillation potential, positive sharp wave", "Reduced MU recruitment", "비정상 (활동성 탈신경)"],
            ["긴종아리근 (Peroneus Longus)", "L5-S1", "fibrillation potential, positive sharp wave", "Giant MUAPs 출현 및 Reduced MU recruitment", "비정상 (만성 재신경지배 동반)"],
            ["가자미근 (Soleus)", "S1-S2", "Silent at rest", "Normal MU recruitment", "정상 범위"],
            ["허리 척추주위근 (Lumbar Paraspinal)", "L5", "fibrillation potential, positive sharp wave", "통증으로 인해 평가불가", "비정상 (활동성 탈신경)"]
        ],
        "interpretation": [
            "다리의 주요 표재 감각신경활동전위(SNAP)들이 정상 보존되어 병터가 허리 뒤뿌리신경절(Dorsal root ganglion, DRG)보다 몸쪽(Proximal)에 국한된 허리 신경뿌리(root) 장애임을 지시합니다.",
            "L5 신경 분절의 지배를 받는 앞정강근 및 긴종아리근, 그리고 허리 척추주위근육(Lumbar paraspinal muscle)에서 비정상 자발전위가 동시에 터져 나와 L5 허리 신경뿌리병증(Lumbar radiculopathy)으로 정의됩니다."
        ],
        "emg_meaning": [
            "Giant MUAP: 손상된 신경을 대신하여 생존 축삭이 발아(Sprouting)해 들어가 해당 탈신경 근섬유를 만성 재지배(Reinnervation)한 결과물입니다."
        ],
        "ddx": "L4-L5 척수 신경뿌리의 디스크 압박 수준을 진단하기 위해 허리엉치 MRI 검사 의뢰가 추천됩니다."
    },

    "오른쪽 발처짐 및 종아리 가쪽 감각 저하 (온종아리신경 마비 의심)": {
        "info": {"age": 32, "sex": "남성", "symptom": "오랫동안 다리를 꼬고 앉은 오른쪽 발목관절 등굽힘(Dorsiflexion) 불능 및 보행 시 발처짐(Foot drop)", "side": "오른쪽"},
        "diagnosis": "오른쪽 온종아리신경 마비(Common peroneal neuropathy)",
        "ncs_sensory": [
            ["얕은종아리신경 (Superficial Peroneal SNAP)", "4 μV", "3.8 ms", "진폭: 감소 / 잠복기: 지연"],
            ["장딴지신경 (Sural SNAP)", "16 μV", "3.0 ms", "정상 범위"]
        ],
        "ncs_motor": [
            ["종아리신경 (Peroneal CMAP)", "발목(Ankle)", "4.5 mV", "4.8 ms", "정상 범위"],
            ["종아리신경 (Peroneal CMAP)", "종아리뼈머리(fibular head)", "1.1 mV", "무반응", "진폭: 감소 (국소 전도차단)"]
        ],
        "emg": [
            ["앞정강근 (Tibialis Anterior)", "L4-L5", "Silent at rest", "No MUAPs on volition (동원 불가)", "비정상 (전도 완전 마비)"],
            ["긴종아리근 (Peroneus Longus)", "L5-S1", "Silent at rest", "Reduced MU recruitment", "비정상 (동원 감소)"],
            ["허리 척추주위근 (Lumbar Paraspinal)", "L5", "Silent at rest", "Normal MU recruitment", "정상 범위"]
        ],
        "interpretation": [
            "종아리뼈머리(Fibular head) 가쪽을 주행하는 온종아리신경(Common peroneal nerve) 자극 시 복합근육활동전위(CMAP) 진폭이 50% 이상 감소하는 국소 전도차단(Conduction block)이 계측됩니다.",
            "얕은종아리신경 감각신경활동전위(SNAP)의 비정상적 진폭 감소가 일어났으나, 허리 척추주위근육(Lumbar paraspinal muscle)은 완전히 정상 상태를 유지하므로 허리 신경뿌리병증(Lumbar radiculopathy)을 배제하고 종아리뼈머리 부위의 말초 포착성 종아리신경 마비로 단정합니다."
        ],
        "emg_meaning": [
            "Conduction Block: 신경 축삭의 물리적 사멸이 유도되지 않은 상황에서 국소 압박에 기인하여 전기 자극 전달이 순간 차단되는 상태입니다."
        ],
        "ddx": "물리치료적으로 보행 보조기(AFO) 처방 검토와 종아리뼈머리 부위의 외부 가해 압박 해소가 중요합니다."
    },

    "양측 발끝 저림 및 감각 저하 (당뇨병성 다발신경병증 의심)": {
        "info": {"age": 68, "sex": "남성", "symptom": "양 발바닥이 대칭적으로 저리고 화끈거리며 무감각한 대칭성 장갑-양말형(Glove-stocking) 감각 마비", "side": "양측"},
        "diagnosis": "길이의존성 축삭성 다발신경병증(Length-dependent axonal polyneuropathy)",
        "ncs_sensory": [
            ["장딴지신경 (Sural SNAP) 오른쪽", "무반응", "무반응", "반응 소실"],
            ["정중신경 (Median SNAP) 오른쪽", "18 μV", "3.4 ms", "정상 범위"]
        ],
        "ncs_motor": [
            ["정강신경 (Tibial CMAP) 오른쪽", "발목(Ankle)", "1.5 mV", "6.2 ms", "진폭: 감소 / 잠복기: 지연"],
            ["정강신경 (Tibial CMAP) 오른쪽", "오금(Popliteal)", "1.2 mV", "15.2 ms", "진폭: 감소"]
        ],
        "emg": [
            ["앞정강근 (Tibialis Anterior)", "L4-L5", "fibrillation potential, positive sharp wave", "Reduced MU recruitment", "비정상 (대칭적 말초 축삭 퇴행)"],
            ["위팔두갈래근 (Biceps brachii)", "C5-C6", "Silent at rest", "Normal MU recruitment", "정상 범위"]
        ],
        "interpretation": [
            "다리의 먼쪽(Distal) 말단 감각전도인 장딴지신경(Sural nerve) SNAP가 대칭 반응 소실을 보여 축삭 손상(Axonal loss)을 고지합니다.",
            "가장 길고 에너지 대사가 취약한 축삭 원단부부터 대칭 시들어 들어가는 당뇨성 길이의존성(Length-dependent, dying-back) 다발신경병증(Polyneuropathy) 기전과 일치합니다."
        ],
        "emg_meaning": [
            "Dying-back pattern: 대사 이상으로 인해 신경 가지 세포체에서 가장 거리가 먼 먼쪽(Distal) 신경망부터 퇴행성 사멸이 역행하여 진입하는 현상입니다."
        ],
        "ddx": "혈중 당화혈색소 수치 추적과 당뇨발 방지를 위한 압박 예방 보행 물리치료 중재가 추천됩니다."
    },

    "상하지 대칭성 근력 저하 (급성 길랭-바레 증후군 의심)": {
        "info": {"age": 41, "sex": "여성", "symptom": "가벼운 장염을 앓고 난 뒤 2주 후부터 대칭적으로 무릎 이하 다리 근력이 빠지고 위쪽으로 상행하는 양상", "side": "양측"},
        "diagnosis": "급성 염증성 탈말이집성 다발신경뿌리병증(Guillain-Barre Syndrome, GBS)",
        "ncs_sensory": [
            ["정중신경 (Median SNAP)", "22 μV", "3.8 ms", "잠복기: 지연"],
            ["장딴지신경 (Sural SNAP)", "12 μV", "3.4 ms", "정상 범위 (Sural Sparing)"]
        ],
        "ncs_motor": [
            ["종아리신경 (Peroneal CMAP)", "발목(Ankle)", "3.0 mV", "8.5 ms", "잠복기: 지연"],
            ["종아리신경 (Peroneal CMAP)", "종아리뼈머리(fibular head)", "1.2 mV", "20.1 ms", "잠복기: 지연 / 전도속도 폭락"]
        ],
        "emg": [
            ["앞정강근 (Tibialis Anterior)", "L4-L5", "Silent at rest", "Reduced MU recruitment", "비정상 (동원 결손)"],
            ["허리 척추주위근 (Lumbar Paraspinal)", "L5", "Silent at rest", "통증으로 인해 평가불가", "정상 범위"]
        ],
        "interpretation": [
            "다수의 다리 전도 속도가 폭락하고 전달 잠복기가 130% 이상 대폭 늘어난 대칭 말이집탈락(Demyelination)성 이상 전도를 나타냅니다.",
            "감각 SNAP은 정상 범위로 생존하면서 오직 운동 신경 복합근육활동전위(CMAP)만 극도로 붕괴되는 길랭-바레 증후군의 전형적인 장단지 스페어링(Sural sparing) 양상을 만족합니다."
        ],
        "emg_meaning": [
            "Sural sparing effect: 자가면역 말이집 손상 시 하지 말단 감각인 장딴지 감각신경활동전위(Sural SNAP) 반응이 홀로 정상 유지되는 전형적 기얭-바레 증후군(GBS) 판독 감별점입니다."
        ],
        "ddx": "급성 상행성 호흡 마비 유무 모니터링을 위해 호흡기 치료 연계 관리가 필수적입니다."
    },

    "오른쪽 팔꿈치 통증 및 손가락 힘 빠짐 (C7 신경뿌리병증 의심)": {
        "info": {"age": 49, "sex": "여성", "symptom": "오른쪽 어깨 뒤부터 삼두근 부위를 지나 가운데 손가락으로 전개되는 통증 및 팔꿉관절 폄(Extension) 근력저하", "side": "오른쪽"},
        "diagnosis": "오른쪽 C7 목 신경뿌리병증(Cervical radiculopathy)",
        "ncs_sensory": [
            ["정중신경 (Median SNAP)", "28 μV", "2.9 ms", "정상 범위"],
            ["자신경 (Ulnar SNAP)", "24 μV", "2.4 ms", "정상 범위"]
        ],
        "ncs_motor": [
            ["정중신경 (Median CMAP)", "손목(Wrist)", "9.2 mV", "3.6 ms", "정상 범위"],
            ["노신경 (Radial CMAP)", "아래팔(forearm)", "6.5 mV", "2.8 ms", "정상 범위"]
        ],
        "emg": [
            ["위팔세갈래근 (Triceps brachii)", "C7-C8", "fibrillation potential, positive sharp wave", "Reduced MU recruitment", "비정상 (활동성 탈신경)"],
            ["손목굽힘근 (Flexor carpi radialis)", "C6-C7", "fibrillation potential, positive sharp wave", "Reduced MU recruitment", "비정상 (활동성 탈신경)"],
            ["위팔두갈래근 (Biceps brachii)", "C5-C6", "Silent at rest", "Normal MU recruitment", "정상 범위"],
            ["목 척추주위근 (Cervical Paraspinal)", "C7", "fibrillation potential, positive sharp wave", "통증으로 인해 평가불가", "비정상 (활동성 탈신경)"]
        ],
        "interpretation": [
            "가운데 손가락 저림 부위(C7 피부분절)에도 불구하고 정중신경 감각신경활동전위(SNAP)가 정상 범위인 것은 뒤뿌리신경절(Dorsal root ganglion, DRG)보다 몸쪽(Proximal) 목 신경뿌리 부위 병소임을 지지합니다.",
            "C7 지배 운동 영역의 핵심 축을 이루는 복수 근육들 및 제7 목 수준의 목 척추주위근육(Cervical paraspinal muscle)에서 일치된 탈신경 비정상 자발전위가 검출되어 C7 목 신경뿌리병증(Cervical radiculopathy)으로 확정됩니다."
        ],
        "emg_meaning": [
            "C7 Myotome mapping: 다른 말초 주행 경로를 가졌으나 오직 C7 분절 신경뿌리를 기원으로 묶이는 복수 표적근에서 동시 탈신경을 의미하는 비정상적인 자발전위가 나오는 기법입니다."
        ],
        "ddx": "위팔세갈래근 반사(Triceps reflex) 감퇴 여부를 검증하고 목 MRI를 통한 제6-7번 목 척추 추간판 유착 확인을 연계합니다."
    },

    "S1 신경뿌리병증 의심 사례": {
        "info": {"age": 53, "sex": "남성", "symptom": "왼쪽 요통(Lumbago), 왼쪽 볼기에서 허벅지 뒤편을 관통하여 발등 가쪽 및 새끼발가락으로 흐르는 칼로 찌르는 듯한 통증", "side": "왼쪽"},
        "diagnosis": "왼쪽 S1 허리 신경뿌리병증(Lumbar radiculopathy)",
        "ncs_sensory": [
            ["장딴지신경 (Sural SNAP)", "14 μV", "3.0 ms", "정상 범위"],
            ["얕은종아리신경 (Superficial Peroneal SNAP)", "11 μV", "2.8 ms", "정상 범위"]
        ],
        "ncs_motor": [
            ["정강신경 (Tibial CMAP)", "발목(Ankle)", "5.8 mV", "4.2 ms", "정상 범위"],
            ["종아리신경 (Peroneal CMAP)", "발목(Ankle)", "4.8 mV", "4.5 ms", "정상 범위"]
        ],
        "emg": [
            ["가자미근 (Soleus)", "S1-S2", "fibrillation potential, positive sharp wave", "Reduced MU recruitment", "비정상 (활동성 탈신경)"],
            ["장딴지근 (Gastrocnemius)", "S1-S2", "fibrillation potential, positive sharp wave", "Reduced MU recruitment", "비정상 (활동성 탈신경)"],
            ["앞정강근 (Tibialis Anterior)", "L4-L5", "Silent at rest", "Normal MU recruitment", "정상 범위"],
            ["허리 척추주위근 (Lumbar Paraspinal)", "S1", "fibrillation potential, positive sharp wave", "통증으로 인해 평가불가", "비정상 (활동성 탈신경)"]
        ],
        "interpretation": [
            "새끼발가락 외측(S1 피부분절) 저림에도 불구하고 장딴지신경(Sural nerve) SNAP가 정상 범위로 완전히 보존되어 병변이 뒤뿌리신경절(DRG) 몸쪽(Proximal)의 척수 신경뿌리 병변임을 의미합니다.",
            "정강신경(Tibial nerve) 지배 하에 있으면서 S1 지배 하에 있는 가자미근(Soleus) 및 장딴지근(Gastrocnemius)에서 탈신경 비정상적인 자발전위가 출현하며, S1 허리 척추주위근육(Lumbar paraspinal muscle)에서 동반 출현하여 S1 허리 신경뿌리병증(Lumbar radiculopathy)으로 판독합니다."
        ],
        "emg_meaning": [
            "S1 Myotome pathway: 아킬레스힘줄 반사(Achilles tendon reflex) 경로를 구성하는 가자미근(Soleus)에서 발생하는 비정상적인 자발 활동을 의미합니다."
        ],
        "ddx": "좌골신경통(Sciatica)과의 구분을 위해 바로누운자세 편다리올림검사(straight leg raising test, SLR test) 물리치료 평가 검사와 허리엉치 MRI 정밀 확인을 권장합니다."
    },

    "오른쪽 어깨 통증 및 손 내재근 위축 (가슴문증후군 의심)": {
        "info": {"age": 38, "sex": "여성", "symptom": "오른쪽 어깨 및 빗장뼈(Clavicle) 하부 통증, 새끼손가락 쪽 감각 이상, 짧은엄지벌림근(APB)의 심한 위축으로 인한 Gilliatt-Sumner 손(Gilliatt-Sumner hand) 양상 동반", "side": "오른쪽"},
        "diagnosis": "오른쪽 가슴문증후군(Thoracic outlet syndrome, TOS)",
        "ncs_sensory": [
            ["가쪽아래팔피부신경 (LAC SNAP)", "25 μV", "2.1 ms", "정상 범위"],
            ["안쪽아래팔피부신경 (MAC SNAP)", "2 μV", "3.9 ms", "진폭: 감소 / 잠복기: 지연"]
        ],
        "ncs_motor": [
            ["정중신경 (Median CMAP)", "손목(Wrist)", "3.8 mV", "4.0 ms", "진폭: 감소"],
            ["자신경 (Ulnar CMAP)", "손목(Wrist)", "4.1 mV", "3.2 ms", "정상 범위"]
        ],
        "emg": [
            ["짧은엄지벌림근 (APB)", "C8-T1", "Silent at rest", "Giant MUAPs 출현 및 Reduced MU recruitment", "비정상 (만성 축삭 손상에 따른 Gilliatt-Sumner 손 양상)"],
            ["첫째등쪽뼈사이근 (FDI)", "C8-T1", "Silent at rest", "Giant MUAPs 출현 및 Reduced MU recruitment", "비정상 (만성 축삭 손상에 따른 손 내재근 위축)"],
            ["위팔두갈래근 (Biceps brachii)", "C5-C6", "Silent at rest", "Normal MU recruitment", "정상 범위"],
            ["목 척추주위근 (C8-T1)", "C8-T1", "Silent at rest", "Normal MU recruitment", "정상 범위"]
        ],
        "interpretation": [
            "위팔신경얼기(Brachial plexus) 하부 신경줄기(Lower trunk)가 빗장뼈(clavicle) 아래 통로에서 물리 압박을 받는 가슴문증후군(Thoracic outlet syndrome, TOS) 기전입니다. 안쪽아래팔피부신경(MAC) SNAP의 진폭이 극적으로 감소(50% 이하)하여 신경얼기(Plexus) 수준의 먼쪽(Distal) 변성을 가리칩니다.",
            "T1 우세 지배인 짧은엄지벌림근 (APB)과 첫째등쪽뼈사이근 (FDI)에서 만성적인 축삭발아(Sprouting) 결과물인 거대운동단위활동전위(Giant MUAP)들이 드문드문 동원되는 반면, 목 척추주위근육(Cervical paraspinal muscle)은 완전 정상이므로 척수 신경뿌리을 배제하고 가슴문(Thoracic outlet) 영역의 압박성 마비(TOS)로 확진합니다."
        ],
        "emg_meaning": [
            "Gilliatt-Sumner hand: 가슴문증후군(TOS) 장기화로 인해 T1 운동 지배 가지가 소실되어, 짧은엄지벌림근(APB)을 중심으로 손 자체기원근육(intrinsic)이 심하게 위축 및 함몰되는 임상적 변성 양상입니다."
        ],
        "ddx": "목갈코근(nasalis)(Scalene muscle) 단축 긴장을 감별하기 위한 Adson 검사 연계 및 이학적 가슴문 압박 가동 검사가 추천됩니다."
    },

    "왼쪽 갑작스러운 한쪽 얼굴 마비 (얼굴신경마비 의심)": {
        "info": {"age": 29, "sex": "남성", "symptom": "급격히 발현된 왼쪽 얼굴 전반 이마 주름 소실, 왼쪽 안구 완전 감김(Closure) 불능, 입꼬리 대칭 이탈", "side": "왼쪽"},
        "diagnosis": "왼쪽 특발성 얼굴신경마비(Bell's palsy)",
        "ncs_sensory": [
            ["오른쪽 이마 (V1 분지)", "22 μV", "2.1 ms", "정상 범위"],
            ["왼쪽 이마 (V1 분지)", "21 μV", "2.2 ms", "정상 범위"]
        ],
        "ncs_motor": [
            ["오른쪽 얼굴신경 (Facial CMAP)", "코근(nasalis)", "3.2 mV", "2.8 ms", "정상 범위"],
            ["왼쪽 얼굴신경 (Facial CMAP)", "코근(nasalis)", "1.1 mV", "4.5 ms", "진폭: 감소 / 잠복기: 지연"]
        ],
        "emg": [
            ["눈둘레근 (Orbicularis Oculi)", "얼굴신경 지배", "Silent at rest", "Normal MU recruitment", "정상 범위"]
        ],
        "interpretation": [
            "왼쪽 얼굴 자극 시 운동 복합근육활동전위(Facial CMAP) 최대 진폭이 정상측 대비 50% 이하인 34% 수준(1.1 mV)으로 폭락해 있어, 심각한 원위부 축삭 사멸 변성이 급격히 진행되고 있음을 정량 계측해 냅니다.",
            "눈깜빡반사(Blink Reflex) 검사 상 왼쪽 각막 자극 시 신호 지연이 심해, 뇌줄기(brain stem) 반사 회로가 기능 마비에 처했음을 보여줍니다.",
            "왼쪽 이마 주름 소실, 눈 감기 불능, 얼굴신경 자극 시 좌/우 진폭 비대칭성 격차 및 눈깜박반사 R1/R2 전도 이상을 종합하여 얼굴신경마비(Bell's palsy)로 최종 진단합니다."
        ],
        "emg_meaning": [
            "얼굴 근육의 원위 운동축삭 변성을 평가하기 위한 얼굴 복합근육활동전위(CMAP) 정량 분석과 뇌줄기 삼차-얼굴신경 반사궁 회로(Blink reflex)를 추적했습니다. 침근전도는 발병 초기(2~3주 미만)에는 검사 프로토콜 상 완전 제외됩니다."
        ],
        "ddx": "중추성 얼굴마비(뇌졸중 등)는 이마 주름 잡기가 정상 보존되나 말초성 벨마비는 불가능하므로, 내원 시 이마 주름 형성 여부를 관찰하여 위운동신경세포(UMN)와 아래운동신경세포(LMN) 장애를 명확히 선별하십시오."
    }
}


def render_input_learning():
    st.markdown("""
    <style>
    .bottom-nav-safe-space {
        height: 12px;
    }
    @media (max-width: 768px) {
        .bottom-nav-safe-space {
            height: 20px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="main-title">가상 결과표 판독학습</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtle" style="font-size:0.84rem; line-height:1.45; word-break:keep-all;">임상 수치 데이터 기반의 가상 결과지를 통해 전기생리학적 해석 논리를 훈련합니다.</div>',
        unsafe_allow_html=True
    )

    if "input_reset_counter" not in st.session_state:
        st.session_state["input_reset_counter"] = 0

    dynamic_radio_key = f"input_report_selector_{st.session_state['input_reset_counter']}"

    st.markdown('<div class="section-card" style="padding: 10px 8px;">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label" style="font-size:0.92rem;">📋 학습할 가상 결과지 선택 (실시간 판독형)</div>', unsafe_allow_html=True)

    case_names = ["선택 안 함"] + list(VIRTUAL_REPORTS.keys())

    selected = st.radio(
        "가상 결과지 리스트",
        case_names,
        key=dynamic_radio_key,
        label_visibility="collapsed"
    )
    st.markdown('</div>', unsafe_allow_html=True)

    if selected != "선택 안 함":
        data = VIRTUAL_REPORTS[selected]

        st.markdown('<div class="info-card" style="padding: 10px 8px;">', unsafe_allow_html=True)
        st.markdown(f'<div class="case-title-mobile" style="font-size:0.94rem;">👤 환자 사례: {selected}</div>', unsafe_allow_html=True)
        st.markdown(
            f'<div class="case-subtitle-mobile" style="font-size:0.82rem; margin-top:2px;">연령/성별: {data["info"]["age"]}세 / {data["info"]["sex"]} | 병변측: {data["info"]["side"]}</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div class="mobile-note" style="font-size:0.8rem; line-height:1.4; color: #475569; background: #f8fafc; padding: 6px; border-radius:4px; margin-top:5px;"><b>주요 임상 증상:</b> {data["info"]["symptom"]}</div>',
            unsafe_allow_html=True
        )
        st.markdown('</div>', unsafe_allow_html=True)

        def create_responsive_table(headers, rows, table_id):
            css = f"""
            <style>
                #{table_id} {{ width: 100%; border-collapse: collapse; margin-bottom: 12px; font-size: 0.8rem; }}
                #{table_id} th {{ background-color: #f1f5f9; padding: 8px; border-bottom: 2px solid #cbd5e1; text-align: center; color: #1e293b; font-weight: 800; }}
                #{table_id} td {{ padding: 8px; border-bottom: 1px solid #e2e8f0; text-align: center; color: #334155; line-height: 1.4; }}
                #{table_id} td.left-align {{ text-align: left; font-weight: 700; color: #1e40af; }}
                @media screen and (max-width: 768px) {{
                    #{table_id} thead {{ display: none; }}
                    #{table_id} tr {{ display: block; border: 1px solid #cbd5e1; border-radius: 6px; margin-bottom: 8px; background: #fff; padding: 4px; }}
                    #{table_id} td {{ display: flex; justify-content: space-between; align-items: center; gap: 10px; border-bottom: 1px solid #f1f5f9; padding: 6px 8px; text-align: right; }}
                    #{table_id} td:last-child {{ border-bottom: none; }}
                    #{table_id} td::before {{ content: attr(data-label); font-weight: 800; color: #64748b; text-align: left; font-size:0.75rem; flex: 0 0 42%; }}
                    #{table_id} td > span {{ flex: 1; text-align: right; word-break: keep-all; }}
                    #{table_id} td.left-align {{ justify-content: center; background: #f8fafc; border-radius: 4px 4px 0 0; text-align: center; padding: 8px; }}
                    #{table_id} td.left-align::before {{ content: none; }}
                    #{table_id} td.left-align > span {{ text-align: center; }}
                }}
            </style>
            """
            tr_html = ""
            for row in rows:
                td_html = ""
                for idx, col in enumerate(row):
                    col = str(col)
                    cls = "left-align" if idx == 0 else ""
                    color_style = ""
                    if idx == len(row) - 1:
                        if "정상" in col and "비정상" not in col:
                            color_style = "color: #16a34a; font-weight:700;"
                        elif any(x in col for x in ["비정상", "침범", "확진", "마비", "소실", "감소", "지연", "Gilliatt-Sumner"]):
                            color_style = "color: #dc2626; font-weight: 800;"

                    formatted_col = col.replace(" / ", "<br/>") if "휴식" in headers[idx] else col
                    td_html += f"<td data-label='{headers[idx]}' class='{cls}' style='{color_style}'><span>{formatted_col}</span></td>"
                tr_html += f"<tr>{td_html}</tr>"
            return f'{css}<table id="{table_id}"><thead><tr>{"".join([f"<th>{h}</th>" for h in headers])}</tr></thead><tbody>{tr_html}</tbody></table>'

        st.markdown('<div class="section-card" style="padding: 10px 8px;">', unsafe_allow_html=True)
        st.markdown(
            f'<div class="case-section-label" style="font-size:0.92rem;">📋 근전도 결과표 (NCS & Needle EMG): 병변측 ({data["info"]["side"]})</div>',
            unsafe_allow_html=True
        )

        st.markdown('<div class="finding-highlight" style="font-size:0.86rem; border-bottom:none; color:#1e40af;">⚡ 감각신경전도검사 (Sensory NCS)</div>', unsafe_allow_html=True)
        st.markdown(create_responsive_table(["검사 신경", "진폭 수치", "잠복기 수치", "최종 판정"], data["ncs_sensory"], "sensory_tbl"), unsafe_allow_html=True)

        st.markdown('<div class="finding-highlight" style="font-size:0.86rem; border-bottom:none; color:#1e40af; margin-top:10px;">⚡ 운동신경전도검사 (Motor NCS)</div>', unsafe_allow_html=True)
        st.markdown(create_responsive_table(["검사 신경", "자극 위치", "진폭 수치", "잠복기 수치", "최종 판정"], data["ncs_motor"], "motor_tbl"), unsafe_allow_html=True)

        is_emg_applicable = "눈꺼풀" not in selected and "뇌졸중" not in selected
        if is_emg_applicable:
            st.markdown('<div class="finding-highlight" style="font-size:0.86rem; border-bottom:none; color:#1e40af; margin-top:10px;">🪡 침근전도검사 (Needle EMG)</div>', unsafe_allow_html=True)
            st.markdown(
                create_responsive_table(
                    ["검사 근육", "해당 분절 (Root)", "휴식 시 반응 (Rest)", "수의수축 시 반응 (Volition)", "근생리 상태 진단"],
                    data["emg"],
                    "emg_tbl"
                ),
                unsafe_allow_html=True
            )

        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="result-card" style="padding: 10px 8px;">', unsafe_allow_html=True)
        st.markdown('<div class="result-title" style="font-size:0.92rem;">✅ 임상 추론 및 생리학적 해석 결과</div>', unsafe_allow_html=True)
        st.markdown(
            f'<div class="result-text" style="font-size:0.84rem; background: #fff1f2; border: 1px solid #fecdd3; padding: 8px; border-radius:6px;"><span class="label-strong text-red" style="font-size:0.85rem; font-weight:800;">최종 교육용 진단:</span> <span style="font-weight:800; color:#9f1239; font-size:0.88rem; margin-left:4px;">{data["diagnosis"]}</span></div>',
            unsafe_allow_html=True
        )
        st.markdown('<div style="height: 10px;"></div>', unsafe_allow_html=True)

        st.markdown('<div class="result-label" style="font-size:0.85rem; padding: 4px 6px;">🧠 데이터 해석 논리</div>', unsafe_allow_html=True)
        for i in data["interpretation"]:
            st.markdown(f'<div class="finding-subtext" style="font-size:0.8rem; line-height:1.45;">• {i}</div>', unsafe_allow_html=True)

        if is_emg_applicable:
            st.markdown('<div class="result-label" style="border-left-color: #d97706; background: #fffbeb; font-size:0.85rem; padding: 4px 6px;">🔬 침근전도 소견 생리학적 의미</div>', unsafe_allow_html=True)
            for m in data["emg_meaning"]:
                parts = m.split(":", 1)
                if len(parts) == 2:
                    st.markdown(
                        f'<div class="finding-subtext" style="font-size:0.8rem; line-height:1.45;"><span class="label-strong text-blue" style="font-size:0.8rem;">{parts[0]}:</span> {parts[1]}</div>',
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(f'<div class="finding-subtext" style="font-size:0.8rem; line-height:1.45;">• {m}</div>', unsafe_allow_html=True)

        st.markdown('<div class="result-label" style="border-left-color: #9333ea; background: #fdf4ff; font-size:0.85rem; padding: 4px 6px;">🧭 감별 진단 및 추가 검사</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="finding-subtext" style="font-size:0.8rem; line-height:1.45;">• {data["ddx"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div style="text-align: center; margin-top: 15px; margin-bottom: 15px;">', unsafe_allow_html=True)
        if st.button("🔄 다른 가상 결과지 분석하기", key="reset_input_report_btn"):
            st.session_state["input_reset_counter"] += 1
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="bottom-nav-safe-space"></div>', unsafe_allow_html=True)
    render_bottom_navigation()
