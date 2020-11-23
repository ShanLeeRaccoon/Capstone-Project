import React, { Component, Fragment } from 'react';
import { BrowserRouter as Router, Route, Link, withRouter } from 'react-router-dom';
import Home from "./components/Home";
import { Nav, Navbar, NavItem } from 'react-bootstrap';
import { LinkContainer } from 'react-router-bootstrap';


class App extends Component {
	constructor(props) {
		super(props);
		this.state = {
			startLocation: " ",
			endLocation: "Please Select a location. ",
			testValue: " ",
			lat: " ",
			lng: " ",
		};
		this.testDropping = this.testDropping.bind(this)
		this.setStartLocation = this.setStartLocation.bind(this)
		this.onAddressChange = this.onAddressChange.bind(this)
	}




	testDropping(e) {
		this.setState({
			testValue: e
		})
		console.log('test dropping', this.state.testValue)
	}

	setStartLocation(e) {
		this.setState({
			startLocation: e
		})
		console.log("start address: ", this.state.startLocation)
	}

	onAddressChange(e) {
		this.setState({
			endLocation: e
		})
		console.log("end address: ", this.state.endLocation)
	}

	render() {
		const childProps = {
			app: this.state,
			testDropping: this.testDropping,
			onAddressChange: this.onAddressChange,
			setStartLocation: this.setStartLocation
		}
		return (

			<div className="App">
				<Navbar bg="dark" variant="dark">
					<Navbar.Brand href="#home">
						<img
							alt=""
							src="https://seeklogo.net/wp-content/files/nAMr39DXwW/bmw-new-2020-SJklslL.svg"
							width="30"
							height="30"
							className="d-inline-block align-top" />{' '}

					</Navbar.Brand>
					<Navbar.Brand href="/">SafeCycle App</Navbar.Brand>
				</Navbar>
				<Router >
					<div>

						<Home {...childProps} />
					</div>
				</Router>
			</div>
		);
	}
}

export default App;