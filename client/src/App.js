import './App.css';
import { 
  BrowserRouter as Router,
  Switch,
  Route
} from'react-router-dom';
import NavBar from './components/navbar';
import HomePage from './components/home';
import SignUpPage from './components/signup';
import LoginPage from './components/login';
import CreateRecipePage from './components/createRecipe';

function App() {

  return (
    <Router>
    <NavBar />
    <Switch>
      <Route path="/signup">
        <SignUpPage />
      </Route>
      <Route path="/login">
        <LoginPage />
      </Route>
      <Route path="/home">
        <HomePage />
      </Route>
      <Route path="/createRecipe">
        <CreateRecipePage />
      </Route>

    </Switch>
    </Router>
  )
    
    
}

export default App;
