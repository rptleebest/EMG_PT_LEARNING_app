# formatters.py

"""
루트 import 호환용 formatters 모듈.
"""

import html
import re
from typing import Any


def html_escape(value: Any) -> str:
    """HTML 특수문자를 안전하게 escape합니다."""
    if value is None:
        return ""
    return html.escape(str(value), quote=True)


def clean_html(value: Any) -> str:
    """
    간단한 HTML/텍스트 정리 함수.
    화면 표시용 문자열을 안전하게 정리합니다.
    """
    if value is None:
        return ""

    text = str(value)

    # script/style 태그 제거
    text = re.sub(
        r"<\s*(script|style).*?>.*?<\s*/\s*\1\s*>",
        "",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # 위험 이벤트 속성 제거
    text = re.sub(
        r"\son\w+\s*=\s*(['\"]).*?\1",
        "",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

    return text.strip()


def format_list(items: Any) -> str:
    """리스트를 줄바꿈 문자열로 변환합니다."""
    if items is None:
        return ""

    if isinstance(items, (list, tuple)):
        return "\n".join(str(item) for item in items)

    return str(items)


def compact_text(value: Any, max_length: int = 80) -> str:
    """긴 텍스트를 짧게 줄입니다."""
    text = "" if value is None else str(value)

    if len(text) <= max_length:
        return text

    return text[: max_length - 1] + "…"
