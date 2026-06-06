# app.py

import streamlit as st

from utils.state import init_app_state
from ui.navigation import render_top_navigation
from ui.router import render_router


def apply_mobile_first_style():
    st.markdown(
        """
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
            --red: #991b1b;
            --shadow: 0 8px 24px rgba(15, 23, 42, 0.05);
        }

        html,
        body,
        #root,
        .stApp,
        [data-testid="stAppViewContainer"],
        [data-testid="stHeader"],
        [data-testid="stMain"],
        [data-testid="stMainBlockContainer"],
        section.main,
        .main {
            background: var(--bg) !important;
            color: var(--text) !important;
        }

        [data-testid="stToolbar"] {
            background: transparent !important;
        }

        .main .block-container {
            max-width: 980px;
            padding-top: 1.2rem;
            padding-bottom: 4rem;
            padding-left: 0.85rem;
            padding-right: 0.85rem;
            background: var(--bg) !important;
        }

        [data-testid="stSidebar"] {
            background: var(--bg) !important;
        }

        div[data-testid="stMarkdownContainer"],
        div[data-testid="stText"],
        p,
        li,
        span,
        label {
            color: var(--text);
        }

        .main-title {
            font-size: 1.34rem;
            font-weight: 800;
            color: var(--text) !important;
            line-height: 1.28;
            margin-bottom: 0.35rem;
            letter-spacing: -0.01em;
            word-break: keep-all;
        }

        .subtle {
            color: var(--muted) !important;
            font-size: 0.92rem;
            line-height: 1.62;
            margin-bottom: 0.9rem;
            word-break: keep-all;
        }

        .section-card,
        .result-card,
        .warn-card,
        .info-card {
            background: var(--card) !important;
            border: 1px solid var(--line) !important;
            border-radius: 16px;
            padding: 14px 13px 15px 13px;
            margin-bottom: 14px;
            box-shadow: var(--shadow);
            color: var(--text) !important;
        }

        .result-card {
            background: #f7fff8 !important;
            border: 1px solid var(--green-soft) !important;
        }

        .warn-card {
            background: #fffaf3 !important;
            border: 1px solid #fed7aa !important;
        }

        .info-card {
            background: #f8fbff !important;
            border: 1px solid var(--blue-soft) !important;
        }

        .big-section-title,
        .case-section-label,
        .result-label {
            font-size: 0.96rem;
            font-weight: 800;
            color: var(--text) !important;
            background: #f8fafc !important;
            border: 1px solid var(--line) !important;
            border-left: 4px solid var(--blue) !important;
            border-radius: 12px;
            padding: 9px 10px;
            margin-top: 8px;
            margin-bottom: 10px;
            line-height: 1.42;
            word-break: keep-all;
        }

        .result-label {
            border-left-color: var(--green) !important;
            background: #f7fff8 !important;
        }

        .section-hint {
            font-size: 0.9rem;
            color: #334155 !important;
            background: #f8fafc !important;
            border-left: 4px solid #22c55e !important;
            padding: 10px 11px;
            border-radius: 12px;
            margin-top: 8px;
            margin-bottom: 12px;
            line-height: 1.62;
        }

        .case-title-mobile,
        .case-subheading,
        .finding-item-title,
        .result-title,
        .input-title {
            font-size: 0.92rem;
            font-weight: 800;
            color: var(--text) !important;
            line-height: 1.48;
            margin-bottom: 6px;
            word-break: keep-all;
        }

        .case-subtitle-mobile,
        .mobile-note,
        .input-meta {
            color: var(--muted) !important;
        }

        .case-bullet,
        .case-bullet-strong,
        .finding-subtext,
        .result-text,
        .result-small {
            font-size: 0.88rem;
            color: #1f2937 !important;
            line-height: 1.7;
            margin-bottom: 7px;
            word-break: keep-all;
        }

        .input-meta {
            font-size: 0.83rem;
        }

        .case-text-block {
            background: #fcfcfd !important;
            border-left: 4px solid var(--line) !important;
            border-radius: 12px;
            padding: 10px 11px;
            margin-bottom: 10px;
        }

        .item-divider {
            border: none;
            border-top: 1px solid #eef2f7 !important;
            margin: 10px 0 12px 0;
        }

        .compact-item {
            padding: 2px 0;
            margin-bottom: 8px;
        }

        .badge-row {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin-top: 4px;
            margin-bottom: 8px;
        }

        .badge {
            display: inline-block;
            font-size: 0.74rem;
            font-weight: 700;
            color: var(--blue) !important;
            background: #eff6ff !important;
            border: 1px solid #bfdbfe !important;
            border-radius: 999px;
            padding: 4px 8px;
        }

        .badge-green {
            color: #166534 !important;
            background: #f0fdf4 !important;
            border-color: #bbf7d0 !important;
        }

        .badge-amber {
            color: #92400e !important;
            background: #fffbeb !important;
            border-color: #fde68a !important;
        }

        .top-bottom-nav-space {
            height: 4px;
        }

        .finding-highlight {
            color: #1e40af !important;
            font-weight: 800 !important;
            font-size: 1.05rem !important;
            margin-top: 10px;
            margin-bottom: 4px;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 4px;
        }

        .label-strong {
            font-weight: 800 !important;
            color: #0f172a !important;
            font-size: 0.92rem !important;
        }

        .text-blue {
            color: #1e40af !important;
            font-weight: 600 !important;
        }

        .text-green {
            color: #15803d !important;
            font-weight: 600 !important;
        }

        .text-red {
            color: #991b1b !important;
            font-weight: 600 !important;
        }

        .result-value {
            font-weight: 600 !important;
            color: #334155 !important;
            margin-left: 4px;
        }

        .case-bullet-strong {
            font-size: 0.88rem;
            font-weight: 600 !important;
            margin-bottom: 5px;
            line-height: 1.6;
            color: #0f172a;
        }

        .bottom-nav-space {
            height: 10px;
        }

        div[role="radiogroup"] label p,
        div[data-testid="stRadio"] label p,
        div[data-testid="stCheckbox"] label p,
        div[data-testid="stSelectbox"] label p,
        div[data-baseweb="select"] * {
            color: var(--text) !important;
            word-break: keep-all !important;
        }

        label[data-testid="stWidgetLabel"] p {
            font-size: 0.84rem !important;
            font-weight: 700 !important;
            color: #334155 !important;
            line-height: 1.42 !important;
        }

        div[data-testid="stButton"] > button,
        div[data-testid="stDownloadButton"] > button {
            font-weight: 800 !important;
            border-radius: 12px !important;
            min-height: 44px !important;
            font-size: 0.94rem !important;
            width: 100% !important;
            margin: 0 auto !important;
            display: block !important;
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
            text-shadow: 0px 1px 2px rgba(0, 0, 0, 0.2) !important;
        }

        div[data-testid="stButton"] > button[kind="primary"],
        div[data-testid="stButton"] > button[data-testid="baseButton-primary"],
        div[data-testid="stButton"] > button[kind="secondary"],
        div[data-testid="stButton"] > button[data-testid="baseButton-secondary"] {
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
            background-color: var(--blue) !important;
            border: none !important;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.15) !important;
        }

        div[data-testid="stButton"] > button:hover,
        div[data-testid="stButton"] > button:active,
        div[data-testid="stButton"] > button:focus {
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
            background-color: #1d4ed8 !important;
            border: none !important;
        }

        div[data-testid="stDownloadButton"] > button:hover,
        div[data-testid="stDownloadButton"] > button:active,
        div[data-testid="stDownloadButton"] > button:focus {
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
        }

        @media (min-width: 769px) {
            div[data-testid="stButton"] > button,
            div[data-testid="stDownloadButton"] > button {
                max-width: 360px !important;
            }
        }

        @media (max-width: 768px) {
            .main .block-container {
                padding-top: 0.9rem;
                padding-bottom: 3rem;
                padding-left: 0.65rem;
                padding-right: 0.65rem;
                max-width: 100%;
            }

            .label-strong {
                font-size: 0.86rem !important;
            }

            .finding-item-title {
                font-size: 0.86rem !important;
            }

            .case-subheading {
                font-size: 0.84rem !important;
            }

            .finding-highlight {
                font-size: 0.95rem !important;
            }

            .result-value {
                font-size: 0.88rem !important;
            }

            .case-bullet-strong {
                font-size: 0.82rem !important;
            }

            .main-title {
                font-size: 1.15rem;
                line-height: 1.28;
                margin-bottom: 0.28rem;
            }

            .subtle {
                font-size: 0.84rem;
                line-height: 1.64;
                margin-bottom: 0.8rem;
            }

            .section-card,
            .result-card,
            .warn-card,
            .info-card {
                border-radius: 14px;
                padding: 11px 10px 13px 10px;
                margin-bottom: 12px;
            }

            .big-section-title,
            .case-section-label,
            .result-label {
                font-size: 0.88rem;
                padding: 8px 9px;
                border-radius: 10px;
                margin-top: 8px;
                margin-bottom: 9px;
            }

            .case-title-mobile,
            .case-subheading,
            .finding-item-title,
            .result-title,
            .input-title {
                font-size: 0.85rem;
                line-height: 1.46;
            }

            .case-bullet,
            .case-bullet-strong,
            .finding-subtext,
            .mobile-note,
            .result-text,
            .result-small,
            .input-meta {
                font-size: 0.82rem;
                line-height: 1.72;
                margin-bottom: 7px;
            }

            .badge {
                font-size: 0.7rem;
                padding: 4px 7px;
            }

            label[data-testid="stWidgetLabel"] p {
                font-size: 0.8rem !important;
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
