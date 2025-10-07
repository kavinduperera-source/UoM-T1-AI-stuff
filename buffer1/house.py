# house_price_predictor.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

def train_model(data_path="Housing.csv"):
    """Train the regression model and save it."""
    # Load data
    df = pd.read_csv(data_path)

    # One-hot encode categorical columns
    df_encoded = pd.get_dummies(df, drop_first=True)

    # Split features and target
    X = df_encoded.drop("price", axis=1)
    y = df_encoded["price"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = mean_squared_error(y_test, y_pred) ** 0.5
    r2 = r2_score(y_test, y_pred)

    print("Model Performance:")
    print(f"MAE  : {mae:,.2f}")
    print(f"RMSE : {rmse:,.2f}")
    print(f"R²   : {r2:.3f}")

    # Save model and columns
    joblib.dump(model, "house_price_model.pkl")
    joblib.dump(X.columns, "model_columns.pkl")
    print("\n✅ Model saved as 'house_price_model.pkl'")

def predict_price(input_data):
    """Predict house price for a given input dictionary."""
    # Load model and columns
    model = joblib.load("house_price_model.pkl")
    columns = joblib.load("model_columns.pkl")

    # Convert input dictionary to DataFrame
    df_input = pd.DataFrame([input_data])

    # One-hot encode and align columns
    df_input_encoded = pd.get_dummies(df_input)
    df_input_encoded = df_input_encoded.reindex(columns=columns, fill_value=0)

    # Predict
    predicted_price = model.predict(df_input_encoded)[0]
    return predicted_price


if __name__ == "_main_":
    # Example usage
    train_model("Housing.csv")

    sample_house = {
        "area": 4000,
        "bedrooms": 3,
        "bathrooms": 2,
        "stories": 2,
        "mainroad": "yes",
        "guestroom": "no",
        "basement": "no",
        "hotwaterheating": "no",
        "airconditioning": "yes",
        "parking": 1,
        "prefarea": "no",
        "furnishingstatus": "semi-furnished",
    }

    predicted = predict_price(sample_house)
    print(f"\n💰 Predicted House Price: ₹{predicted:,.2f}")

