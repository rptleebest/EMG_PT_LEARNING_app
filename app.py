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
            --card-bg: #ffffff;
            --text-main: #334155; /* 눈이 편한 짙은 회색 */
            --title-color: #0f172a;
            --label-main: #1e3a8a; /* 차분한 남색 */
            --line-light: #e2e8f0;
        }

        html, body, .stApp, [data-testid="stAppViewContainer"], .main {
            background: var(--bg) !important;
            color: var(--text-main) !important;
        }

        [data-testid="stToolbar"] { visibility: hidden !important; }

        .main .block-container {
            max-width: 900px;
            padding-top: 1.5rem;
            padding-bottom: 3rem;
        }

        p, span, div { 
            line-height: 1.6; 
            word-break: keep-all; 
        }

        /* 1) 메인 타이틀 */
        .main-title {
            font-size: 1.5rem;
            font-weight: 900;
            color: var(--title-color);
            margin-bottom: 0.4rem;
        }
        
        .sub-desc { 
            color: #64748b; 
            font-size: 0.95rem; 
            margin-bottom: 1.5rem; 
        }

        /* 2) 섹션 소제목 (아이콘 포함) */
        .section-label {
            font-size: 1.15rem;
            font-weight: 800;
            color: var(--title-color);
            margin-top: 1rem;
            margin-bottom: 12px;
            padding-bottom: 6px;
            border-bottom: 2px solid var(--line-light);
        }

        /* 3) 표/항목 소제목 */
        .sub-title { 
            font-weight: 800; 
            color: var(--label-main); 
            margin-top: 16px; 
            margin-bottom: 8px; 
            font-size: 1.05rem;
            display: flex;
            align-items: center;
        }

        /* 4) 라벨-내용 분리형 정렬 (가장 중요한 가독성 개선) */
        .info-row {
            display: flex;
            align-items: baseline;
            margin-bottom: 8px;
            padding-bottom: 4px;
            border-bottom: 1px dashed #f1f5f9;
        }
        .info-label {
            font-weight: 800;
            color: var(--label-main);
            width: 100px; /* 라벨 너비 고정으로 줄맞춤 */
            flex-shrink: 0;
            font-size: 0.95rem;
        }
        .info-value {
            font-weight: 400;
            color: var(--text-main);
            flex-grow: 1;
            font-size: 0.95rem;
        }

        /* 5) 부드러운 왼쪽 선 (설명/증상 나열용) */
        .left-border-box {
            border-left: 4px solid #cbd5e1;
            padding-left: 12px;
            margin-top: 4px;
            margin-bottom: 12px;
            color: #475569;
        }
        
        .left-border-box.success {
            border-left-color: #22c55e;
            background: #f0fdf4;
            padding: 12px;
            border-radius: 0 8px 8px 0;
        }

        /* 6) 감별진단 박스 (눈에 띄되 부드럽게) */
        .ddx-box {
            background: #fbf5ff;
            border-left: 4px solid #9333ea;
            padding: 14px;
            margin-top: 12px;
            border-radius: 4px;
        }

        /* 7) 버튼 최적화 */
        div[data-testid="stButton"] { display: flex; justify-content: center; }
        div[data-testid="stButton"] > button {
            max-width: 100% !important;
            width: 100% !important;
            border-radius: 8px !important;
            font-weight: 800 !important;
            min-height: 48px !important;
        }

        /* 토글(Expander) 디자인 변경 (표 아래에 부드럽게 붙도록) */
        [data-testid="stExpander"] {
            border: 1px solid #bae6fd !important;
            border-radius: 8px !important;
            background: #f8fafc !important;
        }
        [data-testid="stExpander"] p {
            font-weight: 700 !important;
            color: #1e40af !important;
        }

        @media (max-width: 768px) {
            .main .block-container { padding-top: 1rem; padding-left: 0.8rem; padding-right: 0.8rem; }
            .info-label { width: 85px; font-size: 0.9rem; }
            .info-value { font-size: 0.9rem; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def main() -> None:
    st.set_page_config(page_title="근전도 판독 가이드", page_icon="⚡", layout="wide")
    init_app_state()
    apply_mobile_first_style()
    render_top_navigation()
    render_router()

if __name__ == "__main__":
    main()
