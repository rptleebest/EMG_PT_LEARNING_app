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
    /* 가로 스크롤 완벽 차단 */
    html, body { overflow-x: hidden !important; max-width: 100vw !important; margin: 0; padding: 0; }
    
    :root {
        --bg: #f8fafc; --card: #ffffff; --text: #0f172a; --muted: #475569;
        --line: #e2e8f0; --blue: #2563eb; --red: #dc2626;
    }
    
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stMain"] { 
        background: var(--bg) !important; color: var(--text) !important; overflow-x: hidden !important; 
    }
    [data-testid="stToolbar"] { background: transparent !important; }

    .main .block-container { max-width: 980px; padding: 1rem 0.75rem 3rem 0.75rem; overflow-x: hidden !important; }

    /* 기본 텍스트 스타일 */
    .subtle { font-size: 0.88rem; font-weight: 400; color: #64748b; line-height: 1.6; margin-bottom: 1.2rem; word-break: keep-all; }

    /* 카드 스타일 */
    .section-card, .info-card, .warn-card { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 14px 12px; margin-bottom: 14px; }
    .info-card { background: #f8fbff; border-color: #dbeafe; }
    .warn-card { background: #fffaf3; border-color: #fed7aa; }

    /* 🚨 영문 제목 분리 및 간격/톤 최적화 */
    .title-box { background: #f1f5f9; border-left: 4px solid var(--blue); border-radius: 6px; padding: 8px 10px; margin-bottom: 12px; line-height: 1.15; }
    .title-kor { font-size: 0.95rem; font-weight: 800; color: #0f172a; margin-bottom: 2px; }
    .title-eng { font-size: 0.75rem; font-weight: 400; color: #64748b; letter-spacing: -0.01em; }
    
    .main-title-kor { font-size: 1.25rem; font-weight: 800; color: #0f172a; margin-bottom: 2px; line-height: 1.2; word-break: keep-all; }
    .main-title-eng { font-size: 0.85rem; font-weight: 400; color: #64748b; margin-bottom: 10px; line-height: 1.1; }

    .result-label-box { background: #f0f9ff; border-left: 4px solid #0ea5e9; border-radius: 6px; padding: 8px 10px; margin-top: 16px; margin-bottom: 10px; line-height: 1.15; }

    /* 🚨 진단명 스타일 (문장/글자 삭제, 중앙 정렬의 깔끔한 폰트) */
    .diag-box { background: #fdf2f8; border: 1px solid #fce7f3; padding: 16px 12px; border-radius: 10px; margin-bottom: 16px; text-align: center; line-height: 1.2; box-shadow: 0 2px 8px rgba(0,0,0,0.02); }
    .diag-kor { font-size: 1.1rem; font-weight: 800; color: #991b1b; margin-bottom: 3px; word-break: keep-all; }
    .diag-eng { font-size: 0.8rem; font-weight: 400; color: #f87171; letter-spacing: -0.01em; }

    /* 목록 스타일 */
    .case-bullet { font-size: 0.88rem; font-weight: 400; color: #334155; line-height: 1.6; margin-bottom: 8px; word-break: keep-all; }
    .finding-highlight-kor { font-size: 0.92rem; font-weight: 800; color: #1e3a8a; margin-top: 14px; margin-bottom: 1px; }
    .finding-highlight-eng { font-size: 0.75rem; font-weight: 400; color: #64748b; margin-bottom: 8px; border-bottom: 1px solid #e2e8f0; padding-bottom: 4px; }

    /* 🚨 결과표/항목 가독성 역전 해결 (항목은 진하게, 설명은 가늘게) */
    .data-line { display: flex; flex-direction: row; align-items: flex-start; margin-bottom: 6px; padding-bottom: 6px; border-bottom: 1px solid #f8fafc; }
    .data-line:last-child { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }
    .data-lbl { flex: 0 0 95px; font-size: 0.86rem; font-weight: 800; color: #0f172a; line-height: 1.4; }
    .data-val { flex: 1; font-size: 0.86rem; font-weight: 400; color: #475569; line-height: 1.5; word-break: keep-all; }
    
    .text-blue { color: #2563eb !important; font-weight: 600 !important; }
    .text-red { color: #dc2626 !important; font-weight: 600 !important; }
    .text-green { color: #16a34a !important; font-weight: 600 !important; }

    /* 🚨 2D 플랫 버튼 스타일 (입체감 완전 제거, 깔끔한 곡선 처리) */
    div[data-testid="stButton"] > button {
        border-radius: 6px !important; border: none !important; box-shadow: none !important;
        font-weight: 600 !important; font-size: 0.92rem !important; min-height: 44px !important; 
        color: #ffffff !important; transition: opacity 0.2s ease !important;
        transform: none !important; /* 클릭 시 눌리는 효과 제거 (순수 2D) */
    }
    div[data-testid="stButton"] > button:active { opacity: 0.7 !important; }
    div[data-testid="stButton"] > button[kind="primary"] { background-color: #3b82f6 !important; }
    div[data-testid="stButton"] > button[kind="secondary"] { background-color: #64748b !important; }

    /* 단일 중앙 버튼 강제 지정 */
    .center-btn-wrapper div[data-testid="stButton"] > button {
        width: 220px !important; margin: 0 auto !important; display: block !important;
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
