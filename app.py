# app.py

import streamlit as st

from utils.state import init_app_state
from ui.navigation import render_top_navigation
from ui.router import render_router


def apply_mobile_first_style():
    st.markdown("""
    <style>
    :root {
        --bg: #f8fafc;
        --card: #ffffff;
        --text: #0f172a;
        --muted: #475569;
        --line: #e2e8f0;
        --soft: #f1f5f9;
        --blue: #2563eb;
        --blue-soft: #dbeafe;
        --green: #16a34a;
        --green-soft: #dcfce7;
        --amber: #d97706;
        --amber-soft: #ffedd5;
        --shadow: 0 8px 24px rgba(15, 23, 42, 0.05);
    }

    html, body, #root { background: var(--bg) !important; color: var(--text) !important; }
    .stApp { background: var(--bg) !important; color: var(--text) !important; }
    [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stMain"], [data-testid="stMainBlockContainer"], section.main, .main, [data-testid="stSidebar"] {
        background: var(--bg) !important;
    }
    [data-testid="stToolbar"] { background: transparent !important; }

    .main .block-container {
        max-width: 980px;
        padding-top: 1.2rem;
        padding-bottom: 4rem;
        padding-left: 0.85rem;
        padding-right: 0.85rem;
    }

    div[data-testid="stMarkdownContainer"], div[data-testid="stText"], p, li, span, label { color: var(--text); }

    .main-title { font-size: 1.34rem; font-weight: 800; color: var(--text) !important; line-height: 1.3; margin-bottom: 0.4rem; letter-spacing: -0.01em; word-break: keep-all; }
    .subtle { color: var(--muted) !important; font-size: 0.92rem; line-height: 1.65; margin-bottom: 1.2rem; word-break: keep-all; }

    .section-card, .result-card, .warn-card, .info-card {
        background: var(--card) !important; border: 1px solid var(--line) !important; border-radius: 16px; padding: 16px 14px; margin-bottom: 16px; box-shadow: var(--shadow);
    }
    .result-card { background: #f8fafc !important; border: 1px solid #cbd5e1 !important; }
    .warn-card { background: #fffaf3 !important; border: 1px solid #fed7aa !important; }
    .info-card { background: #f8fbff !important; border: 1px solid var(--blue-soft) !important; }

    .big-section-title, .case-section-label, .result-label {
        font-size: 0.98rem; font-weight: 700; color: #0f172a !important; background: #f1f5f9 !important; border-left: 4px solid var(--blue) !important; border-radius: 8px; padding: 10px 12px; margin-top: 8px; margin-bottom: 14px; line-height: 1.45; word-break: keep-all;
    }
    .result-label { border-left-color: #0ea5e9 !important; background: #f0f9ff !important; }

    .case-title-mobile, .case-subheading, .finding-item-title, .result-title, .input-title { font-size: 0.94rem; font-weight: 800; color: var(--text) !important; line-height: 1.5; margin-bottom: 8px; word-break: keep-all; }
    .case-subtitle-mobile, .mobile-note, .input-meta { color: var(--muted) !important; }

    .case-bullet, .case-bullet-strong, .finding-subtext, .result-text, .result-small { font-size: 0.88rem; color: #334155 !important; line-height: 1.65; margin-bottom: 10px; word-break: keep-all; }
    .case-text-block { background: #ffffff !important; border-left: 3px solid #e2e8f0 !important; border-radius: 8px; padding: 12px 14px; margin-bottom: 14px; }
    .item-divider { border: none; border-top: 1px solid #eef2f7 !important; margin: 12px 0; }

    .finding-highlight { color: #1e3a8a !important; font-weight: 700 !important; font-size: 0.98rem !important; margin-top: 14px; margin-bottom: 8px; border-bottom: 1px solid #e2e8f0; padding-bottom: 6px; }
    .label-strong { font-weight: 600 !important; color: #1e293b !important; font-size: 0.88rem !important; }   
    .result-value { font-weight: 400 !important; color: #334155 !important; margin-left: 4px; }

    .text-blue { color: #1e40af !important; font-weight: 600 !important; }
    .text-green { color: #15803d !important; font-weight: 600 !important; }
    .text-red { color: #991b1b !important; font-weight: 600 !important; }
    .case-bullet-strong { font-weight: 600 !important; color: #0f172a !important; }

    div[role="radiogroup"] label p, div[data-testid="stRadio"] label p { color: var(--text) !important; word-break: keep-all !important; line-height: 1.6 !important; }
    label[data-testid="stWidgetLabel"] p { font-size: 0.88rem !important; font-weight: 700 !important; color: #334155 !important; line-height: 1.5 !important; }

    /* ★ 공통 버튼 스타일 */
    div[data-testid="stButton"] > button {
        font-weight: 700 !important;
        border-radius: 12px !important;
        min-height: 48px !important;
        font-size: 0.96rem !important;
        width: 100% !important;
        margin: 0 auto !important;
        border: none !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
    }

    /* 1. 하단 네비게이션 버튼 (Primary) -> 파란색 */
    div[data-testid="stButton"] > button[kind="primary"],
    div[data-testid="stButton"] > button[data-testid="baseButton-primary"] {
        background-color: #1e40af !important; 
        box-shadow: 0 4px 12px rgba(30, 64, 175, 0.15) !important;
    }
    div[data-testid="stButton"] > button[kind="primary"]:hover,
    div[data-testid="stButton"] > button[data-testid="baseButton-primary"]:active {
        background-color: #1e3a8a !important;
    }

    /* 2. 위쪽 동작 버튼 (Secondary) -> 차분한 회색 */
    div[data-testid="stButton"] > button[kind="secondary"],
    div[data-testid="stButton"] > button[data-testid="baseButton-secondary"] {
        background-color: #475569 !important; 
        box-shadow: 0 4px 12px rgba(71, 85, 105, 0.15) !important;
        max-width: 320px !important; /* 위쪽 버튼은 중앙에 적당한 너비로 배치 */
    }
    div[data-testid="stButton"] > button[kind="secondary"]:hover,
    div[data-testid="stButton"] > button[data-testid="baseButton-secondary"]:active {
        background-color: #334155 !important;
    }

    @media (max-width: 768px) {
        .main .block-container { padding-top: 1rem; padding-bottom: 3rem; padding-left: 0.75rem; padding-right: 0.75rem; }
        .main-title { font-size: 1.2rem; } .subtle { font-size: 0.88rem; }
        .section-card, .result-card, .warn-card, .info-card { padding: 14px 12px; margin-bottom: 14px; }
        .big-section-title, .case-section-label, .result-label { font-size: 0.92rem; padding: 10px 10px; margin-bottom: 12px; }
        .case-bullet, .case-bullet-strong, .finding-subtext, .result-text { font-size: 0.86rem !important; line-height: 1.7 !important; margin-bottom: 10px !important; }
        .label-strong, .result-value { font-size: 0.86rem !important; }
        .finding-highlight { font-size: 0.92rem !important; margin-top: 12px; margin-bottom: 8px; }
        
        /* ★ 핵심: 모바일에서 처음으로/이전으로 버튼 무조건 가로(한 줄) 배치 */
        div[data-testid="stHorizontalBlock"] {
            display: flex !important;
            flex-direction: row !important;
            flex-wrap: nowrap !important;
            gap: 8px !important;
        }
        div[data-testid="stHorizontalBlock"] > div[data-testid="column"] {
            width: 50% !important;
            min-width: 0 !important;
            flex: 1 1 50% !important;
        }
        
        /* 텍스트가 한 줄에 들어가도록 크기 소폭 조절 */
        div[data-testid="stButton"] > button {
            font-size: 0.86rem !important;
            min-height: 44px !important;
            padding: 0 4px !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def main():
    st.set_page_config(
        page_title="교육용 근전도 판독 보조",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    init_app_state()
    apply_mobile_first_style()
    render_top_navigation()
    render_router()


if __name__ == "__main__":
    main()
