import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css'
import { BrowserRouter as Router, Route } from 'react-router-dom'

import Navigation from './components/Navigation'
import ListProducts from './components/ListProducts'
import CreateProduct from './components/CreateProduct'

import './App.css';

function App() {
  return (
    <Router>
      <Navigation />
      <div className="container p-4">
        <Route path="/" exact component={ListProducts} />
        <Route path="/create" component={CreateProduct} />
      </div>
    </Router>
  );
}

export default App;
