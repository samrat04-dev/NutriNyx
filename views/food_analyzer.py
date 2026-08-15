import streamlit as st
from datetime import datetime

from engine.nutrition import analyze_meal, suggest_foods
from engine.scorer import calculate_score
from engine.recommender import recommend
from engine.ai import generate_ai_recommendation


def replace_food_in_input(current_input, old_item, new_item):
    """
    Swaps one misspelled food name inside the (possibly comma
    separated) input box with the chosen suggestion, keeping
    every other food the user typed untouched.
    """

    parts = [p.strip() for p in current_input.split(",") if p.strip()]

    parts = [
        new_item if p.lower() == old_item.lower() else p
        for p in parts
    ]

    return ", ".join(parts)


def show_food_analyzer():
    # =========================
    # PAGE CSS
    # =========================

    st.markdown(
        """
        <style>

        .analyzer-header {
            background: linear-gradient(135deg, #1E3A8A, #3B82F6);
            padding: 40px;
            border-radius: 24px;
            color: white;
            margin-bottom: 30px;
        }

        .analyzer-title {
            font-size: 38px;
            font-weight: 800;
            margin-bottom: 10px;
        }

        .analyzer-subtitle {
            font-size: 17px;
            opacity: 0.9;
        }

        .input-card {
            background: white;
            padding: 25px;
            border-radius: 22px;
            box-shadow: 0px 8px 25px rgba(0,0,0,0.08);
            margin-bottom: 30px;
        }

        .nutrition-card {
            background: white;
            padding: 22px;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0px 8px 25px rgba(0,0,0,0.08);
            min-height: 150px;
            transition: 0.3s;
        }

        .nutrition-card:hover {
            transform: translateY(-5px);
        }

        .nutrition-icon {
            font-size: 30px;
        }

        .nutrition-value {
            font-size: 30px;
            font-weight: 800;
            color: #1E3A8A;
            margin: 10px 0;
        }

        .nutrition-label {
            font-size: 14px;
            color: #64748B;
        }

        .result-title {
            font-size: 25px;
            font-weight: 700;
            color: #1E3A8A;
            margin-bottom: 18px;
        }

        .recommendation-card {
            background: linear-gradient(135deg, #EFF6FF, #F4F8FF);
            padding: 25px;
            border-radius: 22px;
            border-left: 6px solid #3B82F6;
            margin-top: 30px;
            box-shadow: 0px 6px 20px rgba(0,0,0,0.05);
        }

        .recommendation-title {
            font-size: 20px;
            font-weight: 900 !important;
            color: #1E3A8A;
        }

        .recommendation-text {
            font-size: 16px;
            color: #475569;
            line-height: 1.6;
        }

        .input-heading {
            font-size: 24px;
            font-weight: 700;
            color: #1E3A8A;
            margin-bottom: 5px;
        }

        .input-description {
            font-size: 15px;
            color: #64748B;
            margin-bottom: 18px;
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
        <div class="analyzer-header">

        <div class="analyzer-title">
        🥗 Food Analyzer
        </div>

        <div class="analyzer-subtitle">
        Enter a food name and discover its nutritional information.
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # =========================
    # INPUT
    # =========================

    st.markdown(
        """
        <div class="input-card">
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="input-heading">
        🍎 What did you eat?
        </div>

        <div class="input-description">
        Enter the name of a food to analyze its nutritional value.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.session_state.setdefault("food_input", "")

    # If a suggestion button was just clicked, apply it BEFORE the
    # text_input widget below is created (Streamlit won't allow
    # changing a widget's value after it's already been drawn).
    if "pending_food_input" in st.session_state:
        st.session_state["food_input"] = st.session_state.pop("pending_food_input")

    food_name = st.text_input(
        "Food name",
        key="food_input",
        placeholder="e.g. Paneer, Apple, Rice, Poha...",
        label_visibility="collapsed"
    )

    col_goal, col_servings = st.columns([2, 1])

    with col_goal:
        goal = st.selectbox(
            "🎯 Your health goal",
            [
                "Balanced",
                "Weight Loss",
                "Weight Gain",
                "Muscle Gain",
                "Diabetic Friendly"
            ]
        )

    with col_servings:
        servings = st.number_input(
            "🍽️ Servings",
            min_value=0.5,
            max_value=10.0,
            value=1.0,
            step=0.5,
            help="How many servings of this did you eat? "
                 "All nutrition values are multiplied by this number."
        )

    analyze = st.button(
        "🔍 Analyze Food",
        use_container_width=True
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

    # =========================
    # ANALYZE FOOD
    # =========================

    if analyze:

        if not food_name.strip():

            st.warning("⚠️ Please enter a food name.")

        else:

            # ==========================================
            # MULTIPLE FOOD INPUT
            # Example:
            # Boiled Egg, Rice, Apple
            # ==========================================

            food_list = [
                item.strip()
                for item in food_name.split(",")
                if item.strip()
            ]

            # Analyze all entered foods
            result = analyze_meal(food_list)

            found_foods = result["foods"]
            not_found_foods = result["not_found"]

            # ==========================================
            # SHOW SUGGESTIONS FOR UNKNOWN FOODS
            # ==========================================

            if not_found_foods:

                st.error(
                    "❌ The following food(s) were not found "
                    "in the nutrition database:"
                )

                for item in not_found_foods:

                    st.write(f"• **{item.title()}**")

                    suggestions = suggest_foods(item)

                    if suggestions:

                        st.markdown("### 💡 Did you mean?")

                        st.write("Tap a match to fix it in the box above:")

                        suggestion_cols = st.columns(len(suggestions))

                        for col, suggestion in zip(
                            suggestion_cols,
                            suggestions
                        ):

                            with col:

                                if st.button(
                                    suggestion,
                                    key=f"suggest_{item}_{suggestion}",
                                    use_container_width=True
                                ):

                                    st.session_state["pending_food_input"] = (
                                        replace_food_in_input(
                                            st.session_state["food_input"],
                                            item,
                                            suggestion
                                        )
                                    )

                                    st.rerun()

                    else:

                        st.info(
                            f"No similar foods were found for "
                            f"'{item.title()}'."
                        )

            # ==========================================
            # IF NOTHING WAS FOUND
            # ==========================================

            if not found_foods:

                st.info(
                    "🥗 No valid foods were found. "
                    "Please check the food names and try again."
                )

            # ==========================================
            # IF AT LEAST ONE FOOD WAS FOUND
            # ==========================================

            else:

                nutrition = result["nutrition"]

                # ==========================================
                # APPLY SERVINGS MULTIPLIER
                # e.g. 2 servings = double every nutrient
                # ==========================================

                nutrition = {
                    key: value * servings
                    for key, value in nutrition.items()
                }

                score_result = calculate_score(nutrition)

                recommendation_result = recommend(
                    nutrition,
                    goal
                )

                ai_response = generate_ai_recommendation(
                    recommendation_result["ai_prompt"]
                )

                # ==========================================
                # SESSION STATE
                # ==========================================

                st.session_state["ai_response"] = ai_response

                st.session_state["recommendations"] = (
                    recommendation_result["recommendations"]
                )

                st.session_state["issues"] = (
                    recommendation_result["issues"]
                )

                st.session_state["goal"] = goal

                st.session_state["analyzed_food"] = ", ".join(
                    found_foods
                )

                st.session_state["nutrition"] = nutrition

                st.session_state["score_result"] = score_result

                # ==========================================
                # LOG TO MEAL HISTORY
                # ==========================================

                st.session_state.setdefault("meal_history", [])

                st.session_state["meal_history"].append({
                    "food": ", ".join(found_foods),
                    "servings": servings,
                    "nutrition": nutrition,
                    "score": score_result["score"],
                    "time": datetime.now().strftime("%I:%M %p")
                })

                # ==========================================
                # SUCCESS MESSAGE
                # ==========================================

                servings_note = (
                    f" ({servings:g} servings)" if servings != 1 else ""
                )

                st.success(
                    f"✅ Nutrition information found for "
                    f"{', '.join(found_foods)}{servings_note}!"
                )
                # =========================
                # RESULT TITLE
                # =========================

                st.markdown(
                    '<div class="result-title">📊 Nutrition Information</div>',
                    unsafe_allow_html=True
                )

                # =========================
                # NUTRITION CARDS
                # =========================

                col1, col2, col3, col4 = st.columns(4)

                with col1:

                    st.markdown(
                        f"""
                        <div class="nutrition-card">

                        <div class="nutrition-icon">
                        🔥
                        </div>

                        <div class="nutrition-value">
                        {nutrition["Calories"]:.1f}
                        </div>

                        <div class="nutrition-label">
                        Calories (kcal)
                        </div>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                with col2:

                    st.markdown(
                        f"""
                        <div class="nutrition-card">

                        <div class="nutrition-icon">
                        💪
                        </div>

                        <div class="nutrition-value">
                        {nutrition["Protein"]:.1f} g
                        </div>

                        <div class="nutrition-label">
                        Protein
                        </div>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                with col3:

                    st.markdown(
                        f"""
                        <div class="nutrition-card">

                        <div class="nutrition-icon">
                        🌾
                        </div>

                        <div class="nutrition-value">
                        {nutrition["Carbs"]:.1f} g
                        </div>

                        <div class="nutrition-label">
                        Carbohydrates
                        </div>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                with col4:

                    st.markdown(
                        f"""
                        <div class="nutrition-card">

                        <div class="nutrition-icon">
                        🥑
                        </div>

                        <div class="nutrition-value">
                        {nutrition["Fat"]:.1f} g
                        </div>

                        <div class="nutrition-label">
                        Fat
                        </div>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                # =========================
                # SECOND ROW
                # =========================

                st.write("")

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.markdown(
                        f"""
                        <div class="nutrition-card">

                        <div class="nutrition-icon">
                        🌿
                        </div>

                        <div class="nutrition-value">
                        {nutrition["Fiber"]:.1f} g
                        </div>

                        <div class="nutrition-label">
                        Fiber
                        </div>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                with col2:

                    st.markdown(
                        f"""
                        <div class="nutrition-card">

                        <div class="nutrition-icon">
                        🍬
                        </div>

                        <div class="nutrition-value">
                        {nutrition["Sugar"]:.1f} g
                        </div>

                        <div class="nutrition-label">
                        Sugar
                        </div>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                with col3:

                    st.markdown(
                        f"""
                        <div class="nutrition-card">

                        <div class="nutrition-icon">
                        🧂
                        </div>

                        <div class="nutrition-value">
                        {nutrition["Sodium"]:.1f} mg
                        </div>

                        <div class="nutrition-label">
                        Sodium
                        </div>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                st.markdown(
                    f"""
                    <div class="recommendation-card">

                    <div class="recommendation-title">
                        🏆 Health Score: {score_result["score"]}/100
                    </div>

                    <div class="recommendation-text">

                    <b>Rating:</b> {score_result["rating"]}

                    <br><br>

                    <b>⭐ Score:</b> {"⭐" * score_result["stars"]}

                    </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    '<div class="result-title">💡 Health Analysis</div>',
                    unsafe_allow_html=True
                )

                for reason in score_result["reasons"]:
                    st.write("•", reason)

                # =========================
                # PERSONALIZED RECOMMENDATIONS
                # =========================

                st.markdown(
                    '<div class="result-title">🤖️ Personalized Recommendations</div>',
                    unsafe_allow_html=True
                )

                if recommendation_result["issues"]:

                    st.markdown("### ⚠️ Areas to Improve")

                    for issue in recommendation_result["issues"]:
                        st.write("•", issue)

                st.markdown("### 💡 Suggestions")

                for suggestion in recommendation_result["recommendations"]:
                    st.write("•", suggestion)

                st.markdown(
                    '<div class="result-title">🤖️ AI Nutrition Insight</div>',
                    unsafe_allow_html=True
                )

                with st.container(border=True):

                    st.markdown(
                        '<div class="recommendation-title">'
                        '✨ Personalized AI Analysis</div>',
                        unsafe_allow_html=True
                    )

                    st.markdown(ai_response)

                # =========================
                # ENGINE STATUS
                # =========================

                st.markdown(
                    f"""
                    <div class="recommendation-card">

                    <div class="recommendation-title">
                    🤖️ NutriNyx Analysis
                    </div>

                    <div class="recommendation-text">
                    Nutrition data successfully retrieved from the
                    NutriNyx food database for
                    <b>{food_name.title()}</b>.
                    </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

