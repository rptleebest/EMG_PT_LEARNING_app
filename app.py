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
    html, body { overflow-x: hidden !important; background-color: #f8fafc !important; color: #1e293b !important; margin: 0; padding: 0; }
    .stApp { background-color: #f8fafc !important; overflow-x: hidden !important; }
    .main .block-container { max-width: 860px; padding: 1.5rem 1rem 4rem 1rem; margin: 0 auto; }
    p, span, div, li { word-break: keep-all; line-height: 1.6; text-align: left; }

    .content-card { background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px; margin-bottom: 16px; }
    .info-card { background: #f0f9ff; border: 1px solid #bae6fd; border-radius: 8px; padding: 16px; margin-bottom: 16px; }

    .section-title { font-size: 1.05rem; font-weight: 800; color: #0f172a; margin-bottom: 12px; border-bottom: 2px solid #3b82f6; padding-bottom: 4px; }
    .sub-title { font-size: 0.95rem; font-weight: 800; color: #1e3a8a; margin-top: 16px; margin-bottom: 12px; border-bottom: 1px dashed #93c5fd; padding-bottom: 4px; }

    .data-row { display: flex; flex-direction: row; align-items: flex-start; padding: 4px 0; border-bottom: 1px solid #f8fafc; }
    .data-row:last-child { border-bottom: none; }
    .data-label { flex: 0 0 100px; font-size: 0.88rem; font-weight: 700; color: #334155; line-height: 1.5; }
    .data-value { flex: 1; font-size: 0.88rem; font-weight: 400; color: #334155; line-height: 1.5; }

    .txt-normal { color: #334155 !important; }
    .txt-blue { color: #1d4ed8 !important; font-weight: 600 !important; }
    .txt-red { color: #b91c1c !important; font-weight: 600 !important; } 
    .txt-green { color: #15803d !important; font-weight: 600 !important; }

    .diagnosis-box { background: #fdf2f8; border: 1px solid #fce7f3; padding: 14px; border-radius: 6px; margin-top: 20px; }

    /* 🚨 모바일 버튼 잘림 방지: 너비 고정 및 중앙 정렬 */
    div[data-testid="stHorizontalBlock"] { 
        display: flex !important; justify-content: center !important; gap: 10px !important; flex-wrap: nowrap !important; 
    }
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"] { 
        flex: 0 0 115px !important; width: 115px !important; min-width: 115px !important;
    }
    div[data-testid="stButton"] > button {
        width: 100% !important; border-radius: 6px !important; border: none !important;
        font-weight: 600 !important; font-size: 0.9rem !important; min-height: 42px !important; 
    }
    div[data-testid="stButton"] > button[kind="primary"] { background-color: #2563eb !important; color: #ffffff !important; }
    div[data-testid="stButton"] > button[kind="secondary"] { background-color: #e2e8f0 !important; color: #1e293b !important; }

    /* 단일 중앙 버튼 */
    .center-btn-container { display: flex; justify-content: center; width: 100%; margin: 20px 0; }
    .center-btn-container div[data-testid="stButton"] > button { width: 180px !important; }

    @media (max-width: 768px) {
        .data-label { flex: 0 0 85px; font-size: 0.85rem; }
        .data-value { font-size: 0.85rem; }
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="근전도 판독 보조", page_icon="🧠", layout="wide", initial_sidebar_state="collapsed")
    init_app_state()
    apply_mobile_first_style()
    render_top_navigation()
    render_router()

if __name__ == "__main__":
    main()
