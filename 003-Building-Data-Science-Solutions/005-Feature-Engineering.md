

## 🔧 What is Feature Engineering?

**Feature Engineering** is the process of **creating, transforming, or selecting the right input variables (features)** that can be used by machine learning models to improve their performance.

In simpler terms, it's about **preparing the data in a smart way** so that the model can learn better and make more accurate predictions.

---

## 🎯 Why is Feature Engineering Important?

### 1. **Enhances Model Performance**

- Raw data may not always represent patterns effectively.

- Well-engineered features often lead to **higher accuracy, precision, and recall**.

### 2. **Bridges Data and Algorithms**

- Even simple models can outperform complex ones **if the right features are used**.

- It ensures models see the data in a **meaningful way**.

### 3. **Improves Interpretability**

- Features crafted with domain knowledge are often more **intuitive and explainable**.

### 4. **Helps Handle Data Issues**

- Feature engineering helps tackle **missing data, scaling problems, skewed distributions**, etc.

### 5. **Critical for Real-World Use Cases**

- In practice, the difference between a working and non-working ML system is often in the **quality of features**, not just the algorithm.

---

### 🧠 Thought:

> “In machine learning, models learn *from features*. The better the features, the smarter the model.”

---

Certainly buddy! Here's the revised and enriched explanation of **Feature Engineering Techniques** — **without code**, and with **real-world use cases**. I've expanded the **encoding section** as requested.

---

# 🔧 Feature Engineering Techniques



<img title="" src="file:///C:/Users/anant/Desktop/AU2025/src_images/feature-engineering-methods.png" alt="Data Science as Cooking Analogy" width="700" style="display: block; margin: auto;">

---

## ✅ 1. **Imputation (Handling Missing Values)**

### 🔹 What It Is:

Filling in missing values so models can work properly without discarding important records.

### 🔹 Real-World Example:

In a hospital dataset, if 10% of patients didn’t report their weight, imputing the average or median weight can ensure that those rows aren’t discarded during modeling.

---

## ✅ 2. **Encoding Categorical Variables**

### 🔹 What It Is:

Transforming categorical values (like “Yes”, “No”, “Male”, “Female”, etc.) into numbers that a machine learning algorithm can interpret.

### 🔹 Types of Encoding & When to Use:

---

#### 🟠 a. **Label Encoding**

- **What**: Assigns a unique integer to each category.

- **Use Case**: Use it only when the categories have **a natural order**.

- **Example**:
  
  - "Low" → 0
  
  - "Medium" → 1
  
  - "High" → 2

- **Real-World Scenario**:  
  Satisfaction levels in employee feedback.

---

#### 🟠 b. **One-Hot Encoding**

- **What**: Converts each category into a new binary (0 or 1) column.

- **Use Case**: Use when categories are **nominal (no order)**.

- **Example**: For "Country" = {India, USA, UK}, three columns:
  
  - `India`: 1/0
  
  - `USA`: 1/0
  
  - `UK`: 1/0

- **Real-World Scenario**:  
  Encoding cities, job roles, departments, or brand names.

---

#### 🟠 c. **Binary Encoding**

- **What**: Converts categories into binary digits and distributes them across fewer columns.

- **Use Case**: When you have **high-cardinality categorical features** (e.g., 50+ categories).

- **Real-World Scenario**:  
  Zip codes, product IDs, or employee codes.

---

#### 🟠 d. **Frequency Encoding**

- **What**: Replaces categories with the **frequency of their occurrence**.

- **Use Case**: Great for tree-based models (like decision trees or random forests).

- **Real-World Scenario**:  
  Encoding car models based on how often they appear in a vehicle insurance dataset.

---

#### 🟠 e. **Target Encoding (Mean Encoding)**

- **What**: Replaces each category with the **mean of the target variable** for that category.

- **Use Case**: Useful in regression problems; but can lead to leakage if not handled carefully.

- **Real-World Scenario**:  
  Predicting loan default rates where "Employer" is replaced by the average default rate among employees of that employer.

---

## ✅ 3. **Scaling and Normalization**

### 🔹 What It Is:

Adjusting the range of numerical values to a standard scale.

