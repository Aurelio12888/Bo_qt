import React, { useState } from 'react';

export default function SignalForm({ onSubmit }) {
  const [email, setEmail] = useState('');
  const [userId, setUserId] = useState('');
  const [asset, setAsset] = useState('EUR/USD');
  const [candles, setCandles] = useState([]);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ email, user_id: userId, asset, candles });
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-2">
      <input placeholder="Email da Quotex" value={email} onChange={e => setEmail(e.target.value)} className="border p-2 w-full" />
      <input placeholder="ID da Quotex" value={userId} onChange={e => setUserId(e.target.value)} className="border p-2 w-full" />
      <input placeholder="Ativo (ex: EUR/USD)" value={asset} onChange={e => setAsset(e.target.value)} className="border p-2 w-full" />
      <textarea placeholder="Cole aqui os candles JSON" onChange={e => setCandles(JSON.parse(e.target.value))} className="border p-2 w-full" />
      <button type="submit" className="bg-green-500 text-white p-2 rounded">Enviar</button>
    </form>
  );
}
