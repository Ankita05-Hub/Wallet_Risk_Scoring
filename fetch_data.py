import requests

SUBGRAPH_URL = "https://api.thegraph.com/subgraphs/name/graphprotocol/compound-v2"

def fetch_account_activity(wallet_address):
    query = f"""
    {{
      account(id: "{wallet_address.lower()}") {{
        id
        tokens {{
          symbol
          supplyBalanceUnderlying
          borrowBalanceUnderlying
        }}
        tokenTransactions(orderBy: blockTimestamp, orderDirection: desc, first: 1000) {{
          __typename
          id
          amount
          blockTimestamp
          underlyingSymbol
        }}
      }}
    }}
    """
    response = requests.post(SUBGRAPH_URL, json={'query': query})
    data = response.json()
    return data.get('data', {}).get('account', None)