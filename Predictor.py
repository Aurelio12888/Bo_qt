import numpy as np
import joblib

model = joblib.load("backend/model/lstm_model.joblib")

def predict_with_lstm(df):
    seq = df[['rsi', 'macd', 'ema']].values[-20:]
    seq = np.expand_dims(seq, axis=0)
    return int(model.predict(seq)[0][0] > 0.5)