### 🔹 Real-World Example:

When predicting property prices, "Area (sqft)" and "No. of Rooms" need to be scaled so one doesn’t dominate the model due to its higher numeric range.

---

## ✅ 4. **Binning (Discretization)**

### 🔹 What It Is:

Grouping continuous values into categories or bins.

### 🔹 Real-World Example:

In customer segmentation, age is often grouped as:

- 18–25 (Young Adults)

- 26–40 (Professionals)

- 41–60 (Mature Adults)

- 60+ (Seniors)

---

## ✅ 5. **Interaction Features**

### 🔹 What It Is:

Creating new features by combining existing ones to uncover relationships.

### 🔹 Real-World Example:

In retail, "Total Spend per Visit" = "Average Spend" × "Frequency of Visit".

---

## ✅ 6. **Polynomial Features**

### 🔹 What It Is:

Introducing non-linear relationships by squaring or multiplying features.

### 🔹 Real-World Example:

In energy consumption prediction, the square of temperature may better explain variation in AC usage.

---

## ✅ 7. **Log Transformation**

### 🔹 What It Is:

Used to reduce skewness in data, especially right-skewed distributions.

### 🔹 Real-World Example:

Salary data is often right-skewed; a log transform helps treat outliers and improve model fit.

---

## ✅ 8. **Datetime Feature Extraction**

### 🔹 What It Is:

Extracting components from datetime fields like day, month, or weekday.

### 🔹 Real-World Example:

In ride-sharing data, trips on weekends or holidays can be very different from weekdays — extracting weekday/weekend info helps improve model accuracy.

---

## ✅ 9. **Text Feature Extraction**

### 🔹 What It Is:

Transforming textual data into numerical format.

### 🔹 Real-World Example:

Customer reviews on Amazon are converted into keyword frequencies or TF-IDF scores to train sentiment classifiers.

---

## ✅ 10. **Feature Selection**

### 🔹 What It Is:

Identifying and retaining only the most meaningful features.

### 🔹 Real-World Example:

In a student performance dataset, if "Roll Number" and "Address" have no bearing on the final grade prediction, they should be dropped.

---

## 🧠 Summary Table

| Technique                   | Real-World Use Case Example                              |
| --------------------------- | -------------------------------------------------------- |
| Imputation                  | Filling missing blood pressure values in patient records |
| Label Encoding              | Education Level: High School < Bachelor < Master < PhD   |
| One-Hot Encoding            | Encoding customer location for churn prediction          |
| Binary Encoding             | Converting ZIP codes with hundreds of levels             |
| Frequency Encoding          | Encoding car model names in insurance fraud prediction   |
| Target Encoding             | Mean loan default rate per employer                      |
| Scaling & Normalization     | Equalizing salary and number of projects before modeling |
| Binning                     | Age grouping for marketing segmentation                  |
| Interaction Features        | Spending per visit, BMI from height & weight             |
| Polynomial Features         | Temperature² in energy demand forecasting                |
| Log Transformation          | Skewed income data in housing price prediction           |
| Datetime Feature Extraction | Extracting month/weekday from order dates                |
| Text Feature Extraction     | TF-IDF for customer review classification                |
| Feature Selection           | Dropping ID columns or unrelated demographic details     |

---

# 🧠 Feature Selection in AI – A Deep Dive



<img title="" src="file:///C:/Users/anant/Desktop/AU2025/src_images/feature-selection-methods.png" alt="Data Science as Cooking Analogy" width="700" style="display: block; margin: auto;">

---

## 🔍 What is Feature Selection?

**Feature Selection** is the process of identifying and retaining only the **most relevant features** in your dataset that contribute meaningfully to the predictive power of a model. It improves performance, reduces overfitting, speeds up computation, and enhances interpretability.

---

## 🎯 Why is Feature Selection Important?

- ✅ Reduces model complexity

- ✅ Improves generalization (prevents overfitting)

- ✅ Makes models faster to train and easier to interpret

- ✅ Helps eliminate noise and irrelevant data

---

## 📊 Types of Feature Selection Methods

Feature selection methods are generally classified into **three broad categories**:

---

### 🔹 1. **Filter Methods**

