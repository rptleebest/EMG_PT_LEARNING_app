# data/cases.py

"""
물리치료학과 학생 교육용 대표 근전도 사례 라이브러리.

구성:
- 총 11개 대표 사례 전체 수록
- NCS 감각신경 가지(Branch)별 중복 데이터 제거 및 대표 신경으로 간소화
- 실제 임상 수치(진폭, 잠복기 등)가 포함된 3단 데이터 구조 적용
- NCS/EMG 내부 판독 코드는 data.terms의 표준 상수를 사용
"""

from data.terms import (
    EMG_NORMAL, EMG_ACTIVE_DENERVATION, EMG_PARASPINAL_DENERVATION,
    EMG_CHRONIC_REINNERVATION, EMG_ACTIVE_CHRONIC, NCS_NORMAL,
    NCS_DELAYED, NCS_REDUCED, NCS_ABSENT, FWAVE_DELAYED_ABSENT,
    H_REFLEX_HYPERACTIVE, H_M_RATIO_INCREASED, BLINK_DELAYED,
    BLINK_DELAYED_ABSENT,
)

CASE_LIBRARY = {
    "목-팔 통증 증상과 팔 근력 약화": {
        "category": "목 신경뿌리병증(Cervical radiculopathy)",
        "difficulty": "초중급",
        "patient": {
            "age": 57, "sex": "남성", "side": "오른쪽",
            "symptoms": ["뒷목(Cervical)에서 오른쪽 어깨와 아래팔 노쪽, 엄지손가락 쪽으로 뻗치는 통증과 저림이 지속됨", "최근 팔꿉관절 굽힘 및 손목관절 폄 동작 시 힘이 빠지는 현상 발생"],
            "physical_exam": {
                "감각 검사": ["아래팔 노쪽 및 엄지/검지 쪽 감각 저하. C6 피부분절 분포와 일치함"],
                "맨손근력검사(MMT)": ["팔꿉관절 굽힘근: Fair (3/5) - 근육피부신경(C5-C6)", "손목관절 폄근: Fair (3/5) - 노신경(C6-C7)", "팔꿉관절 폄근: Normal (5/5) - 노신경(C7-C8)"],
                "반사 검사": ["위팔노근 반사(C6): 감소(DRT 1+)", "위팔두갈래근 반사(C5): 정상(DRT 2+)"],
            },
        },
        "findings": {
            "노신경 감각 (Radial SNAP)": ("20 μV", "2.1 ms", NCS_NORMAL),
            "가쪽아래팔피부신경 감각 (Lat. Antebrachial SNAP)": ("19 μV", "2.2 ms", NCS_NORMAL),
            "근육피부신경 운동 (Musculocutaneous CMAP)": ("5.8 mV", "2.1 ms", NCS_NORMAL),
            "노신경 운동 (Radial CMAP)": ("6.5 mV", "2.5 ms", NCS_NORMAL),
            "목 척추주위근 (Cervical Paraspinal)": ("Fibrillation/PSW", "통증으로 평가 불가", EMG_PARASPINAL_DENERVATION),
            "위팔두갈래근 (Biceps Brachii)": ("Fibrillation/PSW", "Reduced recruitment", EMG_ACTIVE_DENERVATION),
            "노쪽손목폄근 (Extensor Carpi Radialis)": ("Fibrillation/PSW", "Reduced recruitment", EMG_ACTIVE_DENERVATION),
        },
        "teaching_diagnosis": {
            "summary": "C6 중심의 목 신경뿌리병증(Cervical radiculopathy) 패턴입니다.",
            "ncs_reason": [
                "감각신경활동전위(SNAP)가 정상 범위로 완전히 보존됩니다. 목 신경뿌리병증은 뒤뿌리신경절(DRG)보다 몸쪽에 병변이 위치하므로, 말초 감각신경전도는 정상 범위로 도출됩니다.",
                "운동신경전도검사(Motor NCS)가 정상 범위이므로 말초 신경얼기 혹은 단일 신경병증 가능성은 낮습니다."
            ],
            "emg_reason": [
                "목 척추주위근, 위팔두갈래근, 노쪽손목폄근에서 활동성 탈신경(Active denervation)을 의미하는 자발전위가 관찰됩니다.",
                "가장 근위부인 C6 척추주위근의 이상 소견은 병변이 척수 신경뿌리임을 확진하는 핵심 지표입니다."
            ],
            "integration": ["C6 피부분절 감각 저하, 위팔노근 반사 감소, 그리고 C6 지배 하위 말초근육과 척추주위근의 동시 탈신경을 종합하여 C6 신경뿌리병증으로 판단합니다."],
        },
        "differential_diagnosis": [
            {
                "name": "노신경병증(Radial neuropathy)", 
                "why_consider": "손목 폄 약화와 노쪽 감각 이상이 동반되어 혼동하기 쉽습니다.",
                "how_to_differentiate": "노신경병증이라면 노신경 감각전도 진폭 감소가 수반되며, 목 척추주위근 침근전도는 정상이 유지되어야 합니다.",
                "practical_tip": "손목관절 폄 마비 환자 평가 시, 표재노신경 감각전도의 보존 여부와 목 척추주위근의 이상 방전 감별이 임상 판단의 핵심입니다."
            }
        ],
    },

    "야간 손저림과 엄지 근력 약화": {
        "category": "말초 포착신경병증",
        "difficulty": "초중급",
        "patient": {
            "age": 46, "sex": "여성", "side": "오른쪽",
            "symptoms": ["오른손 1~3번째 손가락 중심의 저림이 야간에 심함", "최근 엄지손가락 벌림 동작 시 힘 빠짐 발생"],
            "physical_exam": {
                "감각 검사": ["엄지, 검지, 중지 손바닥쪽 감각 둔화. 정중신경 분포와 일치"],
                "맨손근력검사(MMT)": ["엄지손가락 벌림근: Good (4/5) - 정중신경(C8-T1)"],
                "반사 검사": ["특수 검사: 팔렌 검사 양성, 손목 정중신경 티넬 징후 양성"],
            },
        },
        "findings": {
            "정중신경 감각 (Median SNAP)": ("9 μV (감소)", "4.9 ms (지연)", NCS_DELAYED),
            "정중신경 운동 (Median CMAP)": ("4.5 mV (감소)", "5.8 ms (지연)", NCS_REDUCED),
            "짧은엄지벌림근 (Abductor Pollicis Brevis)": ("Silent", "Normal recruitment", EMG_NORMAL),
        },
        "teaching_diagnosis": {
            "summary": "손목굴증후군(Carpal tunnel syndrome)을 시사하는 정중신경 포착병증입니다.",
            "ncs_reason": [
                "정중신경 감각전도 잠복기 지연은 손목굴 내 국소 말이집탈락(Demyelination)성 전도 지연을 지시합니다.",
                "운동 진폭 감소가 동반된 것은 신경 압박에 따른 운동 축삭 손상이 일부 진행되고 있음을 뜻합니다."
            ],
            "emg_reason": [
                "정중신경 말단 지배인 짧은엄지벌림근에서 비정상 자발전위가 없는 것(Silent)은, 아직 축삭이 완전히 손상되거나 마비에 이르지 않은 상태임을 의미합니다."
            ],
            "integration": ["야간 통증 저림, 정중신경 분포 감각 저하, 전도 지연 데이터를 통합하여 손목굴증후군으로 해석합니다."],
        },
        "differential_diagnosis": [
            {
                "name": "몸쪽 정중신경병증(Proximal median neuropathy)", 
                "why_consider": "정중신경 지배 영역의 근력 저하 및 손가락 저림이 매우 흡사합니다.",
                "how_to_differentiate": "원엎침근 등 손목 상부 정중신경 지배 근육들의 근전도가 정상이므로 압박 부위는 손목 수준으로 국한됩니다.",
                "practical_tip": "포착 신경병증 감별 시, 포착 의심 경계선보다 더 몸쪽(Proximal)에서 기시하는 근육들의 정상 전기활동 보존 여부를 확인하십시오."
            }
        ],
    },

    "위팔뼈 몸통 골절 후 손목처짐": {
        "category": "말초 포착신경병증",
        "difficulty": "초중급",
        "patient": {
            "age": 34, "sex": "남성", "side": "오른쪽",
            "symptoms": ["위팔뼈 몸통 골절 병력 있음", "골절 수술 직후부터 손목처짐(Wrist drop) 현상 발생"],
            "physical_exam": {
                "감각 검사": ["손등 노쪽 영역 감각 소실. 노신경 분포와 일치함"],
                "맨손근력검사(MMT)": ["손목관절 폄근: Poor (2/5)", "손가락 폄근: Poor (2/5)", "팔꿉관절 폄근: Normal (5/5)"],
                "반사 검사": ["위팔세갈래근 반사: 정상(DRT 2+)", "위팔노근 반사: 감소(DRT 1+)"],
            },
        },
        "findings": {
            "노신경 감각 (Radial SNAP)": ("8 μV (감소)", "3.2 ms (지연)", NCS_REDUCED),
            "노신경 운동 (Radial CMAP)": ("1.5 mV (급감)", "7.1 ms (지연)", NCS_REDUCED),
            "노쪽손목폄근 (Extensor Carpi Radialis)": ("Fibrillation/PSW", "Reduced recruitment", EMG_ACTIVE_DENERVATION),
            "집게폄근 (Extensor Indicis Proprius)": ("Fibrillation/PSW", "Reduced recruitment", EMG_ACTIVE_DENERVATION),
            "목 척추주위근 (Cervical Paraspinal)": ("Silent", "Normal recruitment", EMG_NORMAL),
        },
        "teaching_diagnosis": {
            "summary": "위팔뼈 나선고랑(Spiral groove) 부위의 노신경병증(Radial neuropathy)입니다.",
            "ncs_reason": [
                "노신경 감각 진폭 감소는 병변이 뒤뿌리신경절 먼쪽의 말초신경계 마비임을 가리키며, 운동 진폭 저하는 나선고랑 통과 구간의 운동 축삭 손상을 대변합니다."
            ],
            "emg_reason": [
                "나선고랑 하부 지배근(노쪽손목폄근, 집게폄근)에서 활동성 탈신경 소견을 보입니다.",
                "목 척추주위근은 온전히 보존되어 있어 경추 신경뿌리병증을 배제합니다."
            ],
            "integration": ["팔꿉관절 폄 기능 보존 대비 먼쪽 손목/손가락 폄 마비, 노신경 전도 감소, 목 척추주위근 정상 소견을 융합하여 외상성 노신경병증으로 해석합니다."],
        },
        "differential_diagnosis": [
            {
                "name": "뒤뼈사이신경병증(Posterior interosseous neuropathy)", 
                "why_consider": "손가락 및 손목관절 폄 근력 저하가 매우 유사하게 관찰됩니다.",
                "how_to_differentiate": "뒤뼈사이신경은 노신경의 순수 운동 분지이므로, 이 질환이라면 노신경 감각 전도는 완전 정상 범위로 기록되어야 합니다.",
                "practical_tip": "손목 마비 환자에서 표재노신경 감각의 보존 여부가 노신경 주간 경로 마비와 먼쪽 심부 운동 분지 마비를 감별하는 핵심입니다."
            }
        ],
    },

    "4, 5번째 손가락 저림과 손가락 근력 약화": {
        "category": "말초 포착신경병증",
        "difficulty": "초중급",
        "patient": {
            "age": 42, "sex": "남성", "side": "오른쪽",
            "symptoms": ["우측 4, 5번째 손가락 감각 이상 및 새끼손가락 손날 통증", "최근 젓가락질 시 손가락 미세 동작 약화"],
            "physical_exam": {
                "감각 검사": ["반지손가락 자쪽 절반 및 새끼손가락 감각 저하"],
                "맨손근력검사(MMT)": ["새끼손가락 벌림근: Fair (3/5)", "손가락 벌림/모음근: Fair (3/5)"],
                "반사 검사": ["특수 검사: 팔꿈치굴 주행 부위 티넬 징후 양성"],
            },
        },
        "findings": {
            "자신경 감각 (Ulnar SNAP)": ("9 μV (감소)", "3.4 ms (지연)", NCS_DELAYED),
            "자신경 운동 (Ulnar CMAP)": ("3.1 mV (감소)", "8.2 ms (지연)", NCS_REDUCED),
            "새끼벌림근 (Abductor Digiti Minimi)": ("Fibrillation/PSW", "Reduced recruitment", EMG_ACTIVE_DENERVATION),
            "첫째등쪽뼈사이근 (First Dorsal Interosseous)": ("Fibrillation/PSW", "Reduced recruitment", EMG_ACTIVE_DENERVATION),
        },
        "teaching_diagnosis": {
            "summary": "팔꿈치굴증후군(Cubital tunnel syndrome)으로 대표되는 팔꿈치 부위 자신경병증입니다.",
            "ncs_reason": [
                "자신경 감각 전도 지연은 팔꿈치굴 구간 내 국소 말이집탈락성 병변을 가리키며, 운동 진폭 저하는 포착 부위 하단의 운동 축삭 손상을 뜻합니다."
            ],
            "emg_reason": [
                "자신경 하위 지배근인 새끼벌림근과 뼈사이근에서 활동성 탈신경 비정상 자발전위가 도출되어, 압박으로 인한 먼쪽 운동 축삭 변성을 지시합니다."
            ],
            "integration": ["자신경 국한 감각 이상 및 마비, 자신경 전도 지연 및 침근전도 이상 소견을 융합하여 팔꿈치굴증후군으로 진단합니다."],
        },
        "differential_diagnosis": [
            {
                "name": "C8-T1 목 신경뿌리병증(Cervical radiculopathy)", 
                "why_consider": "손 내재근 약화 분절이 C8-T1 영역과 일치하여 자신경 마비와 흡사합니다.",
                "how_to_differentiate": "목 신경뿌리병증은 동일 분절의 정중신경 지배 손가락 근육들도 전반적으로 침범되며, 자신경 감각전도는 대개 보존됩니다.",
                "practical_tip": "아귀 힘이 빠질 때 정중/자신경의 감각전도를 상호 비교하는 것이 목 디스크와 팔꿈치 포착 병변의 감별 잣대입니다."
            }
        ],
    },

    "허리-다리 통증과 발처짐": {
        "category": "허리 신경뿌리병증(Lumbar radiculopathy)",
        "difficulty": "초중급",
        "patient": {
            "age": 61, "sex": "여성", "side": "오른쪽",
            "symptoms": ["허리에서 우측 엉치, 종아리 가쪽, 발등으로 뻗치는 방사통", "최근 보행 시 발끝이 바닥에 끌리는 발처짐(Foot drop) 발생"],
            "physical_exam": {
                "감각 검사": ["종아리 가쪽 및 발등 중앙 부위 감각 둔화. L5 피부분절 범위"],
                "맨손근력검사(MMT)": ["발목관절 등굽힘근: Fair (3/5)", "엄지발가락 폄근: Poor (2/5)", "엉덩관절 벌림근: Good (4/5)"],
                "반사 검사": ["무릎반사(L4): 정상", "아킬레스힘줄반사(S1): 정상"],
            },
        },
        "findings": {
            "얕은종아리신경 감각 (Superficial Peroneal SNAP)": ("15 μV", "2.8 ms", NCS_NORMAL),
            "종아리신경 운동 (Peroneal CMAP)": ("4.8 mV", "4.2 ms", NCS_NORMAL),
            "허리 척추주위근 (Lumbar Paraspinal)": ("Fibrillation/PSW", "통증으로 평가 불가", EMG_PARASPINAL_DENERVATION),
            "앞정강근 (Tibialis Anterior)": ("Fibrillation/PSW", "Reduced recruitment", EMG_ACTIVE_DENERVATION),
            "긴엄지폄근 (Extensor Hallucis Longus)": ("Fibrillation/PSW", "Reduced recruitment", EMG_ACTIVE_DENERVATION),
            "중간볼기근 (Gluteus Medius)": ("Fibrillation/PSW", "Reduced recruitment", EMG_ACTIVE_DENERVATION),
        },
        "teaching_diagnosis": {
            "summary": "발처짐(Foot drop)을 동반한 L5 허리 신경뿌리병증(Lumbar radiculopathy) 패턴입니다.",
            "ncs_reason": [
                "발처짐 증상에도 불구하고 얕은종아리신경 감각 진폭이 정상 보존됩니다. 이는 감각 세포체보다 근위부인 척수 신경뿌리 압박을 의미합니다."
            ],
            "emg_reason": [
                "가장 중요한 지표로 가장 근위부인 허리 척추주위근에서 비정상 자발전위가 검출되었습니다.",
                "L5 분절을 공유하는 앞정강근, 긴엄지폄근, 중간볼기근에서 공통적인 탈신경이 관찰되어 L5 레벨을 확진합니다."
            ],
            "integration": ["L5 감각 저하, 중간볼기근 약화 동반, 감각전도 보존 및 허리 척추주위근 탈신경을 종합하여 L5 신경뿌리병증으로 진단합니다."],
        },
        "differential_diagnosis": [
            {
                "name": "온종아리신경병증(Common peroneal neuropathy)", 
                "why_consider": "발목을 들어올리지 못하는 발처짐(Foot drop) 양상이 매우 비슷합니다.",
                "how_to_differentiate": "온종아리신경 압박 마비라면 얕은종아리신경 감각전도가 대폭 감소하며, 중간볼기근과 척추주위근은 반드시 정상이어야 합니다.",
                "practical_tip": "발처짐(Foot drop) 환자 감별 시 엉덩관절 벌림(중간볼기근) 근력의 보존 여부를 반드시 확인하십시오."
            }
        ],
    },

    "정강뼈 골절로 석고붕대 후 발처짐과 발등 감각저하": {
        "category": "말초 포착신경병증",
        "difficulty": "초중급",
        "patient": {
            "age": 31, "sex": "남성", "side": "왼쪽",
            "symptoms": ["정강뼈 골절 부위 석고붕대 유지 이력", "석고붕대 제거 직후 좌측 발처짐과 발등 감각 소실 발견"],
            "physical_exam": {
                "감각 검사": ["종아리 가쪽 및 발등 부위 감각 소실"],
                "맨손근력검사(MMT)": ["발목 등굽힘근: Poor (2/5)", "발목 가쪽번짐근: Poor (2/5)", "발목 안쪽번짐근: Normal (5/5)"],
                "반사 검사": ["무릎반사 및 아킬레스힘줄반사: 대칭적 정상"],
            },
        },
        "findings": {
            "얕은종아리신경 감각 (Superficial Peroneal SNAP)": ("6 μV (감소)", "4.1 ms (지연)", NCS_REDUCED),
            "종아리신경 운동 (Peroneal CMAP)": ("1.2 mV (급감)", "8.5 ms (지연)", NCS_REDUCED),
            "앞정강근 (Tibialis Anterior)": ("Fibrillation/PSW", "Reduced recruitment", EMG_ACTIVE_DENERVATION),
            "긴종아리근 (Peroneus Longus)": ("Fibrillation/PSW", "Reduced recruitment", EMG_ACTIVE_DENERVATION),
            "허리 척추주위근 (Lumbar Paraspinal)": ("Silent", "Normal recruitment", EMG_NORMAL),
        },
        "teaching_diagnosis": {
            "summary": "종아리뼈머리(Fibular head) 압박으로 인한 온종아리신경 마비(Common peroneal neuropathy)입니다.",
            "ncs_reason": [
                "얕은종아리신경 감각과 종아리신경 운동 전도의 동시 진폭 감소는 무릎 가쪽 부위의 심한 기계적 압박을 입증합니다."
            ],
            "emg_reason": [
                "종아리뼈머리 하부에 위치한 앞정강근, 긴종아리근에서 비정상 탈신경 자발 활동이 관찰됩니다.",
                "척추주위근은 완전히 보존되어 있어 신경뿌리병증을 배제할 수 있습니다."
            ],
            "integration": ["골절 부목 고정력, 정강신경(안쪽번짐) 기능 보존, 종아리 신경 전도 저하를 종합하여 압박성 온종아리신경 마비로 정의합니다."],
        },
        "differential_diagnosis": [
            {
                "name": "L5 허리 신경뿌리병증(Lumbar radiculopathy)", 
                "why_consider": "발처짐 및 발등 감각 이상 양상이 매우 비슷합니다.",
                "how_to_differentiate": "L5 뿌리병증은 감각신경전도가 정상 보존되며 허리 척추주위근에 탈신경이 뚜렷하게 도출되어야 합니다.",
                "practical_tip": "뒤정강근이 분담하는 안쪽번짐(Ankle inversion) 기능 보존 여부가 L5 마비와 말초 종아리신경 마비를 가르는 핵심 열쇠입니다."
            }
        ],
    },

    "골반 외상 후 다리 전반 근력 약화": {
        "category": "신경얼기병증(Plexopathy)",
        "difficulty": "중급",
        "patient": {
            "age": 45, "sex": "여성", "side": "왼쪽",
            "symptoms": ["골반 골절 수술 후 좌측 다리 전반의 심한 근력 약화", "허벅지부터 종아리, 발등까지 광범위한 감각 둔화"],
            "physical_exam": {
                "감각 검사": ["여러 피부분절을 넘는 광범위 감각 소실"],
                "맨손근력검사(MMT)": ["엉덩관절 굽힘근: Poor (2/5)", "무릎관절 폄근: Poor (2/5)", "발목 등굽힘근: Trace (1/5)"],
                "반사 검사": ["무릎반사(L4) 및 아킬레스힘줄반사(S1): 좌측 완전 소실"],
            },
        },
        "findings": {
            "장딴지신경 감각 (Sural SNAP)": ("6 μV (감소)", "4.2 ms (지연)", NCS_REDUCED),
            "종아리신경 운동 (Peroneal CMAP)": ("1.5 mV (감소)", "6.5 ms (지연)", NCS_REDUCED),
            "넓적다리신경 운동 (Femoral CMAP)": ("2.0 mV (감소)", "5.5 ms (지연)", NCS_REDUCED),
            "가쪽넓은근 (Vastus Lateralis)": ("Fibrillation/PSW", "Reduced recruitment", EMG_ACTIVE_DENERVATION),
            "앞정강근 (Tibialis Anterior)": ("Fibrillation/PSW", "Reduced recruitment", EMG_ACTIVE_DENERVATION),
            "허리 척추주위근 (Lumbar Paraspinal)": ("Silent", "Normal recruitment", EMG_NORMAL),
        },
        "teaching_diagnosis": {
            "summary": "외상과 관련된 허리엉치신경얼기병증(Lumbosacral plexopathy) 패턴입니다.",
            "ncs_reason": [
                "장딴지신경, 넓적다리신경 등 복수의 다른 말초 전도에서 진폭 감소가 확인됩니다. 이는 감각세포체 먼쪽의 골반 내 신경얼기 장애를 의미합니다."
            ],
            "emg_reason": [
                "다리 전체 여러 근육에서 광범위하게 탈신경 활동이 관찰됩니다.",
                "그러나 척수와 가장 가까운 척추주위근은 정상으로 보존되어 있어 다발 신경뿌리가 아닌 얼기 수준의 손상임을 입증합니다."
            ],
            "integration": ["골반 골절 수술력, 다리 광범위 근력저하, 다발성 전도 저하, 척추주위근 정상 소견을 종합하여 신경얼기 마비로 진단합니다."],
        },
        "differential_diagnosis": [
            {
                "name": "다발 허리 신경뿌리병증(Lumbar radiculopathy)", 
                "why_consider": "복수 척수 분절의 동시 약화와 깊은힘줄 반사 소실이 나타나 혼동하기 쉽습니다.",
                "how_to_differentiate": "다발 신경뿌리병증은 감각신경전도가 정상 범위로 유지되며, 허리 척추주위근에서 다발성 탈신경이 명확하게 나타납니다.",
                "practical_tip": "다리 전반의 광범위 마비 양상 시, 척추주위근 침범 유무와 감각신경 진폭 저하 여부가 감별의 핵심 척도입니다."
            }
        ],
    },

    "양측 발끝 저림과 발가락 약화": {
        "category": "다발신경병증(Polyneuropathy)",
        "difficulty": "초중급",
        "patient": {
            "age": 67, "sex": "남성", "side": "양쪽",
            "symptoms": ["당뇨병 병력", "양쪽 발끝에서 발목 위로 서서히 올라오는 대칭성 저림"],
            "physical_exam": {
                "감각 검사": ["양측 대칭적인 장갑-양말형(Glove-stocking) 감각 저하"],
                "맨손근력검사(MMT)": ["양측 엄지발가락 폄근/굽힘근: Good (4/5)"],
                "반사 검사": ["양측 아킬레스힘줄반사: 소실(0)", "양측 무릎반사: 보존"],
            },
        },
        "findings": {
            "장딴지신경 감각 (Sural SNAP)": ("무반응 (소실)", "측정불가", NCS_ABSENT),
            "얕은종아리신경 감각 (Superficial Peroneal SNAP)": ("무반응 (소실)", "측정불가", NCS_ABSENT),
            "정강신경 운동 (Tibial CMAP)": ("1.8 mV (감소)", "6.2 ms (지연)", NCS_REDUCED),
            "앞정강근 (Tibialis Anterior)": ("Fibrillation/PSW", "Giant MUAPs", EMG_ACTIVE_CHRONIC),
        },
        "teaching_diagnosis": {
            "summary": "길이 의존성 축삭성 다발신경병증(Length-dependent axonal polyneuropathy) 패턴입니다.",
            "ncs_reason": [
                "가장 긴 신경인 다리 말단부 감각 반응이 소실되고 운동 진폭이 감소하는 전형적인 전신성 축삭 손상 패턴입니다."
            ],
            "emg_reason": [
                "앞정강근에서 탈신경 자발전위와 만성 회복 지표인 거대운동단위활동전위(Giant MUAPs)가 대칭적으로 유도되어 만성 축삭 파괴와 회복을 시사합니다."
            ],
            "integration": ["당뇨 병력, 대칭성 먼쪽 감각 저하, 원위부 신경전도 감소 데이터를 종합하여 다발신경병증으로 해석합니다."],
        },
        "differential_diagnosis": [
            {
                "name": "말이집탈락성 다발신경병증(Demyelinating polyneuropathy)", 
                "why_consider": "상하 대칭적인 다발성 신경 침범 양상이 매우 유사합니다.",
                "how_to_differentiate": "말이집탈락성은 진폭 저하보다는 극심한 전도 잠복기 지연과 전도속도 저하가 선행합니다.",
                "practical_tip": "다발성 다리 마비 환자 판독 시 진폭 감소(축삭성)가 우선인지, 잠복기 지연(말이집탈락성)이 우선인지 구분하십시오."
            }
        ],
    },

    "대칭성 팔다리 근력저하와 보행 저하": {
        "category": "다발신경병증(Polyneuropathy)",
        "difficulty": "중급",
        "patient": {
            "age": 55, "sex": "여성", "side": "양쪽",
            "symptoms": ["몇 달간 양쪽 손발이 대칭적으로 둔함", "계단 오르기와 발목 움직임 진행성 약화"],
            "physical_exam": {
                "감각 검사": ["양측 팔다리 먼쪽의 대칭적인 감각 탈락"],
                "맨손근력검사(MMT)": ["양측 어깨 벌림근: Fair (3/5)", "양측 손목 및 발목 폄근: Fair (3/5)"],
                "반사 검사": ["전신 깊은힘줄 반사: 완전 소실(0)"],
            },
        },
        "findings": {
            "정중신경 감각 (Median SNAP)": ("12 μV (감소)", "6.8 ms (지연)", NCS_DELAYED),
            "자신경 감각 (Ulnar SNAP)": ("14 μV (감소)", "6.5 ms (지연)", NCS_DELAYED),
            "정중신경 운동 (Median CMAP)": ("6.5 mV", "9.2 ms (지연)", NCS_DELAYED),
            "종아리신경 운동 (Peroneal CMAP)": ("4.2 mV", "11.5 ms (지연)", NCS_DELAYED),
            "정강/종아리신경 F파 (F-wave)": ("무반응 (소실)", "측정불가", FWAVE_DELAYED_ABSENT),
            "앞정강근 (Tibialis Anterior)": ("Silent", "Normal recruitment", EMG_NORMAL),
        },
        "teaching_diagnosis": {
            "summary": "만성 염증성 말이집탈락성 다발신경병증(CIDP) 양상입니다.",
            "ncs_reason": [
                "다수의 전도에서 진폭은 보존되나 잠복기가 극심하게 지연되는 다발성 말이집탈락성 변화가 나타납니다.",
                "F파 소실은 근위 전도부의 신경 말이집 손상을 직접 시사합니다."
            ],
            "emg_reason": [
                "침근전도에서 탈신경 자발 활동이 전혀 없는 전기적 침묵(Silent)이 나타나, 축삭 단절이 동반되지 않은 순수 탈말이집 상태임을 입증합니다."
            ],
            "integration": ["근/원위부 동시 마비, 전신 무반사, 다발성 잠복기 지연 및 정상 침근전도를 종합하여 CIDP로 판단합니다."],
        },
        "differential_diagnosis": [
            {
                "name": "근육병증(Myopathy)", 
                "why_consider": "어깨 및 엉덩관절 등 몸쪽(Proximal) 약화 기전이 유사하여 혼동을 초래합니다.",
                "how_to_differentiate": "근육병증은 말단 감각 소실이 없으며 신경전도 잠복기 지연이 나타나지 않습니다.",
                "practical_tip": "감각의 보존 여부와 전신 무반사(Areflexia)의 대조가 신경병과 근육병 감별의 기준선입니다."
            }
        ],
    },

    "눈꺼풀 떨림과 눈 주위 불편감 지속": {
        "category": "뇌신경/반사경로",
        "difficulty": "중급",
        "patient": {
            "age": 62, "sex": "여성", "side": "오른쪽",
            "symptoms": ["우측 눈꺼풀 주변 간헐적 떨림", "우측 눈 가쪽 촉각 저하"],
            "physical_exam": {
                "얼굴 표정근 관찰": ["이마 주름잡기, 눈 감기: 양측 대칭성 정상"],
                "뇌신경 감각 검사": ["우측 이마 및 눈 주변(삼차신경 V1) 촉각 감소"],
                "반사 검사": ["우측 각막반사: 저하 관찰"],
            },
        },
        "findings": {
            "우측 자극-우측 R1 (동측 단일시냅스)": ("잠복기 지연 (지연)", "14.8 ms", BLINK_DELAYED),
            "우측 자극-우측 R2 (동측 다시냅스)": ("반응 소실 (소실)", "측정불가", BLINK_DELAYED_ABSENT),
            "우측 자극-좌측 R2 (대측 다시냅스)": ("반응 소실 (소실)", "측정불가", BLINK_DELAYED_ABSENT),
            "좌측 자극-좌측 R1 (동측 단일시냅스)": ("정상 유발", "10.4 ms", NCS_NORMAL),
            "좌측 자극-좌측 R2 (동측 다시냅스)": ("정상 유발", "32.1 ms", NCS_NORMAL),
            "좌측 자극-우측 R2 (대측 다시냅스)": ("정상 유발", "31.8 ms", NCS_NORMAL),
        },
        "teaching_diagnosis": {
            "summary": "우측 삼차신경(Trigeminal nerve) 들신경 경로(Afferent limb) 손상입니다.",
            "ncs_reason": [
                "우측 자극 시 우측 R1, 우측 R2, 좌측 R2가 모두 반사 유발 소실되거나 지연됩니다.",
                "좌측 자극 시 우측 R2 반사 반응까지 정상 도출되어 운동을 지시하는 얼굴신경은 보존됨을 확증합니다."
            ],
            "emg_reason": [
                "반사궁 회로 전도 결손만을 평가하는 증례로 환자 보호를 위해 침근전도는 배제되었습니다."
            ],
            "integration": ["우측 V1 가지 촉각 저하 및 우측 자극 시에만 나타나는 양측 반사 지연을 종합하여 삼차신경 들신경 장애로 판독합니다."],
        },
        "differential_diagnosis": [
            {
                "name": "우측 얼굴신경병증(Facial neuropathy)", 
                "why_consider": "눈 감기 불편감과 얼굴 불편감이 얼굴마비 초기와 혼동될 수 있습니다.",
                "how_to_differentiate": "우측 얼굴신경(운동) 마비라면 좌측 자극 시 우측 눈 감기 반응(우측 R2)이 소실되어야 합니다.",
                "practical_tip": "눈깜빡반사(Blink reflex) 판독 시 전기 자극을 준 쪽이 문제인지, 반응을 하는 눈꺼풀 근육 쪽이 문제인지 비교해서 확인하세요."
            }
        ],
    },

    "뇌졸중 환자 발목 경직 평가": {
        "category": "중추성 반사이상 (정량적 평가)",
        "difficulty": "중급",
        "patient": {
            "age": 68, "sex": "남성", "side": "오른쪽",
            "symptoms": ["뇌졸중 편마비 상태, 우측 발목 발바닥굽힘근 중증 경직", "보행 제한으로 물리치료 전/후 경직 완화 효과 정량 모니터링"],
            "physical_exam": {
                "근긴장도 검사(MAS)": ["우측 MAS: 3등급(치료 전) -> 2등급(치료 후)"],
                "반사 검사": ["아킬레스힘줄반사: 우측 비정상적 항진", "발목간대경련: 관찰"],
            },
        },
        "findings": {
            "우측 가자미근 H-반사 진폭 (물리치료 전)": ("7.2 mV (항진)", "비정상 과항진", H_REFLEX_HYPERACTIVE),
            "우측 가자미근 H-반사 진폭 (물리치료 후)": ("5.1 mV (감소)", "유의미하게 감소", NCS_NORMAL),
            "우측 가자미근 H/M ratio (물리치료 전)": ("65% (초과)", "정상 기준치 < 40%", H_M_RATIO_INCREASED),
            "우측 가자미근 H/M ratio (물리치료 후)": ("55% (감소)", "경직 일부 완화", NCS_NORMAL),
        },
        "teaching_diagnosis": {
            "summary": "물리치료 중재(지속적 스트레칭 및 대항근 전기자극) 적용 후 우측 가자미근의 척수반사 흥분성 감소 및 경직 완화 효과가 일부 나타난 것으로 평가됩니다.",
            "ncs_reason": [
                "물리치료 적용 전 H/M 비율(ratio)이 65%로 매우 높게 나타난 것은 대뇌-척수 상부 억제계 상실로 우측 가자미근 알파운동신경세포(Alpha motor neuron)의 흥분성이 정상 범위를 초과해 비정상적으로 항진되어 있었음을 의미합니다.",
                "일정기간 스트레칭 및 보행과 함께 적용된 대항근(앞정강근) 기능적 전기자극(FES) 적용 후, H/M 비율이 55%로 소폭 감소하여 척수 반사회로의 과흥분성이 일부 완화된 것으로 평가됩니다."
            ],
            "integration": [
                "MAS 3등급의 보행 제한 환자에게 물리치료를 적용한 후, H-반사의 진폭 감소 및 H/M 비율의 감소(65%에서 55%)를 통해 소폭의 경직 완화를 확인합니다."
            ]
        }
    }
}
