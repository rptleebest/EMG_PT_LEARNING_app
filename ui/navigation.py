# ui/navigation.py

import streamlit as st


def _go_home():
    st.session_state["screen"] = "home"
    st.session_state["selected_case"] = None
    st.session_state["analysis_text"] = None
    st.session_state["last_result"] = None
    st.rerun()


def _go_back():
    current = st.session_state.get("screen")

    if current == "case_detail":
        st.session_state["screen"] = "case_list"
    elif current in ["case_list", "input_learning"]:
        st.session_state["screen"] = "home"
    else:
        st.session_state["screen"] = "home"

    st.rerun()


def render_navigation(position: str = "top"):
    if st.session_state.get("screen") == "home":
        return

    if position == "top":
        st.markdown('<div class="top-bottom-nav-space"></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="bottom-nav-space"></div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🏠 처음으로", use_container_width=True, key=f"nav_home_button_{position}"):
            _go_home()

    with col2:
        if st.button("⬅️ 이전으로", use_container_width=True, key=f"nav_back_button_{position}"):
            _go_back()

    st.markdown("<hr/>", unsafe_allow_html=True)


def render_top_navigation():
    render_navigation("top")


def render_bottom_navigation():
    render_navigation("bottom")
