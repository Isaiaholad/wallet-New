from flask import Flask, render_template, request, url_for, redirect
import os
import requests

app = Flask(__name__)
SUI_RPC = os.getenv("SUI_RPC", "https://fullnode.devnet.sui.io")

def get_balance(address):
    try:
        resp = requests.post(
            SUI_RPC,
            json={
                "jsonrpc": "2.0",
                "id": 1,
                "method": "sui_getBalance",
                "params": [address],
            },
            timeout=10,
        )
        resp.raise_for_status()
        data = resp.json()
        return data.get("result", {}).get("totalBalance")
    except Exception:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    address = request.form.get("address")
    balance = None
    error = None

    if address:
        balance = get_balance(address)
        if balance is None:
            error = "Unable to retrieve balance"

    if request.method == "POST" and "recipient" in request.form:
        # placeholder for transaction call
        pass

    return render_template(
        "index.html", address=address, balance=balance, error=error
    )

if __name__ == "__main__":
    app.run(debug=True)
