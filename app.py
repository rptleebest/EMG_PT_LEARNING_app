# app.py

import streamlit as st
from utils.state import init_app_state
from ui.navigation import render_top_navigation
from ui.router import render_router

def apply_mobile_first_style() -> None:
    """
    모바일/PC 환경 모두에서 최적의 가독성을 제공하는 CSS 스타일입니다.
    양쪽 정렬, 폰트 두께 대비, 사례 선택 박스 색상 구분 등이 포함됩니다.
    """
    st.markdown(
        """
        <style>
        :root {
            --bg: #f8fafc;
            --card: #ffffff;
            --text-main: #334155; 
            --title-color: #0f172a;
            --label-main: #1e3a8a; /* 눈이 피로하지 않은 깊은 남색 */
            --line: #e2e8f0;
        }

        html, body, .stApp, [data-testid="stAppViewContainer"], .main {
            background: var(--bg) !important;
            color: var(--text-main) !important;
        }

        [data-testid="stToolbar"] { visibility: hidden !important; }

        .main .block-container {
            max-width: 900px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        /* 본문 텍스트 양쪽 정렬 및 줄간격 최적화 */
        p, span, div { 
            line-height: 1.65; 
            word-break: keep-all; 
            text-align: justify; 
        }

        .main-title {
            font-size: 1.5rem;
            font-weight: 900;
            color: var(--title-color);
            margin-bottom: 0.6rem;
            text-align: left;
        }
        
        .subtle { 
            color: #64748b; 
            font-size: 0.95rem; 
            margin-bottom: 1.5rem; 
            text-align: justify;
        }

        .section-card {
            background: var(--card);
            padding: 1.2rem;
            margin-bottom: 1.2rem;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);
        }

        /* 소제목 영역 */
        .section-label {
            font-size: 1.05rem;
            font-weight: 800;
            color: var(--title-color);
            margin-bottom: 12px;
            padding-bottom: 6px;
            border-bottom: 2px solid var(--line);
        }

        /* 설명 앞 라벨 텍스트 (조금 더 굵고 깊은 색상) */
        .inline-label { 
            font-weight: 800; 
            color: var(--label-main); 
            margin-right: 6px; 
        }
        
        .inline-content { 
            font-weight: 400; 
            color: var(--text-main); 
        }
        
        .item-title { 
            font-weight: 800; 
            color: var(--title-color); 
            margin-top: 16px; 
            margin-bottom: 6px; 
        }

        /* 감별진단 전용 디자인 */
        .ddx-box {
            background: #faf5ff;
            border-left: 4px solid #9333ea;
            padding: 12px;
            margin-top: 12px;
            border-radius: 6px;
        }
        
        .ddx-title { 
            font-size: 1.05rem; 
            font-weight: 800; 
            color: #7e22ce; 
            margin-bottom: 6px; 
        }

        /* 하단 이동 버튼 너비 및 디자인 */
        div[data-testid="stButton"] { 
            display: flex; 
            justify-content: center; 
        }
        
        div[data-testid="stButton"] > button {
            max-width: 100% !important;
            width: 100% !important;
            border-radius: 8px !important;
            font-weight: 800 !important;
            min-height: 48px !important;
        }
        
        /* 라디오 버튼 (사례 선택) 박스 너비 통일 및 색상 제어 */
        div[role="radiogroup"] {
            display: flex;
            flex-direction: column;
            gap: 8px;
            width: 100%;
        }
        
        div[role="radiogroup"] > label {
            width: 100%;
            padding: 14px 12px;
            border: 1px solid var(--line);
            border-radius: 8px;
            cursor: pointer;
            background: #f8fafc; /* 기본 옅은 파스텔(회파랑) 배경 */
        }
        
        /* 첫 번째 항목('선택 안 함') 배경색 변경 */
        div[role="radiogroup"] > label:first-child {
            background: #f1f5f9; /* 뚜렷한 회색 배경 */
            border: 1px dashed #cbd5e1;
        }

        @media (max-width: 768px) {
            .main .block-container { 
                padding-top: 1rem; 
                padding-left: 0.8rem; 
                padding-right: 0.8rem; 
            }
            .main-title { font-size: 1.3rem; }
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
