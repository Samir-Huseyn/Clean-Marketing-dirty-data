# Marketing Campaign Data Cleaning & Feature Engineering

This project focuses on cleaning and preparing a raw marketing campaign dataset using Python and the Pandas library. The goal is to transform "noisy" data into a structured format ready for visualization and machine learning.

## 🚀 Project Objectives
- Handle missing values and outliers.
- Standardize categorical variables.
- Perform feature engineering to derive meaningful insights from existing data.
- Optimize the dataset for downstream analysis.

## 🛠 Tech Stack
* **Python 3.x**
* **Pandas**: For data manipulation and cleaning.
* **NumPy**: For mathematical operations.

## 📋 Data Cleaning Pipeline

### 1. Data Loading & Inspection
* Loaded the dataset using the Tab (`\t`) separator.
* Initial analysis performed using `df.info()` and `df.describe()` to identify data types and anomalies.

### 2. Handling Missing Values
* Identified 24 missing values in the `Income` column.
* Imputed missing entries using the **Median** to avoid the influence of extreme outliers.

### 3. Outlier Removal
* Filtered out unrealistic birth years (e.g., customers born before 1900) to ensure age accuracy.
* Dropped redundant columns (`Z_CostContact`, `Z_Revenue`) that contained zero variance (constant values).

### 4. Categorical Standardization
* Cleaned the `Marital_Status` column by grouping non-standard entries like "YOLO", "Absurd", and "Alone" into the "Single" category.

### 5. Feature Engineering
* **Age**: Calculated the current age of customers based on `Year_Birth`.
* **Total_Spending**: Aggregated spending across 6 product categories (Wines, Fruits, Meat, Fish, Sweets, and Gold).
* **Children**: Combined `Kidhome` and `Teenhome` to get the total number of children in the household.
* **Family_Size**: Calculated the total number of people in the household by mapping marital status and adding the number of children.

## 📊 Conclusion
The dataset is now cleaned and enriched. The number of features has been optimized, and the logical inconsistencies have been resolved, making it perfect for Exploratory Data Analysis (EDA) or Customer Segmentation models.

## 📂 How to Use
1. Clone the repository:
   ```bash
   git clone [https://github.com/Samir-Huseyn/marketing_campaign.csv.git](https://github.com/Samir-Huseyn/marketing_campaign.csv.git)
