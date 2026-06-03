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
    /* 전체 배경 및 스크롤 안정화 */
    html, body { overflow-x: hidden !important; background-color: #f8fafc !important; color: #1e293b !important; margin: 0; padding: 0; }
    .stApp { background-color: #f8fafc !important; overflow-x: hidden !important; }
    
    /* 모바일/PC 본문 여백 최적화 (양쪽 잘림 방지) */
    .main .block-container { max-width: 860px; padding: 1.5rem 1.2rem 4rem 1.2rem; margin: 0 auto; }

    /* 텍스트 정렬 (양쪽 정렬 부작용 해결 -> 왼쪽 정렬 + 단어 단위 줄바꿈 유지) */
    p, span, div, li { word-break: keep-all; line-height: 1.6; text-align: left; }

    /* 카드 컨테이너 (깔끔한 테두리) */
    .content-card { background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px 14px; margin-bottom: 16px; box-shadow: 0 1px 2px rgba(0,0,0,0.02); }
    .info-card { background: #f0f9ff; border: 1px solid #bae6fd; border-radius: 8px; padding: 16px; margin-bottom: 16px; }

    /* 대항목 제목 */
    .section-title { font-size: 1.05rem; font-weight: 800; color: #0f172a; margin-bottom: 12px; border-bottom: 2px solid #3b82f6; padding-bottom: 4px; }
    
    /* 중항목 제목 (검사명 등) */
    .sub-title { font-size: 0.95rem; font-weight: 800; color: #1e3a8a; margin-top: 16px; margin-bottom: 12px; border-bottom: 1px dashed #93c5fd; padding-bottom: 4px; }

    /* 항목-데이터 나열 포맷 */
    .data-row { display: flex; flex-direction: row; align-items: flex-start; padding: 4px 0; border-bottom: 1px solid #f8fafc; }
    .data-row:last-child { border-bottom: none; }
    .data-label { flex: 0 0 100px; font-size: 0.9rem; font-weight: 700; color: #1e293b; line-height: 1.5; }
    .data-value { flex: 1; font-size: 0.9rem; font-weight: 400; color: #334155; line-height: 1.5; }

    /* 글자 색상 세팅 */
    .txt-normal { color: #334155 !important; }
    .txt-blue { color: #1d4ed8 !important; font-weight: 600 !important; }
    .txt-red { color: #b91c1c !important; font-weight: 600 !important; } 
    .txt-green { color: #15803d !important; font-weight: 600 !important; }

    /* 🚨 2D 플랫 버튼 스타일 */
    div[data-testid="stButton"] > button {
        border-radius: 6px !important; border: none !important; box-shadow: none !important;
        font-weight: 600 !important; font-size: 0.95rem !important; min-height: 44px !important; 
        transition: background-color 0.2s ease !important; transform: none !important;
    }
    div[data-testid="stButton"] > button[kind="primary"] { background-color: #2563eb !important; color: #ffffff !important; }
    div[data-testid="stButton"] > button[kind="secondary"] { background-color: #e2e8f0 !important; color: #1e293b !important; }

    /* 🚨 네비게이션 버튼 짤림 방지 (Streamlit 기본 반응형 시스템 활용) */
    .nav-wrapper { padding: 0 10%; margin-top: 10px; }

    @media (max-width: 768px) {
        .main .block-container { padding: 1rem 0.8rem 3rem 0.8rem; }
        .data-label { flex: 0 0 85px; font-size: 0.85rem; }
        .data-value { font-size: 0.85rem; }
        .nav-wrapper { padding: 0 2%; } /* 모바일에서는 여백 최소화하여 버튼 짤림 방지 */
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
