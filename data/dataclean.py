import pandas as pd

df = pd.read_csv("TestIndianWhole_Cleaned.csv")

print("Original Shape:", df.shape)
print("\nOriginal Columns:")
print(df.columns.tolist())

# CHECK DATA TYPES

print("\n========== DATA TYPES ==========")
print(df.dtypes)


# CHECK MISSING VALUES

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())


# REMOVE DUPLICATE ROWS

print("\nDuplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()
print("Shape after removing duplicates:", df.shape)


# REMOVE DUPLICATE FOOD NAMES

print("\nDuplicate food names:",
      df["Food_Name"].duplicated().sum())

df = df.drop_duplicates(
    subset=["Food_Name"],
    keep="first"
)

print("Shape after removing duplicate food names:",
      df.shape)

# REMOVE EXTRA SPACES

df["Food_Name"] = (
    df["Food_Name"]
    .astype(str)
    .str.strip()
)


# STANDARDIZE FOOD NAME FORMAT

df["Food_Name"] = (
    df["Food_Name"]
    .str.title()
)

# CHECK NUMERIC COLUMNS

numeric_columns = [
    "Calories_kcal",
    "Protein_g",
    "Carbs_g",
    "Fat_g",
    "Fiber_g",
    "Sugar_g",
    "Sodium_mg"
]

print("\n========== NUMERIC DATA ==========")
print(df[numeric_columns].describe())


# CONVERT NUMERIC COLUMNS

for column in numeric_columns:

    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )


# CHECK MISSING VALUES AGAIN

print("\n========== FINAL MISSING VALUES ==========")
print(df.isnull().sum())

# FINAL DATASET INFORMATION

print("\n========== FINAL DATASET ==========")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("\nFinal Columns:")
print(df.columns.tolist())

# SAVE CLEANED DATASET

df.to_csv(
    "TestIndianWhole_cleaned.csv",
    index=False
)

print("\n✅ Data cleaning completed successfully!")
print("✅ Cleaned dataset saved.")