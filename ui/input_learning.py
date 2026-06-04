# ui/input_learning.py

import streamlit as st

from ui.navigation import render_bottom_navigation

try:
    from formatters import html_escape
except ImportError:
    def html_escape(text):
        if text is None:
            return ""
        return (
            str(text)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&#x27;")
        )


# =============================================================================
# 가상 결과표 판독학습 데이터
# =============================================================================
# 설계 원칙
# 1. 가상 결과표 판독학습은 실제 근전도 결과표와 비슷하게 수치 중심으로 구성합니다.
# 2. 판단 열은 삭제합니다.
# 3. 감각신경전도검사와 운동신경전도검사는 자극 위치, 기록 위치, 진폭, 잠복기, 전도속도를 분리합니다.
# 4. 침근전도검사는 휴식 시 반응과 수의수축 시 운동단위동원 양상을 실제 용어로 제시합니다.
# 5. 해석 영역에서 표 읽는 법, 핵심 요약, 의심 질환, 손상 위치, 감별진단, 추가검사를 자세히 설명합니다.
# =============================================================================

VIRTUAL_REPORTS = {
    "실제형 결과표 1: 오른쪽 손목굴증후군 의심": {
        "meta": {
            "age": 52,
            "sex": "여성",
            "side": "오른쪽",
            "chief": "오른쪽 엄지, 검지, 중지 저림과 야간 통증. 손목 굽힘 시 증상 악화.",
            "clinical_hint": "정중신경 분포 감각 이상과 엄지두덩 약화가 의심되는 사례입니다.",
        },
        "diagnosis": "오른쪽 손목굴증후군(Carpal tunnel syndrome), 정중신경 손목 부위 포착성 신경병증",
        "lesion": "오른쪽 손목굴 부위의 정중신경 원위부 감각 및 운동섬유",
        "sensory_ncs": [
            {
                "nerve": "정중신경 감각신경활동전위(Median SNAP)",
                "recording": "검지",
                "stimulation": "손목",
                "side": "우측",
                "amplitude": "7 μV",
                "latency": "4.6 ms",
                "velocity": "32 m/s",
            },
            {
                "nerve": "정중신경 감각신경활동전위(Median SNAP)",
                "recording": "검지",
                "stimulation": "손목",
                "side": "좌측",
                "amplitude": "24 μV",
                "latency": "2.8 ms",
                "velocity": "51 m/s",
            },
            {
                "nerve": "자신경 감각신경활동전위(Ulnar SNAP)",
                "recording": "새끼손가락",
                "stimulation": "손목",
                "side": "우측",
                "amplitude": "23 μV",
                "latency": "2.6 ms",
                "velocity": "54 m/s",
            },
        ],
        "motor_ncs": [
            {
                "nerve": "정중신경 복합근육활동전위(Median CMAP)",
                "recording": "짧은엄지벌림근(APB)",
                "stimulation": "손목",
                "side": "우측",
                "amplitude": "3.0 mV",
                "latency": "5.8 ms",
                "velocity": "-",
            },
            {
                "nerve": "정중신경 복합근육활동전위(Median CMAP)",
                "recording": "짧은엄지벌림근(APB)",
                "stimulation": "팔꿈치",
                "side": "우측",
                "amplitude": "2.8 mV",
                "latency": "10.2 ms",
                "velocity": "48 m/s",
            },
            {
                "nerve": "정중신경 복합근육활동전위(Median CMAP)",
                "recording": "짧은엄지벌림근(APB)",
                "stimulation": "손목",
                "side": "좌측",
                "amplitude": "8.4 mV",
                "latency": "3.4 ms",
                "velocity": "-",
            },
            {
                "nerve": "자신경 복합근육활동전위(Ulnar CMAP)",
                "recording": "새끼벌림근(ADM)",
                "stimulation": "손목",
                "side": "우측",
                "amplitude": "8.8 mV",
                "latency": "2.7 ms",
                "velocity": "-",
            },
        ],
        "needle_emg": [
            {
                "muscle": "짧은엄지벌림근(APB)",
                "root": "C8-T1",
                "nerve": "정중신경",
                "rest": "fibrillation potential, positive sharp wave",
                "volition": "Reduced MU recruitment",
            },
            {
                "muscle": "첫째등쪽뼈사이근(FDI)",
                "root": "C8-T1",
                "nerve": "자신경",
                "rest": "Silent at rest",
                "volition": "Normal MU recruitment",
            },
            {
                "muscle": "목 척추주위근(Cervical paraspinal)",
                "root": "C8-T1",
                "nerve": "후지",
                "rest": "Silent at rest",
                "volition": "평가 제한",
            },
        ],
        "interpretation": {
            "sensory": [
                "오른쪽 정중신경 감각신경활동전위는 정상측에 비해 진폭이 크게 낮고 잠복기가 길며 전도속도가 느립니다.",
                "반면 오른쪽 자신경 감각신경활동전위는 비교적 보존되어 있어, 병변이 손 전체의 다발성 신경병증이라기보다 정중신경 영역에 국한됨을 시사합니다.",
                "감각신경 이상이 손목 부위 정중신경 분포에 집중되어 있으므로 손목굴 부위 포착성 병변을 우선 의심합니다.",
            ],
            "motor": [
                "오른쪽 정중신경 운동반응은 손목 자극에서 원위잠복기가 뚜렷하게 지연되어 있습니다.",
                "오른쪽 정중신경 CMAP 진폭도 정상측보다 낮아 단순 말이집탈락성 지연뿐 아니라 운동축삭 손상 가능성이 동반됩니다.",
                "자신경 운동반응은 보존되어 있어 C8-T1 신경뿌리병증이나 하부상완신경총 병변보다는 정중신경 단일신경병증에 더 부합합니다.",
            ],
            "emg": [
                "짧은엄지벌림근에서 휴식 시 fibrillation potential과 positive sharp wave가 관찰되어 정중신경 지배 근육의 활동성 탈신경을 시사합니다.",
                "첫째등쪽뼈사이근과 목 척추주위근은 보존되어 있어 자신경 병변이나 C8-T1 신경뿌리병증 가능성은 낮아집니다.",
            ],
            "integration": [
                "증상 분포, 정중신경 감각·운동전도 지연, 짧은엄지벌림근의 탈신경 소견을 종합하면 오른쪽 손목굴증후군이 가장 타당합니다.",
                "정상측 대비 정중신경 진폭 감소가 뚜렷하므로 단순 경도 포착보다는 축삭 손상이 동반된 중등도 이상의 병변으로 교육적으로 해석할 수 있습니다.",
            ],
            "differential": [
                "C6 또는 C8 신경뿌리병증: 감각신경활동전위가 보존되는 경우가 많고, 목 척추주위근 또는 같은 분절의 여러 말초신경 지배 근육 이상이 동반될 수 있습니다.",
                "당뇨병성 다발신경병증: 여러 감각신경이 대칭적으로 감소하는 양상이 흔합니다.",
                "하부상완신경총병증: 정중신경뿐 아니라 자신경, 안쪽아래팔피부신경 등의 이상이 함께 나타날 수 있습니다.",
            ],
            "additional": [
                "손목굴 초음파 또는 신경초음파로 정중신경 단면적 증가 여부를 확인할 수 있습니다.",
                "야간 보조기, 손목 자세 교육, 정중신경 활주운동, 증상 지속 시 전문의 협진을 고려합니다.",
            ],
        },
    },

    "실제형 결과표 2: 왼쪽 C6 신경뿌리병증 의심": {
        "meta": {
            "age": 45,
            "sex": "남성",
            "side": "왼쪽",
            "chief": "왼쪽 목 통증, 어깨와 위팔 가쪽 통증, 엄지와 검지 저림. 팔꿉관절 굽힘 약화.",
            "clinical_hint": "감각신경전도는 보존되지만 C6 분절 근육 침근전도 이상이 관찰되는 사례입니다.",
        },
        "diagnosis": "왼쪽 C6 목 신경뿌리병증(C6 cervical radiculopathy)",
        "lesion": "왼쪽 C6 신경뿌리, 뒤뿌리신경절보다 몸쪽 병변",
        "sensory_ncs": [
            {
                "nerve": "정중신경 감각신경활동전위(Median SNAP)",
                "recording": "검지",
                "stimulation": "손목",
                "side": "좌측",
                "amplitude": "26 μV",
                "latency": "2.9 ms",
                "velocity": "52 m/s",
            },
            {
                "nerve": "노신경 표재감각신경활동전위(Superficial radial SNAP)",
                "recording": "손등 노쪽",
                "stimulation": "아래팔",
                "side": "좌측",
                "amplitude": "21 μV",
                "latency": "2.5 ms",
                "velocity": "53 m/s",
            },
            {
                "nerve": "자신경 감각신경활동전위(Ulnar SNAP)",
                "recording": "새끼손가락",
                "stimulation": "손목",
                "side": "좌측",
                "amplitude": "24 μV",
                "latency": "2.6 ms",
                "velocity": "55 m/s",
            },
        ],
        "motor_ncs": [
            {
                "nerve": "정중신경 복합근육활동전위(Median CMAP)",
                "recording": "짧은엄지벌림근(APB)",
                "stimulation": "손목",
                "side": "좌측",
                "amplitude": "8.6 mV",
                "latency": "3.5 ms",
                "velocity": "-",
            },
            {
                "nerve": "정중신경 복합근육활동전위(Median CMAP)",
                "recording": "짧은엄지벌림근(APB)",
                "stimulation": "팔꿈치",
                "side": "좌측",
                "amplitude": "8.1 mV",
                "latency": "7.7 ms",
                "velocity": "54 m/s",
            },
            {
                "nerve": "노신경 복합근육활동전위(Radial CMAP)",
                "recording": "손목폄근",
                "stimulation": "아래팔",
                "side": "좌측",
                "amplitude": "6.7 mV",
                "latency": "2.9 ms",
                "velocity": "-",
            },
        ],
        "needle_emg": [
            {
                "muscle": "위팔두갈래근(Biceps brachii)",
                "root": "C5-C6",
                "nerve": "근육피부신경",
                "rest": "fibrillation potential, positive sharp wave",
                "volition": "Reduced MU recruitment",
            },
            {
                "muscle": "노쪽손목폄근(Extensor carpi radialis)",
                "root": "C6-C7",
                "nerve": "노신경",
                "rest": "fibrillation potential, positive sharp wave",
                "volition": "Giant MUAPs with reduced recruitment",
            },
            {
                "muscle": "삼각근(Deltoid)",
                "root": "C5-C6",
                "nerve": "겨드랑신경",
                "rest": "Silent at rest",
                "volition": "Mildly reduced MU recruitment",
            },
            {
                "muscle": "짧은엄지벌림근(APB)",
                "root": "C8-T1",
                "nerve": "정중신경",
                "rest": "Silent at rest",
                "volition": "Normal MU recruitment",
            },
            {
                "muscle": "목 척추주위근(Cervical paraspinal)",
                "root": "C6",
                "nerve": "후지",
                "rest": "fibrillation potential, positive sharp wave",
                "volition": "평가 제한",
            },
        ],
        "interpretation": {
            "sensory": [
                "정중신경, 노신경 표재감각분지, 자신경 감각신경활동전위가 모두 보존되어 있습니다.",
                "환자는 엄지와 검지 저림을 호소하지만 SNAP가 보존되어 있으므로 병변이 말초 감각신경 자체보다 뒤뿌리신경절보다 몸쪽, 즉 신경뿌리 수준일 가능성이 커집니다.",
            ],
            "motor": [
                "운동신경전도검사에서 원위부 말초신경의 뚜렷한 전도차단이나 원위잠복기 지연이 관찰되지 않습니다.",
                "이는 손목굴증후군이나 노신경 단일 포착병변보다는 신경뿌리병증 가능성을 높입니다.",
            ],
            "emg": [
                "위팔두갈래근과 노쪽손목폄근처럼 서로 다른 말초신경 지배를 받지만 C6 분절을 공유하는 근육에서 탈신경 소견이 나타납니다.",
                "목 척추주위근에서도 비정상 자발전위가 관찰되므로 신경얼기병증보다는 신경뿌리병증을 더 강하게 지지합니다.",
                "C8-T1 지배인 짧은엄지벌림근은 정상으로 보존되어 병변 분절이 C6 중심임을 뒷받침합니다.",
            ],
            "integration": [
                "감각신경전도 보존, 말초 운동전도 보존, C6 분절 근육과 목 척추주위근의 탈신경 소견을 종합하면 왼쪽 C6 신경뿌리병증이 가장 적절합니다.",
                "침근전도에서 활동성 탈신경과 만성 재신경지배 소견이 함께 관찰되므로 급성 악화가 만성 병변 위에 겹친 양상으로 교육적으로 해석할 수 있습니다.",
            ],
            "differential": [
                "손목굴증후군: 정중신경 SNAP와 CMAP의 손목 부위 지연이 주로 관찰됩니다.",
                "노신경병증: 노신경 지배 근육과 노신경 감각분지 이상이 함께 나타날 수 있으나 목 척추주위근 이상은 일반적으로 설명하기 어렵습니다.",
                "상완신경총병증: 감각신경활동전위 감소가 동반될 수 있으며, 목 척추주위근은 보존되는 경우가 많습니다.",
            ],
            "additional": [
                "경추 MRI로 C5-6 또는 C6 신경뿌리 압박 여부를 확인합니다.",
                "Spurling test, 경추 신경학적 검사, 상지 근력·반사 평가를 함께 시행합니다.",
            ],
        },
    },

    "실제형 결과표 3: 오른쪽 온종아리신경병증 의심": {
        "meta": {
            "age": 32,
            "sex": "남성",
            "side": "오른쪽",
            "chief": "다리를 오래 꼬고 앉은 뒤 오른쪽 발처짐 발생. 발등과 종아리 가쪽 감각 저하.",
            "clinical_hint": "종아리뼈머리 부위 전도차단과 얕은종아리신경 감각반응 감소를 확인하는 사례입니다.",
        },
        "diagnosis": "오른쪽 온종아리신경병증(Common peroneal neuropathy), 종아리뼈머리 부위 병변",
        "lesion": "오른쪽 종아리뼈머리 주변 온종아리신경",
        "sensory_ncs": [
            {
                "nerve": "얕은종아리신경 감각신경활동전위(Superficial peroneal SNAP)",
                "recording": "발등",
                "stimulation": "종아리 가쪽",
                "side": "우측",
                "amplitude": "4 μV",
                "latency": "3.6 ms",
                "velocity": "36 m/s",
            },
            {
                "nerve": "얕은종아리신경 감각신경활동전위(Superficial peroneal SNAP)",
                "recording": "발등",
                "stimulation": "종아리 가쪽",
                "side": "좌측",
                "amplitude": "14 μV",
                "latency": "2.8 ms",
                "velocity": "48 m/s",
            },
            {
                "nerve": "장딴지신경 감각신경활동전위(Sural SNAP)",
                "recording": "가쪽 발목",
                "stimulation": "종아리 뒤쪽",
                "side": "우측",
                "amplitude": "16 μV",
                "latency": "3.0 ms",
                "velocity": "47 m/s",
            },
        ],
        "motor_ncs": [
            {
                "nerve": "종아리신경 복합근육활동전위(Peroneal CMAP)",
                "recording": "짧은발가락폄근(EDB)",
                "stimulation": "발목",
                "side": "우측",
                "amplitude": "4.8 mV",
                "latency": "4.4 ms",
                "velocity": "-",
            },
            {
                "nerve": "종아리신경 복합근육활동전위(Peroneal CMAP)",
                "recording": "짧은발가락폄근(EDB)",
                "stimulation": "종아리뼈머리 아래",
                "side": "우측",
                "amplitude": "4.4 mV",
                "latency": "9.1 ms",
                "velocity": "45 m/s",
            },
            {
                "nerve": "종아리신경 복합근육활동전위(Peroneal CMAP)",
                "recording": "짧은발가락폄근(EDB)",
                "stimulation": "종아리뼈머리 위",
                "side": "우측",
                "amplitude": "1.5 mV",
                "latency": "12.8 ms",
                "velocity": "25 m/s",
            },
            {
                "nerve": "정강신경 복합근육활동전위(Tibial CMAP)",
                "recording": "엄지벌림근(AH)",
                "stimulation": "발목",
                "side": "우측",
                "amplitude": "8.1 mV",
                "latency": "4.1 ms",
                "velocity": "-",
            },
        ],
        "needle_emg": [
            {
                "muscle": "앞정강근(Tibialis anterior)",
                "root": "L4-L5",
                "nerve": "깊은종아리신경",
                "rest": "fibrillation potential, positive sharp wave",
                "volition": "Reduced MU recruitment",
            },
            {
                "muscle": "긴종아리근(Peroneus longus)",
                "root": "L5-S1",
                "nerve": "얕은종아리신경",
                "rest": "fibrillation potential, positive sharp wave",
                "volition": "Reduced MU recruitment",
            },
            {
                "muscle": "가자미근(Soleus)",
                "root": "S1-S2",
                "nerve": "정강신경",
                "rest": "Silent at rest",
                "volition": "Normal MU recruitment",
            },
            {
                "muscle": "허리 척추주위근(Lumbar paraspinal)",
                "root": "L5",
                "nerve": "후지",
                "rest": "Silent at rest",
                "volition": "평가 제한",
            },
        ],
        "interpretation": {
            "sensory": [
                "오른쪽 얕은종아리신경 SNAP 진폭이 정상측보다 크게 감소해 종아리신경 감각섬유 침범을 시사합니다.",
                "장딴지신경 SNAP는 보존되어 있어 더 광범위한 좌골신경병증이나 다발신경병증보다는 종아리신경 영역의 국소 병변에 가깝습니다.",
            ],
            "motor": [
                "종아리신경 운동검사에서 종아리뼈머리 위 자극 시 CMAP 진폭이 종아리뼈머리 아래 자극보다 현저히 감소합니다.",
                "이는 종아리뼈머리 부위에서 전기 자극 전달이 차단되는 전도차단 양상으로 해석할 수 있습니다.",
                "정강신경 운동반응은 보존되어 있어 좌골신경 전체 병변 가능성은 낮아집니다.",
            ],
            "emg": [
                "앞정강근과 긴종아리근은 모두 종아리신경 계열 근육이며 탈신경 소견이 있습니다.",
                "정강신경 지배 근육인 가자미근과 허리 척추주위근은 정상으로, L5 신경뿌리병증보다는 말초 종아리신경병증을 지지합니다.",
            ],
            "integration": [
                "발처짐, 얕은종아리신경 감각반응 감소, 종아리뼈머리 부위 전도차단, 종아리신경 지배 근육의 탈신경 소견을 종합하면 오른쪽 온종아리신경병증이 가장 타당합니다.",
                "병변 위치는 종아리뼈머리 주변으로 추정됩니다.",
            ],
            "differential": [
                "L5 신경뿌리병증: 얕은종아리신경 SNAP가 보존되는 경우가 많고, 허리 척추주위근 또는 중간볼기근 이상이 동반될 수 있습니다.",
                "좌골신경병증: 종아리신경뿐 아니라 정강신경 지배 근육도 침범될 수 있습니다.",
                "길이의존성 다발신경병증: 양측성, 대칭성, 원위부 감각신경 감소가 흔합니다.",
            ],
            "additional": [
                "종아리뼈머리 부위 압박 요인, 다리 꼬기 습관, 보조기 착용 여부를 확인합니다.",
                "발처짐이 뚜렷하면 단기적으로 AFO 적용과 낙상 예방 교육이 필요합니다.",
                "필요 시 신경초음파 또는 무릎 주변 영상검사를 고려합니다.",
            ],
        },
    },

    "실제형 결과표 4: 왼쪽 L5 신경뿌리병증 의심": {
        "meta": {
            "age": 58,
            "sex": "여성",
            "side": "왼쪽",
            "chief": "왼쪽 허리 통증과 발등 저림. 엄지발가락 폄과 발목 등굽힘 약화.",
            "clinical_hint": "감각신경전도는 보존되지만 L5 분절 근육과 허리 척추주위근 이상이 관찰되는 사례입니다.",
        },
        "diagnosis": "왼쪽 L5 허리 신경뿌리병증(L5 lumbar radiculopathy)",
        "lesion": "왼쪽 L5 신경뿌리, 뒤뿌리신경절보다 몸쪽 병변",
        "sensory_ncs": [
            {
                "nerve": "얕은종아리신경 감각신경활동전위(Superficial peroneal SNAP)",
                "recording": "발등",
                "stimulation": "종아리 가쪽",
                "side": "좌측",
                "amplitude": "13 μV",
                "latency": "2.9 ms",
                "velocity": "47 m/s",
            },
            {
                "nerve": "장딴지신경 감각신경활동전위(Sural SNAP)",
                "recording": "가쪽 발목",
                "stimulation": "종아리 뒤쪽",
                "side": "좌측",
                "amplitude": "15 μV",
                "latency": "3.1 ms",
                "velocity": "46 m/s",
            },
        ],
        "motor_ncs": [
            {
                "nerve": "종아리신경 복합근육활동전위(Peroneal CMAP)",
                "recording": "짧은발가락폄근(EDB)",
                "stimulation": "발목",
                "side": "좌측",
                "amplitude": "3.9 mV",
                "latency": "4.5 ms",
                "velocity": "-",
            },
            {
                "nerve": "종아리신경 복합근육활동전위(Peroneal CMAP)",
                "recording": "짧은발가락폄근(EDB)",
                "stimulation": "종아리뼈머리",
                "side": "좌측",
                "amplitude": "3.7 mV",
                "latency": "10.5 ms",
                "velocity": "44 m/s",
            },
            {
                "nerve": "정강신경 복합근육활동전위(Tibial CMAP)",
                "recording": "엄지벌림근(AH)",
                "stimulation": "발목",
                "side": "좌측",
                "amplitude": "7.4 mV",
                "latency": "4.2 ms",
                "velocity": "-",
            },
        ],
        "needle_emg": [
            {
                "muscle": "앞정강근(Tibialis anterior)",
                "root": "L4-L5",
                "nerve": "깊은종아리신경",
                "rest": "fibrillation potential, positive sharp wave",
                "volition": "Reduced MU recruitment",
            },
            {
                "muscle": "긴엄지폄근(Extensor hallucis longus)",
                "root": "L5",
                "nerve": "깊은종아리신경",
                "rest": "fibrillation potential, positive sharp wave",
                "volition": "Reduced MU recruitment",
            },
            {
                "muscle": "중간볼기근(Gluteus medius)",
                "root": "L5",
                "nerve": "위볼기신경",
                "rest": "fibrillation potential, positive sharp wave",
                "volition": "Reduced MU recruitment",
            },
            {
                "muscle": "가자미근(Soleus)",
                "root": "S1-S2",
                "nerve": "정강신경",
                "rest": "Silent at rest",
                "volition": "Normal MU recruitment",
            },
            {
                "muscle": "허리 척추주위근(Lumbar paraspinal)",
                "root": "L5",
                "nerve": "후지",
                "rest": "fibrillation potential, positive sharp wave",
                "volition": "평가 제한",
            },
        ],
        "interpretation": {
            "sensory": [
                "얕은종아리신경과 장딴지신경 SNAP가 보존되어 있습니다.",
                "발등 저림이 있어도 감각신경활동전위가 보존되면 병변이 말초 감각신경 원위부보다 뒤뿌리신경절보다 몸쪽에 있을 가능성을 고려합니다.",
            ],
            "motor": [
                "종아리신경 운동검사에서 종아리뼈머리 부위 전도차단이 뚜렷하지 않습니다.",
                "정강신경 운동반응도 보존되어 있어 말초 단일신경병증이나 다발신경병증 가능성은 낮아집니다.",
            ],
            "emg": [
                "앞정강근, 긴엄지폄근, 중간볼기근처럼 서로 다른 말초신경 지배를 받지만 L5 분절을 공유하는 근육에서 탈신경 소견이 관찰됩니다.",
                "허리 척추주위근에서도 비정상 자발전위가 나타나 신경뿌리병증을 강하게 지지합니다.",
                "S1 지배가 우세한 가자미근은 정상으로 보존되어 병변 중심이 L5임을 뒷받침합니다.",
            ],
            "integration": [
                "감각신경전도 보존, 말초 운동전도 보존, L5 분절 근육과 허리 척추주위근 탈신경을 종합하면 왼쪽 L5 신경뿌리병증이 가장 타당합니다.",
                "온종아리신경병증과 달리 중간볼기근과 허리 척추주위근 이상이 함께 나타나는 점이 중요한 감별 포인트입니다.",
            ],
            "differential": [
                "온종아리신경병증: 얕은종아리신경 SNAP 감소와 종아리뼈머리 부위 전도차단이 흔합니다.",
                "좌골신경병증: 종아리신경과 정강신경 지배 근육이 함께 침범될 수 있습니다.",
                "말초 다발신경병증: 양측성 감각신경 진폭 감소가 흔합니다.",
            ],
            "additional": [
                "요추 MRI로 L4-5 또는 L5-S1 추간판 탈출과 L5 신경뿌리 압박 여부를 확인합니다.",
                "SLR test, 하지 근력검사, 감각검사, 보행분석을 함께 시행합니다.",
            ],
        },
    },

    "실제형 결과표 5: 길이의존성 축삭성 다발신경병증 의심": {
        "meta": {
            "age": 68,
            "sex": "남성",
            "side": "양측",
            "chief": "양측 발끝부터 시작된 저림과 화끈거림. 밤에 악화되며 균형감 저하 동반.",
            "clinical_hint": "양측 원위부 감각신경과 운동신경 진폭 감소를 통해 길이의존성 축삭 손상을 해석하는 사례입니다.",
        },
        "diagnosis": "길이의존성 축삭성 감각운동 다발신경병증(Length-dependent axonal sensorimotor polyneuropathy)",
        "lesion": "양측 하지 원위부 말초신경 축삭, 긴 신경부터 우세하게 침범",
        "sensory_ncs": [
            {
                "nerve": "장딴지신경 감각신경활동전위(Sural SNAP)",
                "recording": "가쪽 발목",
                "stimulation": "종아리 뒤쪽",
                "side": "우측",
                "amplitude": "반응 소실",
                "latency": "반응 소실",
                "velocity": "반응 소실",
            },
            {
                "nerve": "장딴지신경 감각신경활동전위(Sural SNAP)",
                "recording": "가쪽 발목",
                "stimulation": "종아리 뒤쪽",
                "side": "좌측",
                "amplitude": "반응 소실",
                "latency": "반응 소실",
                "velocity": "반응 소실",
            },
            {
                "nerve": "얕은종아리신경 감각신경활동전위(Superficial peroneal SNAP)",
                "recording": "발등",
                "stimulation": "종아리 가쪽",
                "side": "우측",
                "amplitude": "3 μV",
                "latency": "3.9 ms",
                "velocity": "33 m/s",
            },
            {
                "nerve": "정중신경 감각신경활동전위(Median SNAP)",
                "recording": "검지",
                "stimulation": "손목",
                "side": "우측",
                "amplitude": "18 μV",
                "latency": "3.2 ms",
                "velocity": "48 m/s",
            },
        ],
        "motor_ncs": [
            {
                "nerve": "정강신경 복합근육활동전위(Tibial CMAP)",
                "recording": "엄지벌림근(AH)",
                "stimulation": "발목",
                "side": "우측",
                "amplitude": "1.4 mV",
                "latency": "5.9 ms",
                "velocity": "-",
            },
            {
                "nerve": "정강신경 복합근육활동전위(Tibial CMAP)",
                "recording": "엄지벌림근(AH)",
                "stimulation": "오금",
                "side": "우측",
                "amplitude": "1.1 mV",
                "latency": "15.5 ms",
                "velocity": "34 m/s",
            },
            {
                "nerve": "종아리신경 복합근육활동전위(Peroneal CMAP)",
                "recording": "짧은발가락폄근(EDB)",
                "stimulation": "발목",
                "side": "우측",
                "amplitude": "1.0 mV",
                "latency": "5.6 ms",
                "velocity": "-",
            },
            {
                "nerve": "정중신경 복합근육활동전위(Median CMAP)",
                "recording": "짧은엄지벌림근(APB)",
                "stimulation": "손목",
                "side": "우측",
                "amplitude": "7.6 mV",
                "latency": "3.8 ms",
                "velocity": "-",
            },
        ],
        "needle_emg": [
            {
                "muscle": "앞정강근(Tibialis anterior)",
                "root": "L4-L5",
                "nerve": "깊은종아리신경",
                "rest": "fibrillation potential, positive sharp wave",
                "volition": "Reduced MU recruitment",
            },
            {
                "muscle": "짧은발가락벌림근(Abductor digiti minimi pedis)",
                "root": "S1-S2",
                "nerve": "발바닥신경",
                "rest": "fibrillation potential, positive sharp wave",
                "volition": "Markedly reduced MU recruitment",
            },
            {
                "muscle": "가쪽넓은근(Vastus lateralis)",
                "root": "L2-L4",
                "nerve": "넓적다리신경",
                "rest": "Silent at rest",
                "volition": "Normal MU recruitment",
            },
            {
                "muscle": "위팔두갈래근(Biceps brachii)",
                "root": "C5-C6",
                "nerve": "근육피부신경",
                "rest": "Silent at rest",
                "volition": "Normal MU recruitment",
            },
        ],
        "interpretation": {
            "sensory": [
                "양측 장딴지신경 SNAP가 반응 소실되어 하지 원위부 감각축삭 손상이 뚜렷합니다.",
                "얕은종아리신경 감각반응도 낮지만, 상지 정중신경 감각반응은 상대적으로 보존되어 있습니다.",
                "이는 신경 길이가 긴 하지 원위부부터 손상되는 길이의존성 양상과 잘 맞습니다.",
            ],
            "motor": [
                "정강신경과 종아리신경 CMAP 진폭이 낮아 운동축삭 침범이 동반됩니다.",
                "전도속도 저하가 일부 있지만, 핵심은 광범위한 진폭 감소이므로 축삭성 다발신경병증으로 해석하는 것이 적절합니다.",
            ],
            "emg": [
                "원위 하지 근육에서 탈신경 소견이 관찰되며, 근위 하지와 상지 근육은 상대적으로 보존됩니다.",
                "이러한 원위부 우세 양상은 dying-back 형태의 길이의존성 축삭 손상과 부합합니다.",
            ],
            "integration": [
                "양측성, 대칭성, 원위부 우세 감각·운동 진폭 감소와 원위 하지 침근전도 이상을 종합하면 길이의존성 축삭성 감각운동 다발신경병증이 가장 타당합니다.",
                "당뇨병, 신장질환, 알코올, 영양결핍, 약물성 신경병증 등을 원인으로 감별해야 합니다.",
            ],
            "differential": [
                "요추 신경뿌리병증: 특정 분절 근육과 척추주위근 이상이 두드러지며 감각신경활동전위는 보존될 수 있습니다.",
                "단일 말초신경병증: 한 신경 영역에 국한된 전도 이상이 주로 나타납니다.",
                "탈말이집성 다발신경병증: 전도속도 저하, 원위잠복기 지연, 전도차단이 더 두드러집니다.",
            ],
            "additional": [
                "혈당, HbA1c, 비타민 B12, 갑상샘기능, 신장기능, 약물력, 음주력 평가가 필요합니다.",
                "물리치료에서는 발 보호, 균형훈련, 낙상 예방, 감각저하 부위 압박 예방 교육이 중요합니다.",
            ],
        },
    },

    "실제형 결과표 6: 급성 탈말이집성 다발신경뿌리병증 의심": {
        "meta": {
            "age": 41,
            "sex": "여성",
            "side": "양측",
            "chief": "장염 후 2주 뒤부터 양측 하지 근력저하가 상행. 심부건반사 저하.",
            "clinical_hint": "전도속도 저하, 원위잠복기 지연, F파 이상을 통해 탈말이집성 다발신경뿌리병증을 해석하는 사례입니다.",
        },
        "diagnosis": "급성 염증성 탈말이집성 다발신경뿌리병증(AIDP, Guillain-Barre syndrome spectrum)",
        "lesion": "다발 말초신경 및 근위부 신경뿌리의 탈말이집성 병변",
        "sensory_ncs": [
            {
                "nerve": "정중신경 감각신경활동전위(Median SNAP)",
                "recording": "검지",
                "stimulation": "손목",
                "side": "우측",
                "amplitude": "18 μV",
                "latency": "3.8 ms",
                "velocity": "39 m/s",
            },
            {
                "nerve": "자신경 감각신경활동전위(Ulnar SNAP)",
                "recording": "새끼손가락",
                "stimulation": "손목",
                "side": "우측",
                "amplitude": "16 μV",
                "latency": "3.6 ms",
                "velocity": "38 m/s",
            },
            {
                "nerve": "장딴지신경 감각신경활동전위(Sural SNAP)",
                "recording": "가쪽 발목",
                "stimulation": "종아리 뒤쪽",
                "side": "우측",
                "amplitude": "14 μV",
                "latency": "3.2 ms",
                "velocity": "45 m/s",
            },
        ],
        "motor_ncs": [
            {
                "nerve": "종아리신경 복합근육활동전위(Peroneal CMAP)",
                "recording": "짧은발가락폄근(EDB)",
                "stimulation": "발목",
                "side": "우측",
                "amplitude": "3.0 mV",
                "latency": "8.4 ms",
                "velocity": "-",
            },
            {
                "nerve": "종아리신경 복합근육활동전위(Peroneal CMAP)",
                "recording": "짧은발가락폄근(EDB)",
                "stimulation": "종아리뼈머리",
                "side": "우측",
                "amplitude": "2.4 mV",
                "latency": "18.9 ms",
                "velocity": "28 m/s",
            },
            {
                "nerve": "정강신경 복합근육활동전위(Tibial CMAP)",
                "recording": "엄지벌림근(AH)",
                "stimulation": "발목",
                "side": "우측",
                "amplitude": "3.5 mV",
                "latency": "7.2 ms",
                "velocity": "-",
            },
            {
                "nerve": "정중신경 복합근육활동전위(Median CMAP)",
                "recording": "짧은엄지벌림근(APB)",
                "stimulation": "손목",
                "side": "우측",
                "amplitude": "5.6 mV",
                "latency": "5.9 ms",
                "velocity": "-",
            },
        ],
        "late_response": [
            {
                "test": "정강신경 F파(Tibial F-wave)",
                "side": "우측",
                "latency": "소실",
                "amplitude": "-",
            },
            {
                "test": "정강신경 F파(Tibial F-wave)",
                "side": "좌측",
                "latency": "소실",
                "amplitude": "-",
            },
            {
                "test": "H-반사(H-reflex)",
                "side": "우측",
                "latency": "지연",
                "amplitude": "감소",
            },
        ],
        "needle_emg": [
            {
                "muscle": "앞정강근(Tibialis anterior)",
                "root": "L4-L5",
                "nerve": "깊은종아리신경",
                "rest": "Silent at rest",
                "volition": "Reduced MU recruitment",
            },
            {
                "muscle": "가자미근(Soleus)",
                "root": "S1-S2",
                "nerve": "정강신경",
                "rest": "Silent at rest",
                "volition": "Reduced MU recruitment",
            },
            {
                "muscle": "허리 척추주위근(Lumbar paraspinal)",
                "root": "L5-S1",
                "nerve": "후지",
                "rest": "Silent at rest",
                "volition": "평가 제한",
            },
        ],
        "interpretation": {
            "sensory": [
                "상지 감각신경에서 잠복기 지연과 전도속도 저하가 관찰되지만, 장딴지신경은 상대적으로 보존되어 있습니다.",
                "이러한 sural sparing 양상은 급성 탈말이집성 다발신경뿌리병증에서 교육적으로 중요한 단서가 될 수 있습니다.",
            ],
            "motor": [
                "여러 운동신경에서 원위잠복기가 길고 전도속도가 느려져 있습니다.",
                "진폭 감소보다 잠복기 지연과 전도속도 저하가 두드러지므로 축삭성 병변보다 탈말이집성 병변을 우선 고려합니다.",
            ],
            "emg": [
                "침근전도에서 휴식 시 비정상 자발전위가 뚜렷하지 않을 수 있습니다.",
                "수의수축 시 운동단위동원 감소는 말초신경 전도 장애로 실제 수축에 참여하는 운동단위가 줄어든 결과로 해석할 수 있습니다.",
            ],
            "integration": [
                "급성 상행성 근력저하, 반사 저하, 다발 운동신경의 탈말이집성 전도 이상, F파 소실을 종합하면 AIDP 또는 Guillain-Barre syndrome spectrum을 의심해야 합니다.",
                "F파 소실은 원위부뿐 아니라 근위부 신경뿌리 전도 이상이 있음을 시사합니다.",
            ],
            "differential": [
                "축삭성 다발신경병증: 진폭 감소가 더 핵심이며 대개 만성 또는 아급성 경과가 많습니다.",
                "척수병증: 감각수준, 병적반사, 배뇨장애 등이 동반될 수 있으며 NCS 양상과 다릅니다.",
                "중증근무력증: 반복신경자극검사나 임상 양상이 다르며 감각신경전도 이상은 설명하기 어렵습니다.",
            ],
            "additional": [
                "호흡근 약화 가능성이 있으므로 폐활량, 산소포화도, 삼킴 기능을 모니터링해야 합니다.",
                "신경과 협진, 뇌척수액 검사, 면역치료 여부 판단이 필요합니다.",
                "물리치료에서는 피로 조절, 호흡관리, 관절가동범위 유지, 안전한 이동훈련이 중요합니다.",
            ],
        },
    },
}


