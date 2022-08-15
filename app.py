from flask import Flask, render_template
from src.scraper import get_cryptocurrency_list

app = Flask(__name__)

@app.route("/cryptocurrency-list")
def get_home_crypto_list():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
