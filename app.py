import streamlit as st

from components.sidebar import show_sidebar
from components.footer import show_footer
from styles.custom_styles import load_custom_styles

from views.home import show_home
from views.food_analyzer import show_food_analyzer
from views.nutrition_report import show_nutrition_report
from views.recommendations import show_recommendations
from views.settings import show_settings


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="NutriNyx",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded"
)





# ==========================================
# GLOBAL STYLES
# ==========================================

load_custom_styles()


# ==========================================
# SIDEBAR
# ==========================================

menu = show_sidebar()


# ==========================================
# PAGE ROUTING
# ==========================================

if menu == "🏠 Home":

    show_home()

elif menu == "🥗 Food Analyzer":

    show_food_analyzer()

elif menu == "📊 Nutrition Report":

    show_nutrition_report()

elif menu == "🤖️ AI Recommendations":

    show_recommendations()

elif menu == "⚙️ Settings":

    show_settings()


# ==========================================
# FOOTER
# ==========================================

show_footer()