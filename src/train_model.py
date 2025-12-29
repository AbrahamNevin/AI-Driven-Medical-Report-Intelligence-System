from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from src.feature_engineering import load_feature_dataframe


def train():
    df = load_feature_dataframe()

    X = df[["num_conditions", "num_symptoms", "num_risk_indicators"]]
    y = df["high_risk"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    print(classification_report(y_test, preds))


if __name__ == "__main__":
    train()
