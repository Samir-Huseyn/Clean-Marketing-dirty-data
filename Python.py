import pandas as pd

df = pd.read_csv("marketing_campaign.csv", sep=None, engine="python")
print(df.head())
print(df.info())
print(df.shape)
print(df.describe())
print(df.duplicated().sum())
print(df.isnull().sum())
df["Income"] = df["Income"].fillna(df["Income"].median())
outliers = df[df["Year_Birth"] <= 1900]
print(outliers)
df = df[df["Year_Birth"] > 1900]
print(df["Year_Birth"].min())
print(df.shape[0])
print(df["Marital_Status"].value_counts())
df["Marital_Status"] = df["Marital_Status"].replace(
    ["YOLO", "Absurd", "Alone"], "Single"
)
print(df["Z_CostContact"].unique())
print(df["Z_Revenue"].unique())
df.drop(columns=["Z_CostContact", "Z_Revenue"], inplace=True)
df["Total_spending"] = (
    df["MntWines"]
    + df["MntFruits"]
    + df["MntMeatProducts"]
    + df["MntFishProducts"]
    + df["MntSweetProducts"]
    + df["MntGoldProds"]
)
df["Children"] = df["Kidhome"] + df["Teenhome"]

living_map = {"Married": 2, "Together": 2, "Single": 1, "Divorced": 1, "Widow": 1}

df["Living_With"] = df["Marital_Status"].map(living_map)
df["Family_Size"] = df["Living_With"] + df["Children"]
df["Age"] = 2024 - df["Year_Birth"]
print(df[["Age", "Children", "Family_Size", "Total_spending"]].head())
