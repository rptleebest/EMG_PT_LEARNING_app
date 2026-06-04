# helpers.py

def safe_index(options, value):
    """
    selectbox/radio 기본 index 계산용 안전 함수.
    value가 options에 없으면 0을 반환합니다.
    """
    try:
        return options.index(value)
    except ValueError:
        return 0


def simplify_level_text(level_text):
    if not level_text:
        return "정보 없음"
    return str(level_text).strip()


def normalize_case_item_name(item_name):
    if item_name is None:
        return ""
    return str(item_name).strip()


def get_compact_item_label(item_name):
    return normalize_case_item_name(item_name)


def is_abnormal(value):
    """
    간단 정상/비정상 판단.
    engine.inference.is_abnormal과 동일 목적이지만,
    기존 코드 호환을 위해 유지합니다.
    """
    if value is None:
        return False

    text = str(value).strip().lower()

    if text == "":
        return False

    normal_tokens = [
        "정상",
        "정상 범위",
        "정상 반응",
        "normal",
        "silent at rest",
    ]

    return not any(token in text for token in normal_tokens)


def get_motor_stimulation_labels(domain):
    """
    검사 종류별 자극 위치 라벨.
    가상 결과표 판독학습에서 표 머리말 또는 설명에 활용할 수 있습니다.
    """
    if domain == "sensory":
        return {
            "distal": "기록 구간",
        }

    if domain == "motor":
        return {
            "distal": "원위부 자극",
            "proximal": "근위부 자극",
        }

    return {
        "distal": "기본 구간",
    }


def get_case_names_for_selection():
    from data.cases import CASE_LIBRARY
    return list(CASE_LIBRARY.keys())


def side_to_korean(side):
    """
    병변측 표기를 화면 표시용으로 통일합니다.
    """
    mapping = {
        "우": "오른쪽",
        "좌": "왼쪽",
        "양측": "양쪽",
        "오른쪽": "오른쪽",
        "왼쪽": "왼쪽",
        "양쪽": "양쪽",
    }
    return mapping.get(side, str(side))


def lesion_side_index(side):
    """
    좌/우 tuple에서 병변측 index 반환.
    좌측: 0
    우측: 1
    양측: None
    """
    if side in {"좌", "왼쪽"}:
        return 0

    if side in {"우", "오른쪽"}:
        return 1

    if side in {"양측", "양쪽"}:
        return None

    return 1


def color_class_for_text(text):
    """
    결과 텍스트에 따라 CSS 색상 class를 반환합니다.
    """
    if text is None:
        return "text-normal"

    value = str(text)

    if any(token in value for token in ["감소", "지연", "소실", "비정상", "전도차단", "항진", "동원감소", "불가"]):
        return "text-red"

    if any(token in value for token in ["정상", "보존", "Silent", "Normal"]):
        return "text-blue"

    return "text-normal"
