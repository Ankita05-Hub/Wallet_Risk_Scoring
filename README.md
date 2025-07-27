# 💼 Wallet Risk Scoring using Aave V2 Data

This project implements a **Wallet Risk Scoring System** that analyzes historical on-chain activity from Aave V2 to assign a **risk score between 0 and 1000** to each wallet. The goal is to help DeFi platforms assess wallet creditworthiness and risk for potential lending, borrowing, or flagging suspicious activity.

---

## 🚀 Project Overview

🔍 **Objective**:  
To analyze 100K+ transaction-level data records from Aave V2 and generate a normalized risk score per wallet.

📊 **Output**:  
A `wallet_risk_scores.csv` file with two columns:
- `wallet_id`: Ethereum wallet address
- `score`: Risk score between 0 (very risky) to 1000 (low risk)

---

## 🧠 Methodology

1. **Data Source**:  
   Pulled on-chain transaction data using The Graph API from Aave V2 subgraph.

2. **Feature Engineering**:
   - Number of borrows and repayments
   - Total borrowed and repaid amounts
   - Repay-to-borrow ratio
   - Days since last transaction
   - Borrowing diversity (tokens used)

3. **Scoring Model**:  
   Used a simple rule-based scoring mechanism combining normalized features. Future plans include replacing it with ML models (e.g., Random Forest, XGBoost).

4. **Data Visualization**:  
   Plotted score distribution to analyze credit risk spread.

---

## 🛠️ Tech Stack

- Python 🐍
- Pandas & NumPy
- Matplotlib / Seaborn
- GitHub + Git LFS (for large data files)
- The Graph (Subgraph API)

---

## 📂 Project Structure
WalletRiskScoring/
├── data/ # Raw or processed CSVs
├── notebooks/ # Jupyter notebooks for analysis
├── src/ # Python scripts (feature_engineering.py, score_model.py, etc.)
├── analysis_plot.py # Visualization script
├── wallet_risk_scores.csv # Final output
├── requirements.txt
└── README.md


