# engine/inference.py

from collections import defaultdict
from typing import Dict, Tuple, Any, List

TEXT_NORMALIZATION_MAP = {
    "정상 범위(within normal limits)": "정상 범위 (within normal limits)",
    "정상 (Normal)": "정상 범위 (within normal limits)",
    "normal": "정상 범위 (within normal limits)",
    "Normal": "정상 범위 (within normal limits)",
    "정상": "정상 범위 (within normal limits)",
    "정상 범위": "정상 범위 (within normal limits)",

    "잠복기 지연(delayed latency)": "잠복기 지연 (Delayed latency) - 정상 대비 130% 이상 초과",
    "잠복기 지연 (Delayed latency)": "잠복기 지연 (Delayed latency) - 정상 대비 130% 이상 초과",
    "delayed": "잠복기 지연 (Delayed latency) - 정상 대비 130% 이상 초과",
    "지연 (Delayed)": "잠복기 지연 (Delayed latency) - 정상 대비 130% 이상 초과",
    "잠복기 지연": "잠복기 지연 (Delayed latency) - 정상 대비 130% 이상 초과",

    "진폭 감소(reduced amplitude)": "진폭 감소 (Reduced amplitude) - 정상 대비 50% 이하 감소",
    "감소 (Reduced)": "진폭 감소 (Reduced amplitude) - 정상 대비 50% 이하 감소",
    "reduced": "진폭 감소 (Reduced amplitude) - 정상 대비 50% 이하 감소",
    "진폭 감소": "진폭 감소 (Reduced amplitude) - 정상 대비 50% 이하 감소",

    "반응 소실(absent response)": "반응 소실 (Absent response) - 전기 자극에 무반응",
    "무반응 (No response)": "반응 소실 (Absent response) - 전기 자극에 무반응",
    "absent": "반응 소실 (Absent response) - 전기 자극에 무반응",
    "소실 (Absent)": "반응 소실 (Absent response) - 전기 자극에 무반응",
    "반응 소실": "반응 소실 (Absent response) - 전기 자극에 무반응",

    "잠복기 지연 또는 반응 소실(delayed or absent response)": "잠복기 지연 또는 반응 소실 (delayed or absent response)",
    "지연 또는 소실 (Delayed/Absent)": "잠복기 지연 또는 반응 소실 (delayed or absent response)",

    "F파 최소잠복기 지연 또는 소실(delayed or absent F-wave)": "F파 최소잠복기 지연 또는 소실 (delayed or absent F-wave)",
    "H-반사 항진 또는 문턱값 감소(hyperactive H-reflex / lower threshold)": "H-반사 항진 또는 문턱값 감소 (hyperactive H-reflex) - 위운동신경세포 병변 시사",
    "H/M 비율 증가 가능(increased H/M ratio possible)": "H/M 비율 증가 가능 (increased H/M ratio possible)",
    "증가 가능 (May be increased)": "H/M 비율 증가 가능 (increased H/M ratio possible)",
    "항진 또는 문턱값 감소 (Hyperactive / lower threshold)": "H-반사 항진 또는 문턱값 감소 (hyperactive H-reflex) - 위운동신경세포 병변 시사",

    "휴식 시 전기적 침묵(no motor unit action potential, MUAP), 수의수축 시 정상 운동단위전위(motor unit action potential, MUAP) 동원": "휴식 시 Silent at rest (전기적 침묵) / 근수축 시 Normal MU recruitment",
    "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)": "휴식 시 Fibrillation 및 Positive sharp wave 출현 / 근수축 시 Reduced MU recruitment",
    "비정상 자발전위 (Fibrillation, Positive sharp wave 등) 출현": "휴식 시 Fibrillation 및 Positive sharp wave 출현 / 근수축 시 Reduced MU recruitment",
    "휴식 시 섬유자발전위(fibrillation potential) 및 양성예파(positive sharp wave) 관찰": "휴식 시 Fibrillation 및 Positive sharp wave 출현 / 근수축 시 Reduced MU recruitment",
    "휴식 시 섬유자발전위(fibrillation potential) 및 양성예파(positive sharp wave) 관찰, 수의수축 시 운동단위전위(motor unit action potential, MUAP) 동원 감소 가능": "휴식 시 Fibrillation 및 Positive sharp wave 출현 / 근수축 시 Reduced MU recruitment",
    "휴식 시 근육다발수축전위(fasciculation potential) 관찰 가능": "휴식 시 Fasciculation potentials 출현 / 근수축 시 Reduced MU recruitment",
    "무반응 / 전기적 침묵 (Electrical silence)": "휴식 시 Silent at rest (전기적 침묵) / 근수축 시 Normal MU recruitment",
}


def normalize_result_text(value: Any) -> str:
    if value is None:
        return ""
    text = str(value).strip()
    return TEXT_NORMALIZATION_MAP.get(text, text)


def is_abnormal(value: Any) -> bool:
    text = normalize_result_text(value)
    return bool(text) and "정상 범위" not in text and "Silent at rest" not in text


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

    lines.extend(["", "[전기진단 소견 (병변측)]"])
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
