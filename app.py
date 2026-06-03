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

    /* ★ 공통 버튼 스타일 (사용자가 확실히 버튼으로 인지하도록 입체감 부여) */
    div[data-testid="stButton"] > button {
        font-weight: 700 !important;
        border-radius: 12px !important;
        min-height: 48px !important;
        font-size: 0.96rem !important;
        width: 100% !important; /* 기본적으로 영역 꽉 채움 */
        max-width: 280px !important; /* PC 및 모바일 공통 최대 너비 제한 (너무 길어지지 않게) */
        margin: 0 auto !important;
        border: none !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        transition: transform 0.1s ease, box-shadow 0.1s ease !important;
    }

    /* 1. Primary 버튼 (처음으로, 이전으로, 학습시작) -> 파란색 입체감 */
    div[data-testid="stButton"] > button[kind="primary"],
    div[data-testid="stButton"] > button[data-testid="baseButton-primary"] {
        background: linear-gradient(180deg, #3b82f6 0%, #1d4ed8 100%) !important;
        box-shadow: 0 4px 6px rgba(29, 78, 216, 0.3), inset 0 1px 1px rgba(255, 255, 255, 0.2) !important;
        border-bottom: 3px solid #1e3a8a !important; /* 입체감 위한 하단 테두리 */
    }
    div[data-testid="stButton"] > button[kind="primary"]:active,
    div[data-testid="stButton"] > button[data-testid="baseButton-primary"]:active {
        transform: translateY(2px) !important; /* 눌리는 효과 */
        border-bottom: 1px solid #1e3a8a !important;
        box-shadow: 0 1px 2px rgba(29, 78, 216, 0.3) !important;
    }

    /* 2. Secondary 버튼 (다른 사례 분석하기) -> 회색 입체감 */
    div[data-testid="stButton"] > button[kind="secondary"],
    div[data-testid="stButton"] > button[data-testid="baseButton-secondary"] {
        background: linear-gradient(180deg, #64748b 0%, #475569 100%) !important;
        box-shadow: 0 4px 6px rgba(71, 85, 105, 0.3), inset 0 1px 1px rgba(255, 255, 255, 0.2) !important;
        border-bottom: 3px solid #334155 !important;
    }
    div[data-testid="stButton"] > button[kind="secondary"]:active,
    div[data-testid="stButton"] > button[data-testid="baseButton-secondary"]:active {
        transform: translateY(2px) !important;
        border-bottom: 1px solid #334155 !important;
        box-shadow: 0 1px 2px rgba(71, 85, 105, 0.3) !important;
    }

    @media (max-width: 768px) {
        .main .block-container { padding-top: 1rem; padding-bottom: 3rem; padding-left: 0.75rem; padding-right: 0.75rem; }
        .main-title { font-size: 1.2rem; } .subtle { font-size: 0.88rem; }
        .section-card, .result-card, .warn-card, .info-card { padding: 14px 12px; margin-bottom: 14px; }
        .big-section-title, .case-section-label, .result-label { font-size: 0.92rem; padding: 10px 10px; margin-bottom: 12px; }
        .case-bullet, .case-bullet-strong, .finding-subtext, .result-text { font-size: 0.86rem !important; line-height: 1.7 !important; margin-bottom: 10px !important; }
        .label-strong, .result-value { font-size: 0.86rem !important; }
        .finding-highlight { font-size: 0.92rem !important; margin-top: 12px; margin-bottom: 8px; }
        
        /* ★ 모바일 처음으로/이전으로 가로 배치 강제화 (잘리지 않도록 여백 조절) */
        div[data-testid="stHorizontalBlock"] {
            display: flex !important;
            flex-direction: row !important;
            flex-wrap: nowrap !important;
            gap: 10px !important; /* 버튼 사이 간격 */
            width: 100% !important;
        }
        div[data-testid="stHorizontalBlock"] > div[data-testid="column"] {
            width: 50% !important; /* 정확히 절반씩 나눔 */
            min-width: 0 !important;
            flex: 1 1 50% !important;
        }
        
        /* 모바일에서는 버튼 최대 너비를 풀어서 컨테이너에 맞춤 */
        div[data-testid="stButton"] > button {
            max-width: 100% !important;
            font-size: 0.88rem !important;
            min-height: 46px !important;
            padding: 0 4px !important;
            white-space: nowrap !important; /* 글자 줄바꿈 방지 */
        }
        
        /* 단일로 나오는 버튼(학습시작, 사례 변경)은 최대 너비 제한 유지 */
        div[data-testid="stVerticalBlock"] > div > div[data-testid="stButton"] > button {
            max-width: 250px !important; 
        }
    }
    
    /* 최상단 스크롤용 앵커 숨기기 */
    #top-anchor {
        display: none;
    }
    </style>
    
    <!-- ★ 화면 전환 시 스크롤을 맨 위로 강제 이동시키는 JS 스크립트 -->
    <script>
        const observer = new MutationObserver((mutations) => {
            for (let mutation of mutations) {
                if (mutation.type === 'childList') {
                    window.scrollTo(0, 0);
                    const mainContainer = parent.document.querySelector('.main');
                    if (mainContainer) {
                        mainContainer.scrollTo(0, 0);
                    }
                }
            }
        });
        observer.observe(document.body, { childList: true, subtree: true });
    </script>
    <div id="top-anchor"></div>
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