These techniques select features based on **statistical tests** and **intrinsic properties** of the data — *independent of any machine learning model*.

#### ✅ Common Techniques:

- **Correlation Matrix**
  
  - Remove features that are highly correlated with others.
  
  - 🔁 Example: “Monthly Income” and “Annual Income”

- **Chi-Square Test**
  
  - Measures dependence between categorical variables.
  
  - 📌 Use Case: Identifying categorical variables that impact loan approval.

- **ANOVA (Analysis of Variance)**
  
  - Tests the variance in a continuous variable across groups of a categorical feature.
  
  - 📌 Use Case: Comparing student grades across education levels.

- **Mutual Information**
  
  - Measures how much one variable tells you about another.
  
  - 📌 Use Case: Selecting customer attributes that influence churn.

#### 🧠 Pros:

- Fast and computationally efficient.

- Simple and interpretable.

#### ⚠️ Cons:

- Ignores feature interactions.

- Not model-specific.

---

### 🔹 2. **Wrapper Methods**

Wrapper methods **train and evaluate models** using different subsets of features to find the best-performing combination.

#### ✅ Common Techniques:

- **Forward Selection**
  
  - Start with no features, add one at a time that improves model performance most.

- **Backward Elimination**
  
  - Start with all features, remove the least useful one iteratively.

- **Recursive Feature Elimination (RFE)**
  
  - Recursively trains a model, ranks features, and eliminates the weakest ones.

#### 📌 Real-World Example:

In predicting employee attrition, wrapper methods may iteratively test combinations like [Age, JobSatisfaction, OverTime] to find the best subset.

#### 🧠 Pros:

- Captures feature interactions.

- Often yields best-performing subset.

#### ⚠️ Cons:

- Computationally expensive (especially with many features).

- Risk of overfitting if cross-validation is not used.

---

### 🔹 3. **Embedded Methods**

These methods combine the **power of models and feature selection** into a single process. They select features as part of model training.

#### ✅ Common Techniques:

- **L1 Regularization (Lasso Regression)**
  
  - Shrinks some feature weights to zero, effectively removing them.

- **Tree-Based Feature Importance (Random Forest, XGBoost)**
  
  - Feature importance is calculated during model building based on how much each feature improves performance.

#### 📌 Real-World Example:

In credit scoring, Random Forest may automatically identify features like “Late Payment Frequency” and “Loan Duration” as important.

#### 🧠 Pros:

- Less computational effort than wrapper methods.

- Accounts for model-specific performance.

- Balances performance and interpretability.

#### ⚠️ Cons:

- Model-dependent.

- May be harder to interpret in non-linear models.

---

## 🧩 Advanced & Hybrid Approaches

- **Boruta Algorithm**: A wrapper built around Random Forest that identifies all relevant features (not just top ones).

- **SHAP / Permutation Importance**: Post-model analysis to estimate feature impact on predictions.

---

## 🧠 Summary Table

| Method Type  | Technique               | Best For                             | Model-Dependent | Speed  |
| ------------ | ----------------------- | ------------------------------------ | --------------- | ------ |
| **Filter**   | Correlation, Chi-Square | Quick screening                      | ❌               | Fast   |
| **Wrapper**  | RFE, Forward Selection  | Small-medium datasets                | ✅               | Slow   |
| **Embedded** | Lasso, Tree Importance  | Auto feature tuning during training  | ✅               | Medium |
| **Hybrid**   | Boruta, SHAP            | Deeper feature insight post-training | ✅               | Medium |

---

## 🔚 Final Thoughts:

> “Not all data is good data — feature selection helps us decide what to keep, what to ignore, and what to question.”

---



## ✅ Case Study 1: Imputing Missing Ratings

### 1. **Case Study Name**

**Imputing Missing Ratings**

---

### 2. **Case Study Description**

User-generated ratings are valuable for understanding customer satisfaction. However, missing values in the `RatingGiven` column can reduce model effectiveness or cause errors during training. This case focuses on handling those missing values responsibly using **imputation**.

---

### 3. **Solution Approach**

- First, identify the number of missing values in the `RatingGiven` column.

