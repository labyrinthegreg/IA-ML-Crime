import React, { useState } from 'react';
import styles from './CrimePrediction.module.css';

const districts = [
  "Central", "Northern", "Southern", "Eastern", "Western", "Northeastern", "Southwestern"
];

const CrimePrediction: React.FC = () => {
  const [date, setDate] = useState<string>('');
  const [district, setDistrict] = useState<string>('');
  const [prediction, setPrediction] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const crimeTypes = ["Vol", "Agression", "Cambriolage", "Vandalisme", "Fraude"];
    // Fetch the prediction from the API by post
    const response = await fetch('http://localhost:8000/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ "Dates": date, "PdDistrict": district }),
    });
    const data = await response.json();
    setPrediction(data.prediction);
    // const randomPrediction = crimeTypes[Math.floor(Math.random() * crimeTypes.length)];
    // setPrediction(randomPrediction);
  };

  return (
    <div className={styles.container}>
      <header className={styles.header}>
        <h1>Prédiction de Crime</h1>
        <p>Découvrez quel type de crime pourrait se produire dans votre district</p>
      </header>

      <main className={styles.main}>
        <form onSubmit={handleSubmit} className={styles.form}>
          <div className={styles.inputGroup}>
            <label htmlFor="date">Date :</label>
            <input
              type="date"
              id="date"
              value={date}
              onChange={(e) => setDate(e.target.value)}
              required
            />
          </div>

          <div className={styles.inputGroup}>
            <label htmlFor="district">District :</label>
            <select
              id="district"
              value={district}
              onChange={(e) => setDistrict(e.target.value)}
              required
            >
              <option value="">Sélectionnez un district</option>
              {districts.map((d) => (
                <option key={d} value={d}>{d}</option>
              ))}
            </select>
          </div>

          <button type="submit" className={styles.button}>Prédire</button>
        </form>

        {prediction && (
          <div className={styles.prediction}>
            <h2>Prédiction :</h2>
            <p>Le type de crime prédit pour le {date} dans le district {district} est :</p>
            <h3>{prediction}</h3>
          </div>
        )}
      </main>
    </div>
  );
};

export default CrimePrediction;

