import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def compute_scores(df):
    features_to_scale = ['num_transactions', 'supply_count', 'borrow_count', 'repay_count', 'liquidation_count']
    
    scaler = MinMaxScaler()
    df_scaled = df.copy()
    df_scaled[features_to_scale] = scaler.fit_transform(df[features_to_scale])
    
    df_scaled['score'] = (
        df_scaled['supply_count'] * 0.3 +
        df_scaled['borrow_count'] * 0.2 +
        df_scaled['repay_count'] * 0.2 +
        df_scaled['num_transactions'] * 0.2 -
        df_scaled['liquidation_count'] * 0.1
    )
    
    df_scaled['score'] = (df_scaled['score'] * 1000).clip(0, 1000).round().astype(int)
    return df_scaled[['wallet', 'score']]