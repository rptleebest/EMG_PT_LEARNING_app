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
    /* 가로 스크롤 및 오버플로우 완벽 차단 */
    html, body { overflow-x: hidden !important; background-color: #f8fafc !important; color: #1e293b !important; margin: 0; padding: 0; }
    .stApp { background-color: #f8fafc !important; overflow-x: hidden !important; }
    
    /* 본문 패딩 최적화 */
    .main .block-container { max-width: 860px; padding: 1.5rem 1rem 4rem 1rem; }

    /* 텍스트 양쪽 정렬 및 어색한 공백 방지 */
    p, span, div, li { word-break: keep-all; line-height: 1.6; text-align: justify; }

    /* 기본 컨테이너 (그림자 제거, 라인 단순화) */
    .content-card { background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px; margin-bottom: 16px; }
    .info-card { background: #f0f9ff; border: 1px solid #bae6fd; border-radius: 8px; padding: 16px; margin-bottom: 16px; }

    /* 대항목 제목 스타일 */
    .title-box { margin-bottom: 16px; border-bottom: 2px solid #3b82f6; padding-bottom: 4px; }
    .title-kor { font-size: 1.1rem; font-weight: 800; color: #0f172a; }

    /* 의심질환 추정 진단명 카드 (색상 톤 다운, 굵기 최적화) */
    .diagnosis-box { background: #f8fafc; border-left: 4px solid #2563eb; padding: 14px; border-radius: 6px; margin-bottom: 20px; }
    .diagnosis-label { font-size: 0.85rem; font-weight: 700; color: #475569; margin-bottom: 4px; }
    .diagnosis-name { font-size: 1.05rem; font-weight: 800; color: #b91c1c; } /* 차분한 딥레드 */

    /* 검사 결과 데이터 나열 레이아웃 */
    .data-row { display: flex; flex-direction: row; align-items: flex-start; padding: 6px 0; border-bottom: 1px dashed #e2e8f0; }
    .data-row:last-child { border-bottom: none; }
    .data-label { flex: 0 0 90px; font-size: 0.9rem; font-weight: 700; color: #1e293b; }
    .data-value { flex: 1; font-size: 0.9rem; font-weight: 400; color: #334155; }

    /* 색상 클래스 (눈 피로도 감소) */
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

    /* 🚨 단일 중앙 버튼 강제 고정 */
    .center-btn div[data-testid="stButton"] > button { width: 220px !important; margin: 0 auto !important; display: block !important; }

    /* 🚨 처음/이전 버튼 오버플로우 방지 및 강제 축소 정렬 */
    div[data-testid="stHorizontalBlock"] { 
        display: flex !important; flex-wrap: nowrap !important; justify-content: center !important; 
        gap: 12px !important; max-width: 100vw !important; overflow: hidden !important; 
    }
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"] { 
        flex: 1 1 0 !important; max-width: 140px !important; min-width: 80px !important; 
    }
    div[data-testid="stHorizontalBlock"] button { width: 100% !important; padding: 0 !important; }

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
