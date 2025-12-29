from pathlib import Path
import shap
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from src.feature_engineering import load_feature_dataframe



RESULTS_DIR = Path("results/shap_plots")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)


def explain_model():
    # Load data
    df = load_feature_dataframe()


    X = df[["num_conditions", "num_symptoms", "num_risk_indicators"]]
    y = df["high_risk"]

    # Train the same model (baseline)
    model = LogisticRegression()
    model.fit(X, y)

    # Create SHAP explainer (LinearExplainer is stable for LR)
    explainer = shap.LinearExplainer(model, X)
    shap_values = explainer.shap_values(X)

    # Convert to DataFrame for clarity
    shap_df = pd.DataFrame(
        shap_values,
        columns=X.columns
    )

    # Save SHAP summary plot
    plt.figure()
    shap.summary_plot(
        shap_values,
        X,
        show=False
    )
    plt.tight_layout()
    plt.savefig(RESULTS_DIR / "shap_summary.png", dpi=200)
    plt.close()

    print("SHAP explainability generated.")
    print("\nMean absolute SHAP values:")
    print(shap_df.abs().mean().sort_values(ascending=False))


if __name__ == "__main__":
    explain_model()
