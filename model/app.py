from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

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

@app.route('/', methods=["GET"])
def hello_world():
    return render_template('index.html')

@app.route('/', methods=["POST"])
def predict():
    # take in the user request
    inquiry = request.form['Inquiry']
    f = open("./inquiries/inquiries.txt", "a")
    f.write(f"{inquiry}\n")
    X_new = vectorizer.transform([inquiry])
    prediction = model.predict(X_new)

    # pass it up to the ML model to actually take care of our request
    classification = ""
    if prediction < 1:
        classification = "HOSS issue, refer to the main line"
    else:
        classification = "Approved, send meeting link"

    print(classification)
    return render_template('index.html', prediction=classification)

if __name__ == "__main__":
    app.run(port=3000, debug=True)