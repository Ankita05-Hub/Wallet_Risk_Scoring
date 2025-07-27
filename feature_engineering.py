def extract_features(account_data):
    txs = account_data.get("tokenTransactions", [])
    
    num_txs = len(txs)
    borrow_count = sum(1 for tx in txs if tx['__typename'] == 'Borrow')
    supply_count = sum(1 for tx in txs if tx['__typename'] == 'Mint')
    repay_count = sum(1 for tx in txs if tx['__typename'] == 'RepayBorrow')
    liquidation_count = sum(1 for tx in txs if tx['__typename'] == 'Liquidation')

    return {
        "wallet": account_data['id'],
        "num_transactions": num_txs,
        "supply_count": supply_count,
        "borrow_count": borrow_count,
        "repay_count": repay_count,
        "liquidation_count": liquidation_count
    }