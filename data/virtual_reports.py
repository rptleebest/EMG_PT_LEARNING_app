# data/virtual_reports.py

"""
가상 결과표 판독학습용 데이터.

설계 원칙:
1. 사례 학습 모드와 달리 실제 근전도 결과표와 유사한 수치 기반 표를 제공합니다.
2. 각 표에서 '판단' 열은 제거합니다.
3. 신경전도검사는 자극/기록 위치, 진폭, 잠복기, 전도속도 등 실제 판독에 필요한 값을 분리합니다.
4. 침근전도검사는 실제 전위명과 운동단위동원 양상을 유지합니다.
5. 해석은 표 아래에서 단계적으로 설명하여 학생이 결과표를 읽는 법을 익히도록 구성합니다.
"""

VIRTUAL_REPORTS = {
    "왼쪽 C6 신경뿌리병증 의심 결과표": {
        "info": {
            "age": 45,
            "sex": "남성",
            "side": "왼쪽",
            "symptom": "왼쪽 목 통증과 어깨 외측 통증, 엄지와 검지 저림, 팔꿉관절 굽힘 및 손목 폄 약화",
        },
        "diagnosis": "왼쪽 C6 목 신경뿌리병증",
        "lesion_location": "C6 신경뿌리, 뒤뿌리신경절보다 몸쪽 병변",
        "sensory_ncs": [
            {
                "nerve": "정중신경 감각신경활동전위",
                "side": "좌",
                "recording": "2번째 손가락",
                "stimulation": "손목",
                "amplitude": "26 μV",
                "latency": "2.8 ms",
                "velocity": "54 m/s",
            },
            {
                "nerve": "정중신경 감각신경활동전위",
                "side": "우",
                "recording": "2번째 손가락",
                "stimulation": "손목",
                "amplitude": "28 μV",
                "latency": "2.7 ms",
                "velocity": "56 m/s",
            },
            {
                "nerve": "노신경 표재감각신경활동전위",
                "side": "좌",
                "recording": "손등",
                "stimulation": "아래팔",
                "amplitude": "18 μV",
                "latency": "2.4 ms",
                "velocity": "52 m/s",
            },
            {
                "nerve": "노신경 표재감각신경활동전위",
                "side": "우",
                "recording": "손등",
                "stimulation": "아래팔",
                "amplitude": "19 μV",
                "latency": "2.3 ms",
                "velocity": "53 m/s",
            },
        ],
        "motor_ncs": [
            {
                "nerve": "정중신경 복합근육활동전위",
                "side": "좌",
                "recording": "짧은엄지벌림근",
                "stimulation": "손목",
                "amplitude": "8.6 mV",
                "latency": "3.4 ms",
                "velocity": "-",
            },
            {
                "nerve": "정중신경 복합근육활동전위",
                "side": "좌",
                "recording": "짧은엄지벌림근",
                "stimulation": "팔꿈치",
                "amplitude": "8.2 mV",
                "latency": "7.8 ms",
                "velocity": "55 m/s",
            },
            {
                "nerve": "노신경 복합근육활동전위",
                "side": "좌",
                "recording": "집게폄근",
                "stimulation": "아래팔",
                "amplitude": "6.2 mV",
                "latency": "2.9 ms",
                "velocity": "-",
            },
            {
                "nerve": "노신경 복합근육활동전위",
                "side": "좌",
                "recording": "집게폄근",
                "stimulation": "위팔",
                "amplitude": "5.9 mV",
                "latency": "6.9 ms",
                "velocity": "53 m/s",
            },
        ],
        "needle_emg": [
            {
                "muscle": "위팔두갈래근",
                "root": "C5-C6",
                "nerve": "근육피부신경",
                "rest": "fibrillation potential, positive sharp wave",
                "volition": "Reduced MU recruitment",
            },
            {
                "muscle": "노쪽손목폄근",
                "root": "C6-C7",
                "nerve": "노신경",
                "rest": "fibrillation potential, positive sharp wave",
                "volition": "Reduced MU recruitment",
            },
            {
                "muscle": "삼각근",
                "root": "C5-C6",
                "nerve": "겨드랑신경",
                "rest": "Silent at rest",
                "volition": "Normal MU recruitment",
            },
            {
                "muscle": "짧은엄지벌림근",
                "root": "C8-T1",
                "nerve": "정중신경",
                "rest": "Silent at rest",
                "volition": "Normal MU recruitment",
            },
            {
                "muscle": "목 척추주위근",
                "root": "C6",
                "nerve": "후지",
                "rest": "fibrillation potential, positive sharp wave",
                "volition": "Pain-limited evaluation",
            },
        ],
        "interpretation": {
            "sensory": [
                "왼쪽 손 저림이 있으나 정중신경과 노신경 표재감각신경활동전위의 진폭과 잠복기가 정상측과 큰 차이 없이 보존되어 있습니다.",
                "감각신경활동전위가 보존된다는 점은 병변이 감각신경 세포체가 위치한 뒤뿌리신경절보다 몸쪽에 있음을 시사합니다.",
                "따라서 손목굴증후군이나 노신경 표재감각분지 병변보다는 목 신경뿌리병증 가능성이 높습니다.",
            ],
            "motor": [
                "정중신경과 노신경 운동전도검사에서 원위부와 근위부 자극 간 진폭 감소나 전도속도 저하가 뚜렷하지 않습니다.",
                "이는 말초신경 주행 중 특정 부위의 포착성 병변이나 전도차단 가능성이 낮다는 뜻입니다.",
            ],
            "emg": [
                "C6 분절을 공유하는 위팔두갈래근과 노쪽손목폄근에서 휴식 시 비정상 자발전위가 관찰됩니다.",
                "수의수축 시 운동단위 동원감소가 있어 운동축삭 손상이 동반된 신경뿌리 병변으로 해석할 수 있습니다.",
                "목 척추주위근에서도 탈신경 소견이 있어 말초신경병증보다 신경뿌리병증을 강하게 지지합니다.",
            ],
            "integrated": [
                "감각신경전도는 보존되고, 말초 운동신경전도는 비교적 정상이며, C6 분절 근육과 목 척추주위근에서 탈신경 소견이 확인됩니다.",
                "이 조합은 왼쪽 C6 목 신경뿌리병증에 가장 적합합니다.",
            ],
            "ddx": [
                "손목굴증후군: 정중신경 감각 및 운동 잠복기 지연이 중심이어야 하나 본 결과표에서는 보이지 않습니다.",
                "노신경병증: 노신경 지배 근육만 선택적으로 침범해야 하나 근육피부신경 지배 근육도 함께 침범되어 신경뿌리 병변이 더 적합합니다.",
                "상부 팔신경얼기병증: 감각신경활동전위 이상이 동반될 수 있으므로 현재 결과와는 덜 부합합니다.",
            ],
            "additional_tests": [
                "목 MRI를 통해 C5-6 또는 C6-7 추간판, 추간공 협착 여부를 확인합니다.",
                "C6 피부절 감각, 위팔두갈래근 반사, 손목폄 근력을 임상적으로 재확인합니다.",
            ],
        },
    },

    "오른쪽 손목굴증후군 의심 결과표": {
        "info": {
            "age": 52,
            "sex": "여성",
            "side": "오른쪽",
            "symptom": "오른쪽 1~3번째 손가락 저림, 야간통, 손목 굽힘 시 증상 악화",
        },
        "diagnosis": "오른쪽 손목굴증후군",
        "lesion_location": "오른쪽 손목굴 부위 정중신경",
        "sensory_ncs": [
            {
                "nerve": "정중신경 감각신경활동전위",
                "side": "우",
                "recording": "2번째 손가락",
                "stimulation": "손목",
                "amplitude": "8 μV",
                "latency": "4.8 ms",
                "velocity": "34 m/s",
            },
            {
                "nerve": "정중신경 감각신경활동전위",
                "side": "좌",
                "recording": "2번째 손가락",
                "stimulation": "손목",
                "amplitude": "27 μV",
                "latency": "2.8 ms",
                "velocity": "55 m/s",
            },
            {
                "nerve": "자신경 감각신경활동전위",
                "side": "우",
                "recording": "5번째 손가락",
                "stimulation": "손목",
                "amplitude": "25 μV",
                "latency": "2.6 ms",
                "velocity": "56 m/s",
            },
        ],
        "motor_ncs": [
            {
                "nerve": "정중신경 복합근육활동전위",
                "side": "우",
                "recording": "짧은엄지벌림근",
                "stimulation": "손목",
                "amplitude": "3.1 mV",
                "latency": "5.5 ms",
                "velocity": "-",
            },
            {
                "nerve": "정중신경 복합근육활동전위",
                "side": "우",
                "recording": "짧은엄지벌림근",
                "stimulation": "팔꿈치",
                "amplitude": "2.9 mV",
                "latency": "9.8 ms",
                "velocity": "49 m/s",
            },
            {
                "nerve": "자신경 복합근육활동전위",
                "side": "우",
                "recording": "새끼벌림근",
                "stimulation": "손목",
                "amplitude": "8.4 mV",
                "latency": "2.7 ms",
                "velocity": "-",
            },
            {
                "nerve": "자신경 복합근육활동전위",
                "side": "우",
                "recording": "새끼벌림근",
                "stimulation": "팔꿈치",
                "amplitude": "8.0 mV",
                "latency": "6.8 ms",
                "velocity": "56 m/s",
            },
        ],
        "needle_emg": [
            {
                "muscle": "짧은엄지벌림근",
                "root": "C8-T1",
                "nerve": "정중신경",
                "rest": "Silent at rest",
                "volition": "Reduced MU recruitment",
            },
            {
                "muscle": "첫째등쪽뼈사이근",
                "root": "C8-T1",
                "nerve": "자신경",
                "rest": "Silent at rest",
                "volition": "Normal MU recruitment",
            },
            {
                "muscle": "목 척추주위근",
                "root": "C8-T1",
                "nerve": "후지",
                "rest": "Silent at rest",
                "volition": "Normal MU recruitment",
            },
        ],
        "interpretation": {
            "sensory": [
                "오른쪽 정중신경 감각신경활동전위는 정상측보다 진폭이 감소하고 잠복기가 지연되어 있습니다.",
                "같은 손의 자신경 감각신경활동전위는 보존되어 있어 전신성 다발신경병증보다는 정중신경 국소 병변을 시사합니다.",
            ],
            "motor": [
                "오른쪽 정중신경 운동전도에서 손목 자극 시 원위잠복기가 길고 CMAP 진폭이 낮습니다.",
                "팔꿈치 자극에서도 진폭이 크게 회복되지 않아 손목굴 부위의 압박과 일부 축삭 손상이 동반된 양상으로 해석할 수 있습니다.",
                "자신경 운동전도는 보존되어 있어 자신경병증 가능성은 낮습니다.",
            ],
            "emg": [
                "짧은엄지벌림근에서 운동단위 동원감소가 관찰되어 정중신경 운동가지 침범 가능성을 뒷받침합니다.",
                "첫째등쪽뼈사이근과 목 척추주위근은 정상으로, C8-T1 신경뿌리병증보다는 손목 부위 정중신경 병변이 적합합니다.",
            ],
            "integrated": [
                "정중신경 감각 및 운동전도 이상이 손목 부위에서 두드러지고, 자신경 및 목 척추주위근은 보존됩니다.",
                "오른쪽 손목굴증후군, 특히 감각섬유와 운동섬유가 함께 침범된 중등도 이상 병변을 의심할 수 있습니다.",
            ],
            "ddx": [
                "C6 또는 C7 신경뿌리병증: 감각신경활동전위가 보존되는 경우가 많고 목 척추주위근 이상이 동반될 수 있습니다.",
                "당뇨병성 다발신경병증: 여러 감각신경이 대칭적으로 저하되는 양상이 필요합니다.",
                "자신경병증: 4~5번째 손가락 저림과 자신경 전도 이상이 중심입니다.",
            ],
            "additional_tests": [
                "Phalen 검사, Tinel 징후, 손목 압박검사를 병행합니다.",
                "정중-자신경 감각잠복기 비교검사 또는 손목 초음파로 정중신경 단면적을 확인할 수 있습니다.",
            ],
        },
    },

    "왼쪽 L5 신경뿌리병증 의심 결과표": {
        "info": {
            "age": 58,
            "sex": "여성",
            "side": "왼쪽",
            "symptom": "왼쪽 허리 통증, 발등과 엄지발가락 저림, 발목 등굽힘과 엄지발가락 폄 약화",
        },
        "diagnosis": "왼쪽 L5 허리 신경뿌Model network connection is unstable or timeout. Please try again later. [1076]
