import logo from './logo.svg';
import './bootstrap.min.css';
import react, {Component} from 'react';
import { Outlet, Link } from "react-router-dom";

class App extends Component {
  
  render(){
    return (
    <div className="App">
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
                <div className="container-fluid">
                  <a className="navbar-brand" href="#">Кофе в Петербурге</a>
                  <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarColor02" aria-controls="navbarColor02" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                  </button>

                  <div className="collapse navbar-collapse" id="navbarColor02">
                    <ul className="navbar-nav me-auto">
                      <li className="nav-item">
                        <Link className='nav-link' to="/coffeelist">Кофейни</Link>
                      </li>
                      <li className="nav-item">
                        <Link className='nav-link' to="/wishlist">Вишлист</Link>
                      </li>
                      
                    </ul>
                    
                  </div>
                </div>
              </nav>
      
      <Outlet/>
    </div>
  );
  }
}

export default App;
