import streamlit as st

from styles.theme import (
    PRIMARY,
    SECONDARY,
    ACCENT,
    BACKGROUND,
    CARD,
    TEXT,
    SUBTEXT,
    BORDER,
    RADIUS,
)


def load_custom_styles():
    """
    Single source of truth for all global CSS.
    Anything added here applies to every page automatically.
    """

    st.markdown(
        f"""
        <style>

        /* ==========================================
           FONT
           Poppins reads friendly + rounded, fits a
           lively nutrition/wellness feel.
           ========================================== */

        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

        html, body, .stApp, [class*="css"] {{
            font-family: 'Poppins', 'Apple Color Emoji', 'Segoe UI Emoji',
                'Segoe UI Symbol', 'Noto Color Emoji', sans-serif;
        }}


        /* ==========================================
           PAGE BACKGROUND
           ========================================== */

        .stApp {{
            background: {BACKGROUND};
            zoom: 90%;
        }}

        .block-container {{
            padding-top: 2rem;
            padding-bottom: 3rem;
            padding-left: 3rem;
            padding-right: 3rem;
        }}


        /* ==========================================
           GENERIC CARD (reused across pages)
           ========================================== */

        .card {{
            background: {CARD};
            border-radius: {RADIUS};
            padding: 24px;
            color: {TEXT};
            border: 1px solid {BORDER};
            box-shadow: 0 8px 25px rgba(30, 58, 138, 0.06);
            transition: 0.25s;
        }}

        .card:hover {{
            transform: translateY(-4px);
        }}


        /* ==========================================
           HERO / HEADER BLOCKS
           ========================================== */

        .hero {{
            background: linear-gradient(135deg, {PRIMARY}, {SECONDARY});
            border-radius: 28px;
            padding: 55px;
            color: white;
            overflow: hidden;
        }}

        .big-title {{
            font-size: 52px;
            font-weight: 700;
            color: white;
        }}

        .subtitle {{
            font-size: 20px;
            opacity: 0.9;
            color: white;
        }}

        .section-title {{
            font-size: 26px;
            font-weight: 700;
            color: {PRIMARY};
        }}


        /* ==========================================
           BUTTONS
           ========================================== */

        .stButton > button {{
            width: 100%;
            height: 52px;
            border-radius: 16px;
            border: none;
            font-size: 16px;
            font-weight: 600;
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, {PRIMARY}, {SECONDARY});
            color: white;
            transition: 0.25s;
        }}

        .stButton > button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 10px 22px rgba(59, 130, 246, 0.25);
            color: white;
        }}


        /* ==========================================
           ALERTS (st.success / st.info / st.warning / st.error)
           ========================================== */

        div[data-testid="stAlert"] {{
            border-radius: 16px;
            border: none;
            box-shadow: 0 6px 18px rgba(0,0,0,0.05);
        }}


        /* ==========================================
           TEXT INPUTS / SELECT BOXES
           Explicit text color so it never inherits a
           dark browser theme and turns invisible.
           ========================================== */

        div[data-baseweb="input"],
        div[data-baseweb="select"] > div {{
            border-radius: 14px !important;
            background: white !important;
            color: {TEXT} !important;
        }}

        div[data-baseweb="input"] input,
        div[data-baseweb="select"] * {{
            color: {TEXT} !important;
        }}


        /* ==========================================
           NATIVE FORM CONTROLS
           Checkboxes, radio buttons, progress bars
           pick up the green accent instead of the
           Streamlit default red.
           ========================================== */

        input[type="checkbox"],
        input[type="radio"] {{
            accent-color: {SECONDARY};
        }}

        div[data-testid="stProgress"] div[role="progressbar"] > div {{
            background-color: {SECONDARY} !important;
        }}


        /* ==========================================
           MAIN CONTENT TEXT
           Keeps body text dark on the light page
           background, independent of viewer theme.
           ========================================== */

        .main p, .main span, .main label, .main li {{
            color: {TEXT};
        }}

        /* ==========================================
           HOVER LIFT (applies to every *-card block
           across all pages, so this one rule covers
           the whole app)
           ========================================== */

        div[class*="-card"] {{
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }}

        div[class*="-card"]:hover {{
            transform: translateY(-4px);
            box-shadow: 0 12px 28px rgba(30, 58, 138, 0.15);
        }}

        </style>
        """,
        unsafe_allow_html=True
    )
