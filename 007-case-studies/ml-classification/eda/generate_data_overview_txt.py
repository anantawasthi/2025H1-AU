import pandas as pd
import numpy as np
from collections import Counter

# Load data
file_path = "synthetic_classification_dataset.csv"
df = pd.read_csv(file_path)

# Data overview
n_rows, n_cols = df.shape
col_names = df.columns.tolist()
dtypes = df.dtypes.astype(str).to_dict()
missing_count = df.isnull().sum().to_dict()
missing_pct = (df.isnull().mean() * 100).round(2).to_dict()
unique_vals = {col: df[col].nunique() for col in df.columns}
describe = df.describe(include='all').T

with open("eda/data_overview.txt", "w", encoding="utf-8") as f:
    f.write(f"Number of rows: {n_rows}\n")
    f.write(f"Number of columns: {n_cols}\n\n")
    f.write("Column Details:\n")
    f.write(f"{'Column Name':20} {'Data Type':10} {'Missing (Count)':15} {'Missing (%)':12} {'Unique':8} {'Sample/Stats'}\n")
    for col in col_names:
        if col in describe.index:
            stats = describe.loc[col]
            if dtypes[col] in ['int64', 'float64']:
                stat_str = f"mean={stats['mean']:.2f}, std={stats['std']:.2f}, min={stats['min']}, max={stats['max']}"
            else:
                stat_str = f"top={stats['top']}, freq={stats['freq']}"
        else:
            stat_str = str(df[col].unique()[:3])
        f.write(f"{col:20} {dtypes[col]:10} {missing_count[col]:15} {missing_pct[col]:12} {unique_vals[col]:8} {stat_str}\n")
print("TXT report saved as eda/data_overview.txt")
