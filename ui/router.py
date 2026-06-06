# ui/router.py

import streamlit as st
from ui.case_learning import render_case_list, render_case_detail
from ui.input_learning import render_input_learning

def render_router():
    """세션 상태에 따라 화면을 분기합니다. app.py의 호출명과 일치시켰습니다."""
    screen = st.session_state.get("screen", "main")
    
    if screen == "case_list":
        render_case_list()
    elif screen == "case_detail":
        render_case_detail()
    elif screen == "input_learning":
        render_input_learning()
    else:
        # 기본 메인 화면 호출 로직 (필요 시 추가)
        pass