- Since the rating scale (1 to 5) is ordinal and moderately symmetric, **median imputation** is chosen over mean to avoid the effect of potential outliers.

- The missing values are then filled with the median rating to ensure consistency across records.

---

### 4. **Python Code with Inline Documentation**

```python
import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv("ecommerce_dataset.csv")

# Step 2: Check how many values are missing in 'RatingGiven'
missing_before = df['RatingGiven'].isnull().sum()
print(f"Missing values before imputation: {missing_before}")

# Step 3: Compute the median of available ratings
median_rating = df['RatingGiven'].median()
print(f"Median Rating: {median_rating}")

# Step 4: Fill missing values with the median rating
df['RatingGiven'].fillna(median_rating, inplace=True)

# Step 5: Confirm that there are no missing values now
missing_after = df['RatingGiven'].isnull().sum()
print(f"Missing values after imputation: {missing_after}")
```

---

**🟢 Output Summary:**

- Missing values before imputation: `38`

- Median rating used for filling: `3.0`

- Missing values after imputation: `0`

---



## ✅ Case Study 2: Encoding Gender and Premium Membership

### 1. **Case Study Name**

**Encoding Gender and Premium Membership**

---

### 2. **Case Study Description**

Machine learning models work only with numerical data. Categorical features such as **Gender** and **Premium Membership status** need to be converted into numerical format for training. This case demonstrates how to encode both **binary** and **multi-class categorical features**.

---

### 3. **Solution Approach**

- For the **binary** feature `IsPremiumMember`, we use **Label Encoding**:  
  `"Yes"` → 1, `"No"` → 0.

- For the **multi-class** feature `Gender`, we use **One-Hot Encoding** with `drop_first=True` to avoid dummy variable trap.
  
  - This will create two binary columns: `Gender_Male` and `Gender_Other`, with `Female` as the baseline.

---

### 4. **Python Code with Inline Documentation**

```python
import pandas as pd

# Step 1: Load dataset and handle missing rating
df = pd.read_csv("ecommerce_dataset.csv")
df['RatingGiven'].fillna(df['RatingGiven'].median(), inplace=True)

# Step 2: Label Encoding for binary column 'IsPremiumMember'
# Converts 'Yes' to 1 and 'No' to 0
df['IsPremiumMember_encoded'] = df['IsPremiumMember'].map({'Yes': 1, 'No': 0})

# Step 3: One-Hot Encoding for 'Gender'
# Creates new columns for each gender except the first (to avoid redundancy)
df_encoded = pd.get_dummies(df, columns=['Gender'], drop_first=True)

# Step 4: Preview the newly created columns
print(df_encoded[['IsPremiumMember', 'IsPremiumMember_encoded', 'Gender_Male', 'Gender_Other']].head())
```

---

**🟢 Output Preview (First 5 Rows):**

| IsPremiumMember | IsPremiumMember_encoded | Gender_Male | Gender_Other |
| --------------- | ----------------------- | ----------- | ------------ |
| Yes             | 1                       | 1           | 0            |
| No              | 0                       | 0           | 0            |
| No              | 0                       | 0           | 1            |
| ...             | ...                     | ...         | ...          |

---



## ✅ Case Study 3: Creating Recency Feature from Last Login

### 1. **Case Study Name**

**Creating Recency Feature from Last Login**

---

### 2. **Case Study Description**

In customer behavior analysis, **recency** (how recently a customer interacted with the platform) is a key driver of churn prediction, re-engagement campaigns, and lifecycle segmentation. This case introduces a derived numerical feature: **`Recency`**, representing the number of days since a customer last logged in.

---

### 3. **Solution Approach**

- Convert the `LastLoginDate` column to a valid datetime format.

- Calculate the number of days between today's date and the last login date.

- Store the result in a new feature called `Recency`.

- This feature enables modeling how **fresh** a customer's interaction is.

---

### 4. **Python Code with Inline Documentation**

```python
import pandas as pd
from datetime import datetime

# Step 1: Ensure the column is in datetime format
df['LastLoginDate'] = pd.to_datetime(df['LastLoginDate'])

# Step 2: Use the current date to compute recency
today = pd.to_datetime("today")  # This returns today's system date

# Step 3: Calculate 'Recency' as days since the last login
df['Recency'] = (today - df['LastLoginDate']).dt.days

# Step 4: Preview the new column
print(df[['CustomerID', 'LastLoginDate', 'Recency']].head())
```

