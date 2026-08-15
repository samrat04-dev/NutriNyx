import streamlit as st

from engine.ai import generate_ai_recommendation


def show_recommendations():

    # =========================
    # GET LATEST ANALYSIS
    # =========================

    ai_response = st.session_state.get("ai_response")
    recommendations = st.session_state.get("recommendations", [])
    issues = st.session_state.get("issues", [])
    goal = st.session_state.get("goal")
    analyzed_food = st.session_state.get("analyzed_food")

    # =========================
    # PAGE CSS
    # =========================

    st.markdown(
        """
<style>

.recommendation-header {
    background: linear-gradient(135deg, #1E3A8A, #3B82F6);
    padding: 40px;
    border-radius: 25px;
    color: white;
    margin-bottom: 30px;
}

.recommendation-title {
    font-size: 38px;
    font-weight: 800;
}

.recommendation-subtitle {
    font-size: 17px;
    opacity: 0.9;
    margin-top: 10px;
}

.goal-card {
    background: white;
    padding: 25px;
    border-radius: 22px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.08);
    margin-bottom: 25px;
}

.food-card {
    background: white;
    padding: 24px;
    border-radius: 22px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.08);
    min-height: 190px;
    transition: 0.3s;
}

.food-card:hover {
    transform: translateY(-5px);
}

.food-icon {
    font-size: 30px;
}

.food-title {
    font-size: 19px;
    font-weight: 700;
    color: #1E3A8A;
    margin: 12px 0;
}

.food-list {
    color: #475569;
    font-size: 15px;
    line-height: 1.8;
}

.meal-card {
    background: #F4F8FF;
    padding: 25px;
    border-radius: 22px;
    border-left: 6px solid #3B82F6;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.05);
    line-height: 1.9;
}

.smart-card {
    background: linear-gradient(135deg, #EFF6FF, #F4F8FF);
    padding: 25px;
    border-radius: 22px;
    border-left: 6px solid #3B82F6;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.05);
}

.smart-title {
    font-size: 20px;
    font-weight: 700;
    color: #1E3A8A;
}

.smart-text {
    font-size: 16px;
    color: #475569;
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
<div class="recommendation-header">

<div class="recommendation-title">
🤖️ AI Nutrition Recommendations
</div>

<div class="recommendation-subtitle">
Get personalized food suggestions based on your health goals.
</div>

</div>
        """,
        unsafe_allow_html=True
    )


    # =========================
    # LATEST ANALYSIS
    # =========================

    if ai_response is None:

        st.info(
            "🥗 Analyze a food in Food Analyzer first to see your personalized AI recommendations."
        )

    else:

        st.markdown(
            f"""
    <div class="goal-card">

    <div class="food-title">
    🎯 Current Goal: {goal}
    </div>

    <div class="food-list">
    🍎 Analyzed Food: {analyzed_food.title()}
    </div>

    </div>
    """,
            unsafe_allow_html=True
        )

    
    # =========================
    # PERSONALIZED RECOMMENDATIONS
    # =========================

    st.subheader("✨ Personalized Recommendations")

    if recommendations:

        for recommendation in recommendations:

            st.markdown(
                f"""
                <div style="
                    padding: 12px 0;
                    font-size: 16px;
                    color: #475569;
                ">
                    • {recommendation}
                </div>
                """,
                unsafe_allow_html=True
            )

    else:

        st.info(
            "No specific recommendations were detected for this meal."
        )

    # =========================
    # MEAL PLAN
    # =========================

    st.subheader("🍽️ Suggested Daily Meal Plan")


    st.markdown(
        """
<div class="meal-card">

<b>🌅 Breakfast</b><br>
Oats + Milk + Fruits

<br><br>

<b>☀️ Lunch</b><br>
Dal + Rice + Salad

<br><br>

<b>🌙 Dinner</b><br>
Paneer + Roti + Vegetables

</div>
        """,
        unsafe_allow_html=True
    )


    # =========================
    # SMART TIP
    # =========================

    st.subheader("✨ NutriNyx Smart Tip")


    st.markdown(
        """
<div class="smart-card">

<div class="smart-title">
🤖️ NutriNyx Smart Tip
</div>

<div class="smart-text">
Based on your nutrition pattern, focus on maintaining
balanced meals and including a variety of nutrient-rich
foods throughout the day.

Stay consistent for better results 💙
</div>

</div>
        """,
        unsafe_allow_html=True
    )


    # =========================
    # NUTRINYX AI CHAT
    # =========================

    st.subheader("💬 NutriNyx AI")

    st.session_state.setdefault("chat_messages", [])

    for message in st.session_state["chat_messages"]:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    user_message = st.chat_input("Ask NutriNyx AI about your nutrition...")

    if user_message:

        st.session_state["chat_messages"].append(
            {"role": "user", "content": user_message}
        )

        with st.chat_message("user"):
            st.write(user_message)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                reply = generate_ai_recommendation(user_message)
                st.write(reply)

        st.session_state["chat_messages"].append(
            {"role": "assistant", "content": reply}
        )