# =============================================================================
# 화면 렌더링 유틸 함수
# =============================================================================

def _value_class(value):
    text = str(value)

    abnormal_tokens = [
        "반응 소실",
        "소실",
        "지연",
        "감소",
        "느림",
        "fibrillation",
        "positive sharp",
        "Reduced",
        "Markedly reduced",
        "No MUAP",
        "Giant",
        "전도차단",
    ]

    normal_tokens = [
        "Silent at rest",
        "Normal",
        "정상",
        "보존",
    ]

    if any(token in text for token in abnormal_tokens):
        return "text-red"

    if any(token in text for token in normal_tokens):
        return "text-blue"

    return "text-normal"


def _render_mobile_table(headers, rows, table_id):
    """
    모바일에서 카드형으로 접히는 반응형 표를 생성합니다.
    판단 열 없이 결과표 수치 자체만 제시합니다.
    """
    safe_table_id = html_escape(table_id)

    css = f"""
    <style>
        #{safe_table_id} {{
            width: 100%;
            border-collapse: collapse;
            margin: 0.55rem 0 1rem 0;
            font-size: 0.84rem;
            background: #ffffff;
        }}

        #{safe_table_id} th {{
            background-color: #f1f5f9;
            padding: 0.62rem 0.5rem;
            border: 1px solid #cbd5e1;
            text-align: center;
            color: #0f172a;
            font-weight: 850;
            line-height: 1.35;
        }}

        #{safe_table_id} td {{
            padding: 0.58rem 0.5rem;
            border: 1px solid #e2e8f0;
            text-align: center;
            color: #334155;
            line-height: 1.45;
            vertical-align: middle;
        }}

        #{safe_table_id} td.left-align {{
            text-align: left;
            font-weight: 800;
            color: #1e3a8a;
        }}

        @media screen and (max-width: 700px) {{
            #{safe_table_id} thead {{
                display: none;
            }}

            #{safe_table_id} tr {{
                display: block;
                border: 1px solid #dbeafe;
                border-radius: 10px;
                margin-bottom: 0.8rem;
                background: #ffffff;
                overflow: hidden;
            }}

            #{safe_table_id} td {{
                display: flex;
                justify-content: space-between;
                align-items: flex-start;
                gap: 0.75rem;
                border: none;
                border-bottom: 1px solid #f1f5f9;
                padding: 0.55rem 0.65rem;
                text-align: right;
            }}

            #{safe_table_id} td:last-child {{
                border-bottom: none;
            }}

            #{safe_table_id} td::before {{
                content: attr(data-label);
                font-weight: 850;
                color: #475569;
                text-align: left;
                font-size: 0.78rem;
                flex: 0 0 38%;
                line-height: 1.45;
            }}

            #{safe_table_id} td > span {{
                flex: 1;
                text-align: right;
                word-break: keep-all;
                overflow-wrap: break-word;
                line-height: 1.45;
            }}

            #{safe_table_id} td.left-align {{
                display: block;
                background: #eff6ff;
                text-align: left;
                padding: 0.7rem 0.75rem;
                color: #1e3a8a;
                font-weight: 900;
            }}

            #{safe_table_id} td.left-align::before {{
                content: none;
            }}

            #{safe_table_id} td.left-align > span {{
                display: block;
                text-align: left;
                font-weight: 900;
            }}
        }}
    </style>
    """

    header_html = "".join([f"<th>{html_escape(header)}</th>" for header in headers])

    body_html = ""

    for row in rows:
        cell_html = ""

        for idx, cell in enumerate(row):
            cell_text = "" if cell is None else str(cell)
            left_class = "left-align" if idx == 0 else ""
            color_class = _value_class(cell_text) if idx > 0 else ""
            label = headers[idx] if idx < len(headers) else ""

            display_text = html_escape(cell_text).replace(" / ", "<br/>")

            cell_html += (
                f'<td data-label="{html_escape(label)}" class="{left_class} {color_class}">'
                f"<span>{display_text}</span>"
                f"</td>"
            )

        body_html += f"<tr>{cell_html}</tr>"

    return (
        css
        + f'<table id="{safe_table_id}">'
        + f"<thead><tr>{header_html}</tr></thead>"
        + f"<tbody>{body_html}</tbody>"
        + "</table>"
    )


