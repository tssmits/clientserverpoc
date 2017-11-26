#!/usr/bin/env python
from flask import Flask, session

app = Flask(__name__)

wallet = 0.0

@app.route('/price', methods=['GET'])
def get_price():
    return "{}".format(1.0)

@app.route('/wallet', methods=['GET'])
def get_wallet():
    return "{}".format(wallet)

@app.route('/buy', methods=['POST'])
def buy(qty):
    global wallet
    wallet += 1.0
    return "ok. New wallet value: {}".format(wallet)

@app.route('/buy/<qty>', methods=['POST'])
def buy_qty(qty):
    global wallet
    wallet += float(qty)
    return "ok. New wallet value: {}".format(wallet)

@app.route('/sell', methods=['POST'])
def sell():
    global wallet
    wallet -= 1
    return "ok. New wallet value: {}".format(wallet)

if __name__ == '__main__':
    app.run(debug=True)
