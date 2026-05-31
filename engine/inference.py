# engine/inference.py

from collections import defaultdict
from typing import Dict, Tuple, Any, List

# 기존 사례들의 텍스트를 학생용/신용어 표준 텍스트로 정규화
TEXT_NORMALIZATION_MAP = {
    "정상 범위(within normal limits)": "정상 범위(within normal limits)",
    "정상 (Normal)": "정상 범위(within normal limits)",
    "normal": "정상 범위(within normal limits)",
    "Normal": "정상 범위(within normal limits)",
    "정상": "정상 범위(within normal limits)",

    "잠복기 지연(delayed latency)": "잠복기 지연(delayed latency) - 말이집탈락성/포착 시사",
    "잠복기 지연 (Delayed latency)": "잠복기 지연(delayed latency) - 말이집탈락성/포착 시사",
    "delayed": "잠복기 지연(delayed latency) - 말이집탈락성/포착 시사",
    "지연 (Delayed)": "잠복기 지연(delayed latency) - 말이집탈락성/포착 시사",
    "잠복기 지연": "잠복기 지연(delayed latency) - 말이집탈락성/포착 시사",

    "진폭 감소(reduced amplitude)": "진폭 감소(reduced amplitude) - 축삭 손상 시사",
    "감소 (Reduced)": "진폭 감소(reduced amplitude) - 축삭 손상 시사",
    "reduced": "진폭 감소(reduced amplitude) - 축삭 손상 시사",
    "진폭 감소": "진폭 감소(reduced amplitude) - 축삭 손상 시사",

    "반응 소실(absent response)": "반응 소실(absent response)",
    "무반응 (No response)": "반응 소실(absent response)",
    "absent": "반응 소실(absent response)",
    "소실 (Absent)": "반응 소실(absent response)",
    "반응 소실": "반응 소실(absent response)",

    "잠복기 지연 또는 반응 소실(delayed or absent response)": "잠복기 지연 또는 반응 소실(delayed or absent response)",
    "지연 또는 소실 (Delayed/Absent)": "잠복기 지연 또는 반응 소실(delayed or absent response)",

    "F파 최소잠복기 지연 또는 소실(delayed or absent F-wave)": "F파 최소잠복기 지연 또는 소실(delayed or absent F-wave)",
    "H-반사 항진 또는 문턱값 감소(hyperactive H-reflex / lower threshold)": "H-반사 항진 또는 문턱값 감소(hyperactive H-reflex) - 위운동신경세포 병변 시사",
    "H/M 비율 증가 가능(increased H/M ratio possible)": "H/M 비율 증가 가능(increased H/M ratio possible)",
    "증가 가능 (May be increased)": "H/M 비율 증가 가능(increased H/M ratio possible)",
    "항진 또는 문턱값 감소 (Hyperactive / lower threshold)": "H-반사 항진 또는 문턱값 감소(hyperactive H-reflex) - 위운동신경세포 병변 시사",

    "휴식 시 전기적 침묵(no motor unit action potential, MUAP), 수의수축 시 정상 운동단위전위(motor unit action potential, MUAP) 동원": "휴식 시 전기적 침묵(electrical silence), 수의수축 시 정상 운동단위 동원패턴",
    "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)": "휴식 시 섬유자발전위(Fibrillation) 및 양성예파(PSW) 관찰",
    "비정상 자발전위 (Fibrillation, Positive sharp wave 등) 출현": "휴식 시 섬유자발전위(Fibrillation) 및 양성예파(PSW) 관찰",
    "휴식 시 섬유자발전위(fibrillation potential) 및 양성예파(positive sharp wave) 관찰": "휴식 시 섬유자발전위(Fibrillation) 및 양성예파(PSW) 관찰",
    "휴식 시 섬유자발전위(fibrillation potential) 및 양성예파(positive sharp wave) 관찰, 수의수축 시 운동단위전위(motor unit action potential, MUAP) 동원 감소 가능": "휴식 시 섬유자발전위 및 양성예파 관찰, 수의수축 시 운동단위 동원 감소",
    "휴식 시 근육다발수축전위(fasciculation potential) 관찰 가능": "휴식 시 근육다발수축전위(fasciculation potentials) 관찰 가능",
    "무반응 / 전기적 침묵 (Electrical silence)": "휴식 시 전기적 침묵(electrical silence), 수의수축 시 정상 운동단위 동원패턴",
}