def _render_patient_summary(title, report):
    meta = report["meta"]

    st.markdown('<div class="info-card">', unsafe_allow_html=True)

    st.markdown(
        f'<div class="case-title-mobile">👤 {html_escape(title)}</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="case-subtitle-mobile">
            <span class="label-strong">연령/성별:</span>
            <span class="result-value">{html_escape(meta.get("age", "-"))}세 / {html_escape(meta.get("sex", "-"))}</span>
            &nbsp;|&nbsp;
            <span class="label-strong">병변측:</span>
            <span class="result-value">{html_escape(meta.get("side", "-"))}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="case-text-block" style="margin-top:0.8rem;">
            <div class="case-bullet">
                <span class="label-strong">주요 임상 정보:</span>
                <span class="result-value"> {html_escape(meta.get("chief", ""))}</span>
            </div>
            <div class="case-bullet">
                <span class="label-strong text-blue">판독 힌트:</span>
                <span class="result-value"> {html_escape(meta.get("clinical_hint", ""))}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)


def _render_reading_guide():
    st.markdown(
        """
        <div class="warn-card">
            <div class="finding-highlight" style="color:#b45309;">🎓 실제형 결과표 판독 순서</div>
            <div class="case-bullet">
                1. 먼저 <b>감각신경전도검사(SNAP)</b>에서 진폭이 정상측 대비 감소했는지 확인합니다.
                감각반응이 보존되면 신경뿌리병증 가능성이 올라가고, 감소하면 말초신경 또는 신경얼기 병변 가능성이 커집니다.
            </div>
            <div class="case-bullet">
                2. 다음으로 <b>운동신경전도검사(CMAP)</b>에서 원위잠복기, 진폭, 자극 위치별 진폭 변화를 봅니다.
                근위부 자극에서 진폭이 크게 떨어지면 국소 전도차단을 의심합니다.
            </div>
            <div class="case-bullet">
                3. 마지막으로 <b>침근전도검사(Needle EMG)</b>에서 휴식 시 비정상 자발전위와 수의수축 시 운동단위동원 양상을 확인합니다.
                서로 다른 말초신경이지만 같은 척수 분절을 공유하는 근육들이 함께 침범되면 신경뿌리병증을 의심합니다.
            </div>
            <div class="case-bullet">
                4. 표의 수치만 보지 말고, 증상 분포·감각전도 보존 여부·운동전도 위치별 변화·침근전도 분절 패턴을 통합해야 합니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_sensory_table(rows):
    table_rows = []

    for row in rows:
        table_rows.append(
            [
                row.get("nerve", ""),
                row.get("side", ""),
                row.get("recording", ""),
                row.get("stimulation", ""),
                row.get("amplitude", ""),
                row.get("latency", ""),
                row.get("velocity", ""),
            ]
        )

    st.markdown(
        '<div class="finding-highlight">⚡ 감각신경전도검사(Sensory NCS, SNAP)</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        _render_mobile_table(
            ["검사 신경", "측", "기록 위치", "자극 위치", "진폭", "잠복기", "전도속도"],
            table_rows,
            "sensory_ncs_table",
        ),
        unsafe_allow_html=True,
    )


def _render_motor_table(rows):
    table_rows = []

    for row in rows:
        table_rows.append(
            [
                row.get("nerve", ""),
                row.get("side", ""),
                row.get("recording", ""),
                row.get("stimulation", ""),
                row.get("amplitude", ""),
                row.get("latency", ""),
                row.get("velocity", ""),
            ]
        )

    st.markdown(
        '<div class="finding-highlight">⚡ 운동신경전도검사(Motor NCS, CMAP)</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        _render_mobile_table(
            ["검사 신경", "측", "기록 근육", "자극 위치", "진폭", "잠복기", "전도속도"],
            table_rows,
            "motor_ncs_table",
        ),
        unsafe_allow_html=True,
    )


def _render_late_response_table(rows):
    if not rows:
        return

    table_rows = []

    for row in rows:
        table_rows.append(
            [
                row.get("test", ""),
                row.get("side", ""),
                row.get("latency", ""),
                row.get("amplitude", ""),
            ]
        )

    st.markdown(
        '<div class="finding-highlight">⏱️ 후기반응 / 반사 검사(F-wave, H-reflex)</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        _render_mobile_table(
            ["검사 항목", "측", "잠복기", "진폭"],
            table_rows,
            "late_response_table",
        ),
        unsafe_allow_html=True,
    )


def _render_emg_table(rows):
    table_rows = []

    for row in rows:
        table_rows.append(
            [
                row.get("muscle", ""),
                row.get("root", ""),
                row.get("nerve", ""),
                row.get("rest", ""),
                row.get("volition", ""),
            ]
        )

    st.markdown(
        '<div class="finding-highlight">🪡 침근전도검사(Needle EMG)</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        _render_mobile_table(
            ["검사 근육", "분절", "말초신경", "휴식 시 반응", "수의수축 시 반응"],
            table_rows,
            "needle_emg_table",
        ),
        unsafe_allow_html=True,
    )


def _render_interpretation(report):
    interpretation = report["interpretation"]

    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.markdown('<div class="result-title">✅ 검사 결과 통합 해석</div>', unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="case-text-block" style="background:#fff1f2!important; border-left-color:#fecdd3!important;">
            <div class="case-bullet">
                <span class="label-strong text-red">최종 교육용 의심 진단:</span>
                <span class="result-value text-red" style="font-weight:800!important;">
                    {html_escape(report.get("diagnosis", ""))}
                </span>
            </div>
            <div class="case-bullet">
                <span class="label-strong">추정 손상 위치:</span>
                <span class="result-value"> {html_escape(report.get("lesion", ""))}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    section_config = [
        ("sensory", "1단계: 감각신경전도검사 해석", "#3b82f6", "#eff6ff"),
        ("motor", "2단계: 운동신경전도검사 해석", "#0f766e", "#f0fdfa"),
        ("emg", "3단계: 침근전도검사 해석", "#d97706", "#fffbeb"),
        ("integration", "4단계: 종합 판독과 병변 위치 추정", "#dc2626", "#fff1f2"),
        ("differential", "감별진단", "#9333ea", "#fdf4ff"),
        ("additional", "추가 검사 및 물리치료 교육 포인트", "#15803d", "#f0fdf4"),
    ]

    for key, title, border_color, bg_color in section_config:
        items = interpretation.get(key, [])

        if not items:
            continue

        st.markdown(
            f"""
            <div class="result-label" style="border-left-color:{border_color}!important; background:{bg_color}!important;">
                {html_escape(title)}
            </div>
            """,
            unsafe_allow_html=True,
        )

        for item in items:
            st.markdown(
                f'<div class="result-text">• {html_escape(item)}</div>',
                unsafe_allow_html=True,
            )

    st.markdown("</div>", unsafe_allow_html=True)


def _render_numeric_criteria_tip():
    st.markdown(
        """
        <div class="info-card">
            <div class="finding-highlight">📌 수치 판독 기준 기억하기</div>
            <div class="case-bullet">
                • <b>진폭</b>은 주로 축삭 손상 정도를 반영합니다. 병변측 진폭이 정상측 대비 약 50% 이하로 감소하면 의미 있는 축삭 손상을 의심합니다.
            </div>
            <div class="case-bullet">
                • <b>잠복기</b>는 자극 후 반응이 시작될 때까지의 시간입니다. 병변측 잠복기가 정상측 대비 약 130% 이상 길어지면 말이집탈락 또는 국소 전도 지연을 의심합니다.
            </div>
            <div class="case-bullet">
                • <b>전도차단</b>은 원위부 자극에서는 반응이 비교적 보존되지만, 병변을 지나 근위부 자극했을 때 진폭이 크게 감소하는 패턴입니다.
            </div>
            <div class="case-bullet">
                • <b>침근전도 휴식 시 비정상 자발전위</b>에는 fibrillation potential, positive sharp wave, fasciculation potential 등이 포함됩니다.
            </div>
            <div class="case-bullet">
                • <b>수의수축 시 Reduced MU recruitment</b>는 동원 가능한 운동단위 수가 줄었다는 뜻이며, 하위운동신경계 병변에서 중요한 단서입니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =============================================================================
# 메인 렌더링 함수
# =============================================================================

def render_input_learning():
    st.markdown('<div class="main-title">가상 결과표 판독학습</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="subtle">
            실제 근전도 결과표와 유사한 형태의 수치 데이터를 읽고,
            감각신경전도검사·운동신경전도검사·침근전도검사를 단계적으로 해석하여
            의심 질환과 손상 위치를 추정하는 학습 모드입니다.
        </div>
        """,
        unsafe_allow_html=True,
    )

    if "input_reset_counter" not in st.session_state:
        st.session_state["input_reset_counter"] = 0

    dynamic_radio_key = f"input_report_selector_{st.session_state['input_reset_counter']}"

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">📋 학습할 실제형 가상 결과표 선택</div>', unsafe_allow_html=True)

    report_names = ["선택 안 함"] + list(VIRTUAL_REPORTS.keys())

    selected = st.radio(
        "가상 결과표 리스트",
        report_names,
        key=dynamic_radio_key,
        label_visibility="collapsed",
    )

    st.markdown("</div>", unsafe_allow_html=True)

    if selected == "선택 안 함":
        st.markdown(
            """
            <div class="info-card">
                <div class="finding-highlight">학습 방법</div>
                <div class="case-bullet">
                    위 목록에서 결과표를 선택하면 실제 임상 결과표와 유사한 표가 나타납니다.
                    먼저 표를 스스로 읽어본 뒤, 아래의 단계별 해석을 확인해 보세요.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        render_bottom_navigation()
        return

    report = VIRTUAL_REPORTS[selected]

    _render_patient_summary(selected, report)
    _render_reading_guide()

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown(
        '<div class="case-section-label">📋 실제형 근전도 결과표</div>',
        unsafe_allow_html=True,
    )

    _render_sensory_table(report.get("sensory_ncs", []))
    _render_motor_table(report.get("motor_ncs", []))
    _render_late_response_table(report.get("late_response", []))
    _render_emg_table(report.get("needle_emg", []))

    st.markdown("</div>", unsafe_allow_html=True)

    _render_numeric_criteria_tip()
    _render_interpretation(report)

    st.markdown('<div class="start-button-wrap">', unsafe_allow_html=True)

    if st.button("🔄 다른 결과표 분석", type="secondary", use_container_width=True, key="reset_input_report_btn"):
        st.session_state["input_reset_counter"] += 1
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    render_bottom_navigation()
