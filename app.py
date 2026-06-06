import streamlit as st

# 최상단 배치 필수
st.set_page_config(
    page_title="교육용 근전도 판독 보조",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

from utils.state import init_app_state
from ui.router import render_router
from ui.navigation import render_top_navigation

def apply_global_style():
    st.markdown(
        """
        <style>
        .stApp { background-color: #f8fafc; }
        p, span, div, li, label {
            font-weight: 400 !important; 
            color: #334155; 
            line-height: 1.6;
            word-break: keep-all;
        }
        h1, h2, h3, .header-label, .main-title {
            font-weight: 700 !important;
            color: #1e293b;
        }
        .text-red { color: #c2410c !important; font-weight: 600; background-color: #fff7ed; padding: 2px 4px; border-radius: 4px; }
        .text-blue { color: #1d4ed8 !important; font-weight: 600; background-color: #eff6ff; padding: 2px 4px; border-radius: 4px; }
        div[role="radiogroup"] > label {
            width: 100%; background-color: #ffffff; border: 1px solid #e2e8f0;
            border-radius: 8px; padding: 12px; margin-bottom: 8px; display: flex;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        }
        </style>
        """, unsafe_allow_html=True
    )

def main():
    init_app_state()
    apply_global_style()
    render_top_navigation()
    render_router()

if __name__ == "__main__":
    main()