def normalize_result_text(value: Any) -> str:
    if value is None:
        return ""
    text = str(value).strip()
    return TEXT_NORMALIZATION_MAP.get(text, text)


def is_abnormal(value: Any) -> bool:
    text = normalize_result_text(value)
    return bool(text) and "정상 범위" not in text and "전기적 침묵" not in text


def split_findings_by_domain(
    findings: Dict[str, Tuple[Any, Any]],
    anatomy_map: Dict[str, Dict[str, str]],
) -> Dict[str, Dict[str, Tuple[Any, Any]]]:
    grouped = {
        "sensory": {},
        "motor": {},
        "muscle": {},
        "reflex": {},
        "other": {},
    }

    for item, values in findings.items():
        domain = anatomy_map.get(item, {}).get("domain", "")
        if domain == "sensory":
            grouped["sensory"][item] = values
        elif domain == "motor":
            grouped["motor"][item] = values
        elif domain == "muscle":
            grouped["muscle"][item] = values
        elif domain in {"h_reflex", "h_ratio", "f_wave", "blink"}:
            grouped["reflex"][item] = values
        else:
            grouped["other"][item] = values

    return grouped


def summarize_case_metadata(case_name: str, case: Dict[str, Any]) -> Dict[str, Any]:
    patient = case.get("patient", {})
    symptoms = patient.get("symptoms", [])
    return {
        "case_name": case_name,
        "category": case.get("category", "기타"),
        "difficulty": case.get("difficulty", "기타"),
        "age": patient.get("age", "-"),
        "sex": patient.get("sex", "-"),
        "side": patient.get("side", "-"),
        "chief_summary": symptoms[0] if symptoms else "",
    }


def build_case_report_text(case_name: str, case: Dict[str, Any]) -> str:
    patient = case.get("patient", {})
    teaching = case.get("teaching_diagnosis", {})
    diff_dx = case.get("differential_diagnosis", [])
    findings = case.get("findings", {})

    lines = [
        f"사례명: {case_name}",
        f"범주: {case.get('category', '')}",
        f"난이도: {case.get('difficulty', '')}",
        f"연령/성별/병변측: {patient.get('age', '-')}세 / {patient.get('sex', '-')} / {patient.get('side', '-')}",
        "",
        "[주요 증상]",
    ]

    for s in patient.get("symptoms", []):
        lines.append(f"- {s}")

    lines.extend(["", "[이학적 검사]"])
    for sec, items in patient.get("physical_exam", {}).items():
        lines.append(sec)
        for i in items:
            lines.append(f"  - {i}")

    lines.extend(["", "[전기진단 소견]"])
    for item, values in findings.items():
        left = values[0] if len(values) > 0 else ""
        right = values[1] if len(values) > 1 else ""
        if str(right).strip():
            lines.append(f"- {item}")
            lines.append(f"  좌측: {normalize_result_text(left)}")
            lines.append(f"  우측: {normalize_result_text(right)}")
        else:
            lines.append(f"- {item}: {normalize_result_text(left)}")

    lines.extend(["", "[교육용 진단 요약]", teaching.get("summary", ""), "", "[NCS 해석 포인트]"])
    for x in teaching.get("ncs_reason", []):
        lines.append(f"- {x}")

    lines.extend(["", "[EMG 해석 포인트]"])
    for x in teaching.get("emg_reason", []):
        lines.append(f"- {x}")

    lines.extend(["", "[통합 해석]"])
    for x in teaching.get("integration", []):
        lines.append(f"- {x}")

    lines.extend(["", "[감별진단]"])
    for d in diff_dx:
        lines.append(f"- {d.get('name', '')}")
        lines.append(f"  왜 고려하나: {d.get('why_consider', '')}")
        lines.append(f"  어떻게 구분하나: {d.get('how_to_differentiate', '')}")
        lines.append(f"  실전 팁: {d.get('practical_tip', '')}")

    lines.extend(["", "※ 교육용 참고자료이며 실제 임상 진단을 대체하지 않습니다."])
    return "\n".join(lines)


def match_cases_by_filters(
    case_library: Dict[str, Dict[str, Any]],
    category: str = "전체",
    difficulty: str = "전체",
    keyword: str = "",
):
    results = []
    kw = keyword.strip().lower()

    for name, case in case_library.items():
        if category != "전체" and case.get("category") != category:
            continue
        if difficulty != "전체" and case.get("difficulty") != difficulty:
            continue

        if kw:
            patient = case.get("patient", {})
            blob = " ".join([
                name,
                case.get("category", ""),
                case.get("difficulty", ""),
                " ".join(patient.get("symptoms", [])),
            ]).lower()
            if kw not in blob:
                continue

        results.append((name, case))

    return results


