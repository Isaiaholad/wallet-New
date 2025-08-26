# Flask Wallet

A minimal Flask replica of the Suiet wallet. It lets you look up Sui balances and provides a placeholder form for sending tokens.

## Setup

```bash
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

Set `SUI_RPC` to point at a custom Sui JSON-RPC endpoint if desired:

```bash
export SUI_RPC=https://fullnode.testnet.sui.io
```
