# utils/state.py

import streamlit as st
from data.constants import MODE_CASE


def init_app_state():
    defaults = {
        "screen": "home",
        "mode": MODE_CASE,
        "selected_case": None,
        "analysis_text": None,
        "last_result": None,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value