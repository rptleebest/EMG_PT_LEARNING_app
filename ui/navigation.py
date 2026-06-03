# ui/navigation.py

import streamlit as st

def _go_home():
    st.session_state["screen"] = "home"
    st.rerun()

def _go_back():
    current = st.session_state.get("screen")
    st.session_state["screen"] = "case_list" if current == "case_detail" else "home"
    st.rerun()

def render_bottom_navigation():
    if st.session_state.get("screen", "home") == "home": return
    st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
    
    # CSS에서 너비를 제어하므로 컬럼만 선언하면 중앙 정렬됨
    col1, col2 = st.columns(2)
    with col1:
        if st.button("처음", type="secondary", key="nav_home"): _go_home()
    with col2:
        if st.button("이전", type="primary", key="nav_back"): _go_back()

def render_top_navigation(): pass
