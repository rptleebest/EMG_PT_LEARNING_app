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
    
    # CSS에서 너비를 강제하므로 st.columns 개수만 선언하면 중앙에 딱 맞게 정렬됨
    col1, col2 = st.columns(2)

    with col1:
        if st.button("처음", type="secondary", key="nav_home"):
            _go_home()
    with col2:
        if st.button("이전", type="primary", key="nav_back"):
            _go_back()

    st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)

def render_top_navigation():
    pass