---

**🟢 Output Preview (First 5 Rows):**

| CustomerID | LastLoginDate | Recency (Days) |
| ---------- | ------------- | -------------- |
| CUST1000   | 2025-05-05    | 9              |
| CUST1001   | 2025-05-02    | 12             |
| CUST1002   | 2025-05-07    | 7              |
| CUST1003   | 2025-04-27    | 17             |
| CUST1004   | 2025-05-11    | 3              |

---



## ✅ Case Study 4: Binning Total Spend into Customer Segments

### 1. **Case Study Name**

**Binning Total Spend into Customer Segments**

---

### 2. **Case Study Description**

Continuous numerical variables like `TotalSpend` can be **binned into categories** to simplify modeling and improve interpretability. In this case, we categorize customers into **Low, Medium, and High** spenders based on their total spending using **quantile-based binning**.

---

### 3. **Solution Approach**

- Use `qcut()` from Pandas to divide the `TotalSpend` variable into **three equally populated segments**: Low, Medium, and High.

- Assign labels to each bin.

- This allows for behavior-based segmentation useful in marketing and customer retention strategies.

---

### 4. **Python Code with Inline Documentation**

```python
import pandas as pd

# Step 1: Use quantile-based binning to split 'TotalSpend' into 3 segments
# 'q=3' means we create 3 bins with equal counts
df['SpendSegment'] = pd.qcut(
    df['TotalSpend'],
    q=3,
    labels=['Low', 'Medium', 'High']
)

# Step 2: Review distribution across the segments
segment_distribution = df['SpendSegment'].value_counts().sort_index()
print("Segment Distribution:\n", segment_distribution)

# Step 3: Preview results
print(df[['CustomerID', 'TotalSpend', 'SpendSegment']].head())
```

---

**🟢 Output Summary:**

- Customers in each segment:
  
  - **Low**: 334
  
  - **Medium**: 333
  
  - **High**: 333

---



## ✅ Case Study 5: Frequency Encoding of Preferred Category

### 1. **Case Study Name**

**Frequency Encoding of Preferred Category**

---

### 2. **Case Study Description**

High-cardinality categorical variables like `PreferredCategory` can create excessive features when one-hot encoded. **Frequency Encoding** is a smart alternative — replacing each category with its **relative frequency** in the dataset. This retains information while reducing dimensionality.

---

### 3. **Solution Approach**

- Compute the **proportion of each category** in the `PreferredCategory` column.

- Map these frequencies back into the dataset to form a new **numerical column** called `PreferredCategory_encoded`.

- This helps simplify model input without losing categorical signal strength.

---

### 4. **Python Code with Inline Documentation**

```python
import pandas as pd

# Step 1: Calculate frequency of each category
category_freq = df['PreferredCategory'].value_counts(normalize=True)

# Step 2: Map frequencies to create a new encoded feature
df['PreferredCategory_encoded'] = df['PreferredCategory'].map(category_freq)

# Step 3: Preview the encoded feature
print(df[['CustomerID', 'PreferredCategory', 'PreferredCategory_encoded']].head())

# Step 4: Optional – display full frequency mapping
print("Category Frequency:\n", category_freq)
```

---

**🟢 Frequency Mapping Example:**

| Category    | Frequency |
| ----------- | --------- |
| Clothing    | 22.6%     |
| Beauty      | 21.3%     |
| Home        | 20.2%     |
| Books       | 18.0%     |
| Electronics | 17.9%     |

---



## ✅ Case Study 6: Extracting Time-based Features from SignUpDate

### 1. **Case Study Name**

**Extracting Time-based Features from SignUpDate**

---

### 2. **Case Study Description**

Time-based behavior analysis is crucial in e-commerce. By **extracting components from datetime fields** like `SignUpDate`, we can uncover patterns related to seasonality, weekday trends, and signup cycles — enabling **targeted marketing** and **lifecycle segmentation**.

---

### 3. **Solution Approach**

