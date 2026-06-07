# ui/navigation.py

import streamlit as st


def _clear_learning_state() -> None:
    """
    화면 이동 시 이전 학습 결과나 선택값이 과도하게 남지 않도록 정리합니다.
    """
    st.session_state["selected_case"] = None
    st.session_state["analysis_text"] = None
    st.session_state["last_result"] = None

    if "input_reset_counter" not in st.session_state:
        st.session_state["input_reset_counter"] = 0


def _go_home() -> None:
    """홈 화면으로 이동합니다."""
    st.session_state["screen"] = "home"
    _clear_learning_state()
    st.rerun()


def _go_back() -> None:
    """현재 화면에 따라 이전 화면으로 이동합니다."""
    current = st.session_state.get("screen", "home")

    if current == "case_detail":
        st.session_state["screen"] = "case_list"
    elif current in {"case_list", "input_learning"}:
        st.session_state["screen"] = "home"
        _clear_learning_state()
    else:
        st.session_state["screen"] = "home"
        _clear_learning_state()

    st.rerun()


def render_top_navigation() -> None:
    """
    요청에 따라 상단 네비게이션 버튼은 출력하지 않습니다.
    """
    pass


def render_bottom_navigation() -> None:
    """
    하단 네비게이션을 출력합니다. 버튼을 중앙으로 정렬합니다.
    """
    if st.session_state.get("screen", "home") == "home":
        return

    st.markdown('<div style="height: 32px;"></div>', unsafe_allow_html=True)

    # [여백, 버튼1, 버튼2, 여백] 비율로 중앙 정렬
    spacer1, col1, col2, spacer2 = st.columns([1, 1.2, 1.2, 1])

    with col1:
        if st.button("🏠 처음", type="primary", use_container_width=True, key="nav_home_bottom"):
            _go_home()

    with col2:
        if st.button("⬅️ 이전", type="primary", use_container_width=True, key="nav_back_bottom"):
            _go_back()

    st.markdown("<div style='height: 24px;'></div>", unsafe_allow_html=True)
