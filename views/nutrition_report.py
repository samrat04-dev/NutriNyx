import streamlit as st

from engine import nutrition


def show_nutrition_report():
    # =========================
    # GET LATEST ANALYSIS
    # =========================

    nutrition = st.session_state.get("nutrition")
    score_result = st.session_state.get("score_result")
    ai_response = st.session_state.get("ai_response")
    analyzed_food = st.session_state.get("analyzed_food")
    
    # =========================
    # PAGE CSS
    # =========================

    st.markdown(
        """
<style>

.report-header {
    background: linear-gradient(135deg, #1E3A8A, #3B82F6);
    padding: 40px;
    border-radius: 25px;
    color: white;
    margin-bottom: 30px;
}

.report-title {
    font-size: 38px;
    font-weight: 800;
}

.report-subtitle {
    font-size: 17px;
    opacity: 0.9;
    margin-top: 10px;
}

.report-card {
    background: white;
    padding: 22px;
    border-radius: 22px;
    text-align: center;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.08);
    min-height: 150px;
    transition: 0.3s;
}

.report-card:hover {
    transform: translateY(-5px);
}

.report-icon {
    font-size: 28px;
}

.report-value {
    font-size: 32px;
    font-weight: 800;
    color: #1E3A8A;
    margin: 10px 0;
}

.report-label {
    font-size: 14px;
    color: #64748B;
}

.ai-summary {
    background: linear-gradient(135deg, #EFF6FF, #F4F8FF);
    padding: 25px;
    border-radius: 22px;
    border-left: 6px solid #3B82F6;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.05);
}

.ai-title {
    font-size: 20px;
    font-weight: 700;
    color: #1E3A8A;
    margin-bottom: 12px;
}

.ai-text {
    font-size: 16px;
    color: #475569;
    line-height: 1.7;
}

.history-card {
    background: white;
    padding: 16px 20px;
    border-radius: 16px;
    box-shadow: 0px 4px 14px rgba(0,0,0,0.06);
    color: #1E293B;
    font-size: 15px;
    line-height: 1.6;
    margin-bottom: 10px;
}

.history-card b {
    color: #1E3A8A;
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
<div class="report-header">

<div class="report-title">
📊 Nutrition Report
</div>

<div class="report-subtitle">
Track your daily nutrition, understand your progress,
and improve your health.
</div>

</div>
        """,
        unsafe_allow_html=True
    )


    # =========================
    # HEALTH SCORE
    # =========================

    st.subheader("💙 Overall Health Score")

    if score_result:

        score = score_result["score"]

        st.progress(score / 100)

        st.success(
            f"Your current nutrition health score is {score}/100 — "
            f"{score_result['rating']}."
        )

    else:

        st.info(
            "🥗 Analyze a food first to generate your nutrition report."
        )


    st.divider()


    # =========================
    # DAILY INTAKE
    # =========================

    st.subheader("🍽️ Today's Intake")

    if nutrition is not None:

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.markdown(
                f"""
                <div class="report-card">
                    <div class="report-icon">🔥</div>
                    <div class="report-value">
                        {nutrition["Calories"]}
                    </div>
                    <div class="report-label">
                        Calories
                    </div>
                    <div class="report-label">
                        kcal
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with c2:
            st.markdown(
                f"""
                <div class="report-card">
                    <div class="report-icon">💪</div>
                    <div class="report-value">
                        {nutrition["Protein"]} g
                    </div>
                    <div class="report-label">
                        Protein
                    </div>
                    <div class="report-label">
                        Analyzed meal
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with c3:
            st.markdown(
                f"""
                <div class="report-card">
                    <div class="report-icon">🍞</div>
                    <div class="report-value">
                        {nutrition["Carbs"]} g
                    </div>
                    <div class="report-label">
                        Carbohydrates
                    </div>
                    <div class="report-label">
                        Analyzed meal
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with c4:
            st.markdown(
                f"""
                <div class="report-card">
                    <div class="report-icon">🥑</div>
                    <div class="report-value">
                        {nutrition["Fat"]} g
                    </div>
                    <div class="report-label">
                        Fat
                    </div>
                    <div class="report-label">
                        Analyzed meal
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    else:

        st.info(
            "🥗 Analyze a food in Food Analyzer first to see your nutrition intake."
        )

    st.write("")

    # =========================
    # MEAL HISTORY
    # =========================

    st.subheader("🕐 Meal History")

    meal_history = st.session_state.get("meal_history", [])

    if meal_history:

        clear_col, _ = st.columns([1, 3])

        with clear_col:

            if st.button("🗑️ Clear All", use_container_width=True):

                st.session_state["meal_history"] = []

                st.rerun()

        st.write("")

        # Most recent meal first
        for display_i, entry in enumerate(reversed(meal_history)):

            real_index = len(meal_history) - 1 - display_i

            row_left, row_right = st.columns([6, 1])

            with row_left:

                servings_tag = (
                    f" • {entry['servings']:g}x servings"
                    if entry.get("servings", 1) != 1
                    else ""
                )

                st.markdown(
                    f"""
                    <div class="history-card">
                        <b>{entry['food'].title()}</b>{servings_tag}
                        <br>
                        {entry['nutrition']['Calories']:.0f} kcal
                        • {entry['nutrition']['Protein']:.1f}g protein
                        • Score {entry['score']}/100
                        • {entry['time']}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with row_right:

                if st.button("🗑️", key=f"del_meal_{real_index}"):

                    st.session_state["meal_history"].pop(real_index)

                    st.rerun()

    else:

        st.info(
            "🥗 No meals logged yet. Analyzed foods will show up here."
        )

    st.write("")

    # =========================
    # NUTRIENT BALANCE
    # =========================

    st.subheader("⚖️ Nutrient Balance")

    if nutrition is not None:

        # Reference values used only to visualize the balance
        protein_progress = min(nutrition["Protein"] / 70, 1.0)
        carbs_progress = min(nutrition["Carbs"] / 250, 1.0)
        fat_progress = min(nutrition["Fat"] / 65, 1.0)

        st.write(
            f"💪 Protein — {nutrition['Protein']:.1f} g"
        )
        st.progress(protein_progress)

        st.write(
            f"🍞 Carbohydrates — {nutrition['Carbs']:.1f} g"
        )
        st.progress(carbs_progress)

        st.write(
            f"🥑 Fat — {nutrition['Fat']:.1f} g"
        )
        st.progress(fat_progress)

    else:

        st.info(
            "🥗 Analyze a food first to see your nutrient balance."
        )

    # =========================
    # AI SUMMARY
    # =========================

    st.subheader("🤖️ NutriNyx AI Summary")

    if ai_response:

        st.markdown(
            """
            <div class="ai-summary">
                <div class="ai-title">
                    🤖️ Your Nutrition Summary
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(ai_response)

    else:

        recommendations = st.session_state.get(
            "recommendations",
            []
        )

        if recommendations:

            st.markdown(
                """
                <div class="ai-summary">
                    <div class="ai-title">
                        💡 Personalized Nutrition Suggestions
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            for recommendation in recommendations:
                st.markdown(f"• {recommendation}")

        else:

            st.info(
                "🥗 Analyze a food first to generate recommendations."
            )