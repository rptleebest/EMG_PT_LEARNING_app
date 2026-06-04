# formatters.py

import html


def normalize_result_text(value):
    """
    화면 표시용 결과 텍스트 간략화.
    표 안에서는 괄호 설명을 줄이고, 자세한 기준은 판독 기준 팁에서 설명합니다.
    """
    if value is None:
        return ""

    text = str(value).strip()

    mapping = {
        "정상 (Normal)": "정상 범위",
        "정상": "정상 범위",
        "normal": "정상 범위",
        "Normal": "정상 범위",
        "ncs_normal": "정상 범위",

        "감소 (Reduced)": "감소",
        "reduced": "감소",
        "ncs_reduced": "감소",
        "진폭 감소": "감소",
        "진폭 감소 (Reduced amplitude) - 정상 대비 50% 이하 감소": "감소",

        "잠복기 지연 (Delayed latency)": "지연",
        "잠복기 지연": "지연",
        "delayed": "지연",
        "ncs_delayed": "지연",
        "지연 (Delayed)": "지연",

        "무반응 (No response)": "반응 소실",
        "소실 (Absent)": "반응 소실",
        "absent": "반응 소실",
        "ncs_absent": "반응 소실",

        "ncs_conduction_block": "전도차단",

        "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)": "비정상 자발전위 출현",
        "비정상 자발전위 (Fibrillation, Positive sharp wave 등) 출현": "비정상 자발전위 출현",
        "무반응 / 전기적 침묵 (Electrical silence)": "전기적 침묵",
        "지연 또는 소실 (Delayed/Absent)": "지연 또는 소실",
        "항진 또는 문턱값 감소 (Hyperactive / lower threshold)": "항진",
        "증가 가능 (May be increased)": "증가",
        "소실 (Absent)": "소실",
    }

    return mapping.get(text, text)


def summarize_status(left, right, side="미선택"):
    """
    좌우 결과를 한 줄 요약합니다.
    """
    left_disp = normalize_result_text(left)
    right_disp = normalize_result_text(right)

    if str(right).strip() == "":
        return f"결과: {left_disp}"

    if side in {"양측", "양쪽"}:
        return f"좌측: {left_disp} / 우측: {right_disp}"

    if side in {"좌", "왼쪽"}:
        return f"좌측 병변측: {left_disp} / 우측 정상측: {right_disp}"

    if side in {"우", "오른쪽"}:
        return f"좌측 정상측: {left_disp} / 우측 병변측: {right_disp}"

    return f"좌측: {left_disp} / 우측: {right_disp}"


def severity_text(total_abnormal, no_response_count):
    if no_response_count >= 2 or total_abnormal >= 6:
        return "중등도 이상"

    if total_abnormal >= 3:
        return "경도-중등도"

    if total_abnormal >= 1:
        return "경도"

    return "뚜렷한 이상 없음"


def html_escape(text):
    """
    unsafe_allow_html=True로 HTML 레이아웃을 쓸 때,
    사용자/데이터 텍스트만 안전하게 escape합니다.
    """
    if text is None:
        return ""

    return html.escape(str(text), quote=True)


def color_class_for_result(text):
    if text is None:
        return "text-normal"

    value = str(text)

    if any(token in value for token in ["감소", "지연", "소실", "비정상", "전도차단", "항진", "불가", "동원감소"]):
        return "text-red"

    if any(token in value for token in ["정상", "보존", "Silent", "Normal"]):
        return "text-blue"

    return "text-normal"
