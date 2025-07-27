import pandas as pd

def load_wallets(file_path):
    df = pd.read_csv(file_path)
    wallets = df['wallet_address'].dropna().unique().tolist()
    return wallets