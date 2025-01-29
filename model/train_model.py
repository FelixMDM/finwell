import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib

# Load and preprocess data
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

# Convert Y/N to 1 & 0 in dataset
data['Decision'] = data['Decision'].str.strip().str.upper()
data['Decision'] = data['Decision'].map({'Y': 1, 'N': 0})
data['Decision'].fillna(-1, inplace=True)

# Vectorize text data
vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
X = vectorizer.fit_transform(data["Inquiry"].values.astype('U'))
y = data["Decision"]

# Split data and train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Serialize model and vectorizer
joblib.dump(model, 'model.joblib')
joblib.dump(vectorizer, 'vectorizer.joblib')

print("Model and vectorizer serialized successfully!")