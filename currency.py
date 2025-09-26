# app.py
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    url = "https://api.currencyapi.com/v3/latest?apikey=cur_live_xDJIahtAIeCeYI96swfOSBAF1gax8tVhlOVABilc"
    response = requests.get(url)
    tjs_value = "Не удалось загрузить"

    if response.status_code == 200:
        data = response.json()
        tjs_value = round(data['data']['TJS']['value'], 3)

    return render_template('index.html', tjs_value=tjs_value)

if __name__ == "__main__":
    app.run(debug=True)
