# data/virtual_reports.py (Part 1: 결과표 1~5)

from data.terms import translate_value

VIRTUAL_REPORTS = {
    "오른쪽 손목굴증후군 의심 결과표": {
        "meta": {"age": 52, "sex": "여성", "side": "오른쪽", "chief": "오른쪽 엄지~중지 저림, 야간 통증으로 잠에서 깸."},
        "sensory_ncs": [
            {"nerve": "정중신경 SNAP", "side": "오른쪽", "recording": "검지", "stimulation": "손목", "amplitude": "7 μV", "latency": "4.6 ms", "velocity": "32 m/s"},
            {"nerve": "정중신경 SNAP", "side": "왼쪽", "recording": "검지", "stimulation": "손목", "amplitude": "24 μV", "latency": "2.8 ms", "velocity": "51 m/s"},
            {"nerve": "자신경 SNAP", "side": "오른쪽", "recording": "새끼손가락", "stimulation": "손목", "amplitude": "23 μV", "latency": "2.6 ms", "velocity": "54 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "정중신경 CMAP", "side": "오른쪽", "recording": "APB", "stimulation": "손목", "amplitude": "3.0 mV", "latency": "5.8 ms", "velocity": "-"}
        ],
        "needle_emg": [
            {"muscle": "짧은엄지벌림근", "root": "C8-T1", "nerve": "정중신경", "rest": "비정상적 자발전위 출현", "volition": "감소된 운동단위 동원패턴"},
            {"muscle": "목 척추주위근", "root": "C6-C7", "nerve": "뒤가지", "rest": "전기적 침묵 (정상 반응)", "volition": "통증/협조 부족으로 검사 제한"}
        ],
        "interpretation": {
            "sensory": ["오른쪽 정중신경 감각 진폭이 현저히 감소하고 잠복기가 지연되었습니다. 이는 손목 부위의 감각 축삭 손상을 의미합니다."],
            "motor": ["운동 원위잠복기가 5.8 ms로 뚜렷하게 지연되어 손목 구간의 국소 전도 지연을 입증합니다."],
            "emg": ["짧은엄지벌림근에서 비정상 자발전위가 확인되며 척추주위근은 정상입니다."],
            "integration": ["추정 질환: 오른쪽 손목굴증후군 (Carpal tunnel syndrome)"]
        }
    },
    "왼쪽 C6 신경뿌리병증 의심 결과표": {
        "meta": {"age": 45, "sex": "남성", "side": "왼쪽", "chief": "뒷목에서 왼쪽 어깨 및 엄지로 뻗치는 방사통."},
        "sensory_ncs": [
            {"nerve": "정중신경 SNAP", "side": "왼쪽", "recording": "검지", "stimulation": "손목", "amplitude": "26 μV", "latency": "2.9 ms", "velocity": "52 m/s"},
            {"nerve": "노신경 SNAP", "side": "왼쪽", "recording": "손등 노쪽", "stimulation": "아래팔", "amplitude": "21 μV", "latency": "2.5 ms", "velocity": "53 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "정중신경 CMAP", "side": "왼쪽", "recording": "APB", "stimulation": "손목", "amplitude": "8.6 mV", "latency": "3.5 ms", "velocity": "-"}
        ],
        "needle_emg": [
            {"muscle": "위팔두갈래근", "root": "C5-C6", "nerve": "근육피부", "rest": "비정상적 자발전위 출현", "volition": "감소된 운동단위 동원패턴"},
            {"muscle": "목 척추주위근", "root": "C6", "nerve": "뒤가지", "rest": "비정상적 자발전위 출현", "volition": "정상 운동단위 동원패턴"}
        ],
        "interpretation": {
            "sensory": ["하지 및 상지 말초 감각전도가 대칭적으로 완벽하게 보존되어 있습니다. 이는 병변이 DRG 몸쪽임을 시사합니다."],
            "motor": ["말초 운동신경의 속도 및 잠복기는 정상 범위 내에 있습니다."],
            "emg": ["목 척추주위근과 C6 지배 근육에서 동시 탈신경 소견이 관찰됩니다."],
            "integration": ["추정 질환: 왼쪽 C6 목 신경뿌리병증"]
        }
    },
    "오른쪽 온종아리신경병증 의심 결과표": {
        "meta": {"age": 41, "sex": "남성", "side": "오른쪽", "chief": "석고붕대 제거 직후 발견된 우측 발처짐."},
        "sensory_ncs": [
            {"nerve": "얕은종아리 SNAP", "side": "오른쪽", "recording": "발등", "stimulation": "종아리", "amplitude": "4 μV", "latency": "3.6 ms", "velocity": "36 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "종아리 CMAP", "side": "오른쪽", "recording": "EDB", "stimulation": "발목", "amplitude": "4.4 mV", "latency": "4.1 ms", "velocity": "-"},
            {"nerve": "종아리 CMAP", "side": "오른쪽", "recording": "EDB", "stimulation": "무릎 위", "amplitude": "1.5 mV", "latency": "12.8 ms", "velocity": "25 m/s"}
        ],
        "needle_emg": [
            {"muscle": "앞정강근", "root": "L4-L5", "nerve": "깊은종아리", "rest": "비정상적 자발전위 출현", "volition": "감소된 운동단위 동원패턴"}
        ],
        "interpretation": {
            "sensory": ["우측 얕은종아리신경 SNAP 진폭이 크게 감소하여 먼쪽 말초 축삭 손상을 보여줍니다."],
            "motor": ["무릎 위/아래 비교 시 진폭이 급감하는 국소 전도차단 소견이 뚜렷합니다."],
            "emg": ["앞정강근에서 활동성 탈신경 소견이 확인됩니다."],
            "integration": ["추정 질환: 오른쪽 온종아리신경병증"]
        }
    },
    "왼쪽 L5 신경뿌리병증 의심 결과표": {
        "meta": {"age": 58, "sex": "여성", "side": "왼쪽", "chief": "무거운 물건을 든 후 발생한 좌측 하지 방사통과 발처짐."},
        "sensory_ncs": [
            {"nerve": "얕은종아리 SNAP", "side": "왼쪽", "recording": "발등", "amplitude": "13 μV", "latency": "2.9 ms", "velocity": "47 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "종아리 CMAP", "side": "왼쪽", "recording": "EDB", "amplitude": "3.9 mV", "latency": "4.5 ms", "velocity": "-"}
        ],
        "needle_emg": [
            {"muscle": "중간볼기근", "root": "L5", "nerve": "위볼기", "rest": "비정상적 자발전위 출현", "volition": "감소된 운동단위 동원패턴"},
            {"muscle": "허리 척추주위근", "root": "L5", "rest": "비정상적 자발전위 출현", "volition": "통증/협조 부족으로 검사 제한"}
        ],
        "interpretation": {
            "sensory": ["하지 감각전도가 보존되어 병변이 신경뿌리 수준임을 지지합니다."],
            "motor": ["말초 운동신경의 국소적 압박 징후는 관찰되지 않습니다."],
            "emg": ["L5 지배 근육과 허리 척추주위근에서 동시에 비정상 자발전위가 출현합니다."],
            "integration": ["추정 질환: 왼쪽 L5 허리 신경뿌리병증"]
        }
    },
    "오른쪽 노신경병증 의심 결과표": {
        "meta": {"age": 31, "sex": "남성", "side": "오른쪽", "chief": "음주 후 팔을 걸치고 잠든 뒤 발생한 손목처짐."},
        "sensory_ncs": [
            {"nerve": "노신경 SNAP", "side": "오른쪽", "recording": "손등", "amplitude": "4 μV", "latency": "3.5 ms", "velocity": "42 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "노신경 CMAP", "side": "오른쪽", "recording": "ECR", "stimulation": "아래팔", "amplitude": "4.5 mV", "latency": "2.8 ms", "velocity": "-"},
            {"nerve": "노신경 CMAP", "side": "오른쪽", "recording": "ECR", "stimulation": "위팔", "amplitude": "1.2 mV", "latency": "6.8 ms", "velocity": "38 m/s"}
        ],
        "needle_emg": [
            {"muscle": "노쪽손목폄근", "root": "C6-C7", "rest": "비정상적 자발전위 출현", "volition": "감소된 운동단위 동원패턴"}
        ],
        "interpretation": {
            "sensory": ["표재노신경 SNAP 진폭 감소는 병변이 먼쪽 말초 축삭 손상임을 시사합니다."],
            "motor": ["나선고랑 부위 자극 시 진폭이 급감하는 명확한 전도차단이 관찰됩니다."],
            "emg": ["노쪽손목폄근의 활동성 탈신경 소견이 확인됩니다."],
            "integration": ["추정 질환: 위팔뼈 나선고랑 노신경병증"]
        }
    }
}
# data/virtual_reports.py (Part 2: 결과표 6~11 완결)

    "왼쪽 팔꿈치굴증후군 의심 결과표": {
        "meta": {"age": 39, "sex": "여성", "side": "왼쪽", "chief": "장시간 요리사로 일하며 발생한 4, 5지 저림과 내재근 약화."},
        "sensory_ncs": [
            {"nerve": "자신경 SNAP", "side": "왼쪽", "recording": "새끼손가락", "amplitude": "5 μV", "latency": "3.6 ms", "velocity": "37 m/s"},
            {"nerve": "정중신경 SNAP", "side": "왼쪽", "recording": "검지", "amplitude": "23 μV", "latency": "2.8 ms", "velocity": "51 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "자신경 CMAP", "side": "왼쪽", "recording": "ADM", "stimulation": "손목", "amplitude": "7.1 mV", "latency": "2.6 ms", "velocity": "-"},
            {"nerve": "자신경 CMAP", "side": "왼쪽", "recording": "ADM", "stimulation": "팔꿈치 위", "amplitude": "3.5 mV", "latency": "8.8 ms", "velocity": "34 m/s"}
        ],
        "needle_emg": [
            {"muscle": "새끼벌림근", "root": "C8-T1", "nerve": "자신경", "rest": "비정상적 자발전위 출현", "volition": "감소된 운동단위 동원패턴"}
        ],
        "interpretation": {
            "sensory": ["자신경 감각신경 진폭이 감소하고 잠복기가 지연되었습니다. 반면 정중신경은 완전히 정상입니다."],
            "motor": ["팔꿈치 위 자극 시 CMAP 진폭이 절반으로 급감하는 명확한 국소 전도차단이 관찰됩니다."],
            "emg": ["자신경 지배 손 내재근에서 휴식 시 비정상 자발전위가 도출되어 운동 축삭 변성을 지시합니다."],
            "integration": ["추정 질환: 왼쪽 팔꿈치굴증후군 (Cubital tunnel syndrome)"]
        }
    },
    "축삭성 다발신경병증 의심 결과표": {
        "meta": {"age": 61, "sex": "여성", "side": "양측", "chief": "항암화학치료 후 발생한 양측 발끝/손끝 저림(장갑-양말형)."},
        "sensory_ncs": [
            {"nerve": "장딴지신경 SNAP", "side": "양측", "recording": "발목", "amplitude": "반응 소실", "latency": "반응 소실", "velocity": "반응 소실"},
            {"nerve": "정중신경 SNAP", "side": "양측", "recording": "검지", "amplitude": "12 μV", "latency": "3.3 ms", "velocity": "46 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "정강신경 CMAP", "side": "양측", "recording": "AH", "amplitude": "1.2 mV", "latency": "5.7 ms", "velocity": "-"}
        ],
        "needle_emg": [
            {"muscle": "앞정강근", "root": "L4-L5", "nerve": "깊은종아리", "rest": "비정상적 자발전위 출현", "volition": "감소된 운동단위 동원패턴"},
            {"muscle": "가쪽넓은근", "root": "L2-L4", "nerve": "넓적다리", "rest": "전기적 침묵 (정상 반응)", "volition": "정상 운동단위 동원패턴"}
        ],
        "interpretation": {
            "sensory": ["다리 먼쪽(장딴지신경) 감각반응이 완전히 소실되었으며, 상지는 저하되긴 했으나 보존되어 길이의존성(Dying-back) 패턴을 보입니다."],
            "motor": ["하지 운동신경의 CMAP 진폭 역시 대칭적으로 크게 낮아 만성 축삭 파괴를 지지합니다."],
            "emg": ["다리 먼쪽 근육(앞정강근)에서만 탈신경 전위가 확인되며 몸쪽 근육은 정상입니다."],
            "integration": ["추정 질환: 항암제 유발성 축삭성 다발신경병증 (CIPN)"]
        }
    },
    "급성 말이집탈락성 다발신경뿌리병증 의심 결과표": {
        "meta": {"age": 41, "sex": "여성", "side": "양측", "chief": "장염 2주 후 상행성 대칭성 근력 저하 및 무반사 발생."},
        "sensory_ncs": [
            {"nerve": "정중신경 SNAP", "side": "양측", "amplitude": "18 μV", "latency": "3.8 ms", "velocity": "39 m/s"},
            {"nerve": "장딴지신경 SNAP", "side": "양측", "amplitude": "14 μV", "latency": "3.2 ms", "velocity": "45 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "종아리신경 CMAP", "side": "양측", "amplitude": "2.4 mV", "latency": "18.9 ms", "velocity": "28 m/s"}
        ],
        "late_response": [
            {"test": "정강신경 F파(Tibial F-wave)", "side": "양측", "latency": "반응 소실", "amplitude": "-"}
        ],
        "interpretation": {
            "sensory": ["장딴지신경(Sural SNAP)이 상대적으로 잘 보존되는 Sural Sparing 양상이 관찰되어 AIDP를 시사합니다."],
            "motor": ["다수 운동신경에서 잠복기가 크게 연장되고 전도속도가 심각하게 저하되어 다발성 말이집탈락성 마비를 입증합니다."],
            "reflex": ["F파의 완전 소실은 말초뿐만 아니라 몸쪽 척수 신경뿌리까지 병변이 침범했음을 증명합니다."],
            "integration": ["추정 질환: 급성 염증성 말이집탈락성 다발신경뿌리병증 (AIDP)"]
        }
    },
    "상부 위팔신경얼기병증 의심 결과표": {
        "meta": {"age": 28, "sex": "남성", "side": "왼쪽", "chief": "무거운 배낭을 멘 후 어깨 짓눌림. 좌측 어깨 벌림 및 팔꿉 굽힘 약화."},
        "sensory_ncs": [
            {"nerve": "가쪽아래팔피부신경 SNAP", "side": "왼쪽", "amplitude": "4 μV", "latency": "3.3 ms", "velocity": "35 m/s"}
        ],
        "motor_ncs": [
            {"nerve": "겨드랑신경 CMAP", "side": "왼쪽", "recording": "Deltoid", "amplitude": "1.8 mV", "latency": "5.1 ms", "velocity": "-"}
        ],
        "needle_emg": [
            {"muscle": "어깨세모근", "root": "C5-C6", "nerve": "겨드랑", "rest": "비정상적 자발전위 출현", "volition": "감소된 운동단위 동원패턴"},
            {"muscle": "목 척추주위근", "root": "C5-C6", "nerve": "뒤가지", "rest": "전기적 침묵 (정상 반응)", "volition": "통증/협조 부족으로 검사 제한"}
        ],
        "interpretation": {
            "sensory": ["가쪽아래팔피부신경 감각 진폭이 비정상으로 저하되어, 병변이 신경얼기 수준에 있음을 증명합니다."],
            "motor": ["겨드랑신경 반응 진폭이 소실되어 상부 줄기(Upper trunk) 손상이 확인됩니다."],
            "emg": ["어깨 근육에서 활동성 탈신경 전위가 도출되나 목 척추주위근은 정상으로 유지되어 신경뿌리 병변을 배제합니다."],
            "integration": ["추정 질환: 왼쪽 상부 위팔신경얼기병증"]
        }
    },
    "눈꺼풀 떨림과 눈 주위 불편감 의심 결과표": {
        "meta": {"age": 62, "sex": "여성", "side": "오른쪽", "chief": "우측 눈꺼풀 떨림 및 우측 이마 감각 둔화."},
        "late_response": [
            {"test": "눈깜빡반사 오른쪽 자극-오른쪽 R1", "side": "오른쪽", "latency": "지연", "amplitude": "감소"},
            {"test": "눈깜빡반사 오른쪽 자극-오른쪽 R2", "side": "오른쪽", "latency": "소실", "amplitude": "소실"},
            {"test": "눈깜빡반사 오른쪽 자극-왼쪽 R2", "side": "왼쪽", "latency": "소실", "amplitude": "소실"},
            {"test": "눈깜빡반사 왼쪽 자극-왼쪽 R1", "side": "왼쪽", "latency": "정상 범위", "amplitude": "정상 범위"},
            {"test": "눈깜빡반사 왼쪽 자극-오른쪽 R2", "side": "오른쪽", "latency": "정상 범위", "amplitude": "정상 범위"}
        ],
        "interpretation": {
            "reflex": [
                "오른쪽 이마 자극 시 연관된 3가지 반사 반응(Rt R1, Rt R2, Lt R2)이 모두 지연/소실되었습니다.",
                "반면 왼쪽 자극 시에는 동측 반응뿐 아니라 건너편 오른쪽 반응도 정상입니다.",
                "이는 안면신경(날신경)은 정상이지만, 자극을 감지하는 우측 삼차신경(들신경) 경로가 손상되었음을 확증합니다."
            ],
            "integration": ["추정 질환: 우측 삼차신경 들신경 전도 장애"]
        }
    },
    "뇌졸중 후 경직 정량평가 결과표": {
        "meta": {"age": 68, "sex": "남성", "side": "왼쪽", "chief": "좌측 편마비 및 발목 장딴지 근육 강직. 치료 전후 효과 정량평가."},
        "late_response": [
            {"test": "가자미근 H-반사 진폭 (치료 전)", "side": "왼쪽", "latency": "-", "amplitude": "비정상적 증가"},
            {"test": "가자미근 H/M 비율 (치료 전)", "side": "왼쪽", "latency": "-", "amplitude": "0.65 (65%)"},
            {"test": "가자미근 H/M 비율 (치료 후)", "side": "왼쪽", "latency": "-", "amplitude": "0.45 (45%)"}
        ],
        "interpretation": {
            "reflex": [
                "물리치료 전 H/M 비율이 65%로 폭발적으로 항진된 것은 중추신경계의 억제 상실로 인한 척수 반사회로 과흥분을 입증합니다.",
                "치료 후 H/M 비율이 45%로 감소하여 경직이 정량적으로 완화되었음을 확인합니다."
            ],
            "integration": ["추정 진단: 위운동신경세포 증후군에 의한 좌측 하지 경직 정량평가"]
        }
    }
}
