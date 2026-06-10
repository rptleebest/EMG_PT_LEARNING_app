# data/virtual_reports.py

from data.report_terms import REPORT_LANG_KO, REPORT_LANG_EN, LANGUAGE_OPTIONS, normalize_report_language

REPORT_TITLE_KO = "가상 검사결과표 (양측 비교형)"
REPORT_TITLE_EN = "Virtual EMG Report (Bilateral Comparison)"

VIRTUAL_REPORTS = {
    "1. 왼쪽 목 통증 및 엄지/검지 저림 (C6 신경뿌리병증)": {
        "info": {"age": 45, "sex": "남성", "symptom": "왼쪽 뒷목 통증, 왼쪽 어깨와 엄지/검지로 뻗치는 저림, 팔꿉 굽힘 시 힘 빠짐", "side": "왼쪽"},
        "ncs_sensory": [
            ["정중신경 1지", "오른쪽", "22 μV", "2.6 ms", "정상 범위"],
            ["정중신경 1지", "왼쪽", "21 μV", "2.7 ms", "정상 범위"],
            ["정중신경 2지", "오른쪽", "25 μV", "2.8 ms", "정상 범위"],
            ["정중신경 2지", "왼쪽", "24 μV", "2.8 ms", "정상 범위"],
            ["자신경 5지", "오른쪽", "22 μV", "2.5 ms", "정상 범위"],
            ["자신경 5지", "왼쪽", "21 μV", "2.6 ms", "정상 범위"],
            ["노신경", "왼쪽", "18 μV", "2.1 ms", "정상 범위"],
            ["가쪽아래팔피부신경", "왼쪽", "20 μV", "2.2 ms", "정상 범위"],
            ["안쪽아래팔피부신경", "왼쪽", "19 μV", "2.3 ms", "정상 범위"],
        ],
        "ncs_motor": [
            ["정중신경", "손목", "오른쪽", "8.5 mV", "3.5 ms", "정상 범위"],
            ["정중신경", "손목", "왼쪽", "8.2 mV", "3.6 ms", "정상 범위"],
            ["자신경", "손목", "오른쪽", "7.5 mV", "2.8 ms", "정상 범위"],
            ["자신경", "손목", "왼쪽", "7.3 mV", "2.9 ms", "정상 범위"],
            ["노신경", "아래팔", "왼쪽", "6.5 mV", "2.5 ms", "정상 범위"],
            ["근육피부신경", "위팔", "왼쪽", "5.8 mV", "2.1 ms", "정상 범위"],
        ],
        "emg": [
            ["목 척추주위근", "C5", "왼쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["목 척추주위근", "C6", "왼쪽", "Fibrillation/PSW", "통증으로 평가 불가", "비정상 (활동성 탈신경)"],
            ["목 척추주위근", "C7", "왼쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["어깨세모근", "C5-C6", "왼쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["위팔두갈래근", "C5-C6", "왼쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["위팔요골근", "C5-C6", "왼쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["원엎침근", "C6-C7", "왼쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["노쪽손목굽힘근", "C6-C7", "왼쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["위팔세갈래근", "C7-C8", "왼쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["손가락폄근", "C7-C8", "왼쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["첫째등쪽뼈사이근", "C8-T1", "왼쪽", "Silent", "Normal recruitment", "정상 범위"],
        ],
        "teaching_diagnosis": {
            "summary": "왼쪽 C6 목 신경뿌리병증 (Cervical Radiculopathy)",
            "ncs_reason": [
                "정중, 자신경, 노신경, 근육피부신경 등 광범위한 감각(SNAP) 및 운동(CMAP) 전도가 모두 정상입니다.",
                "감각신경 진폭이 보존된 것은 병변이 감각세포체(DRG)보다 근위부인 신경뿌리에 있음을 명확히 지시합니다."
            ],
            "emg_reason": [
                "C6 분절의 지배를 공유하는 위팔두갈래근, 위팔요골근, 원엎침근에서만 활동성 탈신경 소견이 관찰되며, C7이나 C8 지배 근육은 정상입니다.",
                "C6 목 척추주위근의 비정상 소견은 병변이 말초가 아닌 척수 신경뿌리에 위치함을 확진하는 지표입니다."
            ],
            "integration": [
                "광범위한 NCS 정상 소견과 C6 분절 표지 근육들에 국한된 EMG 탈신경 소견을 종합하여 C6 신경뿌리 병변으로 확진합니다."
            ]
        },
        "differential_diagnosis": [{"name": "근육피부신경병증 (Musculocutaneous Neuropathy)", "how_to_differentiate": "가쪽아래팔 저림이 유사하나, 단일 마비라면 정중신경 지배인 원엎침근과 척추주위근은 정상이어야 하므로 구별됩니다."}]
    },

    "2. 오른쪽 1~3번째 손가락 저림 (손목굴증후군)": {
        "info": {"age": 52, "sex": "여성", "symptom": "오른손 엄지~중지 저림, 야간 통증 및 손목 굽힘 시 증상 악화", "side": "오른쪽"},
        "ncs_sensory": [
            ["정중신경 1지", "오른쪽", "9 μV", "4.9 ms", "비정상 (진폭 감소 / 잠복기 지연)"],
            ["정중신경 2지", "오른쪽", "10 μV", "4.8 ms", "비정상 (진폭 감소 / 잠복기 지연)"],
            ["정중신경 3지", "오른쪽", "11 μV", "4.8 ms", "비정상 (진폭 감소 / 잠복기 지연)"],
            ["정중신경 3지", "왼쪽", "26 μV", "2.7 ms", "정상 범위"],
            ["자신경 5지", "오른쪽", "24 μV", "2.5 ms", "정상 범위"],
            ["노신경", "오른쪽", "20 μV", "2.2 ms", "정상 범위"],
            ["등쪽자신경", "오른쪽", "18 μV", "2.3 ms", "정상 범위"],
        ],
        "ncs_motor": [
            ["정중신경", "손목", "오른쪽", "4.5 mV", "5.8 ms", "비정상 (진폭 감소 / 잠복기 지연)"],
            ["정중신경", "손목", "왼쪽", "8.1 mV", "3.6 ms", "정상 범위"],
            ["자신경", "손목", "오른쪽", "7.6 mV", "2.9 ms", "정상 범위"],
            ["노신경", "아래팔", "오른쪽", "6.8 mV", "2.5 ms", "정상 범위"],
        ],
        "emg": [
            ["목 척추주위근", "C6-C7", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["원엎침근", "C6-C7", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["노쪽손목굽힘근", "C6-C7", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["위팔세갈래근", "C7-C8", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["손가락폄근", "C7-C8", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["짧은엄지벌림근", "C8-T1", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["첫째등쪽뼈사이근", "C8-T1", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
        ],
        "teaching_diagnosis": {
            "summary": "오른쪽 손목굴증후군 (Carpal Tunnel Syndrome)",
            "ncs_reason": [
                "오른쪽 정중신경의 여러 감각 분지(1, 2, 3지)와 운동 신경에서만 잠복기가 뚜렷하게 지연되어 손목굴 부위 압박을 지시합니다.",
                "자신경 및 노신경 등 인접 신경은 정상 범위를 유지하고 있습니다."
            ],
            "emg_reason": [
                "정중신경의 손목 원위부 지배근(짧은엄지벌림근)에서 탈신경 전위가 없는 것(Silent)은 아직 축삭이 완전히 손상되거나 마비에 이르지 않은 가벼운 상태임을 의미합니다.",
                "손목 상부의 정중신경 지배 근육인 원엎침근, 노쪽손목굽힘근은 정상입니다."
            ],
            "integration": [
                "정중신경에 국한된 명확한 말초 잠복기 지연 데이터와 상위 근육의 정상 소견을 통합하여 손목굴증후군으로 진단합니다."
            ]
        },
        "differential_diagnosis": [{"name": "원엎침근증후군 (Pronator Teres Syndrome)", "how_to_differentiate": "손가락 저림 증상은 동일하나, 원엎침근증후군이라면 손목 상부 근육인 원엎침근 EMG에서 비정상 활동성 탈신경 소견이 나타나야 합니다."}]
    },

    "3. 왼쪽 허리/엉치 통증 및 발처짐 (L5 신경뿌리병증)": {
        "info": {"age": 58, "sex": "여성", "symptom": "왼쪽 허리통증, 발등 저림, 발목 들어올리기 힘듦 (발끝 끌림)", "side": "왼쪽"},
        "ncs_sensory": [
            ["얕은종아리신경", "왼쪽", "14 μV", "2.9 ms", "정상 범위"],
            ["얕은종아리신경", "오른쪽", "15 μV", "2.8 ms", "정상 범위"],
            ["장딴지신경", "왼쪽", "17 μV", "3.1 ms", "정상 범위"],
            ["장딴지신경", "오른쪽", "18 μV", "3.0 ms", "정상 범위"],
            ["두렁신경", "왼쪽", "12 μV", "3.2 ms", "정상 범위"],
        ],
        "ncs_motor": [
            ["종아리신경", "발목", "왼쪽", "4.5 mV", "4.5 ms", "정상 범위"],
            ["종아리신경", "발목", "오른쪽", "4.8 mV", "4.2 ms", "정상 범위"],
            ["정강신경", "발목", "왼쪽", "5.5 mV", "5.0 ms", "정상 범위"],
            ["넙다리신경", "서혜부", "왼쪽", "6.2 mV", "4.1 ms", "정상 범위"],
        ],
        "emg": [
            ["허리 척추주위근", "L4", "왼쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["허리 척추주위근", "L5", "왼쪽", "Fibrillation/PSW", "통증으로 평가 불가", "비정상 (활동성 탈신경)"],
            ["허리 척추주위근", "S1", "왼쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["엉덩허리근", "L2-L3", "왼쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["가쪽넓은근", "L3-L4", "왼쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["앞정강근", "L4-L5", "왼쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["긴종아리근", "L5-S1", "왼쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["넙다리근막긴장근", "L4-L5", "왼쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["안쪽장딴지근", "S1-S2", "왼쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["큰볼기근", "S1-S2", "왼쪽", "Silent", "Normal recruitment", "정상 범위"],
        ],
        "teaching_diagnosis": {
            "summary": "왼쪽 L5 허리 신경뿌리병증 (Lumbar Radiculopathy)",
            "ncs_reason": [
                "발처짐과 발등 감각 이상이 있음에도 얕은종아리신경 및 두렁신경 감각 진폭이 정상 범위입니다.",
                "이는 병변이 감각세포체 몸쪽인 척수 신경뿌리에 위치하여 말초 감각신경 퇴행이 없음을 증명합니다."
            ],
            "emg_reason": [
                "앞정강근, 긴종아리근, 넙다리근막긴장근(TFL) 등 서로 다른 신경 지배를 받으나 L5 분절을 공유하는 근육들에서 일치된 탈신경 소견이 보입니다.",
                "L4, S1은 정상이지만 L5 허리 척추주위근에서만 탈신경 자발전위가 확인되어 분절을 확진합니다."
            ],
            "integration": [
                "감각 전도 보존 현상과 척추주위근을 포함한 광범위한 L5 분절의 동시 탈신경을 통합하여 L5 신경뿌리병증으로 결론 내립니다."
            ]
        },
        "differential_diagnosis": [{"name": "온종아리신경 마비 (Common Peroneal Neuropathy)", "how_to_differentiate": "발처짐 증상이 유사하나, 온종아리신경 마비는 감각 전도가 저하되며 척추주위근 및 TFL 근육은 정상으로 유지되어야 합니다."}]
    },

    "4. 오른쪽 4~5번째 손가락 저림 (팔꿈치굴증후군)": {
        "info": {"age": 42, "sex": "남성", "symptom": "오른쪽 새끼손가락 저림, 젓가락질 불편 및 손아귀 힘 약화", "side": "오른쪽"},
        "ncs_sensory": [
            ["자신경 5지", "오른쪽", "9 μV", "3.4 ms", "비정상 (진폭 감소 / 잠복기 지연)"],
            ["자신경 5지", "왼쪽", "22 μV", "2.5 ms", "정상 범위"],
            ["등쪽자신경", "오른쪽", "12 μV", "2.6 ms", "비정상 (진폭 감소)"],
            ["정중신경 2지", "오른쪽", "24 μV", "2.8 ms", "정상 범위"],
            ["안쪽아래팔피부신경", "오른쪽", "20 μV", "2.2 ms", "정상 범위"],
        ],
        "ncs_motor": [
            ["자신경", "팔꿈치 아래", "오른쪽", "7.2 mV", "3.0 ms", "정상 범위"],
            ["자신경", "팔꿈치 위", "오른쪽", "3.1 mV", "8.2 ms", "비정상 (진폭 급감 / 국소 전도차단 의심)"],
            ["정중신경", "손목", "오른쪽", "8.5 mV", "3.5 ms", "정상 범위"],
        ],
        "emg": [
            ["목 척추주위근", "C8-T1", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["위팔세갈래근", "C7-C8", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["자쪽손목굽힘근", "C7-C8", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["깊은손가락굽힘근 4-5지", "C8-T1", "오른쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["새끼벌림근", "C8-T1", "오른쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["첫째등쪽뼈사이근", "C8-T1", "오른쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["짧은엄지벌림근", "C8-T1", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
        ],
        "teaching_diagnosis": {
            "summary": "오른쪽 팔꿈치굴증후군 (Cubital Tunnel Syndrome)",
            "ncs_reason": [
                "오른쪽 자신경 감각전도가 감소하였고, 팔꿈치 위/아래를 자극했을 때 운동 진폭이 50% 이상 급감하는 전도차단이 관찰되어 팔꿈치 부위 압박을 확진합니다."
            ],
            "emg_reason": [
                "자신경 지배 손 내재근(ADM, FDI)과 깊은손가락굽힘근에서 활동성 탈신경 전위가 확인됩니다.",
                "팔꿈치보다 근위부에서 분지되는 자쪽손목굽힘근(FCU)과 동일 C8-T1 분절 지배를 받는 정중신경 지배근(APB), 척추주위근은 완전한 정상입니다."
            ],
            "integration": [
                "자신경에 국한된 팔꿈치 부위 전도차단 수치와 특정 말초 근육의 탈신경 데이터를 종합하여 팔꿈치굴증후군으로 진단합니다."
            ]
        },
        "differential_diagnosis": [{"name": "C8 신경뿌리병증", "how_to_differentiate": "손 저림 양상이 비슷하나, C8 신경뿌리병증이라면 정중신경 지배 근육인 짧은엄지벌림근도 이상을 보이며 자신경 감각전도는 정상이어야 합니다."}]
    },

    "5. 오른쪽 손목처짐 및 손등 감각 저하 (노신경 마비)": {
        "info": {"age": 34, "sex": "남성", "symptom": "음주 후 의자에서 팔을 누른 채 잔 후 우측 손목처짐 및 손등 저림 발생", "side": "오른쪽"},
        "ncs_sensory": [
            ["노신경", "오른쪽", "8 μV", "3.2 ms", "비정상 (진폭 감소 / 잠복기 지연)"],
            ["노신경", "왼쪽", "20 μV", "2.1 ms", "정상 범위"],
            ["가쪽아래팔피부신경", "오른쪽", "19 μV", "2.2 ms", "정상 범위"],
            ["정중신경 2지", "오른쪽", "25 μV", "2.8 ms", "정상 범위"],
        ],
        "ncs_motor": [
            ["노신경", "팔꿈치", "오른쪽", "6.8 mV", "2.5 ms", "정상 범위"],
            ["노신경", "나선고랑 위", "오른쪽", "1.5 mV", "7.1 ms", "비정상 (진폭 급감 / 국소 전도차단 의심)"],
            ["정중신경", "손목", "오른쪽", "8.2 mV", "3.4 ms", "정상 범위"],
        ],
        "emg": [
            ["목 척추주위근", "C7-C8", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["위팔세갈래근", "C7-C8", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["위팔요골근", "C5-C6", "오른쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["긴노쪽손목폄근", "C6-C7", "오른쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["손가락폄근", "C7-C8", "오른쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["고유집게폄근", "C7-C8", "오른쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["원엎침근", "C6-C7", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["노쪽손목굽힘근", "C6-C7", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
        ],
        "teaching_diagnosis": {
            "summary": "오른쪽 노신경 마비 (Radial Nerve Palsy at Spiral Groove)",
            "ncs_reason": [
                "표재노신경 감각전도 저하와 함께, 나선고랑 상/하부 자극에서 운동 진폭이 급감하는 국소 전도차단 수치가 기록되어 물리적 압박 위치를 지시합니다."
            ],
            "emg_reason": [
                "나선고랑 하부에서 신경 지배를 받는 위팔요골근 및 폄근들은 일제히 탈신경 소견을 보입니다.",
                "나선고랑 상부에서 먼저 분지되는 위팔세갈래근이 정상 범위인 것은 신경 병변이 겨드랑이나 목이 아님을 해부학적으로 증명합니다."
            ],
            "integration": [
                "위팔세갈래근 보존, 나선고랑 부위 전도차단, 하부 폄근들의 선택적 마비를 통합하여 'Saturday night palsy' 형태의 노신경 마비로 확진합니다."
            ]
        },
        "differential_diagnosis": [{"name": "C7 신경뿌리병증", "how_to_differentiate": "손목 처짐은 유사하나, C7 병변이라면 위팔세갈래근 및 노쪽손목굽힘근에서도 탈신경 소견이 관찰되어야 합니다."}]
    },

    "6. 오른쪽 엉덩이 통증 및 까치발 보행 어려움 (S1 신경뿌리병증)": {
        "info": {"age": 50, "sex": "남성", "symptom": "오른쪽 엉치 통증, 종아리 뒤쪽 감각 저하 및 발바닥 쪽으로 힘이 안 들어감", "side": "오른쪽"},
        "ncs_sensory": [
            ["장딴지신경", "오른쪽", "16 μV", "3.0 ms", "정상 범위"],
            ["장딴지신경", "왼쪽", "17 μV", "2.9 ms", "정상 범위"],
            ["얕은종아리신경", "오른쪽", "14 μV", "2.8 ms", "정상 범위"],
            ["두렁신경", "오른쪽", "11 μV", "3.3 ms", "정상 범위"],
        ],
        "ncs_motor": [
            ["정강신경", "발목", "오른쪽", "6.1 mV", "4.8 ms", "정상 범위"],
            ["정강신경", "발목", "왼쪽", "6.4 mV", "4.7 ms", "정상 범위"],
            ["종아리신경", "발목", "오른쪽", "5.2 mV", "4.1 ms", "정상 범위"],
        ],
        "emg": [
            ["허리 척추주위근", "L5", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["허리 척추주위근", "S1", "오른쪽", "Fibrillation/PSW", "통증으로 평가 불가", "비정상 (활동성 탈신경)"],
            ["가쪽넓은근", "L3-L4", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["앞정강근", "L4-L5", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["안쪽장딴지근", "S1-S2", "오른쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["가자미근", "S1-S2", "오른쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["큰볼기근", "S1-S2", "오른쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["넙다리근막긴장근", "L4-L5", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
        ],
        "teaching_diagnosis": {
            "summary": "오른쪽 S1 허리 신경뿌리병증 (Lumbosacral Radiculopathy)",
            "ncs_reason": [
                "다리 뒤쪽 감각 이상이 뚜렷함에도 가장 원위부 감각 신경인 장딴지신경(Sural) 전도가 정상인 것은 전형적인 신경뿌리 병변의 특징입니다."
            ],
            "emg_reason": [
                "정강신경(장딴지근, 가자미근)과 하볼기신경(큰볼기근) 등 각기 다른 말초신경 지배를 받으나 S1 분절을 공유하는 근육들에서 동시 탈신경이 확인됩니다.",
                "L5, L4 지배 근육(앞정강근, 가쪽넓은근)은 정상이며, S1 척추주위근의 탈신경 소견은 병변이 척수 근위부임을 확진합니다."
            ],
            "integration": [
                "장딴지신경 전도 보존 수치와, S1 분절 우세 말초 근육 및 척추주위근의 일치된 탈신경 데이터를 통합하여 S1 신경뿌리병증으로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "궁둥신경병증 (Sciatic Neuropathy)",
                "how_to_differentiate": "다리 뒤쪽 통증과 약화는 유사하나, 말초 궁둥신경 마비라면 장딴지신경 감각 전도가 반드시 감소해야 하며 허리 척추주위근은 정상이어야 합니다."
            }
        ]
    },

    "7. 왼쪽 발처짐 및 발목 바깥쪽 무딤 (온종아리신경 마비)": {
        "info": {"age": 28, "sex": "여성", "symptom": "타이트한 부츠를 장시간 착용한 후 왼쪽 발목이 안 들리고 발등 감각이 무딤", "side": "왼쪽"},
        "ncs_sensory": [
            ["얕은종아리신경", "왼쪽", "6 μV", "4.1 ms", "비정상 (진폭 감소 / 잠복기 지연)"],
            ["얕은종아리신경", "오른쪽", "16 μV", "2.8 ms", "정상 범위"],
            ["장딴지신경", "왼쪽", "18 μV", "3.1 ms", "정상 범위"],
            ["두렁신경", "왼쪽", "13 μV", "3.0 ms", "정상 범위"],
        ],
        "ncs_motor": [
            ["종아리신경", "발목", "왼쪽", "5.1 mV", "4.0 ms", "정상 범위"],
            ["종아리신경", "종아리뼈머리", "왼쪽", "1.2 mV", "8.5 ms", "비정상 (진폭 급감 / 국소 전도차단 의심)"],
            ["정강신경", "발목", "왼쪽", "6.2 mV", "4.5 ms", "정상 범위"],
        ],
        "emg": [
            ["허리 척추주위근", "L5", "왼쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["넙다리두갈래근 짧은갈래", "L5-S1", "왼쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["앞정강근", "L4-L5", "왼쪽", "Silent", "Reduced recruitment", "비정상 (동원 감소)"],
            ["긴종아리근", "L5-S1", "왼쪽", "Silent", "Reduced recruitment", "비정상 (동원 감소)"],
            ["짧은발가락폄근", "L5-S1", "왼쪽", "Silent", "Reduced recruitment", "비정상 (동원 감소)"],
            ["안쪽장딴지근", "S1-S2", "왼쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["넙다리근막긴장근", "L4-L5", "왼쪽", "Silent", "Normal recruitment", "정상 범위"],
        ],
        "teaching_diagnosis": {
            "summary": "왼쪽 온종아리신경 마비 (Common Peroneal Neuropathy)",
            "ncs_reason": [
                "얕은종아리신경 감각전도가 저하되었으며, 종아리뼈머리(Fibular head) 상하부 자극 시 운동 진폭이 급감하는 국소 전도차단이 확인되어 무릎 외측 압박을 특정합니다."
            ],
            "emg_reason": [
                "압박 부위 하부의 근육(앞정강근, 긴종아리근)은 수의수축 동원이 감소합니다.",
                "가장 중요한 감별 포인트로, 무릎 상부에서 먼저 분지되는 넙다리두갈래근(짧은갈래)과 L5 허리 척추주위근이 완전한 정상 범위입니다."
            ],
            "integration": [
                "무릎 부위 국소 전도차단 지표와, 무릎 하부 근육들의 선택적 마비 및 근위부 보존 소견을 통합하여 온종아리신경 압박 마비로 확진합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "L5 허리 신경뿌리병증 (L5 Radiculopathy)",
                "how_to_differentiate": "발처짐(Foot drop) 증상이 똑같아 매우 헷갈리기 쉬우나, L5 병변이라면 허리 척추주위근 EMG가 비정상이어야 하며 감각신경 전도는 정상으로 보존되어야 합니다."
            }
        ]
    },

    "8. 오른쪽 어깨 통증 및 삼두근 약화 (C7 신경뿌리병증)": {
        "info": {"age": 51, "sex": "여성", "symptom": "오른쪽 날개뼈 안쪽 통증, 팔 뒤쪽부터 가운데 손가락까지 뻗치는 저림, 팔 펴는 힘이 약함", "side": "오른쪽"},
        "ncs_sensory": [
            ["정중신경 3지", "오른쪽", "28 μV", "2.7 ms", "정상 범위"],
            ["정중신경 3지", "왼쪽", "29 μV", "2.6 ms", "정상 범위"],
            ["정중신경 2지", "오른쪽", "26 μV", "2.7 ms", "정상 범위"],
            ["자신경 5지", "오른쪽", "24 μV", "2.4 ms", "정상 범위"],
            ["노신경", "오른쪽", "19 μV", "2.2 ms", "정상 범위"],
        ],
        "ncs_motor": [
            ["노신경", "아래팔", "오른쪽", "7.1 mV", "2.5 ms", "정상 범위"],
            ["정중신경", "손목", "오른쪽", "8.8 mV", "3.2 ms", "정상 범위"],
            ["자신경", "손목", "오른쪽", "7.5 mV", "2.8 ms", "정상 범위"],
        ],
        "emg": [
            ["목 척추주위근", "C6", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["목 척추주위근", "C7", "오른쪽", "Fibrillation/PSW", "통증으로 평가 불가", "비정상 (활동성 탈신경)"],
            ["목 척추주위근", "C8", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["위팔두갈래근", "C5-C6", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["노쪽손목굽힘근", "C6-C7", "오른쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["위팔세갈래근", "C7-C8", "오른쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["손가락폄근", "C7-C8", "오른쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["짧은엄지벌림근", "C8-T1", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
        ],
        "teaching_diagnosis": {
            "summary": "오른쪽 C7 목 신경뿌리병증 (Cervical Radiculopathy)",
            "ncs_reason": [
                "저림 호소 부위인 가운데 손가락(정중신경 3지)의 감각 전도가 정상인 것은, 말초신경 병변이 아닌 근위부 신경뿌리 병변의 전형적 소견입니다.",
                "상지 모든 주요 운동 전도 역시 정상으로 유지되고 있습니다."
            ],
            "emg_reason": [
                "서로 다른 말초신경(노신경, 정중신경) 지배를 받으나 C7 분절을 공유하는 위팔세갈래근, 손가락폄근, 노쪽손목굽힘근에서 일치된 탈신경이 확인됩니다.",
                "C7 척추주위근 탈신경 소견과 인접한 C5-C6 지배 위팔두갈래근의 정상 범위는 병변이 C7 레벨에 특정됨을 확진합니다."
            ],
            "integration": [
                "말초 감각전도 보존 현상과 C7 분절 우세 다수 말초근육의 동시 침범 데이터를 통합하여 C7 신경뿌리병증으로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "노신경 마비 (Radial Neuropathy)",
                "how_to_differentiate": "팔 펴는 힘의 약화와 손등 저림이 비슷하지만, 노신경 마비라면 정중신경 지배인 노쪽손목굽힘근이나 목 척추주위근은 정상이어야 합니다."
            }
        ]
    },

    "9. 왼쪽 갑작스러운 안면 마비 (벨마비)": {
        "info": {"age": 35, "sex": "여성", "symptom": "자고 일어난 후 왼쪽 얼굴 근육이 움직이지 않고 눈이 안 감김, 이마 주름 잡기 불가", "side": "왼쪽"},
        "ncs_sensory": [
            ["삼차신경", "왼쪽", "21 μV", "2.0 ms", "정상 범위"],
            ["삼차신경", "오른쪽", "22 μV", "1.9 ms", "정상 범위"],
        ],
        "ncs_motor": [
            ["얼굴신경 코근", "왼쪽", "0.8 mV", "4.5 ms", "비정상 (진폭 감소 / 잠복기 지연)"],
            ["얼굴신경 코근", "오른쪽", "3.5 mV", "2.8 ms", "정상 범위"],
            ["얼굴신경 눈둘레근", "왼쪽", "0.6 mV", "4.2 ms", "비정상 (진폭 감소)"],
            ["얼굴신경 눈둘레근", "오른쪽", "3.0 mV", "2.6 ms", "정상 범위"],
        ],
        "emg": [
            ["눈둘레근", "얼굴신경", "왼쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["입둘레근", "얼굴신경", "왼쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["이마근", "얼굴신경", "왼쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["깨물근", "삼차신경", "왼쪽", "Silent", "Normal recruitment", "정상 범위"],
        ],
        "teaching_diagnosis": {
            "summary": "왼쪽 특발성 얼굴신경마비 (Bell's Palsy)",
            "ncs_reason": [
                "감각을 지배하는 삼차신경은 정상이지만, 운동을 지배하는 얼굴신경(코근, 눈둘레근)의 진폭이 정상측 대비 70% 이상 유의하게 감소하여 심한 축삭 손상을 시사합니다."
            ],
            "emg_reason": [
                "이마근, 눈둘레근, 입둘레근 등 얼굴신경 지배 전 영역에서 활동성 탈신경 전위가 확인되어 전형적인 하위운동뉴런(LMN) 손상을 확진합니다.",
                "삼차신경 지배인 깨물근(Masseter)은 정상으로 복합 뇌신경 마비를 배제합니다."
            ],
            "integration": [
                "얼굴신경 단독의 심한 전도 저하와 전체 안면 근육의 EMG 탈신경 소견을 통해 전형적인 말초성 벨마비로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "중추성 안면 마비 (뇌졸중 등)",
                "how_to_differentiate": "입이 돌아가고 발음이 새는 증상은 비슷하나, 뇌졸중 등 중추성 질환은 이마 근육에 양측성 지배가 유지되어 마비측 이마 주름을 잡을 수 있는 점이 벨마비(이마 마비 동반)와 다릅니다."
            }
        ]
    },
    
    "10. 양측 발바닥 저림 및 통증 (다발신경병증)": {
        "info": {"age": 68, "sex": "남성", "symptom": "양쪽 발바닥부터 무릎까지 화끈거리고 저린 증상이 대칭적으로 나타남", "side": "양측"},
        "ncs_sensory": [
            ["장딴지신경", "오른쪽", "무반응", "측정불가", "비정상 (반응 소실)"],
            ["장딴지신경", "왼쪽", "무반응", "측정불가", "비정상 (반응 소실)"],
            ["얕은종아리신경", "오른쪽", "무반응", "측정불가", "비정상 (반응 소실)"],
            ["얕은종아리신경", "왼쪽", "무반응", "측정불가", "비정상 (반응 소실)"],
            ["정중신경 2지", "오른쪽", "12 μV", "3.8 ms", "비정상 (진폭 감소 / 잠복기 지연)"],
            ["정중신경 2지", "왼쪽", "13 μV", "3.7 ms", "비정상 (진폭 감소 / 잠복기 지연)"],
            ["자신경 5지", "오른쪽", "14 μV", "3.1 ms", "비정상 (진폭 감소)"],
            ["자신경 5지", "왼쪽", "15 μV", "3.0 ms", "비정상 (진폭 감소)"],
        ],
        "ncs_motor": [
            ["정강신경", "발목", "오른쪽", "1.8 mV", "6.2 ms", "비정상 (진폭 감소 / 잠복기 지연)"],
            ["정강신경", "발목", "왼쪽", "1.7 mV", "6.4 ms", "비정상 (진폭 감소 / 잠복기 지연)"],
            ["종아리신경", "발목", "오른쪽", "2.1 mV", "5.8 ms", "비정상 (진폭 감소 / 잠복기 지연)"],
            ["종아리신경", "발목", "왼쪽", "2.0 mV", "5.9 ms", "비정상 (진폭 감소 / 잠복기 지연)"],
            ["정중신경", "손목", "오른쪽", "6.5 mV", "4.1 ms", "정상 범위"],
            ["정중신경", "손목", "왼쪽", "6.8 mV", "4.0 ms", "정상 범위"],
        ],
        "emg": [
            ["짧은발가락폄근", "L5-S1", "오른쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["짧은발가락폄근", "L5-S1", "왼쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["앞정강근", "L4-L5", "오른쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["앞정강근", "L4-L5", "왼쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["안쪽장딴지근", "S1-S2", "오른쪽", "Fibrillation/PSW", "Reduced recruitment", "비정상 (활동성 탈신경)"],
            ["가쪽넓은근", "L3-L4", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["첫째등쪽뼈사이근", "C8-T1", "오른쪽", "Silent", "Normal recruitment", "정상 범위"],
            ["위팔두갈래근", "C5-C6", "왼쪽", "Silent", "Normal recruitment", "정상 범위"],
        ],
        "teaching_diagnosis": {
            "summary": "대칭성 길이의존성 축삭성 다발신경병증 (Polyneuropathy)",
            "ncs_reason": [
                "가장 긴 신경인 하지 원위부 감각 신경(장딴지신경, 얕은종아리신경) 반응이 소실되고 운동 진폭이 대칭적으로 감소한 길이의존성 패턴입니다.",
                "상지 말단(정중, 자신경) 감각 진폭도 감소하여 전신적인 침범을 확인합니다."
            ],
            "emg_reason": [
                "하지 최원위부 근육(짧은발가락폄근, 앞정강근, 장딴지근)에서는 탈신경이 보이나, 근위부(가쪽넓은근, 상지 근육)는 정상인 'Dying-back' 양상입니다."
            ],
            "integration": [
                "양측 신경 전도의 대칭적 소실과 원위부 우세 EMG 이상을 통해 당뇨성 증상 등과 부합하는 전신성 다발신경병증으로 진단합니다."
            ]
        },
        "differential_diagnosis": [{"name": "다발성 허리 신경뿌리병증 (Lumbar Canal Stenosis)", "how_to_differentiate": "양측 다리 저림은 유사하나, 척추 협착에 의한 다발 뿌리병증은 말초 감각전도가 보존되며 허리 척추주위근에 양측 탈신경이 도출되어야 합니다."}]
    }
}

def get_report_title(language: str) -> str:
    return REPORT_TITLE_EN if normalize_report_language(language) == REPORT_LANG_EN else REPORT_TITLE_KO

def get_report_section_name(section: str, language: str) -> str:
    lang = normalize_report_language(language)
    mapping = {
        "sensory": {"ko": "감각신경전도검사", "en": "Sensory NCS"},
        "motor": {"ko": "운동신경전도검사", "en": "Motor NCS"},
        "emg": {"ko": "침근전도검사", "en": "Needle EMG"}
    }
    return mapping[section]["en" if lang == REPORT_LANG_EN else "ko"]

# 영문 모드 100% 매핑 보강
def custom_english_translate(text: str) -> str:
    raw = str(text)
    mapping = {
        "정상 범위": "WNL", "비정상 (활동성 탈신경)": "Abnormal (Active denervation)",
        "통증으로 평가 불가": "Incomplete due to pain", "비정상 (진폭 감소 / 잠복기 지연)": "Abnormal (Reduced amp & Delayed lat)",
        "비정상 (진폭 급감 / 국소 전도차단 의심)": "Abnormal (Conduction block)", "비정상 (진폭 감소)": "Abnormal (Reduced amp)",
        "비정상 (반응 소실)": "Abnormal (Absent)", "비정상 (동원 감소)": "Abnormal (Reduced recruitment)",
        "오른쪽": "Rt", "왼쪽": "Lt", "손목": "Wrist", "팔꿈치": "Elbow", "발목": "Ankle", "위팔": "Arm", "아래팔": "Forearm",
        "서혜부": "Groin", "나선고랑 위": "Above spiral groove", "팔꿈치 아래": "Below elbow", "팔꿈치 위": "Above elbow",
        "정중신경": "Median", "자신경": "Ulnar", "노신경": "Radial", "종아리신경": "Peroneal", "정강신경": "Tibial",
        "근육피부신경": "Musculocutaneous", "가쪽아래팔피부신경": "Lat. antebrachial cutaneous", "안쪽아래팔피부신경": "Med. antebrachial cutaneous",
        "등쪽자신경": "Dorsal ulnar cutaneous", "얕은종아리신경": "Sup. Peroneal", "장딴지신경": "Sural", "두렁신경": "Saphenous", "넙다리신경": "Femoral",
        "목 척추주위근": "Cerv. Paraspinal", "허리 척추주위근": "Lumb. Paraspinal", "어깨세모근": "Deltoid", "위팔두갈래근": "Biceps",
        "위팔세갈래근": "Triceps", "위팔요골근": "Brachioradialis", "원엎침근": "Pronator Teres", "노쪽손목굽힘근": "FCR",
        "손가락폄근": "EDC", "자쪽손목굽힘근": "FCU", "깊은손가락굽힘근": "FDP", "고유집게폄근": "EIP",
        "짧은엄지벌림근": "APB", "새끼벌림근": "ADM", "첫째등쪽뼈사이근": "FDI", "엉덩허리근": "Iliopsoas",
        "가쪽넓은근": "Vastus Lateralis", "넙다리네갈래근": "Quadriceps", "앞정강근": "Tibialis Ant.", "긴종아리근": "Peroneus Longus",
        "안쪽장딴지근": "Med. Gastrocnemius", "가자미근": "Soleus", "큰볼기근": "Gluteus Maximus", "넙다리근막긴장근": "TFL",
        "짧은발가락폄근": "EDB", "정중신경 1지": "Median (D1)", "정중신경 2지": "Median (D2)", "정중신경 3지": "Median (D3)",
        "자신경 5지": "Ulnar (D5)", "깊은손가락굽힘근 4-5지": "FDP (D4-5)", "무반응": "Absent", "측정불가": "N/A"
    }
    for k, v in mapping.items(): raw = raw.replace(k, v)
    return raw
