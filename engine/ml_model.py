# MACHINE LEARNING MODEL

import pandas as pd

from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


# LOAD DATASET

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "TestIndianWhole_cleaned.csv"

df = pd.read_csv(DATA_PATH)


# FEATURES USED BY THE ML MODEL

features = [
    "Calories_kcal",
    "Protein_g",
    "Carbs_g",
    "Fat_g",
    "Fiber_g",
    "Sugar_g",
    "Sodium_mg"
]


# Removed rows where important values are missing

df = df.dropna(
    subset=features + [
        "WeightLoss",
        "MuscleGain",
        "WeightGain",
        "HealthyLifestyle"
    ]
)


# TRAIN MODELS

models = {}

def train_models():

    targets = {
        "Weight Loss": "WeightLoss",
        "Muscle Gain": "MuscleGain",
        "Weight Gain": "WeightGain",
        "Healthy Lifestyle": "HealthyLifestyle"
    }

    results = {}

    x = df[features]

    for goal, target in targets.items():

        y = df[target]

        # Split dataset into training and testing data

        x_train, x_test, y_train, y_test = train_test_split(
            x,
            y,
            test_size=0.2,
            random_state=42,
            stratify=y
        )

        # Created Decision Tree model

        model = DecisionTreeClassifier(
            max_depth=5,
            random_state=42
        )

        # Train model

        model.fit(x_train, y_train)

        # Predict test data

        predictions = model.predict(x_test)

        # Calculate accuracy

        accuracy = accuracy_score(
            y_test,
            predictions
        )

        # Confusion matrix

        matrix = confusion_matrix(
            y_test,
            predictions
        )

        # Save trained model

        models[goal] = model

        results[goal] = {
            "accuracy": accuracy,
            "confusion_matrix": matrix
        }

    return results


# PREDICT USER'S FOOD

def predict_goal(nutrition, goal):

    # Train models if they have not been trained yet

    if not models:
        train_models()

    # Get the correct model

    model = models.get(goal)

    # Diabetic Friendly does not currently
    # have an ML model

    if model is None:

        return {
            "prediction": "Not Available",
            "confidence": 0
        }


    # Convert nutrition dictionary into
    # the same feature format used during training

    input_data = pd.DataFrame(
        [[
            nutrition["Calories"],
            nutrition["Protein"],
            nutrition["Carbs"],
            nutrition["Fat"],
            nutrition["Fiber"],
            nutrition["Sugar"],
            nutrition["Sodium"]
        ]],
        columns=features
    )


    # Make prediction

    prediction = model.predict(input_data)[0]


    # Get prediction probabilities

    probabilities = model.predict_proba(
        input_data
    )[0]


    # Highest probability

    confidence = max(probabilities) * 100


    return {
        "prediction": prediction,
        "confidence": confidence
    }










# ==========================================
# TESTING 

if __name__ == "__main__":

    results = train_models()


    print("\n========== ML MODEL RESULTS ==========")


    for goal, result in results.items():

        accuracy = result["accuracy"] * 100

        print(
            f"{goal} Accuracy: {accuracy:.2f} %"
        )


    print("\n========== CONFUSION MATRICES ==========")


    for goal, result in results.items():

        print(f"\n{goal}:")

        print(
            result["confusion_matrix"]
        )