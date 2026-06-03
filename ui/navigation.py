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


def render_bottom_navigation():
    if st.session_state.get("screen", "home") == "home":
        return

    st.markdown('<div style="height: 24px;"></div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        # type="primary"를 주어 무조건 파란색이 되도록 지정
        if st.button("🏠 처음으로", type="primary", use_container_width=True, key="nav_home_bottom"):
            _go_home()

    with col2:
        # type="primary"를 주어 무조건 파란색이 되도록 지정
        if st.button("⬅️ 이전으로", type="primary", use_container_width=True, key="nav_back_bottom"):
            _go_back()

    st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)


def render_top_navigation():
    pass
