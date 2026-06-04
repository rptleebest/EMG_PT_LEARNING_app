# utils/state.py

import streamlit as st
from data.constants import MODE_CASE


def init_app_state():
    """
    앱 전체 세션 상태 초기화.
    기존 코드에서 app.py와 utils/state.py에 초기화 함수가 중복되어 있었으므로
    이 파일을 단일 기준으로 사용합니다.
    """
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
