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
    /* 기본 여백 및 배경 설정 (가로 스크롤 방지) */
    html, body { overflow-x: hidden !important; background-color: #f8fafc !important; color: #1e293b !important; }
    .stApp { background-color: #f8fafc !important; overflow-x: hidden !important; }
    
    /* 본문 너비 조절 및 모바일 패딩 최적화 */
    .main .block-container { max-width: 860px; padding: 1.5rem 1.2rem 4rem 1.2rem; }

    /* 텍스트 양쪽 정렬 적용 (가독성 증대) */
    p, span, div, li { word-break: keep-all; line-height: 1.6; text-align: justify; }

    /* 카드 컨테이너 (그림자 없이 깔끔하게) */
    .content-card { background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px 14px; margin-bottom: 16px; }
    
    /* 제목 스타일 (불필요한 여백/크기 축소) */
    .title-box { margin-bottom: 12px; border-bottom: 2px solid #3b82f6; padding-bottom: 4px; }
    .title-kor { font-size: 1.05rem; font-weight: 800; color: #0f172a; }

    /* 진단명 카드 (글자 크기 축소, 색상/굵기 대비로 세련되게) */
    .diagnosis-box { background: #f8fafc; border-left: 4px solid #2563eb; padding: 12px 14px; border-radius: 6px; margin-bottom: 16px; }
    .diagnosis-label { font-size: 0.9rem; font-weight: 600; color: #64748b; margin-bottom: 2px; }
    .diagnosis-name { font-size: 1.0rem; font-weight: 800; color: #b91c1c; } /* 차분한 딥 레드 */

    /* 항목(굵게)과 내용(얇게) 인라인/블록 레이아웃 */
    .data-row { display: flex; flex-direction: row; align-items: flex-start; padding: 4px 0; }
    .data-label { flex: 0 0 100px; font-size: 0.9rem; font-weight: 700; color: #1e293b; }
    .data-value { flex: 1; font-size: 0.9rem; font-weight: 400; color: #334155; }

    /* 침근전도 근육별 구분을 위한 블록 스타일 */
    .muscle-block { background: #f1f5f9; padding: 12px; border-radius: 8px; margin-bottom: 12px; border: 1px solid #e2e8f0; }
    .muscle-title { font-size: 0.95rem; font-weight: 800; color: #0f172a; border-bottom: 1px dashed #cbd5e1; padding-bottom: 6px; margin-bottom: 8px; }

    /* 색상 톤 다운 (시각적 편안함) */
    .txt-normal { color: #334155 !important; }
    .txt-blue { color: #1d4ed8 !important; font-weight: 600 !important; }
    .txt-red { color: #b91c1c !important; font-weight: 600 !important; } 
    .txt-green { color: #15803d !important; font-weight: 600 !important; }

    /* 🚨 2D 플랫 버튼 스타일 */
    div[data-testid="stButton"] > button {
        border-radius: 6px !important; border: none !important; box-shadow: none !important;
        font-weight: 600 !important; font-size: 0.95rem !important; min-height: 42px !important; 
        transition: background-color 0.2s ease !important; transform: none !important;
    }
    div[data-testid="stButton"] > button[kind="primary"] { background-color: #2563eb !important; color: #ffffff !important; }
    div[data-testid="stButton"] > button[kind="secondary"] { background-color: #e2e8f0 !important; color: #1e293b !important; }

    /* 🚨 단일 버튼 및 네비게이션 가로 중앙 정렬 (본문 밖으로 나가지 않게) */
    .stButton { text-align: center; }
    div[data-testid="stHorizontalBlock"] { display: flex !important; flex-wrap: nowrap !important; justify-content: center !important; gap: 10px !important; max-width: 100%; margin: 0 auto !important; }
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"] { flex: 0 0 120px !important; width: 120px !important; min-width: 120px !important; }
    div[data-testid="stHorizontalBlock"] button { width: 100% !important; padding: 0 !important; }

    @media (max-width: 768px) {
        .main .block-container { padding: 1rem 0.75rem 3rem 0.75rem; }
        .data-label { flex: 0 0 85px; font-size: 0.85rem; }
        .data-value { font-size: 0.85rem; }
        /* 모바일에서는 버튼 너비 조정 */
        div[data-testid="stHorizontalBlock"] > div[data-testid="column"] { flex: 0 0 48% !important; width: 48% !important; min-width: 48% !important; }
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
