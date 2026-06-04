# app.py

import streamlit as st

from utils.state import init_app_state
from ui.router import render_router
from ui.navigation import render_top_navigation


def apply_mobile_first_style():
    """
    모바일 우선 전역 스타일.
    - 학생들이 모바일에서 주로 사용할 것을 고려해 폭, 여백, 버튼, 표, 카드 가독성을 최적화합니다.
    - PC에서도 본문 폭을 제한해 읽기 피로를 줄입니다.
    """
    st.markdown(
        """
        <style>
        /* ------------------------------------------------------------
           1. Global layout
        ------------------------------------------------------------ */
        html, body {
            overflow-x: hidden !important;
            background-color: #f8fafc !important;
            color: #1e293b !important;
            margin: 0 !important;
            padding: 0 !important;
        }

        .stApp {
            background-color: #f8fafc !important;
            overflow-x: hidden !important;
        }

        .main .block-container {
            max-width: 900px !important;
            padding: 1.35rem 1rem 4rem 1rem !important;
            margin: 0 auto !important;
        }

        @media (min-width: 1024px) {
            .main .block-container {
                max-width: 920px !important;
                padding-top: 1.7rem !important;
            }
        }

        @media (max-width: 480px) {
            .main .block-container {
                padding: 1rem 0.78rem 3.5rem 0.78rem !important;
            }
        }

        * {
            box-sizing: border-box !important;
        }

        p, span, div, li {
            word-break: keep-all;
            overflow-wrap: break-word;
            line-height: 1.62;
        }

        /* ------------------------------------------------------------
           2. Typography
        ------------------------------------------------------------ */
        .main-title {
            font-size: 1.62rem;
            font-weight: 900;
            color: #0f172a;
            line-height: 1.35;
            letter-spacing: -0.03em;
            margin: 0.2rem 0 0.5rem 0;
        }

        .subtle {
            font-size: 0.94rem;
            color: #64748b;
            line-height: 1.65;
            margin-bottom: 1.05rem;
        }

        .big-section-title {
            font-size: 1.06rem;
            font-weight: 900;
            color: #0f172a;
            margin-bottom: 0.8rem;
            padding-bottom: 0.45rem;
            border-bottom: 2px solid #bfdbfe;
        }

        .case-section-label,
        .section-title {
            font-size: 1rem;
            font-weight: 900;
            color: #0f172a;
            margin: 0 0 0.7rem 0;
            padding-bottom: 0.35rem;
            border-bottom: 2px solid #3b82f6;
            line-height: 1.45;
        }

        .sub-title {
            font-size: 0.95rem;
            font-weight: 800;
            color: #1e3a8a;
            margin-top: 1rem;
            margin-bottom: 0.55rem;
            padding-bottom: 0.25rem;
            border-bottom: 1px dashed #93c5fd;
        }

        .case-title-mobile {
            font-size: 1.06rem;
            font-weight: 900;
            color: #0f172a;
            margin-bottom: 0.35rem;
            line-height: 1.45;
        }

        .case-subtitle-mobile {
            font-size: 0.9rem;
            color: #475569;
            line-height: 1.55;
        }

        .label-strong {
            font-weight: 800 !important;
            color: #334155 !important;
        }

        .result-value {
            color: #334155 !important;
            font-weight: 500 !important;
        }

        .txt-normal,
        .text-normal {
            color: #334155 !important;
        }

        .txt-blue,
        .text-blue {
            color: #1d4ed8 !important;
            font-weight: 700 !important;
        }

        .txt-red,
        .text-red {
            color: #b91c1c !important;
            font-weight: 700 !important;
        }

        .txt-green,
        .text-green {
            color: #15803d !important;
            font-weight: 700 !important;
        }

        /* ------------------------------------------------------------
           3. Cards
        ------------------------------------------------------------ */
        .section-card,
        .content-card {
            background: #ffffff;
            border: 1px solid #cbd5e1;
            border-radius: 12px;
            padding: 1rem;
            margin: 0.9rem 0;
            box-shadow: 0 1px 2px rgba(15, 23, 42, 0.035);
        }

        .info-card {
            background: #f0f9ff;
            border: 1px solid #bae6fd;
            border-radius: 12px;
            padding: 1rem;
            margin: 0.9rem 0;
        }

        .warn-card {
            background: #fff7ed;
            border: 1px solid #fed7aa;
            border-left: 5px solid #f97316;
            border-radius: 12px;
            padding: 0.95rem 1rem;
            margin: 0.9rem 0;
        }

        .result-card {
            background: #ffffff;
            border: 1px solid #cbd5e1;
            border-radius: 12px;
            padding: 1rem;
            margin: 1rem 0;
            box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04);
        }

        .result-title {
            font-size: 1.05rem;
            font-weight: 900;
            color: #0f172a;
            margin-bottom: 0.9rem;
            padding-bottom: 0.45rem;
            border-bottom: 2px solid #fecaca;
        }

        .result-label {
            font-size: 0.95rem;
            font-weight: 900;
            color: #1e3a8a;
            background: #eff6ff;
            border-left: 4px solid #3b82f6;
            border-radius: 8px;
            padding: 0.55rem 0.7rem;
            margin-top: 0.95rem;
            margin-bottom: 0.55rem;
        }

        .result-text,
        .finding-subtext,
        .case-bullet,
        .case-bullet-strong {
            font-size: 0.9rem;
            color: #334155;
            line-height: 1.65;
            margin: 0.28rem 0;
        }

        .case-bullet-strong {
            font-weight: 800;
        }

        .case-text-block {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-left: 4px solid #bfdbfe;
            border-radius: 10px;
            padding: 0.85rem 0.9rem;
            margin: 0.6rem 0 0.9rem 0;
        }

        .finding-highlight {
            font-size: 0.92rem;
            font-weight: 850;
            color: #1e3a8a;
            line-height: 1.55;
            margin: 0.45rem 0;
        }

        .compact-item {
            padding: 0.4rem 0;
        }

        .item-divider {
            border: none;
            height: 1px;
            background: #e2e8f0;
            margin: 0.55rem 0;
        }

        .diagnosis-box {
            background: #fdf2f8;
            border: 1px solid #fce7f3;
            padding: 0.9rem;
            border-radius: 10px;
            margin-top: 1rem;
        }

        /* ------------------------------------------------------------
           4. Data rows
        ------------------------------------------------------------ */
        .data-row {
            display: flex;
            flex-direction: row;
            align-items: flex-start;
            gap: 0.75rem;
            padding: 0.45rem 0;
            border-bottom: 1px solid #f1f5f9;
        }

        .data-row:last-child {
            border-bottom: none;
        }

        .data-label {
            flex: 0 0 105px;
            font-size: 0.88rem;
            font-weight: 800;
            color: #334155;
            line-height: 1.5;
        }

        .data-value {
            flex: 1;
            font-size: 0.88rem;
            color: #334155;
            line-height: 1.5;
        }

        @media (max-width: 480px) {
            .data-row {
                gap: 0.55rem;
            }
            .data-label {
                flex: 0 0 88px;
                font-size: 0.82rem;
            }
            .data-value {
                font-size: 0.82rem;
            }
        }

        /* ------------------------------------------------------------
           5. Buttons
        ------------------------------------------------------------ */
        div[data-testid="stButton"] > button {
            border-radius: 9px !important;
            border: 0 !important;
            box-shadow: none !important;
            font-weight: 800 !important;
            font-size: 0.94rem !important;
            min-height: 42px !important;
            line-height: 1.25 !important;
            transition: opacity 0.15s ease, background-color 0.15s ease !important;
            transform: none !important;
            white-space: nowrap !important;
        }

        div[data-testid="stButton"] > button:active {
            opacity: 0.82 !important;
        }

        div[data-testid="stButton"] > button[kind="primary"] {
            background-color: #2563eb !important;
            color: #ffffff !important;
        }

        div[data-testid="stButton"] > button[kind="secondary"] {
            background-color: #e2e8f0 !important;
            color: #1e293b !important;
        }

        /* 시작 버튼이 너무 넓어지는 것을 방지 */
        .start-button-wrap {
            max-width: 360px;
            margin: 1.25rem auto 0.2rem auto;
        }

        /* ------------------------------------------------------------
           6. Bottom navigation
           - 모바일에서 처음 버튼이 사라지지 않도록 중앙 고정 폭 그룹 구성
        ------------------------------------------------------------ */
        .nav-actions {
            width: 100%;
            max-width: 300px;
            margin: 1.25rem auto 0.8rem auto;
        }

        .nav-actions div[data-testid="stHorizontalBlock"] {
            display: flex !important;
            flex-direction: row !important;
            flex-wrap: nowrap !important;
            gap: 10px !important;
            justify-content: center !important;
            align-items: center !important;
        }

        .nav-actions div[data-testid="column"] {
            flex: 0 0 140px !important;
            width: 140px !important;
            min-width: 0 !important;
            padding: 0 !important;
        }

        .nav-actions div[data-testid="stButton"] > button {
            width: 140px !important;
            min-width: 0 !important;
        }

        @media (max-width: 360px) {
            .nav-actions {
                max-width: 272px;
            }

            .nav-actions div[data-testid="stHorizontalBlock"] {
                gap: 8px !important;
            }

            .nav-actions div[data-testid="column"] {
                flex: 0 0 132px !important;
                width: 132px !important;
            }

            .nav-actions div[data-testid="stButton"] > button {
                width: 132px !important;
                font-size: 0.88rem !important;
            }
        }

        /* ------------------------------------------------------------
           7. Radio / form readability
        ------------------------------------------------------------ */
        div[role="radiogroup"] label {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            padding: 0.55rem 0.65rem;
            margin-bottom: 0.42rem;
        }

        div[role="radiogroup"] label:hover {
            background: #f8fafc;
            border-color: #bfdbfe;
        }

        /* ------------------------------------------------------------
           8. Responsive table base
        ------------------------------------------------------------ */
        .edu-table-wrap {
            width: 100%;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
            margin: 0.65rem 0 1rem 0;
        }

        table.edu-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.86rem;
            background: #ffffff;
        }

        table.edu-table th {
            background: #f1f5f9;
            color: #0f172a;
            font-weight: 850;
            padding: 0.65rem 0.55rem;
            border: 1px solid #cbd5e1;
            text-align: center;
            line-height: 1.4;
        }

        table.edu-table td {
            padding: 0.6rem 0.55rem;
            border: 1px solid #e2e8f0;
            color: #334155;
            text-align: center;
            line-height: 1.45;
            vertical-align: middle;
        }

        table.edu-table td.left {
            text-align: left;
            font-weight: 750;
            color: #1e3a8a;
        }

        .table-note {
            font-size: 0.82rem;
            color: #64748b;
            line-height: 1.55;
            margin-top: -0.3rem;
            margin-bottom: 0.8rem;
        }

        @media (max-width: 640px) {
            table.edu-table {
                font-size: 0.8rem;
            }

            table.edu-table th,
            table.edu-table td {
                padding: 0.5rem 0.45rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def main():
    st.set_page_config(
        page_title="교육용 근전도 판독 보조",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    init_app_state()
    apply_mobile_first_style()
    render_top_navigation()
    render_router()


if __name__ == "__main__":
    main()
