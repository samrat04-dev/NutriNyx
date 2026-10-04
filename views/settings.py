import streamlit as st

from engine.ml_model import train_models


@st.cache_data
def get_model_accuracy():
    """
    Trains the models once and remembers the result, so we
    don't retrain every single time this page is opened.
    Returns each goal's accuracy as a whole-number percentage.
    """

    results = train_models()

    return {
        goal: round(result["accuracy"] * 100, 1)
        for goal, result in results.items()
    }


def show_settings():

    # =========================
    # PAGE CSS
    # =========================

    st.markdown(
        """
<style>

.settings-header {
    background: linear-gradient(135deg, #1E3A8A, #3B82F6);
    padding: 40px;
    border-radius: 25px;
    color: white;
    margin-bottom: 30px;
}

.settings-title {
    font-size: 38px;
    font-weight: 800;
}

.settings-subtitle {
    font-size: 17px;
    opacity: 0.9;
    margin-top: 10px;
}

.settings-card {
    background: white;
    padding: 25px;
    border-radius: 22px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.08);
    margin-bottom: 25px;
}

.settings-card-title {
    font-size: 20px;
    font-weight: 700;
    color: #1E3A8A;
    margin-bottom: 8px;
}

.settings-card-text {
    color: #64748B;
    font-size: 14px;
    margin-bottom: 20px;
}

.about-card {
    background: linear-gradient(135deg, #EFF6FF, #F4F8FF);
    padding: 25px;
    border-radius: 22px;
    border-left: 6px solid #3B82F6;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.05);
}

.about-title {
    font-size: 20px;
    font-weight: 700;
    color: #1E3A8A;
}

.about-text {
    color: #475569;
    font-size: 16px;
    line-height: 1.7;
    margin-top: 10px;
}

</style>
        """,
        unsafe_allow_html=True
    )


    # =========================
    # HEADER
    # =========================

    st.markdown(
        """
<div class="settings-header">

<div class="settings-title">
⚙️ Settings
</div>

<div class="settings-subtitle">
Manage your NutriNyx profile and preferences.
</div>

</div>
        """,
        unsafe_allow_html=True
    )


    # =========================
    # TABS
    # =========================

    tab_profile, tab_goals, tab_about = st.tabs(
        ["👤 Profile", "🎯 Goals & Preferences", "💙 About"]
    )


    # =========================
    # PROFILE TAB
    # =========================

    with tab_profile:

        st.markdown(
            """
<div class="settings-card">

<div class="settings-card-title">
Personal Information
</div>

<div class="settings-card-text">
Keep your basic information updated for personalized nutrition guidance.
</div>

</div>
            """,
            unsafe_allow_html=True
        )

        # Give every field a starting value the first time
        # this page loads, so widgets below can rely on the
        # key= mechanism to remember whatever the user enters.
        st.session_state.setdefault("user_name", "User")
        st.session_state.setdefault("user_age", 17)
        st.session_state.setdefault("user_height", 153)
        st.session_state.setdefault("user_weight", 45)

        col1, col2 = st.columns(2)

        with col1:

            name = st.text_input(
                "Name",
                key="user_name"
            )

            age = st.number_input(
                "Age",
                min_value=10,
                max_value=100,
                key="user_age"
            )

        with col2:

            height = st.number_input(
                "Height (cm)",
                min_value=50,
                max_value=250,
                key="user_height"
            )

            weight = st.number_input(
                "Weight (kg)",
                min_value=20,
                max_value=300,
                key="user_weight"
            )


    # =========================
    # GOALS & PREFERENCES TAB
    # =========================

    with tab_goals:

        st.subheader("🎯 Health Goal")

        st.caption(
            "This is the single goal used everywhere in NutriNyx — "
            "Food Analyzer and AI Recommendations both read it from here."
        )

        st.session_state.setdefault("user_goal", "Healthy Lifestyle")

        goal = st.selectbox(
            "Choose your goal",
            [
                "Healthy Lifestyle",
                "Weight Loss",
                "Weight Gain",
                "Muscle Gain",
                "Diabetic Friendly"
            ],
            key="user_goal"
        )

        st.divider()

        st.subheader("🔔 Preferences")

        st.session_state.setdefault("pref_notifications", False)
        st.session_state.setdefault("pref_reports", False)
        st.session_state.setdefault("pref_ai_suggestions", False)

        notifications = st.checkbox(
            "Nutrition reminders",
            key="pref_notifications"
        )

        reports = st.checkbox(
            "Weekly nutrition reports",
            key="pref_reports"
        )

        ai = st.checkbox(
            "AI suggestions",
            key="pref_ai_suggestions"
        )


    # =========================
    # ABOUT TAB
    # =========================

    with tab_about:

        st.markdown(
            """
<div class="about-card">

<div class="about-title">
NutriNyx 🥗
</div>

<div class="about-text">
Your AI-powered nutrition companion that helps you
understand food, track your health, and receive
personalized nutrition guidance.
</div>

</div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        st.subheader("🧠 Model Performance")

        st.caption(
            "Accuracy of our Decision Tree model on test data, "
            "for each health goal."
        )

        for goal, accuracy in get_model_accuracy().items():

            st.write(f"**{goal}** — {accuracy}% accurate")

            st.progress(accuracy / 100)


    # =========================
    # SAVE
    # =========================

    st.divider()

    if st.button(
        "💾 Save Changes",
        use_container_width=True
    ):

        st.success(
            "✅ Your settings have been saved!"
        )