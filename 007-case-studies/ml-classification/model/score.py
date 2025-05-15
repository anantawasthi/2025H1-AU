import pandas as pd
import joblib
import sys
import os

# Load model and pipeline
model_path = os.path.join(os.path.dirname(__file__), 'final_model.pkl')
pipeline_path = os.path.join(os.path.dirname(__file__), '../model/fe_pipeline.joblib')
model = joblib.load(model_path)
fe_pipeline = joblib.load(pipeline_path)

# Helper: preprocess input
def preprocess_input(input_df):
    num_cols = fe_pipeline['num_cols']
    cat_cols = fe_pipeline['cat_cols']
    scaler = fe_pipeline['scaler']
    encoders = fe_pipeline['encoders']
    # Impute missing
    input_df[num_cols] = input_df[num_cols].fillna(input_df[num_cols].median())
    input_df[cat_cols] = input_df[cat_cols].fillna(input_df[cat_cols].mode().iloc[0])
    # Outlier clip
    for col in num_cols:
        lower, upper = input_df[col].quantile(0.01), input_df[col].quantile(0.99)
        input_df[col] = input_df[col].clip(lower, upper)
    # Encode categoricals
    for col in cat_cols:
        if col in encoders:
            enc = encoders[col]
            if hasattr(enc, 'transform') and hasattr(enc, 'classes_'):
                input_df[col] = enc.transform(input_df[col])
            elif hasattr(enc, 'transform'):
                ohe_arr = enc.transform(input_df[[col]])
                ohe_cols = [f"{col}_{cat}" for cat in enc.categories_[0][1:]]
                for i, ohe_col in enumerate(ohe_cols):
                    input_df[ohe_col] = ohe_arr[:, i]
                input_df.drop(columns=[col], inplace=True)
    # Scale numerics
    input_df[num_cols] = scaler.transform(input_df[num_cols])
    # New feature
    input_df['Spend_per_Year'] = input_df['Monthly_Spend'] / (input_df['Tenure_Years'] + 1)
    return input_df

def score(input_csv):
    df = pd.read_csv(input_csv)
    X = preprocess_input(df.copy())
    preds = model.predict(X.drop(['Customer_ID'], axis=1, errors='ignore'))
    df['Churn_Prediction'] = preds
    print(df[['Customer_ID', 'Churn_Prediction']])
    return df[['Customer_ID', 'Churn_Prediction']]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python score.py <input_csv>")
        sys.exit(1)
    score(sys.argv[1])
