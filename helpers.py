# helpers.py

"""
루트 import 호환용 helpers 모듈.

ui/case_learning.py에서
from helpers import lesion_side_index
형태로 import하므로, app.py와 같은 위치에 이 파일이 필요합니다.
"""

from typing import Any, Sequence


def safe_index(options: Sequence[Any], value: Any) -> int:
    """options 안에서 value의 index를 반환하고, 없으면 0을 반환합니다."""
    try:
        return list(options).index(value)
    except ValueError:
        return 0


def lesion_side_index(side: Any) -> int:
    """
    병변측 문자열을 선택 위젯 index로 변환합니다.

    일반적으로:
    0 = 오른쪽
    1 = 왼쪽
    2 = 양측
    """
    text = str(side).strip().lower()

    if text in {"오른쪽", "우", "right", "rt", "r"}:
        return 0

    if text in {"왼쪽", "좌", "left", "lt", "l"}:
        return 1

    if text in {"양쪽", "양측", "both", "bilateral", "bilat"}:
        return 2

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


def choose_pathologic_value(left: Any, right: Any, side: str) -> Any:
    """좌우 결과 중 병변측 값을 반환합니다."""
    if side in {"오른쪽", "우", "right", "Right", "rt", "R"}:
        return right

    if side in {"왼쪽", "좌", "left", "Left", "lt", "L"}:
        return left

    return left


def is_bilateral_side(side: Any) -> bool:
    """측 정보가 양측인지 판정합니다."""
    return str(side).strip() in {
        "양쪽",
        "양측",
        "both",
        "Both",
        "bilateral",
        "Bilateral",
    }


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


def is_abnormal(value: Any) -> bool:
    """결과값이 비정상인지 판정합니다."""
    try:
        from data.terms import is_abnormal_code
        return is_abnormal_code(value)
    except Exception:
        try:
            from data.terms import is_abnormal_result
            return is_abnormal_result(value)
        except Exception:
            text = str(value)
            return any(
                keyword in text
                for keyword in [
                    "비정상",
                    "감소",
                    "지연",
                    "소실",
                    "무반응",
                    "탈신경",
                    "재신경지배",
                    "reduced",
                    "delayed",
                    "absent",
                    "denervation",
                ]
            )


def is_normal(value: Any) -> bool:
    """결과값이 정상인지 판정합니다."""
    try:
        from data.terms import is_normal_code
        return is_normal_code(value)
    except Exception:
        try:
            from data.terms import is_normal_result
            return is_normal_result(value)
        except Exception:
            text = str(value)
            return "정상" in text or "normal" in text.lower()
