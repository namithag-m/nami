import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

data = pd.read_csv("transactions.csv")

X = data[["amount","time"]]   # features
y = data["is_fraud"]

model = LogisticRegression()
model.fit(X,y)

joblib.dump(model, "fraud_model.pkl")

print("MODEL SAVED SUCCESSFULLY")