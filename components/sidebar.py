import streamlit as st


def show_sidebar():

    pages = [
        "🏠 Home",
        "🥗 Food Analyzer",
        "📊 Nutrition Report",
        "🤖️ AI Recommendations",
        "⚙️ Settings"
    ]

    # ==========================================
    # SIDEBAR CSS
    # ==========================================

    st.markdown(
        """
        <style>

        /* ======================================
           SIDEBAR BACKGROUND
           ====================================== */

        section[data-testid="stSidebar"] {
            background: linear-gradient(
                180deg,
                #1E3A8A 0%,
                #0F1F4D 100%
            ) !important;
        }


        /* ======================================
           SIDEBAR TEXT
           ====================================== */

        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] span,
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3 {
            color: white !important;
        }


        /* ======================================
           LOGO
           ====================================== */

        section[data-testid="stSidebar"] h2 {
            text-align: center !important;
            font-size: 32px !important;
            font-weight: 800 !important;
            margin-top: 0px !important;
            margin-bottom: 5px !important;
        }


        /* ======================================
           TAGLINE
           ====================================== */

        section[data-testid="stSidebar"] .stCaption {
            color: #FFFFFF !important;
            text-align: center !important;
            font-size: 14px !important;
        }


        /* ======================================
           ALL BORDERED CARDS
           ====================================== */

        section[data-testid="stSidebar"]
        div[data-testid="stVerticalBlockBorderWrapper"] {

            background-color: #24408A !important;

            border: 2px solid #4C79D9 !important;

            border-radius: 22px !important;

            box-shadow: 0 0 0 1px #4C79D9 !important;

            padding: 18px 6px !important;

        }


        /* ======================================
           FORCE INNER CARD BACKGROUND
           ====================================== */

        section[data-testid="stSidebar"]
        div[data-testid="stVerticalBlockBorderWrapper"]
        > div {

            background-color: transparent !important;

        }


        /* ======================================
           RADIO
           ====================================== */

        section[data-testid="stSidebar"]
        [data-testid="stRadio"] label {

            color: white !important;

            font-size: 16px !important;

            font-weight: 600 !important;

            padding: 10px 14px !important;

            border-radius: 12px !important;

            width: 100% !important;

            transition: background 0.15s ease !important;

        }


        section[data-testid="stSidebar"]
        [data-testid="stRadio"] label:hover {

            background-color: rgba(255,255,255,0.12) !important;

        }


        section[data-testid="stSidebar"]
        [data-testid="stRadio"] {

            margin-top: 0px !important;

            margin-bottom: 15px !important;

        }


        /* ======================================
           RADIO CIRCLES
           ====================================== */

        section[data-testid="stSidebar"]
        [data-testid="stRadio"] div[role="radiogroup"] {

            gap: 6px !important;

        }


        /* ======================================
           DIVIDER
           ====================================== */

        section[data-testid="stSidebar"] hr {

            border-color: rgba(255,255,255,0.18) !important;

        }

        </style>
        """,
        unsafe_allow_html=True
    )


    # ==========================================
    # SIDEBAR CONTENT
    # ==========================================

    with st.sidebar:

        # ======================================
        # LOGO
        # ======================================

        st.markdown("## 🥗 NutriNyx")

        st.caption("AI Nutrition Companion")

        st.caption("Know What You Eat.")


        # Small gap
        st.write("")


        # ======================================
        # PROFILE CARD
        # ======================================

        with st.container(border=True):

            st.markdown("### 👤 User Profile")

            st.write("Health Tracking")

            st.write("Personalized Nutrition")


        # Space after profile
        st.write("")
        st.write("")


        # ======================================
        # MENU
        # ======================================

        st.caption("MENU")


        # ======================================
        # WORKING RADIO
        # DO NOT CHANGE
        # ======================================

        menu = st.radio(
            "Navigation",
            pages,
            label_visibility="collapsed"
        )


        # Space before divider
        st.write("")

        st.divider()


        # ======================================
        # DAILY TIP
        # ======================================

        with st.container(border=True):

            st.markdown("### 💡 Daily Tip")

            st.write("Eat smart.")

            st.write("Stay healthy.")


    return menu