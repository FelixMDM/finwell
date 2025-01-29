from flask import Flask, jsonify, request
from flask_cors import CORS
import joblib
import os 

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "https://finwellml-frontend.onrender.com"]}})

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model.joblib')
VECTORIZER_PATH = os.path.join(BASE_DIR, 'vectorizer.joblib')

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

@app.route('/', methods=["GET"])
def hello_world():
    return "Flask backend is running!"

@app.route('/inquiry', methods=["POST"])
def predict():
    try:
        data = request.json
        inquiry = f"{data.get('Inquiry')}"

        # Write to file (optional)
        with open("./inquiries/inquiries.txt", "a") as f:
            f.write(f"{inquiry}\n")

        # Process with ML model
        X_new = vectorizer.transform([inquiry])
        prediction = model.predict(X_new)

        classification = "HOSS issue, refer to the main line" if prediction < 1 else "Approved, send meeting link"
        print(classification)

        # Return JSON response
        return jsonify({
            'status': 'error' if prediction < 1 else 'success',
            'classification': classification,
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(port=8080, debug=True)