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

    # 🚨 버튼 사이 간격을 좁히고 화면 정중앙에 오도록 여백 컬럼 배치
    # 비율: 양끝 여백(1.5), 중앙 버튼(1, 1), 사이 간격(0.2)
    col_left, col_home, col_gap, col_back, col_right = st.columns([1.5, 1, 0.2, 1, 1.5])

    with col_home:
        if st.button("처음", type="primary", use_container_width=True, key="nav_home_bottom"):
            _go_home()

    with col_back:
        if st.button("이전", type="primary", use_container_width=True, key="nav_back_bottom"):
            _go_back()

    st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

def render_top_navigation():
    pass
