"""
The file initializes flask and contains all the required paths or api-routes.
To run the server locally- Run
..\cryptocoins\python app.py
"""
## Import Statements
from flask import Flask, render_template, redirect, url_for
from src.scraper import get_cryptocurrency_list

app = Flask(__name__)

## base route - Redirects to /cryptocurrency-list.
@app.route("/")
def base_function():
    return redirect(url_for("get_home_crypto_list"))

## route for list of top-12 cryptocurrencies by MCAP.
@app.route("/cryptocurrency-list")
def get_home_crypto_list():
    crypto_lists = get_cryptocurrency_list()
    return render_template("home.html", crypto_list=crypto_lists)

if __name__ == "__main__":
    app.run()
