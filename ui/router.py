import streamlit as st
from ui.home import render_home
from ui.case_learning import render_case_list
from ui.input_learning import render_input_learning

def render_router():
    screen = st.session_state.get("screen", "home")
    if screen == "home":
        render_home()
    elif screen == "case_list":
        render_case_list()
    elif screen == "input_learning":
        render_input_learning()
    else:
        st.session_state["screen"] = "home"
        st.rerun()
