from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import json

input_file = "../data/clean_data/data.csv"

df = pd.read_csv(input_file, header=None, sep=",,,", engine='python')

inquiry_data = []
decision_data = []

for i in range(len(df)):
    row = df.iloc[i].tolist()
    if len(row) == 2:
        decision = row[1]
        inquiry = row[0]

        inquiry_data.append(inquiry)
        decision_data.append(decision)

data = pd.DataFrame({
    "Inquiry": inquiry_data,
    "Decision": decision_data
})

# convert Y/N to 1 & 0 in dataset
data['Decision'] = data['Decision'].str.strip().str.upper()
data['Decision'] = data['Decision'].map({'Y': 1, 'N': 0})
data['Decision'].fillna(-1, inplace=True)

vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))

X = vectorizer.fit_transform(data["Inquiry"].values.astype('U'))
y = data["Decision"]

# print(y)
# Split the data into training and testing data (80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the model on a data (model=LogisticRegression)
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate the performance of the model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

app = Flask(__name__)
CORS(app)

@app.route('/', methods=["GET"])
def hello_world():
    return render_template('index.html')

@app.route('/inquiry', methods=["POST"])
def predict():
    try:
        data = request.json
        inquiry = f"{data.get('Inquiry')}"

        # Write to file
        with open("./inquiries/inquiries.txt", "a") as f:
            f.write(f"{inquiry}\n")

        # Process with ML model
        X_new = vectorizer.transform([inquiry])
        prediction = model.predict(X_new)

        classification = "HOSS issue, refer to the main line" if prediction < 1 else "Approved, send meeting link"
        print(classification)

        # Return JSON instead of HTML
        return jsonify({
            'status': 'success',
            'classification': classification,
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(port=8080, debug=True)