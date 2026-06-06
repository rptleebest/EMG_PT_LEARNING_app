# data/terms.py

import re

def parse_ncs_value(value_str):
    if not value_str:
        return "Normal"
    lower_val = value_str.lower()
    
    if "정상" in lower_val or "normal" in lower_val or "보존" in lower_val:
        return "Normal"
    if "소실" in lower_val or "absent" in lower_val or "no response" in lower_val or "반응 소실" in lower_val:
        return "Absent"
    if "지연" in lower_val or "delayed" in lower_val or "느림" in lower_val:
        return "Delayed"
    if "감소" in lower_val or "reduced" in lower_val or "decreased" in lower_val:
        return "Reduced"
    return value_str

def ncs_amplitude_latency(value_str):
    if isinstance(value_str, tuple):
        return {
            "amplitude": parse_ncs_value(value_str[0]),
            "latency": parse_ncs_value(value_str[1])
        }
    val = parse_ncs_value(value_str)
    return {"amplitude": val, "latency": val}

def special_term_label(val):
    if not val:
        return ""
    if isinstance(val, tuple):
        return val[0]
    return str(val)

def emg_case_label(state_str):
    if not state_str:
        return {"rest": "Normal", "volition": "Normal"}
        
    s = str(state_str).lower()
    
    if "normal" in s or "정상" in s or s == "emg_normal":
        return {"rest": "Silent at rest", "volition": "Normal MU recruitment"}
    if "active_denervation" in s:
        return {"rest": "fibrillation potential, positive sharp wave", "volition": "Reduced MU recruitment"}
    if "paraspinal_denervation" in s:
        return {"rest": "fibrillation potential, positive sharp wave", "volition": "통증 및 환자 협조 부족으로 검사 제한"}
    if "chronic_reinnervation" in s:
        return {"rest": "Silent at rest", "volition": "Giant MUAPs with reduced recruitment"}
    if "active_chronic" in s:
        return {"rest": "fibrillation potential", "volition": "Giant MUAPs with reduced recruitment"}
        
    return {"rest": "Unknown", "volition": "Unknown"}
