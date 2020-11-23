import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import DisplayRoute from "./components/DisplayRoute";
import reportWebVitals from './reportWebVitals';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'antd/dist/antd.css';
import { BrowserRouter as Router, Route, IndexRoute } from 'react-router-dom';
import Home from "./components/Home";

// import routedMap from "./components/routedMap"

ReactDOM.render((
  <Router >
    <div>
      <Route exact path="/">
        <App />
      </Route>
      <Route path="/DisplayRoute" component={DisplayRoute}>
        <DisplayRoute  />
      </Route>
    </div>
  </Router>
), document.getElementById('root'));

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
