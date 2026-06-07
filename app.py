# app.py

import streamlit as st
from utils.state import init_app_state
from ui.navigation import render_top_navigation
from ui.router import render_router

def apply_mobile_first_style() -> None:
    st.markdown(
        """
        <style>
        :root {
            --bg: #f8fafc;
            --card: #ffffff;
            --text-main: #334155; 
            --label-main: #1e40af; 
            --line: #e2e8f0;
            --shadow: 0 4px 12px rgba(15, 23, 42, 0.04);
        }

        html, body, .stApp, [data-testid="stAppViewContainer"], .main {
            background: var(--bg) !important;
            color: var(--text-main) !important;
        }

        [data-testid="stToolbar"] { visibility: hidden !important; }

        .main .block-container {
            max-width: 900px;
            padding-top: 2rem;
            padding-bottom: 2rem;
        }

        p, span, div { line-height: 1.6; word-break: keep-all; }

        .main-title {
            font-size: 1.4rem;
            font-weight: 900;
            color: #0f172a;
            margin-bottom: 0.5rem;
        }
        
        .subtle { color: #64748b; font-size: 0.95rem; margin-bottom: 1.5rem; }

        .section-card {
            background: var(--card);
            padding: 1.2rem;
            margin-bottom: 1rem;
            border-radius: 12px;
            box-shadow: var(--shadow);
        }

        .section-label {
            font-size: 1.05rem;
            font-weight: 800;
            color: #0f172a;
            margin-bottom: 12px;
            padding-bottom: 6px;
            border-bottom: 2px solid var(--line);
        }

        /* 구분용 인라인 텍스트 디자인 (기호 삭제) */
        .inline-label { font-weight: 700; color: var(--label-main); margin-right: 6px; }
        .inline-content { font-weight: 400; color: var(--text-main); }
        .item-title { font-weight: 800; color: #0f172a; margin-top: 16px; margin-bottom: 4px; }

        /* 감별진단 전용 디자인 */
        .ddx-box {
            background: #faf5ff;
            border-left: 4px solid #9333ea;
            padding: 12px;
            margin-top: 10px;
            border-radius: 4px;
        }
        .ddx-title { font-size: 1rem; font-weight: 800; color: #7e22ce; margin-bottom: 8px; }
        .ddx-label { font-weight: 700; color: #581c87; display: block; margin-top: 6px; }
        .ddx-content { font-weight: 400; color: #4c1d95; }

        /* 버튼 디자인 및 간격 축소 */
        div[data-testid="stButton"] { display: flex; justify-content: center; margin-top: 0; margin-bottom: 0; }
        div[data-testid="stButton"] > button {
            max-width: 100% !important;
            width: 100% !important;
            border-radius: 8px !important;
            font-weight: 700 !important;
            min-height: 48px !important;
            transition: all 0.2s;
        }
        
        div[role="radiogroup"] > label {
            padding: 12px 10px;
            background: #ffffff;
            border: 1px solid var(--line);
            border-radius: 8px;
            margin-bottom: 8px;
            cursor: pointer;
        }
        
        @media (max-width: 768px) {
            .main .block-container { padding-top: 1rem; padding-left: 0.8rem; padding-right: 0.8rem; }
            .main-title { font-size: 1.25rem; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def main() -> None:
    st.set_page_config(page_title="근전도 판독 가이드", page_icon="🧠", layout="wide")
    init_app_state()
    apply_mobile_first_style()
    render_top_navigation()
    render_router()

if __name__ == "__main__":
    main()
