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

    st.markdown('<div style="height: 12px;"></div>', unsafe_allow_html=True)

    # st.columns를 화면 양쪽 여백(빈 컬럼)을 두어 가운데로 쏠리게 구성
    col_space1, col1, col2, col_space2 = st.columns([1, 2, 2, 1])

    with col1:
        if st.button("🏠 처음", type="primary", use_container_width=True, key="nav_home_bottom"):
            _go_home()

    with col2:
        if st.button("⬅️ 이전", type="primary", use_container_width=True, key="nav_back_bottom"):
            _go_back()

    st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

def render_top_navigation():
    pass
