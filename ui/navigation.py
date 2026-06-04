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
    elif current in ["case_list", "input_learning"]:
        st.session_state["screen"] = "home"
    else:
        st.session_state["screen"] = "home"

    st.rerun()


def render_bottom_navigation():
    """
    하단 내비게이션.
    개선점:
    - 기존 st.columns가 전체 본문 폭을 차지하면서 모바일에서 버튼이 양끝으로 밀리는 문제가 있었음.
    - .nav-actions 래퍼 안에서 고정 폭 2열을 구성해 '처음 / 이전'이 항상 중앙에 바로 붙어 보이도록 수정.
    """
    if st.session_state.get("screen", "home") == "home":
        return

    st.markdown("<div class='nav-actions'>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🏠 처음", type="primary", use_container_width=True, key="nav_home_bottom"):
            _go_home()

    with col2:
        if st.button("⬅️ 이전", type="primary", use_container_width=True, key="nav_back_bottom"):
            _go_back()

    st.markdown("</div>", unsafe_allow_html=True)


def render_top_navigation():
    """
    현재는 상단 내비게이션을 사용하지 않습니다.
    필요 시 여기에 간단한 홈 버튼 또는 앱 제목 바를 추가할 수 있습니다.
    """
    return
