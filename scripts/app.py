from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Laden des Modells
model = joblib.load('/Users/userlow/Documents/kreditkarte_aufgabe/models/basis_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame(data, index=[0])
    prediction = model.predict(df)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)