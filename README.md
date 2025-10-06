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

📦 machine-learning-flask-aws
│
├── artifacts/ # Intermediate files (data, models, etc.)
├── data/ # Raw and processed datasets
├── logs/ # Auto-generated log files
├── notebooks/ # EDA and experimentation notebooks
│
├── src/
│ ├── components/
│ │ ├── data_ingestion.py # Reads and splits data
│ │ ├── data_transformation.py # Cleans and encodes data
│ │ ├── model_trainer.py # Trains and evaluates models
│ │
│ ├── pipeline/
│ │ ├── training_pipeline.py # Automates full ML workflow
│ │ └── prediction_pipeline.py # Handles predictions for Flask app
│ │
│ ├── exception.py # Custom exception handling class
│ ├── logger.py # Logging configuration
│ └── utils.py # Helper functions
│
├── templates/ # HTML templates for Flask web app
│ ├── index.html
│ └── result.html
│
├── static/ # CSS, JS, and image files
├── app.py # Main Flask web application
├── model.pkl # Final trained model
├── requirements.txt # Dependencies list
├── setup.py # (optional) Package setup
├── README.md # Project documentation (you’re here)
└── .gitignore # Ignore unnecessary files