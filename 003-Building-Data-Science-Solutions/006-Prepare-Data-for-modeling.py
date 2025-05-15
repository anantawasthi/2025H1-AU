"""
Dataset Splitting Methods with Detailed Documentation and Inline Comments
Using a Synthetic Fashion E-commerce Dataset
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import (
    train_test_split, KFold, StratifiedKFold,
    LeaveOneOut, TimeSeriesSplit, GroupKFold
)
import datetime

# Load the prepared Fashion dataset
df = pd.read_csv("fashion_dataset.csv")

# Convert date columns to datetime format
df['LastPurchaseDate'] = pd.to_datetime(df['LastPurchaseDate'])
df['SignupDate'] = pd.to_datetime(df['SignupDate'])

# Generate new engineered features for time-based splits
df['RecencyDays'] = (datetime.datetime.today() - df['LastPurchaseDate']).dt.days

# Assign a group variable (Location used for Group K-Fold)
df['GroupID'] = df['Location']

# Prepare features and target
y = df['Rating']
X = df.drop(columns=['CustomerID', 'Rating', 'LastPurchaseDate', 'SignupDate', 'Location'])

# One-hot encode categorical variables
X = pd.get_dummies(X, drop_first=True)

"""
1. Holdout Method
Split dataset into training and testing (e.g., 80/20 split)
"""
X_train_hold, X_test_hold, y_train_hold, y_test_hold = train_test_split(
    X, y, test_size=0.2, random_state=42
)

"""
2. Train-Validation-Test Split
Split into training (60%), validation (20%), and testing (20%)
"""
X_train_tv, X_temp_tv, y_train_tv, y_temp_tv = train_test_split(
    X, y, test_size=0.4, random_state=42
)
X_val_tv, X_test_tv, y_val_tv, y_test_tv = train_test_split(
    X_temp_tv, y_temp_tv, test_size=0.5, random_state=42
)

"""
3. K-Fold Cross-Validation
Split into k subsets and rotate validation set across folds
"""
kf = KFold(n_splits=5, shuffle=True, random_state=42)
kf_splits = [(train_idx, val_idx) for train_idx, val_idx in kf.split(X)]

"""
4. Stratified K-Fold Cross-Validation
Same as K-Fold but maintains class distribution in target variable
"""
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
skf_splits = [(train_idx, val_idx) for train_idx, val_idx in skf.split(X, y)]

"""
5. Leave-One-Out Cross-Validation (LOOCV)
Each observation used once as test set
"""
loo = LeaveOneOut()
loo_sample = [(train_idx, val_idx) for train_idx, val_idx in loo.split(X)][:5]  # Preview first 5

"""
6. Time Series Split
Maintain order of data while splitting for time-dependent datasets
"""
df_sorted = df.sort_values('LastPurchaseDate')
X_ts = df_sorted.drop(columns=['CustomerID', 'Rating', 'LastPurchaseDate', 'SignupDate', 'Location'])
X_ts = pd.get_dummies(X_ts, drop_first=True)
y_ts = df_sorted['Rating']

# Time-based cross-validation
tscv = TimeSeriesSplit(n_splits=5)
ts_splits = [(train_idx, val_idx) for train_idx, val_idx in tscv.split(X_ts)]

"""
7. Group K-Fold
Ensure that the same group (e.g., customer, session) doesn't appear in both train and test
"""
gkf = GroupKFold(n_splits=5)
groups = df['GroupID']
group_splits = [(train_idx, val_idx) for train_idx, val_idx in gkf.split(X, y, groups=groups)]

"""
Each method is now implemented with index splits stored for model training.
This script is designed for demonstration and can be expanded for benchmarking workflows.
"""
