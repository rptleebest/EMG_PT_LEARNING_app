# ui/router.py

import streamlit as st

from ui.home import render_home
from ui.case_learning import render_case_list, render_case_detail
from ui.input_learning import render_input_learning


VALID_SCREENS = {
    "home",
    "case_list",
    "case_detail",
    "input_learning",
}


def render_router():
    screen = st.session_state.get("screen", "home")

    if screen not in VALID_SCREENS:
        st.session_state["screen"] = "home"
        render_home()
        return

    if screen == "home":
        render_home()
        return

    if screen == "case_list":
        render_case_list()
        return

    if screen == "case_detail":
        if not st.session_state.get("selected_case"):
            st.session_state["screen"] = "case_list"
            render_case_list()
            return
        render_case_detail()
        return

    if screen == "input_learning":
        render_input_learning()
        return
