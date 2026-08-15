# ==========================================
# NutriNyx - Nutrition Engine
# ==========================================

import pandas as pd
from pathlib import Path
from difflib import get_close_matches, SequenceMatcher


# ==========================================
# LOAD DATASET
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "TestIndianWhole_cleaned.csv"

food = pd.read_csv(DATA_PATH)

# Remove accidental spaces from food names
food["Food_Name"] = food["Food_Name"].astype(str).str.strip()

# Remove duplicate food names
food = food.drop_duplicates(
    subset="Food_Name",
    keep="first"
)

# Use Food_Name as index
food.set_index("Food_Name", inplace=True)


# ==========================================
# GET FOOD
# ==========================================

def get_food(food_name):

    if not food_name:
        return None

    food_name = str(food_name).strip().title()

    if food_name in food.index:

        data = food.loc[food_name]

        # Safety check in case duplicates somehow remain
        if isinstance(data, pd.DataFrame):
            data = data.iloc[0]

        return data

    return None


# ==========================================
# FOOD SIMILARITY
# ==========================================

def similarity(a, b):

    return SequenceMatcher(
        None,
        a.lower(),
        b.lower()
    ).ratio()


# ==========================================
# SUGGEST FOOD NAMES
# ==========================================

def suggest_foods(food_name, limit=5):

    if not food_name:
        return []

    query = str(food_name).strip().lower()

    if not query:
        return []

    food_names = list(food.index)

    scored = []

    for item in food_names:

        item_lower = str(item).lower()

        # ----------------------------------
        # 1. Exact match
        # ----------------------------------

        if query == item_lower:

            scored.append(
                (1.0, item)
            )

            continue

        # ----------------------------------
        # 2. Word/substring match
        # ----------------------------------

        if query in item_lower:

            score = 0.90

            scored.append(
                (score, item)
            )

            continue

        # ----------------------------------
        # 3. Fuzzy similarity
        # ----------------------------------

        score = similarity(
            query,
            item_lower
        )

        # Only keep reasonably similar results
        if score >= 0.45:

            scored.append(
                (score, item)
            )


    # Sort by highest similarity
    scored.sort(
        key=lambda x: x[0],
        reverse=True
    )


    # ======================================
    # REMOVE DUPLICATES
    # ======================================

    results = []

    seen = set()

    for score, item in scored:

        normalized = item.lower()

        if normalized not in seen:

            results.append(item)

            seen.add(normalized)

        if len(results) >= limit:
            break


    return results


# ==========================================
# ANALYZE WHOLE MEAL
# ==========================================

def analyze_meal(food_list):

    total = {

        "Calories": 0.0,
        "Protein": 0.0,
        "Carbs": 0.0,
        "Fat": 0.0,
        "Fiber": 0.0,
        "Sugar": 0.0,
        "Sodium": 0.0

    }


    found_foods = []

    not_found = []


    # ======================================
    # LOOP THROUGH ALL FOODS
    # ======================================

    for item in food_list:

        item = str(item).strip()

        if not item:
            continue


        data = get_food(item)


        # ----------------------------------
        # FOOD FOUND
        # ----------------------------------

        if data is not None:

            # Store the actual dataset name
            actual_name = str(data.name)

            found_foods.append(actual_name)


            total["Calories"] += float(
                data["Calories_kcal"]
            )

            total["Protein"] += float(
                data["Protein_g"]
            )

            total["Carbs"] += float(
                data["Carbs_g"]
            )

            total["Fat"] += float(
                data["Fat_g"]
            )

            total["Fiber"] += float(
                data["Fiber_g"]
            )

            total["Sugar"] += float(
                data["Sugar_g"]
            )

            total["Sodium"] += float(
                data["Sodium_mg"]
            )


        # ----------------------------------
        # FOOD NOT FOUND
        # ----------------------------------

        else:

            not_found.append(item)


    # ======================================
    # RETURN RESULT
    # ======================================

    return {

        "foods": found_foods,

        "not_found": not_found,

        "nutrition": total

    }














# ==========================================
# TESTING
# ==========================================

if __name__ == "__main__":

    print("\n================================")
    print("       NUTRINYX FOOD TEST")
    print("================================")


    # ======================================
    # FOOD SEARCH
    # ======================================

    search = input(
        "\nEnter food name: "
    ).strip()


    # Exact search
    data = get_food(search)


    if data is not None:

        print("\n========== FOOD FOUND ==========")

        print("✓", data.name)

        print(
            f"Calories : {data['Calories_kcal']} kcal"
        )

        print(
            f"Protein  : {data['Protein_g']} g"
        )

        print(
            f"Carbs    : {data['Carbs_g']} g"
        )

        print(
            f"Fat      : {data['Fat_g']} g"
        )

        print(
            f"Fiber    : {data['Fiber_g']} g"
        )

        print(
            f"Sugar    : {data['Sugar_g']} g"
        )

        print(
            f"Sodium   : {data['Sodium_mg']} mg"
        )


    else:

        print("\n========== FOOD NOT FOUND ==========")

        print("✗", search)


        suggestions = suggest_foods(search)


        if suggestions:

            print("\n========== DID YOU MEAN? ==========")

            for suggestion in suggestions:

                print("→", suggestion)

        else:

            print(
                "\nNo similar foods were found."
            )


    # ======================================
    # MULTIPLE FOOD TEST
    # ======================================

    print("\n================================")
    print("          MEAL TEST")
    print("================================")


    meal_input = input(
        "\nEnter food items separated by commas:\n> "
    )


    meal = meal_input.split(",")


    result = analyze_meal(meal)


    # ======================================
    # FOUND FOODS
    # ======================================

    print("\n========== FOUND FOODS ==========")


    if result["foods"]:

        for item in result["foods"]:

            print("✓", item)

    else:

        print("No foods found.")


    # ======================================
    # NOT FOUND
    # ======================================

    if result["not_found"]:

        print("\n========== NOT FOUND ==========")


        for item in result["not_found"]:

            print("✗", item)


            suggestions = suggest_foods(item)


            if suggestions:

                print("  Did you mean:")

                for suggestion in suggestions:

                    print(
                        "  →",
                        suggestion
                    )


    # ======================================
    # MEAL SUMMARY
    # ======================================

    print("\n========== MEAL SUMMARY ==========")


    print(
        f"Calories : "
        f"{result['nutrition']['Calories']:.1f} kcal"
    )

    print(
        f"Protein  : "
        f"{result['nutrition']['Protein']:.1f} g"
    )

    print(
        f"Carbs    : "
        f"{result['nutrition']['Carbs']:.1f} g"
    )

    print(
        f"Fat      : "
        f"{result['nutrition']['Fat']:.1f} g"
    )

    print(
        f"Fiber    : "
        f"{result['nutrition']['Fiber']:.1f} g"
    )

    print(
        f"Sugar    : "
        f"{result['nutrition']['Sugar']:.1f} g"
    )

    print(
        f"Sodium   : "
        f"{result['nutrition']['Sodium']:.1f} mg"
    )


    print("\n================================")
    print("          TEST COMPLETE")
    print("================================")