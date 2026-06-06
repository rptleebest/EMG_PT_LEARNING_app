# utils/helpers.py

"""
UI와 데이터 처리에서 반복적으로 사용하는 보조 함수.
"""

from typing import Any, Sequence

from data.terms import is_abnormal_code, is_normal_code


def safe_index(options: Sequence[Any], value: Any) -> int:
    """options 안에서 value의 index를 반환하고, 없으면 0을 반환합니다."""
    try:
        return list(options).index(value)
    except ValueError:
        return 0


def simplify_level_text(level_text: Any) -> str:
    """분절/해부학 레벨 문구를 안전하게 정리합니다."""
    if not level_text:
        return "정보 없음"
    return str(level_text).strip()


def normalize_case_item_name(item_name: Any) -> str:
    """검사항목명을 안전하게 문자열로 정규화합니다."""
    if item_name is None:
        return ""
    return str(item_name).strip()


def get_compact_item_label(item_name: Any) -> str:
    """모바일 화면용 짧은 검사항목 라벨을 반환합니다."""
    return normalize_case_item_name(item_name)


def is_abnormal(value: Any) -> bool:
    """결과값이 비정상인지 판정합니다."""
    return is_abnormal_code(value)


def is_normal(value: Any) -> bool:
    """결과값이 정상인지 판정합니다."""
    return is_normal_code(value)


def get_motor_stimulation_labels(domain: str) -> dict:
    """검사 domain에 따른 자극 구간 라벨을 반환합니다."""
    if domain == "sensory":
        return {"distal": "기본 구간"}
    if domain == "motor":
        return {"distal": "원위부", "proximal": "근위부"}
    return {"distal": "기본"}


def get_case_names_for_selection() -> list:
    """사례 선택용 이름 목록을 반환합니다."""
    from data.cases import CASE_LIBRARY

    return list(CASE_LIBRARY.keys())


def choose_pathologic_value(left: Any, right: Any, side: str) -> Any:
    """좌우 결과 중 병변측 값을 반환합니다."""
    if side in {"오른쪽", "우", "right", "Right"}:
        return right
    if side in {"왼쪽", "좌", "left", "Left"}:
        return left
    return left


def is_bilateral_side(side: str) -> bool:
    """측 정보가 양측인지 판정합니다."""
    return side in {"양쪽", "양측", "both", "Both", "bilateral"}
