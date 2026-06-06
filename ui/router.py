# ui/router.py

import streamlit as st

from ui.home import render_home
from ui.case_learning import render_case_list, render_case_detail
from ui.input_learning import render_input_learning


VALID_SCREENS = {
    "home",
    "case_list",
    "case_detail",
    "input_learning",
}


def go_home() -> None:
    """
    잘못된 화면 상태가 들어왔을 때 안전하게 홈으로 이동합니다.
    """
    st.session_state["screen"] = "home"
    render_home()


def render_router() -> None:
    """
    현재 session_state['screen'] 값에 맞는 화면을 렌더링합니다.

    화면 구조:
    - home: 홈 화면
    - case_list: 사례 학습 목록
    - case_detail: 사례 상세 학습
    - input_learning: 가상 검사결과표 해석
    """
    screen = st.session_state.get("screen", "home")

    if screen not in VALID_SCREENS:
        go_home()
        return

    if screen == "home":
        render_home()
        return

    if screen == "case_list":
        render_case_list()
        return

    if screen == "case_detail":
        selected_case = st.session_state.get("selected_case")

        if not selected_case:
            st.session_state["screen"] = "case_list"
            render_case_list()
            return

        render_case_detail()
        return

    if screen == "input_learning":
        render_input_learning()
        return

    go_home()
