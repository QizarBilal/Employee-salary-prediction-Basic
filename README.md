# 🧑‍💼 Employee Salary Prediction App

A full-stack Machine Learning project to predict whether a person's salary is >$50K or <=$50K based on demographic and work-related attributes. Built using **Python, Flask, React, and Scikit-learn**.

## 🚀 Features

- ML model trained using the [Adult Income Dataset](https://archive.ics.uci.edu/ml/datasets/adult) or using a similar dataset in this project
- Flask API backend for prediction
- React frontend with dark/light theme toggle
- Dynamic form with responsive layout
- Real-time predictions via API calls

## 🛠️ Tech Stack

### Frontend:
- React + Vite
- TailwindCSS (with custom CSS variables)
- Theme toggle (Dark/Light)

### Backend:
- Python Flask
- Scikit-learn
- Pandas
- Joblib for model serialization

### ML Pipeline:
- Data preprocessing
- Label encoding for categorical features
- Model training with Logistic Regression / Random Forest (customizable)
- Model export as `salary_model.pkl`

---

## 📁 Folder Structure

employee-salary-prediction/
├── backend/
│ ├── app.py # Flask API
│ ├── model/ # Saved model + encoders
│ └── pipeline/
│ └── train_model.py # Training script
├── frontend/
│ ├── src/
│ │ ├── Form.jsx
│ │ ├── Result.jsx
│ │ ├── App.jsx
│ │ └── main.jsx
│ └── index.html
├── README.md
└── requirements.txt
