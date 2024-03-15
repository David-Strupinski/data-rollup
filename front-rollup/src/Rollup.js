import React, { useEffect, useState } from 'react';
import './App.css';

export default function RollupList() {
  const [rolled_data, setRollup] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/rolled_values/')
      .then(response => response.json())
      .then(data => setRollup(data))
      .catch(error => console.error('Error:', error));
  }, []);
  
  return (
    <div className='grid-container'>
      {rolled_data.map(payment => (
        <RollupItem
          paytype_id={payment.paytype_id}
          date={payment.date}
          amount={payment.amount}
        />
      ))}
    </div>
  );
}

function RollupItem({paytype_id, date, amount}) {
  return (
    <div className='grid-item'>
      <h2>{date}</h2>
      <p>Payment Type: {paytype_id}</p>
      <p>Total Amount: ${amount}</p>
    </div>
  );
}
