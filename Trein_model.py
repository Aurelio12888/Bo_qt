# training/train_model.py
import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
import joblib
import os

# Gerar dados simulados
n = 500
df = pd.DataFrame({
    'rsi': np.random.uniform(10, 90, n),
    'macd': np.random.uniform(-2, 2, n),
    'ema': np.random.uniform(1.1, 1.5, n),
    'target': np.random.randint(0, 2, n)
})

# Normalizar
scaler = MinMaxScaler()
X = scaler.fit_transform(df[['rsi', 'macd', 'ema']])
y = df['target'].values

# Criar sequências
X_seq = []
y_seq = []
seq_len = 20
for i in range(len(X) - seq_len):
    X_seq.append(X[i:i+seq_len])
    y_seq.append(y[i+seq_len])

X_seq = np.array(X_seq)
y_seq = np.array(y_seq)

# Criar modelo LSTM
model = Sequential([
    LSTM(32, input_shape=(seq_len, 3)),
    Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_seq, y_seq, epochs=10, verbose=1)

# Salvar modelo
os.makedirs("backend/model", exist_ok=True)
joblib.dump(model, "backend/model/lstm_model.joblib")
