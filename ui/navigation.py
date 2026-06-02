# ui/navigation.py

import streamlit as st


def _go_home():
    """메인 홈 화면으로 상태를 초기화하고 이동합니다."""
    st.session_state["screen"] = "home"
    st.session_state["selected_case"] = None
    st.session_state["analysis_text"] = None
    st.session_state["last_result"] = None
    st.rerun()


def _go_back():
    """현재 화면 상태를 기반으로 적절한 이전 화면으로 이동합니다."""
    current = st.session_state.get("screen")

    if current == "case_detail":
        st.session_state["screen"] = "case_list"
    elif current in ["case_list", "input_learning"]:
        st.session_state["screen"] = "home"
    else:
        st.session_state["screen"] = "home"

    st.rerun()


def render_bottom_navigation():
    """하단 내비게이션 렌더링 (모바일 최적화 여백 포함)"""
    # 홈 화면에서는 내비게이션을 숨김
    if st.session_state.get("screen", "home") == "home":
        return

    # 하단 내비게이션 상단 여백
    st.markdown('<div style="height: 24px;"></div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🏠 처음으로", use_container_width=True, key="nav_home_bottom"):
            _go_home()

    with col2:
        if st.button("⬅️ 이전으로", use_container_width=True, key="nav_back_bottom"):
            _go_back()

    # 하단 기기 베젤 겹침 방지용 안전 여백
    st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)


def render_top_navigation():
    """
    [상단 버튼 완전 차단(Kill-Switch)]
    main.py 등 다른 파일에서 이 함수를 호출하더라도 
    화면에 아무것도 그리지 않고 무시하도록 처리합니다.
    """
    pass
