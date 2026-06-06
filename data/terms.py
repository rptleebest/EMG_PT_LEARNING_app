# data/terms.py

def parse_amp(val):
    s = str(val).lower()
    if "normal" in s or "정상" in s: return "정상 범위"
    if "reduced" in s or "감소" in s: return "진폭 감소"
    if "absent" in s or "소실" in s: return "반응 소실"
    return "정상 범위"

def parse_lat(val):
    s = str(val).lower()
    if "normal" in s or "정상" in s: return "정상 범위"
    if "delayed" in s or "지연" in s: return "잠복기 지연"
    if "absent" in s or "소실" in s: return "반응 소실"
    return "정상 범위"

def ncs_amplitude_latency(value):
    """NCS 결과를 진폭(Amplitude)과 잠복기(Latency) 상태로 정밀 파싱합니다."""
    if isinstance(value, tuple) and len(value) == 2:
        return {"amplitude": parse_amp(value[0]), "latency": parse_lat(value[1])}
    return {"amplitude": parse_amp(value), "latency": parse_lat(value)}

def emg_case_label(val):
    """침근전도 상태를 임상적 용어로 완벽히 매핑합니다."""
    s = str(val).lower()
    if "normal" in s or "정상" in s or "emg_normal" in s:
        return {"rest": "전기적 침묵 (정상 반응)", "volition": "정상 운동단위 동원패턴"}
    if "active_denervation" in s:
        return {"rest": "비정상적 자발전위 출현", "volition": "감소된 운동단위 동원패턴"}
    if "paraspinal_denervation" in s:
        return {"rest": "비정상적 자발전위 출현", "volition": "통증/협조 부족으로 검사 제한"}
    if "chronic_reinnervation" in s:
        return {"rest": "전기적 침묵 (정상 반응)", "volition": "증가된 운동단위 동원패턴 (거대 전위)"}
    if "active_chronic" in s:
        return {"rest": "비정상적 자발전위 출현", "volition": "감소된 운동단위 동원패턴"}
    return {"rest": "-", "volition": "-"}

def special_term_label(val):
    """특수/반사 검사 용어를 매핑합니다."""
    if not val: return ""
    s = str(val[0] if isinstance(val, tuple) else val).lower()
    if "normal" in s or "정상" in s: return "정상 범위"
    if "delay" in s or "지연" in s: return "잠복기 지연"
    if "absent" in s or "소실" in s: return "반응 소실"
    if "hyper" in s or "increase" in s or "증가" in s: return "비정상적 증가"
    return str(val[0] if isinstance(val, tuple) else val)
