# engine/inference.py

from typing import Dict, Tuple, Any, List


TEXT_NORMALIZATION_MAP = {
    # Normal
    "정상 범위(within normal limits)": "정상 범위",
    "정상 범위 (within normal limits)": "정상 범위",
    "정상 (Normal)": "정상 범위",
    "normal": "정상 범위",
    "Normal": "정상 범위",
    "정상": "정상 범위",
    "정상 범위": "정상 범위",
    "ncs_normal": "정상 범위",
    "emg_normal": "정상 반응",

    # NCS delayed
    "ncs_delayed": "잠복기 지연",
    "delayed": "잠복기 지연",
    "잠복기 지연(delayed latency)": "잠복기 지연",
    "잠복기 지연 (Delayed latency)": "잠복기 지연",
    "잠복기 지연 (Delayed latency) - 정상 대비 130% 이상 초과": "잠복기 지연",
    "지연 (Delayed)": "잠복기 지연",
    "잠복기 지연": "잠복기 지연",

    # NCS reduced
    "ncs_reduced": "진폭 감소",
    "reduced": "진폭 감소",
    "진폭 감소(reduced amplitude)": "진폭 감소",
    "감소 (Reduced)": "진폭 감소",
    "진폭 감소 (Reduced amplitude) - 정상 대비 50% 이하 감소": "진폭 감소",
    "진폭 감소": "진폭 감소",

    # NCS absent
    "ncs_absent": "반응 소실",
    "absent": "반응 소실",
    "반응 소실(absent response)": "반응 소실",
    "무반응 (No response)": "반응 소실",
    "반응 소실 (Absent response) - 전기 자극에 무반응": "반응 소실",
    "소실 (Absent)": "반응 소실",
    "반응 소실": "반응 소실",

    # Conduction block
    "ncs_conduction_block": "전도차단",
    "전도차단": "전도차단",
    "Conduction block": "전도차단",

    # Special
    "fwave_delayed_absent": "F파 지연 또는 소실",
    "h_reflex_hyperactive": "H-반사 항진",
    "h_m_ratio_increased": "H/M 비율 증가",
    "blink_delayed": "눈깜빡반사 지연",
    "blink_delayed_absent": "눈깜빡반사 지연 또는 소실",
    "지연 또는 소실 (Delayed/Absent)": "지연 또는 소실",
    "잠복기 지연 또는 반응 소실(delayed or absent response)": "지연 또는 소실",

    # EMG
    "emg_active_denervation": "비정상 자발전위 출현 / 운동단위 동원감소",
    "emg_paraspinal_denervation": "비정상 자발전위 출현 / 평가 제한",
    "emg_chronic_reinnervation": "만성 재신경지배 소견 / 운동단위 동원감소",
    "emg_active_chronic": "비정상 자발전위 및 만성 재신경지배 소견",
    "emg_fasciculation": "근육다발수축전위 출현",
    "emg_no_response": "수의수축 시 운동단위 동원 불가",
    "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)": "비정상 자발전위 출현",
    "비정상 자발전위 (Fibrillation, Positive sharp wave 등) 출현": "비정상 자발전위 출현",
}


def normalize_result_text(value: Any) -> str:
    """
    여러 파일과 예전 코드에서 사용하던 결과 표현을 교육용 간략 표현으로 통일합니다.
    """
    if value is None:
        return ""

    text = str(value).strip()
    if not text:
        return ""

    return TEXT_NORMALIZATION_MAP.get(text, text)


def is_abnormal(value: Any) -> bool:
    """
    정상 여부 판단.
    단, 침근전도의 'Silent at rest'는 휴식 시 정상 반응으로 간주합니다.
    """
    text = normalize_result_text(value)

    if not text:
        return False

    normal_tokens = [
        "정상",
        "정상 범위",
        "정상 반응",
        "Silent at rest",
        "Normal MU recruitment",
    ]

    return not any(token in text for token in normal_tokens)


