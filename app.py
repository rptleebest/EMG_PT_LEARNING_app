# app.py

import streamlit as st
from utils.state import init_app_state
from ui.navigation import render_top_navigation
from ui.router import render_router

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

    /* 영문 병기용 CSS (괄호 삭제, 아래줄, 톤 다운, 간격 축소) */
    .title-eng { display: block; font-size: 0.75rem; color: #94a3b8; font-weight: 400; margin-top: 1px; letter-spacing: -0.01em; }

    /* 기본 텍스트 스타일 */
    .main-title { font-size: 1.25rem; font-weight: 800; color: #0f172a; line-height: 1.3; margin-bottom: 0.2rem; word-break: keep-all; }
    .subtle { font-size: 0.88rem; font-weight: 400; color: #64748b; line-height: 1.6; margin-bottom: 1.2rem; word-break: keep-all; }

    /* 카드 스타일 */
    .section-card, .info-card, .warn-card { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 14px 12px; margin-bottom: 14px; }
    .info-card { background: #f8fbff; border-color: #dbeafe; }
    .warn-card { background: #fffaf3; border-color: #fed7aa; }

    /* 소제목 스타일 */
    .case-section-label { font-size: 0.95rem; font-weight: 700; color: #0f172a; background: #f1f5f9; border-left: 4px solid var(--blue); border-radius: 6px; padding: 8px 10px; margin-bottom: 12px; }
    .result-label { font-size: 0.95rem; font-weight: 700; color: #0f172a; background: #f0f9ff; border-left: 4px solid #0ea5e9; border-radius: 6px; padding: 8px 10px; margin-top: 16px; margin-bottom: 10px; }

    /* 진단명 스타일 (최종 교육용 진단 글자 삭제, 진단명만 굵고 깔끔하게) */
    .diag-box { background: #fff1f2; border-left: 4px solid #fecdd3; padding: 12px 14px; border-radius: 8px; margin-bottom: 16px; }
    .diag-name { font-size: 1.05rem; font-weight: 800; color: #991b1b; line-height: 1.4; word-break: keep-all; }

    /* 목록/총알 스타일 */
    .case-bullet { font-size: 0.88rem; font-weight: 400; color: #334155; line-height: 1.6; margin-bottom: 8px; word-break: keep-all; }
    .finding-highlight { font-size: 0.92rem; font-weight: 700; color: #1e3a8a; margin-top: 14px; margin-bottom: 8px; border-bottom: 1px solid #e2e8f0; padding-bottom: 4px; }

    /* 🚨 결과표/항목 가독성 극대화 (항목은 굵게, 설명은 가늘게) */
    .result-row { display: flex; flex-direction: row; align-items: flex-start; margin-bottom: 6px; padding-bottom: 6px; border-bottom: 1px solid #f8fafc; }
    .result-row:last-child { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }
    .lbl { flex: 0 0 95px; font-size: 0.86rem; font-weight: 700; color: #1e293b; line-height: 1.4; }
    .val { flex: 1; font-size: 0.86rem; font-weight: 400; color: #475569; line-height: 1.5; word-break: keep-all; }
    
    .text-blue { color: #2563eb !important; font-weight: 600; }
    .text-red { color: #dc2626 !important; font-weight: 600; }
    .text-green { color: #16a34a !important; font-weight: 600; }

    /* 🚨 2D 플랫 버튼 스타일 (입체감 제거, 단순하고 세련된 모바일 앱 버튼) */
    div[data-testid="stButton"] > button {
        border-radius: 8px !important; border: none !important; box-shadow: none !important;
        font-weight: 600 !important; font-size: 0.9rem !important; min-height: 42px !important; 
        color: #ffffff !important; transition: opacity 0.2s ease !important;
    }
    div[data-testid="stButton"] > button:active { opacity: 0.7 !important; transform: none !important; }
    div[data-testid="stButton"] > button[kind="primary"] { background-color: #3b82f6 !important; }
    div[data-testid="stButton"] > button[kind="secondary"] { background-color: #64748b !important; }

    /* 네비게이션 버튼 중앙 정렬 및 여백 축소 */
    .nav-container { display: flex; justify-content: center; gap: 12px; margin-top: 10px; margin-bottom: 10px; width: 100%; }
    div[data-testid="stHorizontalBlock"] { justify-content: center !important; gap: 10px !important; }
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"] { flex: 0 0 auto !important; width: auto !important; min-width: 0 !important; }
    
    /* 처음/이전 버튼 크기 축소 */
    div[data-testid="stHorizontalBlock"] button { width: 110px !important; padding: 0 !important; }
    
    /* 단일 중앙 버튼 (학습 시작, 다른 사례 분석) */
    .center-btn-wrapper div[data-testid="stButton"] > button { width: 220px !important; margin: 0 auto !important; display: block !important; }

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
