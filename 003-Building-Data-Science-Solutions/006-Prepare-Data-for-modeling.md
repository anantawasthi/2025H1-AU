

# 🧪 Dataset Splitting Methods Before Model Building

Splitting your data before training a machine learning model is a **crucial step** to ensure that your model is trained, validated, and tested on the right subsets — allowing you to **measure performance reliably** and avoid overfitting or data leakage.



<img title="" src="file:///C:/Users/anant/Desktop/AU2025/src_images/data-split-methods.png" alt="Data Science as Cooking Analogy" width="700" style="display: block; margin: auto;">

---

## ✅ 1. **Holdout Method (Train-Test Split)**

### 🔹 What It Is:

Split the dataset into **training and testing** sets (commonly 70:30 or 80:20).

### 🔹 Use Case:

Quick baseline models, large datasets.

### 🔹 Pros:

- Simple and fast.

- Easy to implement.

### 🔹 Cons:

- Performance is **dependent on a single random split**.

- Not ideal for small datasets — may cause high variance in results.

- Doesn’t account for time-based or class imbalance issues.

---

## ✅ 2. **Train–Validation–Test Split**

### 🔹 What It Is:

Split data into **three sets**: training (~60%), validation (~20%), and test (~20%).

### 🔹 Use Case:

When tuning hyperparameters or selecting models.

### 🔹 Pros:

- Enables **model selection** and **hyperparameter tuning**.

- Final test set remains untouched until the end.

### 🔹 Cons:

- Further reduces training data, especially problematic with small datasets.

- Requires careful separation to prevent **data leakage**.

---

## ✅ 3. **K-Fold Cross-Validation**

### 🔹 What It Is:

Divide the data into **K equal parts (folds)**. Train on K-1 folds and validate on the remaining one. Repeat K times.

### 🔹 Use Case:

Reliable model evaluation, especially for small/medium datasets.

### 🔹 Pros:

- **Robust and reliable**; model is validated on multiple splits.

- Every sample is used for both training and validation.

### 🔹 Cons:

- Computationally **expensive**.

- Not ideal for time-series data (violates temporal structure).

---

## ✅ 4. **Stratified K-Fold Cross-Validation**

### 🔹 What It Is:

Same as K-Fold, but ensures that each fold preserves the **class distribution** (important for imbalanced classification).

### 🔹 Use Case:

Classification problems with **imbalanced classes**.

### 🔹 Pros:

- Better for skewed datasets.

- Avoids training on unbalanced folds.

### 🔹 Cons:

- Only applicable to classification.

- Still computationally heavier than a simple holdout split.

---

## ✅ 5. **Leave-One-Out Cross-Validation (LOOCV)**

### 🔹 What It Is:

Each sample is used as a test set once, and the rest for training.

### 🔹 Use Case:

Small datasets (e.g., medical or rare-event data).

### 🔹 Pros:

- Uses almost all data for training in each iteration.

- Maximum usage of data.

### 🔹 Cons:

- **Extremely slow** for large datasets.

- Can result in **high variance** in evaluation scores.

---

## ✅ 6. **Time Series Split (Rolling or Expanding Window)**

### 🔹 What It Is:

Train-test split that **respects chronological order** of the data (no shuffling!).

### 🔹 Types:

- **Rolling window**: keep size fixed, shift both start and end.

- **Expanding window**: keep start fixed, extend the end.

### 🔹 Use Case:

Forecasting, financial data, any **temporal sequence**.

### 🔹 Pros:

- Respects time-based data structure.

- Prevents future data leakage.

### 🔹 Cons:

- Can’t shuffle data.

- Imbalanced splits if not done properly.

- May require manual configuration of window sizes.

---

## ✅ 7. **Group K-Fold / Group Shuffle Split**

### 🔹 What It Is:

Splits data by **grouping** (e.g., all entries from a user or session go into one fold).

### 🔹 Use Case:

Data where **rows are not independent**, e.g., user logs, session data.

### 🔹 Pros:

- Prevents data leakage when groups are correlated.

- Ensures **group-level generalization**.

### 🔹 Cons:

- Requires a meaningful group key.

- May create unbalanced splits depending on group sizes.

---

## ✅ 8. **Nested Cross-Validation**

### 🔹 What It Is:

An outer CV loop for **model evaluation** and an inner CV loop for **hyperparameter tuning**.

### 🔹 Use Case:

Rigorous model benchmarking, particularly in **research or competitions**.

### 🔹 Pros:

- Avoids overfitting in hyperparameter tuning.

- Provides **unbiased estimate** of model performance.

### 🔹 Cons:

- **Very computationally intensive**.

- Difficult to implement in production workflows.

---

## 🧠 Summary Comparison Table

| Method                | Ideal For                         | Pros                             | Cons                            |
| --------------------- | --------------------------------- | -------------------------------- | ------------------------------- |
| Holdout               | Large datasets, baseline models   | Simple, quick                    | May be unstable                 |
| Train-Validation-Test | Model selection + final eval      | Easy tuning and test separation  | Less data for training          |
| K-Fold CV             | Medium datasets                   | More robust, multiple validation | Slow, can overfit on validation |
| Stratified K-Fold     | Imbalanced classification         | Keeps class balance              | Classification only             |
| Leave-One-Out         | Very small datasets               | Maximum data usage               | Very slow                       |
| Time Series Split     | Forecasting, temporal models      | Time-aware, avoids leakage       | Needs careful config            |
| Group K-Fold          | Sessions/users/groups             | Prevents group leakage           | Risk of imbalance               |
| Nested CV             | Research-grade performance checks | Unbiased tuning + evaluation     | Very heavy computational load   |

---

## Python Implementation

[Dataset Preperation](006-Prepare-Data-for-modeling.py)