def split_findings_by_domain(
    findings: Dict[str, Tuple[Any, Any]],
    anatomy_map: Dict[str, Dict[str, str]],
) -> Dict[str, Dict[str, Tuple[Any, Any]]]:
    """
    검사 항목을 anatomy_map의 domain 기준으로 분류합니다.

    반환 그룹:
    - sensory: 감각신경전도검사
    - motor: 운동신경전도검사
    - muscle: 침근전도검사
    - reflex: H-reflex, F-wave, blink reflex 등
    - other: 해부학 사전에 없는 항목
    """
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
    """
    선택된 사례를 텍스트 리포트 형태로 변환합니다.
    추후 다운로드 기능을 붙일 때 그대로 활용할 수 있습니다.
    """
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

    for symptom in patient.get("symptoms", []):
        lines.append(f"- {symptom}")

    lines.extend(["", "[이학적 검사]"])

    for section_name, items in patient.get("physical_exam", {}).items():
        lines.append(section_name)
        for item in items:
            lines.append(f"  - {item}")

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

    lines.extend(["", "[교육용 진단 요약]"])
    lines.append(teaching.get("summary", ""))

    lines.extend(["", "[신경전도검사 및 특수검사 해석 포인트]"])
    for text in teaching.get("ncs_reason", []):
        lines.append(f"- {text}")

    lines.extend(["", "[침근전도 해석 포인트]"])
    for text in teaching.get("emg_reason", []):
        lines.append(f"- {text}")

    lines.extend(["", "[통합 해석]"])
    for text in teaching.get("integration", []):
        lines.append(f"- {text}")

    lines.extend(["", "[감별진단]"])
    for item in diff_dx:
        lines.append(f"- {item.get('name', '')}")
        lines.append(f"  왜 고려하나: {item.get('why_consider', '')}")
        lines.append(f"  어떻게 구분하나: {item.get('how_to_differentiate', '')}")
        lines.append(f"  실전 팁: {item.get('practical_tip', '')}")

    lines.extend(["", "※ 교육용 참고자료이며 실제 임상 진단을 대체하지 않습니다."])

    return "\n".join(lines)


def match_cases_by_filters(
    case_library: Dict[str, Dict[str, Any]],
    category: str = "전체",
    difficulty: str = "전체",
    keyword: str = "",
) -> List[Tuple[str, Dict[str, Any]]]:
    """
    추후 검색/필터 UI를 추가할 때 사용할 수 있는 사례 필터 함수입니다.
    현재 화면에서는 전체 목록 라디오 선택을 사용하지만, 함수는 유지합니다.
    """
    results = []
    kw = keyword.strip().lower()

    for name, case in case_library.items():
        if category != "전체" and case.get("category") != category:
            continue

        if difficulty != "전체" and case.get("difficulty") != difficulty:
            continue

        if kw:
            patient = case.get("patient", {})
            searchable_text = " ".join(
                [
                    name,
                    case.get("category", ""),
                    case.get("difficulty", ""),
                    " ".join(patient.get("symptoms", [])),
                ]
            ).lower()

            if kw not in searchable_text:
                continue

        results.append((name, case))

    return results


def severity_from_abnormal_count(count: int) -> str:
    if count >= 6:
        return "중증"
    if count >= 3:
        return "중등도"
    if count >= 1:
        return "경도"
    return "뚜렷한 이상 소견 없음"


def summarize_abnormal_findings(
    findings: Dict[str, Tuple[Any, Any]],
    lesion_side: str = "우",
) -> Dict[str, Any]:
    """
    사례의 이상 소견 개수를 간단히 요약합니다.
    교육용 카드에서 병변측 이상이 얼마나 많은지 보여줄 때 사용할 수 있습니다.
    """
    side_index = 1 if lesion_side in {"우", "오른쪽"} else 0

    if lesion_side in {"양측", "양쪽"}:
        side_index = None

    abnormal_items = []

    for item, values in findings.items():
        if side_index is None:
            left = values[0] if len(values) > 0 else ""
            right = values[1] if len(values) > 1 else ""
            if is_abnormal(left) or is_abnormal(right):
                abnormal_items.append(item)
        else:
            value = values[side_index] if len(values) > side_index else ""
            if is_abnormal(value):
                abnormal_items.append(item)

    return {
        "count": len(abnormal_items),
        "severity": severity_from_abnormal_count(len(abnormal_items)),
        "items": abnormal_items,
    }
