from flask import Flask, request, jsonify, render_template
from twilio.rest import Client
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("fraud_model.pkl")


# -------- SMS FUNCTION ----------
def send_sms(message):

    account_sid = "sid"
    auth_token = "d"

    client = Client(account_sid, auth_token)

    client.messages.create(
        body=message,
        from_="+1",   # Twilio number
        to="+91xxxx"      # your phone number
    )


# -------- ROUTES ----------

@app.route("/dashboard")
def dashboard():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    amount = float(data["amount"])
    time = int(data["time"])

    # ML prediction
    features = [[amount, time]]
    prediction = model.predict(features)[0]

    if prediction == 1:

        send_sms("⚠️ Fraud Alert! Suspicious transaction detected.")

        return jsonify({
            "prediction": "Fraud",
            "alert": "Fraud detected! SMS sent."
        })

    else:
        return jsonify({
            "prediction": "Safe"
        })


# -------- RUN SERVER ----------
if __name__ == "__main__":
    app.run(debug=True)