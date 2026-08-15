# HEALTH SCORE CALCULATOR

def calculate_score(nutrition):

    score = 100

    reasons = []

    calories = nutrition["Calories"]
    protein = nutrition["Protein"]
    carbs = nutrition["Carbs"]
    fat = nutrition["Fat"]
    fiber = nutrition["Fiber"]
    sugar = nutrition["Sugar"]
    sodium = nutrition["Sodium"]


# Calories

    if calories < 300:
        score -= 15
        reasons.append("Very low calorie meal.")

    elif calories > 900:
        score -= 15
        reasons.append("Very high calorie meal.")

    else:
        reasons.append("Calories are within a healthy range.")


# Protein

    if protein >= 20:
        score += 5
        reasons.append("Good protein intake.")

    else:
        score -= 10
        reasons.append("Protein intake is low.")


# Fiber

    if fiber >= 8:
        score += 5
        reasons.append("Good fiber intake.")

    else:
        score -= 5
        reasons.append("Fiber intake is low.")


# Sugar

    if sugar > 30:
        score -= 10
        reasons.append("High sugar intake.")


# Sodium

    if sodium > 2000:
        score -= 10
        reasons.append("High sodium intake.")


# Fat

    if fat > 40:
        score -= 5
        reasons.append("Fat intake is high.")


# Keep score between 0 and 100

    score = max(0, min(score, 100))


# Rating

    if score >= 90:
        rating = "Excellent"

    elif score >= 75:
        rating = "Good"

    elif score >= 60:
        rating = "Average"

    else:
        rating = "Needs Improvement"

    return {

        "score": score,

        "rating": rating,

        "stars": min(5, max(1, round(score / 20))),

        "reasons": reasons

    }