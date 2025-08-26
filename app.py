from flask import Flask, render_template, request, redirect, url_for
import requests, os

app = Flask(__name__)
SUI_RPC = os.getenv("SUI_RPC", "https://fullnode.devnet.sui.io")

def get_balance(address):
    resp = requests.post(
        SUI_RPC,
        json={"jsonrpc": "2.0", "id": 1, "method": "sui_getBalance", "params": [address]},
    )
    return resp.json()["result"]["totalBalance"]

@app.route("/", methods=["GET", "POST"])
def index():
    address = request.form.get("address")
    balance = get_balance(address) if address else None
    if request.method == "POST" and "recipient" in request.form:
        # placeholder for transaction call
        pass
    return render_template("index.html", address=address, balance=balance)

if __name__ == "__main__":
    app.run(debug=True)
