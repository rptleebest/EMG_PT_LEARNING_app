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

    st.markdown('<div style="height: 16px;"></div>', unsafe_allow_html=True)

    # st.columns를 생성하고 CSS flex 설정을 통해 항상 가운데로 모이도록 함
    col1, col2 = st.columns(2)

    with col1:
        if st.button("처음", type="secondary", use_container_width=True, key="nav_home"):
            _go_home()
    with col2:
        if st.button("이전", type="primary", use_container_width=True, key="nav_back"):
            _go_back()

    st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)

def render_top_navigation():
    pass
