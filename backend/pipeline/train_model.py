import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

# 1. Load your dataset
df = pd.read_csv("adult 3.csv")

# 2. Rename columns to match API expectations
df.rename(columns={
    'education-num': 'education_num',
    'marital-status': 'marital_status',
    'capital-gain': 'capital_gain',
    'capital-loss': 'capital_loss',
    'hours-per-week': 'hours_per_week',
    'native-country': 'native_country'
}, inplace=True)

# 3. Drop missing values if any
df.dropna(inplace=True)

# 4. Encode categorical columns
categorical_cols = [
    'workclass', 'education', 'marital_status', 'occupation',
    'relationship', 'race', 'gender', 'native_country'
]

label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le  # 🔁 SAVE EVERY encoder

# 5. Define X and y
X = df.drop('income', axis=1)
y = df['income'].apply(lambda x: 1 if x == '>50K' else 0)

# 6. Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# 7. Save model and encoders
model_dir = "backend/model"
os.makedirs(model_dir, exist_ok=True)

joblib.dump(model, os.path.join(model_dir, "salary_model.pkl"))
joblib.dump(label_encoders, os.path.join(model_dir, "label_encoders.pkl"))

print("✅ Model and encoders saved successfully.")
print(f"🎯 Saved encoders: {list(label_encoders.keys())}")