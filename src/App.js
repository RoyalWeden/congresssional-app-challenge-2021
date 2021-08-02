import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [theHello, setTheHello] = useState('no hello');
  const [theDatetime, setTheDatetime] = useState('no datetime');
  const [theTime, setTheTime] = useState('no time');

  useEffect(() => {
    fetch('/api/home').then(res => res.json()).then(data => {
      setTheHello(data['hello']);
    });
  }, []);

  useEffect(() => {
    fetch('/api/time').then(res => res.json()).then(data => {
      setTheDatetime(data['datetime']);
      setTheTime(data['time']);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <p>We say hello like this: {theHello}.</p>
        <p>We say hello like this: {theDatetime}.</p>
        <p>We say hello like this: {theTime}.</p>
      </header>
    </div>
  );
}

export default App;
