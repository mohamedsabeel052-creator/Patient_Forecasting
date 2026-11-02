


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error


data = {
    "day": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "admissions": [45, 48, 42, 50, 55, 53, 58, 60, 57, 65]
}

df = pd.DataFrame(data)


X = df[["day"]]
y = df["admissions"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)


predictions = model.predict(X_test)


mae = mean_absolute_error(y_test, predictions)

print("Patient Admission Forecasting")
print("Mean Absolute Error:", mae)


future = pd.DataFrame({"day": [11, 12, 13]})
forecast = model.predict(future)

print("Future Admission Forecast:", forecast)