def _severity_from_abnormal_count(count: int) -> str:
    if count >= 6:
        return "중증"
    if count >= 3:
        return "중등도"
    if count >= 1:
        return "경도"
    return "뚜렷한 이상 소견 없음"


def _build_top3_details(final_dx: str) -> List[Dict[str, str]]:
    mapping = {
        "신경뿌리병증 가능성": [
            {
                "name": "말초 단일신경병증",
                "why_consider": "국소 근력저하와 감각 증상이 비슷하게 보일 수 있습니다.",
                "how_to_differentiate": "감각신경전도 보존, 척추주위근 침범, 같은 분절 공유 근육 침범 여부를 함께 봅니다.",
                "practical_tip": "SNAP 보존 + paraspinal 이상이면 root lesion 가능성을 먼저 떠올리세요.",
            },
            {
                "name": "신경얼기병증",
                "why_consider": "여러 신경 분포 이상이 섞여 보이면 얼기 병변과 혼동될 수 있습니다.",
                "how_to_differentiate": "신경얼기병증은 감각신경 이상 동반 가능성이 높고 척추주위근은 대체로 보존됩니다.",
                "practical_tip": "척추주위근 이상 여부는 root와 plexus 감별에 중요합니다.",
            },
            {
                "name": "다발신경병증",
                "why_consider": "여러 부위 이상이 있으면 혼동될 수 있습니다.",
                "how_to_differentiate": "대칭성, 길이의존성, 다신경 분포 여부를 함께 해석합니다.",
                "practical_tip": "비대칭·분절성 패턴이면 다발신경병증보다 국소 병변 가능성을 먼저 보세요.",
            },
        ],
        "말초 단일신경병증 또는 신경얼기병증 가능성": [
            {
                "name": "신경뿌리병증",
                "why_consider": "통증/근력저하 분포만으로는 비슷해 보일 수 있습니다.",
                "how_to_differentiate": "감각신경전도 보존과 척추주위근 침범이 있으면 root lesion을 더 지지합니다.",
                "practical_tip": "SNAP 감소가 있으면 root보다는 말초 병변 가능성이 올라갑니다.",
            },
            {
                "name": "다발신경병증",
                "why_consider": "둘 이상 신경 이상이 보이면 혼동될 수 있습니다.",
                "how_to_differentiate": "다발신경병증은 더 대칭적이고 길이의존적인 분포가 흔합니다.",
                "practical_tip": "국소성/비대칭성이 강하면 mononeuropathy 또는 plexopathy를 먼저 보세요.",
            },
            {
                "name": "중추성 병변",
                "why_consider": "기능저하 자체만 보면 말초 병변과 혼동될 수 있습니다.",
                "how_to_differentiate": "말초 전기생리 이상이 명확하면 중추 단독 병변 가능성은 상대적으로 낮아집니다.",
                "practical_tip": "전기생리 이상이 말초 분포와 일치하는지 먼저 확인하세요.",
            },
        ],
        "다발신경병증 가능성": [
            {
                "name": "신경뿌리병증",
                "why_consider": "다분절 병변이면 여러 이상이 섞여 보일 수 있습니다.",
                "how_to_differentiate": "신경뿌리병증은 감각신경전도 보존과 척추주위근 침범이 도움이 됩니다.",
                "practical_tip": "양측 대칭성 원위부 침범이면 다발신경병증 쪽이 더 전형적입니다.",
            },
            {
                "name": "신경얼기병증",
                "why_consider": "광범위 말초신경 이상처럼 보일 수 있습니다.",
                "how_to_differentiate": "신경얼기병증은 대개 더 비대칭적이고 국소적입니다.",
                "practical_tip": "대칭성 여부를 먼저 확인하세요.",
            },
            {
                "name": "근육병증",
                "why_consider": "근력저하가 주증상이면 혼동될 수 있습니다.",
                "how_to_differentiate": "근육병증은 감각이 대체로 보존되고 신경전도 이상 양상이 다릅니다.",
                "practical_tip": "감각신경 이상 동반 여부를 항상 같이 보세요.",
            },
        ],
        "근위부 신경/신경뿌리 또는 초기 급성 염증성 다발신경병증 가능성": [
            {
                "name": "초기 길랭-바레증후군",
                "why_consider": "원위부 전도는 비교적 정상이어도 F파 이상이 먼저 보일 수 있습니다.",
                "how_to_differentiate": "급성 진행성 약화와 반사저하/소실 여부를 임상과 함께 봅니다.",
                "practical_tip": "초기에는 F파 이상이 중요한 단서가 될 수 있습니다.",
            },
            {
                "name": "신경뿌리병증",
                "why_consider": "근위부 병변에서도 F파 이상이 가능합니다.",
                "how_to_differentiate": "국소 분절성 증상, 척추주위근 이상이 있으면 root lesion을 더 지지합니다.",
                "practical_tip": "F파 이상만으로 단정하지 말고 임상 분포를 함께 보세요.",
            },
            {
                "name": "다발신경병증",
                "why_consider": "초기에는 일부 후기반응 이상만 먼저 보일 수 있습니다.",
                "how_to_differentiate": "추적검사에서 원위부 이상이 뒤따르는지 확인합니다.",
                "practical_tip": "급성기 전기생리는 반복 평가가 중요합니다.",
            },
        ],
        "중추성 경직/상위운동신경세포 병변 가능성": [
            {
                "name": "말초 S1 병변",
                "why_consider": "같은 반사 경로 평가 상황에서 혼동될 수 있습니다.",
                "how_to_differentiate": "말초 병변은 보통 H반사 지연/소실 쪽이며, 항진은 중추성 해석과 더 잘 맞습니다.",
                "practical_tip": "반사 증가인지 감소인지 방향을 먼저 확인하세요.",
            },
            {
                "name": "신경뿌리병증",
                "why_consider": "동일 분절 반사 평가라는 점에서 혼동될 수 있습니다.",
                "how_to_differentiate": "신경뿌리병증은 보통 반사항진보다 저하/소실이 더 전형적입니다.",
                "practical_tip": "UMN 징후를 임상과 함께 확인하세요.",
            },
            {
                "name": "비특이 반사변화",
                "why_consider": "단독 반사 수치만으로는 제한적 해석일 수 있습니다.",
                "how_to_differentiate": "경직, 병적반사, 기능저하를 함께 종합합니다.",
                "practical_tip": "반사 수치 하나보다 임상 문맥을 우선하세요.",
            },
        ],
        "뇌신경 반사경로 이상 가능성": [
            {
                "name": "삼차신경 들경로 이상",
                "why_consider": "자극측 기준으로 이상 패턴이 반복되면 우선 고려합니다.",
                "how_to_differentiate": "같은 쪽 자극에서 양측 반응 이상이 반복되는지 확인합니다.",
                "practical_tip": "blink reflex는 자극측과 반응측을 분리해서 보세요.",
            },
            {
                "name": "얼굴신경 날경로 이상",
                "why_consider": "반응측 기준 이상 패턴으로 나타날 수 있습니다.",
                "how_to_differentiate": "반대쪽 자극 시에도 동일 반응측만 이상한지 봅니다.",
                "practical_tip": "좌우 자극-반응 매트릭스로 정리하면 해석이 쉬워집니다.",
            },
            {
                "name": "뇌줄기 반사연결 이상",
                "why_consider": "중간 회로 연결의 문제도 가능하기 때문입니다.",
                "how_to_differentiate": "R1과 R2 패턴을 함께 보고 임상 뇌신경 소견을 종합합니다.",
                "practical_tip": "blink reflex는 단일 신경보다 회로 해석에 가깝습니다.",
            },
        ],
        "특정 패턴 단정 어려움": [
            {
                "name": "추가 감별 필요",
                "why_consider": "입력 소견이 제한적이거나 혼합적입니다.",
                "how_to_differentiate": "병력, 진찰, 영상, 추적 전기생리 결과를 함께 봐야 합니다.",
                "practical_tip": "국소성/대칭성/감각 보존 여부부터 구조화해 보세요.",
            }
        ],
        "뚜렷한 전기생리학적 이상 소견 없음": [
            {
                "name": "정상 또는 초기/경미 병변",
                "why_consider": "임상 증상과 검사 시점에 따라 이상이 아직 뚜렷하지 않을 수 있습니다.",
                "how_to_differentiate": "임상 증상이 지속되면 추적검사와 신체진찰을 함께 봅니다.",
                "practical_tip": "정상 전기생리 소견이 항상 증상 부재를 뜻하는 것은 아닙니다.",
            }
        ],
    }

    return mapping.get(final_dx, [{
        "name": "추가 감별 필요",
        "why_consider": "입력 소견이 제한적이거나 혼합적입니다.",
        "how_to_differentiate": "임상 정보와 추가 검사가 필요합니다.",
        "practical_tip": "감각 보존, 척추주위근, 대칭성 여부를 먼저 보세요.",
    }])


