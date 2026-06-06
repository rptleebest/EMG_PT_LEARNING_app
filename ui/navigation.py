# ui/navigation.py

import streamlit as st


def _go_home():
    st.session_state["screen"] = "home"
    st.session_state["selected_case"] = None
    st.session_state["analysis_text"] = None
    st.session_state["last_result"] = None
    st.rerun()


def _go_back():
    current = st.session_state.get("screen", "home")

    if current == "case_detail":
        st.session_state["screen"] = "case_list"
    elif current in {"case_list", "input_learning"}:
        st.session_state["screen"] = "home"
    else:
        st.session_state["screen"] = "home"

    st.rerun()


def render_top_navigation():
    """상단 네비게이션. 홈에서는 표시하지 않습니다."""
    if st.session_state.get("screen", "home") == "home":
        return

    st.markdown('<div class="top-bottom-nav-space"></div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 4])

    with col1:
        if st.button("🏠 처음", type="secondary", use_container_width=True, key="nav_home_top"):
            _go_home()

    with col2:
        if st.button("⬅️ 이전", type="secondary", use_container_width=True, key="nav_back_top"):
            _go_back()

    with col3:
        st.markdown("")


def render_bottom_navigation():
    """하단 네비게이션. 홈에서는 표시하지 않습니다."""
    if st.session_state.get("screen", "home") == "home":
        return

    st.markdown('<div style="height: 24px;"></div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("🏠 처음", type="primary", use_container_width=True, key="nav_home_bottom"):
            _go_home()

    with col2:
        if st.button("⬅️ 이전", type="primary", use_container_width=True, key="nav_back_bottom"):
            _go_back()

    st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)