- Convert the `SignUpDate` column to a datetime format.

- Derive new features:
  
  - `Signup_Year`: Year of signup
  
  - `Signup_Month`: Month of signup
  
  - `Signup_Weekday`: Day of the week (e.g., Monday, Friday)

- These features are especially useful in **cohort analysis**, **seasonal modeling**, and **customer retention studies**.

---

### 4. **Python Code with Inline Documentation**

```python
import pandas as pd

# Step 1: Convert 'SignUpDate' to proper datetime format
df['SignUpDate'] = pd.to_datetime(df['SignUpDate'])

# Step 2: Extract date components
df['Signup_Year'] = df['SignUpDate'].dt.year         # Extract year
df['Signup_Month'] = df['SignUpDate'].dt.month       # Extract numeric month
df['Signup_Weekday'] = df['SignUpDate'].dt.day_name()# Extract weekday name

# Step 3: Preview new features
print(df[['CustomerID', 'SignUpDate', 'Signup_Year', 'Signup_Month', 'Signup_Weekday']].head())
```

---

**🟢 Output Sample:**

| CustomerID | SignUpDate | Signup_Year | Signup_Month | Signup_Weekday |
| ---------- | ---------- | ----------- | ------------ | -------------- |
| CUST1000   | 2023-08-26 | 2023        | 8            | Saturday       |
| CUST1001   | 2024-11-08 | 2024        | 11           | Friday         |
| CUST1002   | 2023-08-29 | 2023        | 8            | Tuesday        |

---



## ✅ Case Study 7: Log Transformation of Total Spend

### 1. **Case Study Name**

**Log Transformation of Total Spend**

---

### 2. **Case Study Description**

In many business datasets, features like `TotalSpend` are **heavily right-skewed** — most users spend moderately while a few spend disproportionately more. This skewness can distort the model’s learning. A **log transformation** compresses high values and stretches low ones, resulting in a more **normal distribution** that improves many algorithms’ performance.

---

### 3. **Solution Approach**

- Use `np.log1p()` for transformation — which applies log(x + 1) to safely handle **zero values**.

- Create a new column `Log_TotalSpend` that can be used for training instead of the raw `TotalSpend`.

- This technique is particularly beneficial for models sensitive to feature scales, like linear regression or neural networks.

---

### 4. **Python Code with Inline Documentation**

```python
import numpy as np
import pandas as pd

# Step 1: Apply log transformation to reduce skewness
# np.log1p(x) is used instead of np.log(x) to handle zero values safely
df['Log_TotalSpend'] = np.log1p(df['TotalSpend'])

# Step 2: Preview the transformed column
print(df[['CustomerID', 'TotalSpend', 'Log_TotalSpend']].head())
```

---

**🟢 Output Sample:**

| CustomerID | TotalSpend | Log_TotalSpend |
| ---------- | ---------- | -------------- |
| CUST1000   | 18326      | 9.82           |
| CUST1001   | 25481      | 10.15          |
| CUST1002   | 10882      | 9.29           |
| CUST1003   | 4937       | 8.50           |
| CUST1004   | 5935       | 8.69           |

---



## ✅ Case Study 8: Interaction Feature – Spend per Order

### 1. **Case Study Name**

**Interaction Feature: Spend per Order**

---

### 2. **Case Study Description**

Sometimes, combining two features reveals more meaningful patterns than either one alone. In this case, we calculate **average spend per order** by dividing `TotalSpend` by `NoOfOrders`. This derived feature helps measure **customer value** and purchasing behavior with more granularity.

---

### 3. **Solution Approach**

- Create a new feature `SpendPerOrder` by dividing `TotalSpend` by `NoOfOrders`.

- Handle edge cases like **zero orders** to avoid division errors by replacing 0s with `NaN`, then filling them as needed.

- This feature helps in understanding the **average ticket size** of each customer.

---

### 4. **Python Code with Inline Documentation**

