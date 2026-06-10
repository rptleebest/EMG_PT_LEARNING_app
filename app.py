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
            --text-main: #334155; 
            --title-color: #0f172a;
            --label-main: #1e3a8a; 
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

        /* [수정됨] 전체 div 강제 정렬 해제, p 태그 기본 설정만 유지 */
        p { 
            line-height: 1.65; 
            word-break: keep-all; 
        }

        /* 본문 텍스트 성격의 클래스에만 '양쪽 정렬' 적용 */
        .info-value, .left-border-box, .ddx-box, [data-testid="stExpander"] div {
            text-align: justify !important;
            line-height: 1.65;
            word-break: keep-all;
        }

        /* [수정됨] 메인 타이틀 완벽한 중앙 정렬 */
        .main-title {
            font-size: 1.6rem;
            font-weight: 800;
            color: var(--title-color);
            margin-bottom: 0.5rem;
            text-align: center !important;
            width: 100%;
            display: block;
        }
        
        /* [수정됨] 메인 타이틀 아래 설명글 중앙 정렬 */
        .sub-desc { 
            color: #64748b; 
            font-size: 0.95rem; 
            margin-bottom: 2rem; 
            text-align: center !important;
            width: 100%;
            display: block;
        }

        /* 각 섹션 소제목은 안정감 있게 좌측 정렬 유지 */
        .section-label {
            font-size: 1.15rem;
            font-weight: 800;
            color: var(--title-color);
            margin-top: 1.5rem;
            margin-bottom: 12px;
            padding-bottom: 6px;
            border-bottom: 2px solid var(--line-light);
            text-align: left !important;
        }

        .sub-title { 
            font-weight: 800; 
            color: var(--label-main); 
            margin-top: 16px; 
            margin-bottom: 8px; 
            font-size: 1.05rem;
            text-align: left !important;
        }

        /* 이학적 검사 전용 박스 */
        .exam-box {
            background: #f1f5f9;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            padding: 12px;
            margin-bottom: 12px;
            width: 100%;
        }
        .exam-title {
            font-size: 1rem;
            font-weight: 800;
            color: #0f172a;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
        }

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
            width: 100px; 
            flex-shrink: 0;
        }
        .info-value {
            font-weight: 400;
            color: var(--text-main);
            flex-grow: 1;
        }

        .left-border-box {
            border-left: 4px solid #cbd5e1;
            padding-left: 12px;
            margin-top: 4px;
            margin-bottom: 12px;
            color: #475569;
        }

        .ddx-box {
            background: #fbf5ff;
            border-left: 4px solid #9333ea;
            padding: 14px;
            margin-top: 12px;
            border-radius: 4px;
        }

        div[data-testid="stButton"] { display: flex; justify-content: center; }
        div[data-testid="stButton"] > button {
            max-width: 100% !important;
            width: 100% !important;
            border-radius: 8px !important;
            font-weight: 800 !important;
            min-height: 48px !important;
        }

        /* 토글 디자인 */
        [data-testid="stExpander"] {
            border: 1px solid #bae6fd !important;
            border-radius: 8px !important;
            background: #f8fafc !important;
        }
        [data-testid="stExpander"] p {
            font-weight: 800 !important;
            color: #1e40af !important;
        }

        @media (max-width: 768px) {
            .main .block-container { padding-top: 1rem; padding-left: 0.8rem; padding-right: 0.8rem; }
            .info-label { width: 85px; font-size: 0.9rem; }
            .main-title { font-size: 1.4rem; }
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
