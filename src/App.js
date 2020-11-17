import React, { Component, Fragment } from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import Home from "./components/Home";
import { Nav, Navbar, NavItem } from 'react-bootstrap';
import { LinkContainer } from 'react-router-bootstrap';


class App extends Component {
	render() {
		return (

			<div className="App">
				<Navbar bg="dark" variant="dark">
					<Navbar.Brand href="#home">
						<img
							alt=""
							src="/logo.svg"
							width="30"
							height="30"
							className="d-inline-block align-top"/>{' '}
      						
    				</Navbar.Brand>
					<Navbar.Brand href="#home">SafeCycle App</Navbar.Brand>
				</Navbar>
				<Router>
					<div>

						<Route exact path="/" component={Home} />
					</div>
				</Router>
			</div>
		);
	}
}

export default App;