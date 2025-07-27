from load_wallets import load_wallets
from fetch_data import fetch_account_activity
from feature_engineering import extract_features
from score_model import compute_scores
import pandas as pd
import time

wallets = load_wallets("wallet.csv")

features = []
for wallet in wallets:
    print(f"Fetching: {wallet}")
    account = fetch_account_activity(wallet)
    if account:
        features.append(extract_features(account))
    time.sleep(0.5)

df_features = pd.DataFrame(features)
df_scores = compute_scores(df_features)

df_scores.to_csv("wallet_risk_scores.csv", index=False)
print("✅ Risk scoring complete. Output saved to wallet_risk_scores.csv")