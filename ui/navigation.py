# ui/navigation.py

import streamlit as st


def _go_home():
    """
    메인 화면(처음)으로 이동합니다.
    모든 모드 선택 및 세부 데이터 바인딩을 리셋하고 홈으로 돌아갑니다.
    """
    st.session_state["screen"] = "home"
    st.session_state["selected_case"] = None
    st.session_state["analysis_text"] = None
    st.session_state["last_result"] = None

    # 라디오 선택 버튼 상태도 자동으로 '선택 안 함'으로 초기화되도록 카운터 증가
    st.session_state["case_reset_counter"] = st.session_state.get("case_reset_counter", 0) + 1
    st.session_state["input_reset_counter"] = st.session_state.get("input_reset_counter", 0) + 1

    st.rerun()


def _go_back():
    """
    이전 단계로 지능형 이동합니다.
    - 세부 결과표/임상사례 상세 화면이 열려 있을 때: 해당 학습 모드의 '목록 화면(선택 안 함)'으로 돌아갑니다.
    - 이미 목록 화면일 때: 메인 홈 화면으로 돌아갑니다.
    """
    current_screen = st.session_state.get("screen", "home")

    if current_screen == "case_list":
        # 1. 사례 학습 모드 단계 확인
        counter = st.session_state.get("case_reset_counter", 0)
        radio_key = f"case_radio_selector_{counter}"
        current_selection = st.session_state.get(radio_key, "선택 안 함")

        if current_selection != "선택 안 함":
            # 상세 분석을 보던 중이면 목록 화면으로 1단계 이전 (카운터 증가로 라디오 리셋)
            st.session_state["case_reset_counter"] = counter + 1
        else:
            # 이미 목록 화면 상태이면 메인 홈으로 이동
            st.session_state["screen"] = "home"

    elif current_screen == "input_learning":
        # 2. 가상 결과표 판독 모드 단계 확인
        counter = st.session_state.get("input_reset_counter", 0)
        radio_key = f"input_report_selector_{counter}"
        current_selection = st.session_state.get(radio_key, "선택 안 함")

        if current_selection != "선택 안 함":
            # 가상 결과표 상세 분석 중이면 목록 화면으로 1단계 이전 (카운터 증가로 라디오 리셋)
            st.session_state["input_reset_counter"] = counter + 1
        else:
            # 이미 목록 화면 상태이면 메인 홈으로 이동
            st.session_state["screen"] = "home"

    else:
        # 기타 화면은 홈으로 이동
        st.session_state["screen"] = "home"

    st.rerun()


def render_bottom_navigation():
    """
    하단 내비게이션 바 렌더링.
    모바일 화면에서도 본문 중앙 정렬 및 여백 레이아웃이 무너지지 않도록 설정합니다.
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
    필요 시 상단 바 구현을 위한 플레이스홀더 함수입니다.
    """
    pass
