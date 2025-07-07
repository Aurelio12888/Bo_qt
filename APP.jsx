import React, { useState } from 'react';
import axios from 'axios';
import SignalForm from './components/SignalForm';

export default function App() {
  const [signal, setSignal] = useState(null);

  const handleSubmit = async (formData) => {
    const res = await axios.post('https://teu-backend-no-render.onrender.com/predict', formData);
    setSignal(res.data);
  };

  return (
    <div className="p-4 font-sans">
      <h1 className="text-2xl font-bold mb-4">BOT IA - Quotex Style</h1>
      <SignalForm onSubmit={handleSubmit} />
      {signal && (
        <div className="mt-4 p-4 bg-gray-100 rounded">
          <p><strong>Sinal:</strong> {signal.signal}</p>
          <p><strong>Ativo:</strong> {signal.asset}</p>
          <p><strong>Estratégias:</strong></p>
          <ul>
            {signal.strategies.map((s, i) => <li key={i}>• {s}</li>)}
          </ul>
        </div>
      )}
    </div>
  );
          }
