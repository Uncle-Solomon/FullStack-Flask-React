import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';
import { 
  BrowserRouter as Router,
  Switch,
  Route
} from'react-router-dom';
import NavBar from './components/navbar';

function App() {

  return (
    <Router>
    <NavBar />
    <Switch>

    </Switch>
    </Router>
  )
    
    
}

export default App;
