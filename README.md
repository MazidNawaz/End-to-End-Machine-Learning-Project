# 🧠 Machine Learning End-to-End Project (Flask + AWS)

This repository contains a complete **Machine Learning Project** built from **data ingestion to model deployment**.  
The project includes data preprocessing, model training, exception handling, and deployment using a **Flask web application** hosted on **AWS EC2**.

---

## 🚀 Project Overview

This project demonstrates the full lifecycle of a machine learning system:

1. **Data Ingestion** – Load and split data for training/testing.  
2. **Data Transformation** – Clean, encode, and scale data.  
3. **Model Training** – Train multiple algorithms and save the best one.  
4. **Model Evaluation** – Measure accuracy, F1-score, or RMSE.  
5. **Logging & Exception Handling** – Ensure the pipeline is traceable and reliable.  
6. **Flask Web App** – Serve model predictions via a user-friendly interface.  
7. **AWS Deployment** – Host the app on AWS EC2 for real-world access.

---

## 🗂️ Project Structure


---

## ⚙️ Installation & Local Setup

Follow these steps to run the project locally:

```bash
# Clone the repository
git clone https://github.com/yourusername/machine-learning-flask-aws.git

# Navigate to the directory
cd machine-learning-flask-aws

# Create a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate     # For Windows
source venv/bin/activate  # For macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py

│
├── static/ # CSS, JS, and image files
├── app.py # Main Flask web application
├── model.pkl # Final trained model
├── requirements.txt # Dependencies list
├── setup.py # (optional) Package setup
├── README.md # Project documentation (you’re here)
└── .gitignore # Ignore unnecessary files
