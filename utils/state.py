# utils/state.py

import streamlit as st

from data.constants import MODE_CASE


def init_app_state():
    """Streamlit session_state 기본값을 초기화합니다."""
    defaults = {
        "screen": "home",
        "mode": MODE_CASE,
        "selected_case": None,
        "analysis_text": None,
        "last_result": None,
        "case_reset_counter": 0,
        "input_reset_counter": 0,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def reset_analysis_state():
    """분석 결과 관련 session_state만 초기화합니다."""
    st.session_state["analysis_text"] = None
    st.session_state["last_result"] = None


def reset_case_selection():
    """사례 선택 상태를 초기화합니다."""
    st.session_state["selected_case"] = None
    st.session_state["case_reset_counter"] = st.session_state.get("case_reset_counter", 0) + 1
    reset_analysis_state()


def reset_input_selection():
    """가상 결과표 선택 상태를 초기화합니다."""
    st.session_state["input_reset_counter"] = st.session_state.get("input_reset_counter", 0) + 1
    reset_analysis_state()
