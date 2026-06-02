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


def render_navigation(position: str = "bottom"):
    """
    위치(top/bottom)에 따라 최적화된 여백과 버튼을 렌더링합니다.
    """
    # 홈 화면에서는 내비게이션을 숨김
    if st.session_state.get("screen", "home") == "home":
        return

    # 위치별 상단 여백 (하단 내비게이션일 경우 모바일 스크롤 여유 공간 확보)
    if position == "top":
        st.markdown('<div style="height: 4px;"></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="height: 24px;"></div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🏠 처음으로", use_container_width=True, key=f"nav_home_{position}"):
            _go_home()

    with col2:
        if st.button("⬅️ 이전으로", use_container_width=True, key=f"nav_back_{position}"):
            _go_back()

    # 상단 내비게이션일 경우에만 콘텐츠와의 분리를 위해 구분선(hr) 렌더링
    if position == "top":
        st.markdown("<hr style='margin-top: 12px; margin-bottom: 20px;'/>", unsafe_allow_html=True)
    else:
        # 하단 내비게이션일 경우 기기 하단 베젤 겹침 방지용 여백 추가
        st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)


def render_top_navigation():
    """짧은 안내 화면 등에서 호출할 상단 내비게이션"""
    render_navigation("top")


def render_bottom_navigation():
    """길이가 긴 학습/판독 화면 등에서 호출할 하단 내비게이션"""
    render_navigation("bottom")
