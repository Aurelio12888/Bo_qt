from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from indicators import calculate_indicators
from strategies import run_strategies
from model.predictor import predict_with_lstm

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    candles = pd.DataFrame(data['candles'])
    email = data.get("email")
    user_id = data.get("user_id")
    asset = data.get("asset")

    try:
        df = calculate_indicators(candles)
        strategy_result = run_strategies(df)
        lstm_result = predict_with_lstm(df)

        return jsonify({
            "asset": asset,
            "email": email,
            "user_id": user_id,
            "signal": "CALL" if lstm_result == 1 else "PUT",
            "strategies": strategy_result
        })
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
