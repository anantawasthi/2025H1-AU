import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('feature-engineering/processed_data.csv')

target = 'Customer_Churn'
train, test = train_test_split(df, test_size=0.2, random_state=42, stratify=df[target])
train.to_csv('model-data/train.csv', index=False)
test.to_csv('model-data/test.csv', index=False)
print('Train and test sets saved to model-data/.')
