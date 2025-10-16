from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import os
import sys

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sklearn.preprocessing import StandardScaler

try:
    from src.pipeline.predict_pipeline import CustomData, PredictPipeline
    print("✅ Successfully imported custom modules")
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Current working directory:", os.getcwd())
    print("Python path:", sys.path)

application = Flask(__name__)
app = application

## Route for home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            # Fix: You had reading_score and writing_score swapped
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('reading_score')),  # Fixed
                writing_score=float(request.form.get('writing_score'))   # Fixed
            )
            
            pred_df = data.get_data_as_data_frame()
            print("📊 Prediction DataFrame:")
            print(pred_df)
            
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            
            print(f"🎯 Prediction result: {results[0]}")
            return render_template('home.html', results=results[0])
            
        except Exception as e:
            print(f"❌ Error during prediction: {e}")
            return render_template('home.html', results=f"Error: {str(e)}")

if __name__ == "__main__":
    print("🚀 Starting Flask application...")
    print("📁 Current directory:", os.getcwd())
    print("🌐 Server will be available at http://127.0.0.1:5000")
    
    # Run with explicit configuration
    app.run(
        host="0.0.0.0", 
        port=5000, 
        debug=True,  # Enable debug mode for better error messages
        use_reloader=True
    )