```python
import pandas as pd
import numpy as np

# Step 1: Compute SpendPerOrder while handling division by zero
# Replace 0 in NoOfOrders with NaN to avoid division errors
df['SpendPerOrder'] = df['TotalSpend'] / df['NoOfOrders'].replace(0, np.nan)

# Step 2: Optional – Fill resulting NaN values with 0
df['SpendPerOrder'].fillna(0, inplace=True)

# Step 3: Preview the interaction feature
print(df[['CustomerID', 'TotalSpend', 'NoOfOrders', 'SpendPerOrder']].head())
```

---

**🟢 Output Sample:**

| CustomerID | TotalSpend | NoOfOrders | SpendPerOrder |
| ---------- | ---------- | ---------- | ------------- |
| CUST1000   | 18326      | 12         | 1527.17       |
| CUST1001   | 25481      | 12         | 2123.42       |
| CUST1002   | 10882      | 14         | 777.29        |
| CUST1003   | 4937       | 14         | 352.64        |
| CUST1004   | 5935       | 12         | 494.58        |

---



## ✅ Case Study 9: Device and Payment Method Encoding

### 1. **Case Study Name**

**Device and Payment Method Encoding**

---

### 2. **Case Study Description**

To enable machine learning models to understand **categorical features** like `DeviceUsed` and `PaymentMethod`, we must convert these into **numeric formats**. One-Hot Encoding is a robust technique for handling such **multi-class nominal features**.

---

### 3. **Solution Approach**

- Apply **One-Hot Encoding** to the `DeviceUsed` and `PaymentMethod` columns.

- Use the `drop_first=True` option to prevent **multicollinearity** (dummy variable trap).

- The resulting features are binary columns like `DeviceUsed_Mobile`, `PaymentMethod_Wallet`, etc., usable by ML algorithms.

---

### 4. **Python Code with Inline Documentation**

```python
import pandas as pd

# Step 1: Apply One-Hot Encoding
df_encoded = pd.get_dummies(df, columns=['DeviceUsed', 'PaymentMethod'], drop_first=True)

# Step 2: List the encoded column names
encoded_columns = [col for col in df_encoded.columns if 'DeviceUsed_' in col or 'PaymentMethod_' in col]

# Step 3: Preview the encoded features
print(df_encoded[encoded_columns].head())
```

---

**🟢 Output Sample (Encoded Columns):**

| DeviceUsed_Mobile | DeviceUsed_Tablet | PaymentMethod_Credit Card | PaymentMethod_Debit Card | PaymentMethod_Net Banking | PaymentMethod_Wallet |
| ----------------- | ----------------- | ------------------------- | ------------------------ | ------------------------- | -------------------- |
| 0                 | 0                 | 0                         | 0                        | 0                         | 0                    |
| 1                 | 0                 | 0                         | 0                        | 0                         | 0                    |
| 1                 | 0                 | 0                         | 1                        | 0                         | 0                    |

---



## ✅ Case Study 10: Feature Selection Using Correlation Analysis

### 1. **Case Study Name**

**Feature Selection Using Correlation Analysis**

---

### 2. **Case Study Description**

High correlation between input variables can cause **redundancy** and **overfitting** in machine learning models. In this case, we use **correlation analysis** to examine numerical variables and identify **strong relationships** — helping in **feature selection or dimensionality reduction**.

---

### 3. **Solution Approach**

- Extract all **numerical features** from the dataset.

- Use **Pearson correlation** to compute pairwise correlations.

- Visualize relationships using a **heatmap**.

- Highly correlated pairs (e.g., `TotalSpend` and `SpendPerOrder`) can be examined further for potential removal or transformation.

---

### 4. **Python Code with Inline Documentation**

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Select numerical features
numeric_df = df.select_dtypes(include=[np.number])

# Step 2: Compute correlation matrix
correlation_matrix = numeric_df.corr()

# Step 3: Visualize with heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(
    correlation_matrix,
    annot=True,         # Display correlation values
    fmt=".2f",          # Format to 2 decimal places
    cmap="coolwarm",    # Diverging color palette
    square=True,
    linewidths=0.5
)
plt.title("Correlation Matrix for Numeric Features", fontsize=16)
plt.tight_layout()
plt.show()
```

---

**🧠 Insight Example:**

- If `TotalSpend` and `SpendPerOrder` are **highly correlated**, we might **retain only one** for certain models to reduce multicollinearity.

---


