import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css'
import { BrowserRouter as Router, Route } from 'react-router-dom'

import Navigation from './components/Navigation'
import ListTweets from './components/ListTweets'
import CreateTweet from './components/CreateTweet'

import './App.css';

function App() {
  return (
    <Router>
      <Navigation />
      <div className="container p-4">
        <Route path="/" exact component={ListTweets} />
        <Route path="/create" component={CreateTweet} />
      </div>
    </Router>
  );
}

export default App;
