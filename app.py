# app.py

import streamlit as st
from ui.home import render_home
from ui.case_learning import render_case_list
from ui.input_learning import render_input_learning
from ui.navigation import render_top_navigation

def init_app_state():
    defaults = {"screen": "home", "mode": "case", "case_reset_counter": 0, "input_reset_counter": 0}
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

def render_router():
    screen = st.session_state.get("screen", "home")
    if screen == "case_list": 
        render_case_list()
    elif screen == "input_learning": 
        render_input_learning()
    else: 
        render_home()

def apply_mobile_first_style():
    st.markdown("""
    <style>
    /* 화면 기본 설정 및 가로 스크롤 방지 */
    html, body { overflow-x: hidden !important; background-color: #f8fafc !important; color: #1e293b !important; }
    .stApp { background-color: #f8fafc !important; overflow-x: hidden !important; }
    .main .block-container { max-width: 900px; padding: 1.5rem 1rem 4rem 1rem; }

    /* 텍스트 기본 가독성 */
    p, span, div { word-break: keep-all; line-height: 1.6; }
    
    /* 카드 컨테이너 (그림자 최소화, 깔끔한 테두리) */
    .content-card { background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px 16px; margin-bottom: 16px; }
    .info-card { background: #f0f9ff; border: 1px solid #bae6fd; border-radius: 8px; padding: 16px; margin-bottom: 16px; }

    /* 제목 스타일 (한글 아래 영문 바짝 붙이기) */
    .title-box { margin-bottom: 14px; border-bottom: 2px solid #3b82f6; padding-bottom: 6px; }
    .title-kor { font-size: 1.15rem; font-weight: 800; color: #0f172a; line-height: 1.2; margin-bottom: 2px; }
    .title-eng { font-size: 0.85rem; font-weight: 500; color: #64748b; line-height: 1.0; margin-top: 0px; letter-spacing: -0.01em; }

    /* 항목(굵게)과 내용(얇게) 분리 레이아웃 */
    .data-row { display: flex; flex-direction: row; align-items: flex-start; padding: 6px 0; border-bottom: 1px solid #f1f5f9; }
    .data-row:last-child { border-bottom: none; }
    .data-label { flex: 0 0 100px; font-size: 0.9rem; font-weight: 700; color: #1e293b; line-height: 1.5; }
    .data-value { flex: 1; font-size: 0.9rem; font-weight: 400; color: #334155; line-height: 1.5; }

    /* 색상 톤 다운 (눈 피로도 감소) */
    .txt-normal { color: #334155 !important; }
    .txt-blue { color: #2563eb !important; font-weight: 500 !important; }
    .txt-red { color: #b91c1c !important; font-weight: 600 !important; } /* 쨍한 빨강 대신 차분한 딥레드 */
    .txt-green { color: #15803d !important; font-weight: 600 !important; }

    /* 의심질환 추정 진단명 카드 (좌측 정렬) */
    .diagnosis-box { background: #f8fafc; border-left: 5px solid #3b82f6; padding: 16px; border-radius: 6px; margin-bottom: 20px; }
    .diagnosis-label { font-size: 0.85rem; font-weight: 600; color: #64748b; margin-bottom: 4px; }
    .diagnosis-name { font-size: 1.1rem; font-weight: 800; color: #0f172a; }

    /* 2D 플랫 버튼 스타일 */
    div[data-testid="stButton"] > button {
        border-radius: 6px !important; border: none !important; box-shadow: none !important;
        font-weight: 600 !important; font-size: 0.95rem !important; min-height: 44px !important; 
        transition: background-color 0.2s ease !important; transform: none !important;
    }
    div[data-testid="stButton"] > button[kind="primary"] { background-color: #2563eb !important; color: #ffffff !important; }
    div[data-testid="stButton"] > button[kind="secondary"] { background-color: #e2e8f0 !important; color: #1e293b !important; }

    /* 단일 버튼 중앙 정렬 */
    .center-btn div[data-testid="stButton"] > button { width: 200px !important; margin: 0 auto !important; display: block !important; }

    /* 네비게이션(처음/이전) 강제 가로 중앙 정렬 (모바일 세로쌓임 방지) */
    .nav-container { display: flex !important; flex-direction: row !important; justify-content: center !important; gap: 12px !important; width: 100% !important; }
    div[data-testid="stHorizontalBlock"] { display: flex !important; flex-wrap: nowrap !important; justify-content: center !important; gap: 12px !important; }
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"] { flex: 0 0 auto !important; width: 120px !important; min-width: 120px !important; }
    div[data-testid="stHorizontalBlock"] button { width: 100% !important; }

    @media (max-width: 768px) {
        .main .block-container { padding: 1rem 0.5rem 3rem 0.5rem; }
        .data-label { flex: 0 0 85px; font-size: 0.85rem; }
        .data-value { font-size: 0.85rem; }
    }
    #top-anchor { display: none; }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="교육용 근전도 판독 보조", page_icon="🧠", layout="wide", initial_sidebar_state="collapsed")
    init_app_state()
    apply_mobile_first_style()
    render_top_navigation()
    render_router()

if __name__ == "__main__":
    main()
