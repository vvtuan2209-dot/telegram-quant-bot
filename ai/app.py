from flask import Flask, jsonify
import random

from markov import build, predict
from monte_carlo import simulate, top_pick
from backtest import run

app = Flask(__name__)


def load_data():
    import json
    with open("../data/history.json") as f:
        return json.load(f)


@app.route("/predict/<region>", methods=["POST"])
def predict_all(region):

    data = load_data()

    markov_model = build(data)
    markov = predict(markov_model)

    # giả lập XGBoost output nhẹ
    xgb = {str(i).zfill(2): random.random() for i in range(100)}

    combined = {}

    for k in markov:
        combined[k] = 0.65*xgb[k] + 0.35*markov[k]

    mc = simulate(combined, runs=100000)

    top2 = top_pick(mc)

    top3 = str(int(top2[0]) * 11 % 1000).zfill(3)

    return jsonify({
        "region": region,
        "top_2digit": {
            "num": top2[0],
            "score": top2[1]
        },
        "top_3digit": {
            "num": top3,
            "score": top2[1]*0.9
        },
        "backtest": run()
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
