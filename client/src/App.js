import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';

function App() {

  useEffect(
    () => {
      fetch('/recipe/hello')
      .then(response => response.json())
      .then(data=>{
        console.log(data)
        setMessage(data.message)
      })
      .catch(err=>console.log(err))
    },
    []
  )
  const [message, setMessage] = useState('')
  return (
    <div className="App">
      {message}
    </div>
  );
}

export default App;
