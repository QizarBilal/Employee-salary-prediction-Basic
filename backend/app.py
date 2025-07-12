from flask_cors import CORS
from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
import os

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "*"}})

# Load model and encoders
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "salary_model.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "model", "label_encoders.pkl")

model = joblib.load(MODEL_PATH)
label_encoders = joblib.load(ENCODER_PATH)

# Expected input fields (snake_case format used in training)
expected_fields = [
    'age', 'workclass', 'fnlwgt', 'education', 'educational-num',
    'marital_status', 'occupation', 'relationship', 'race', 'gender',
    'capital_gain', 'capital_loss', 'hours_per_week', 'native_country'
]

@app.route('/')
def index():
    return jsonify({"message": "Employee Salary Prediction API is running."})

@app.route('/predict', methods=['POST'])
def predict_salary():
    data = request.json
    print("📨 Received:", data)

    # Rename keys to match training schema
    key_map = {
        'education-num': 'educational-num',
        'marital-status': 'marital_status',
        'capital-gain': 'capital_gain',
        'capital-loss': 'capital_loss',
        'hours-per-week': 'hours_per_week',
        'native-country': 'native_country',
        'sex': 'gender'
    }
    for old_key, new_key in key_map.items():
        if old_key in data:
            data[new_key] = data.pop(old_key)

    print("✅ Keys after renaming:", list(data.keys()))

    # Validate required fields
    missing_fields = [field for field in expected_fields if field not in data]
    print("🧩 Missing fields:", missing_fields)
    if missing_fields:
        return jsonify({"error": f"Missing required fields: {missing_fields}"}), 400

    try:
        # Cast numerics
        for field in ['age', 'fnlwgt', 'educational-num', 'capital_gain', 'capital_loss', 'hours_per_week']:
            data[field] = int(data[field])

        input_df = pd.DataFrame([data])
        print("📊 Input DataFrame:", input_df.to_dict(), flush=True)

        # Encode categorical features
        for column in input_df.select_dtypes(include='object').columns:
            le = label_encoders.get(column)
            if le:
                print(f"🎯 Encoding column: {column}")
                input_df[column] = le.transform(input_df[column])
            else:
                print(f"⚠️ No encoder for: {column}")
                return jsonify({"error": f"Missing label encoder for '{column}'"}), 500

        # Predict
        input_df = input_df[expected_fields]
        prediction = model.predict(input_df)[0]
        result = ">50K" if prediction == 1 else "<=50K"
        print("✅ Prediction:", result)
        return jsonify({"prediction": result})

    except Exception as e:
        print("❌ Prediction error:", str(e))
        return jsonify({"error": str(e)}), 500

# Auto-train if models not found
if not os.path.exists(MODEL_PATH) or not os.path.exists(ENCODER_PATH):
    print("Model not found. Running training script...")
    import pipeline.train_model

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