def analyze_manual_input(
    selected_findings: Dict[str, str],
    anatomy_map: Dict[str, Dict[str, str]],
) -> Dict[str, Any]:
    abnormalities = []
    abnormal_items_for_view = []

    nerves = defaultdict(int)
    levels = defaultdict(int)
    domains = defaultdict(int)

    sensory_abn_count = 0
    motor_abn_count = 0
    muscle_abn_count = 0

    paraspinal_abnormal = False
    f_wave_abnormal = False
    h_reflex_hyper = False
    h_reflex_delayed_or_absent = False
    blink_abnormal = False

    for item, result in selected_findings.items():
        if not result or result == "미선택":
            continue

        normalized = normalize_result_text(result)
        meta = anatomy_map.get(item, {})
        domain = meta.get("domain", "")
        nerve = meta.get("nerve", "")
        level = meta.get("level", "")

        # 엄격한 정상 필터링
        if "정상 범위" in normalized or "전기적 침묵" in normalized:
            continue

        abnormalities.append({
            "item": item,
            "result": normalized,
            "domain": domain,
            "nerve": nerve,
            "level": level,
        })

        abnormal_items_for_view.append({
            "항목": item,
            "신경": nerve or "-",
            "레벨": level or "-",
            "결과": normalized,
        })

        if nerve:
            nerves[nerve] += 1
        if level:
            levels[level] += 1
        if domain:
            domains[domain] += 1

        if domain == "sensory":
            sensory_abn_count += 1
        elif domain == "motor":
            motor_abn_count += 1
        elif domain == "muscle":
            muscle_abn_count += 1

        if "Paraspinal" in item or "척추주위근" in item:
            paraspinal_abnormal = True
        if domain == "f_wave":
            f_wave_abnormal = True
        if domain == "h_reflex":
            if "항진" in normalized or "증가" in normalized:
                h_reflex_hyper = True
            elif "지연" in normalized or "소실" in normalized:
                h_reflex_delayed_or_absent = True
        if domain == "blink":
            blink_abnormal = True

    top_nerves = sorted(nerves.items(), key=lambda x: x[1], reverse=True)
    top_levels = sorted(levels.items(), key=lambda x: x[1], reverse=True)
    top_domains = sorted(domains.items(), key=lambda x: x[1], reverse=True)

    lesion_tags: List[str] = []
    candidate_scores = defaultdict(int)
    reasons: List[str] = []
    suggestions: List[str] = []

    if blink_abnormal:
        lesion_tags.append("뇌신경 반사경로")
        candidate_scores["뇌신경 반사경로 이상 가능성"] += 95
        reasons.append("눈깜빡반사 이상이 있어 삼차신경-뇌줄기-얼굴신경 반사경로 평가가 중요합니다.")
        suggestions.append("blink reflex는 자극측과 반응측을 분리하여 패턴을 읽어보세요.")

    if h_reflex_hyper:
        lesion_tags.append("중추성 반사 항진")
        candidate_scores["중추성 경직/위운동신경세포 병변 가능성"] += 90
        reasons.append("H반사 항진 또는 H/M 비율 증가는 척수 반사 흥분성 증가를 시사합니다.")
        suggestions.append("반사항진, 간대경련, 병적반사 등 위운동신경세포(UMN) 징후를 함께 확인하세요.")

    if f_wave_abnormal and sensory_abn_count == 0 and motor_abn_count == 0:
        lesion_tags.append("근위부 전도 이상")
        candidate_scores["근위부 신경/신경뿌리 또는 초기 급성 염증성 다발신경병증 가능성"] += 88
        reasons.append("원위부 전도 이상은 두드러지지 않으나 F파 이상이 있어 근위부 전도 이상 가능성을 고려합니다.")
        suggestions.append("급성기에는 추적 신경전도검사와 반사 변화 확인이 중요합니다.")

    if h_reflex_delayed_or_absent and sensory_abn_count == 0 and motor_abn_count == 0 and not h_reflex_hyper:
        lesion_tags.append("S1 근위부 반사경로")
        candidate_scores["근위부 신경/신경뿌리 또는 초기 급성 염증성 다발신경병증 가능성"] += 35
        reasons.append("H반사 지연/소실은 S1 분절 또는 근위부 반사경로 이상 가능성을 시사할 수 있습니다.")
        suggestions.append("정강신경 말초 전도와 척추주위근/장딴지근 침범 여부를 함께 보세요.")

    if sensory_abn_count == 0 and paraspinal_abnormal and muscle_abn_count >= 1:
        lesion_tags.extend(["척추주위근 침범", "감각 보존"])
        candidate_scores["신경뿌리병증 가능성"] += 92
        reasons.append("감각신경전도 보존과 척추주위근 이상은 신경뿌리병증 해석에 유리합니다.")
        suggestions.append("같은 분절을 공유하지만 서로 다른 말초신경이 지배하는 근육이 함께 이상인지 확인해 보세요.")

    if sensory_abn_count >= 1 and not paraspinal_abnormal and muscle_abn_count >= 1:
        lesion_tags.extend(["감각신경 이상", "말초성 패턴"])
        candidate_scores["말초 단일신경병증 또는 신경얼기병증 가능성"] += 85
        reasons.append("감각신경 이상이 있고 척추주위근 이상이 없다면 뒤뿌리신경절 원위부 병변 가능성이 높습니다.")
        suggestions.append("SNAP 감소가 단일신경 분포인지 여러 신경 분포인지 나누어 보세요.")

    if sensory_abn_count >= 2 and motor_abn_count >= 1:
        lesion_tags.append("다신경 침범")
        candidate_scores["다발신경병증 가능성"] += 87
        reasons.append("여러 감각/운동신경 이상이 함께 나타나 다발신경병증 패턴을 고려합니다.")
        suggestions.append("대칭성, 길이의존성, 축삭성/말이집탈락성 경향을 함께 정리해 보세요.")

    if not candidate_scores and abnormalities:
        candidate_scores["특정 패턴 단정 어려움"] += 50
        reasons.append("입력된 이상 소견이 제한적이거나 혼합적이어서 추가 임상 정보와 비교가 필요합니다.")
        suggestions.append("병력, 반사, 감각 분포, 척추주위근 여부를 추가로 확인하세요.")

    if not abnormalities:
        candidate_scores["뚜렷한 전기생리학적 이상 소견 없음"] += 100
        reasons.append("선택된 항목 중 뚜렷한 이상 소견이 확인되지 않았습니다.")
        suggestions.append("임상 증상이 지속되면 검사 시기와 추적검사를 함께 고려하세요.")

    if top_nerves:
        reasons.append(f"가장 많이 연관된 신경: {', '.join([n for n, _ in top_nerves[:3] if n])}")
    if top_levels:
        reasons.append(f"가장 많이 연관된 분절/레벨: {', '.join([l for l, _ in top_levels[:3] if l])}")
    if top_domains:
        reasons.append(f"주된 이상 영역: {', '.join([d for d, _ in top_domains[:3] if d])}")

    top3 = sorted(candidate_scores.items(), key=lambda x: x[1], reverse=True)[:3]
    final_dx = top3[0][0] if top3 else "특정 패턴 단정 어려움"

    involved_nerves = ", ".join([n for n, _ in top_nerves[:3] if n]) if top_nerves else "-"
    involved_levels = ", ".join([l for l, _ in top_levels[:3] if l]) if top_levels else "-"
    severity = _severity_from_abnormal_count(len(abnormalities))
    top3_details = _build_top3_details(final_dx)

    return {
        "abnormalities": abnormalities,
        "top_nerves": top_nerves,
        "top_levels": top_levels,
        "top_domains": top_domains,
        "impression": [dx for dx, _ in top3] if top3 else [final_dx],
        "reasoning": reasons,
        "final_dx": final_dx,
        "lesion_tags": lesion_tags,
        "involved_nerves": involved_nerves,
        "involved_levels": involved_levels,
        "severity": severity,
        "top3": top3,
        "top3_details": top3_details,
        "reasons": reasons,
        "abnormal_items": abnormal_items_for_view,
        "suggestions": suggestions,
    }
