# PERSONAL NUTRITION RECOMMENDATION ENGINE

from engine.ml_model import predict_goal


def recommend(nutrition, goal):

    recommendations = []
    issues = []

    calories = nutrition["Calories"]
    protein = nutrition["Protein"]
    carbs = nutrition["Carbs"]
    fat = nutrition["Fat"]
    fiber = nutrition["Fiber"]
    sugar = nutrition["Sugar"]
    sodium = nutrition["Sodium"]


    # ML PREDICTION

    ml_result = predict_goal(nutrition, goal)

    ml_prediction = ml_result["prediction"]
    ml_confidence = ml_result["confidence"]


    # GOAL BASED RECOMMENDATIONS

    # WEIGHT LOSS

    if goal == "Weight Loss":

        if calories > 700:
            issues.append("High Calories")
            recommendations.append(
                "Reduce overall calorie intake."
            )

        if sugar > 25:
            issues.append("High Sugar")
            recommendations.append(
                "Reduce sugary foods and drinks."
            )

        if fat > 30:
            issues.append("High Fat")
            recommendations.append(
                "Choose low-fat food options."
            )

        if fiber < 8:
            issues.append("Low Fiber")
            recommendations.append(
                "Increase vegetables and salads for better satiety."
            )

        recommendations.append(
            "Prefer grilled, boiled or steamed food over fried food."
        )


    # WEIGHT GAIN

    elif goal == "Weight Gain":

        if calories < 700:
            issues.append("Low Calories")
            recommendations.append(
                "Increase healthy calorie intake."
            )

        if protein < 25:
            issues.append("Low Protein")
            recommendations.append(
                "Increase protein using eggs, paneer, chicken or soy."
            )

        recommendations.append(
            "Include milk, nuts and dry fruits."
        )


    # MUSCLE GAIN

    elif goal == "Muscle Gain":

        if protein < 30:
            issues.append("Low Protein")
            recommendations.append(
                "Increase protein intake."
            )

            recommendations.append(
                "Add paneer, eggs, chicken or soy chunks."
            )

        if calories < 600:
            issues.append("Low Calories")
            recommendations.append(
                "Increase calorie intake slightly."
            )

        recommendations.append(
            "Spread protein intake across multiple meals."
        )

        recommendations.append(
            "Stay hydrated throughout the day."
        )


    # DIABETIC FRIENDLY

    elif goal == "Diabetic Friendly":

        if sugar > 20:
            issues.append("High Sugar")
            recommendations.append(
                "Reduce sugar intake."
            )

        if carbs > 90:
            issues.append("High Carbohydrates")
            recommendations.append(
                "Control carbohydrate portion size."
            )

        recommendations.append(
            "Choose whole grains over refined grains."
        )

        recommendations.append(
            "Increase fiber-rich foods."
        )


    # BALANCED

    else:

        recommendations.append(
            "Maintain a balanced diet."
        )


    # GENERAL NUTRITION CHECKS

    if sodium > 2000:

        if "High Sodium" not in issues:
            issues.append("High Sodium")

        recommendations.append(
            "Reduce processed and salty foods."
        )

    else:

        recommendations.append(
            "Sodium intake is within healthy limits."
        )


    if fiber >= 8:

        recommendations.append(
            "Good fiber intake."
        )


    if protein >= 25:

        recommendations.append(
            "Protein intake is good."
        )


    if calories < 300:

        if "Very Low Calories" not in issues:
            issues.append("Very Low Calories")

        recommendations.append(
            "Meal calories are very low."
        )


    # COMBINE ML RESULT WITH RULE-BASED RESULT

    ml_message = (
        f"For the goal '{goal}', the ML model predicts "
        f"'{ml_prediction}' suitability "
        f"with approximately {ml_confidence:.1f}% confidence."
    )

    recommendations.append(ml_message)


    # AI PROMPT

    ai_prompt = f"""
You are an experienced nutritionist.

Health Goal:
{goal}

Nutrition Summary:

Calories: {calories} kcal
Protein: {protein} g
Carbs: {carbs} g
Fat: {fat} g
Fiber: {fiber} g
Sugar: {sugar} g
Sodium: {sodium} mg

Machine Learning Prediction:
{ml_prediction}

ML Confidence:
{ml_confidence:.1f}%

Detected Issues:
{', '.join(issues) if issues else 'None'}

Give:

1. A short health summary.
2. Three personalized suggestions.
3. Explain the ML prediction in simple language.
4. Keep the response below 120 words.
5. Do not change the calculated nutrition values.
6. Be encouraging and practical.
"""


    # RETURN RESULTS

    return {

        "issues": issues,

        "recommendations": recommendations,

        "ml_prediction": ml_prediction,

        "ml_confidence": ml_confidence,

        "ai_prompt": ai_prompt

    }