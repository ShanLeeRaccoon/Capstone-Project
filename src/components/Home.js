import React, { Component } from 'react';
import Map from './Map';
import { Button } from 'antd';
import Table from 'react-bootstrap/Table'
import Swal from 'sweetalert2'

class Home extends Component {
	constructor(props) {
		super(props);
		this.state = {
			start: " ",
			end: " ",
			redirect: false
		}
		this.setState({
			start: this.props.app.startLocation,
			end: this.props.app.endLocation
		})
	

	}

	  

	confirmLocation = (event) => {
		console.log('send location', this.state.testValue)
		// console.log()
		this.props.testDropping(this.state.testValue)
	}
	//Button Click Function
	opensweetalert() {
		
		Swal.fire({
			title: 'Location Confirmed!',
			text: "Directing to routing screen...",
			type: 'success',
		})
		setTimeout(() => { window.location = "DisplayRoute"; }, 3000);
		
		
	}
	

	render() {
		localStorage.setItem("startLocation", this.props.app.startLocation)
		localStorage.setItem("endLocation", this.props.app.endLocation)
		// console.log("here:", this.props.app.startLocation)
		return (
			<div>
				<div style={{ margin: '0px' }}>
					<Map
						{...this.props}
						// google={this.props.google}
						// default center - fetch raspberry pi location 10.726560, 106.708471
						center={{ lat: 10.726560, lng: 106.708471 }}
						zoom={15}
					/>
					<Table striped bordered hover variant="dark">
						<tbody>
							<tr>
								<th>From</th>
								<td>{this.props.app.startLocation}</td>
							</tr>
							<tr>
								<th>To</th>
								<td>{this.props.app.endLocation}</td>
							</tr>

						</tbody>
					</Table>

					<Button style={{ marginBottom: '10px' }} block onClick={this.opensweetalert} class="btn btn-primary">Confirm location</Button>
					<h1></h1>
					<p></p>
				</div>
			</div>


		);
	}
}

export default Home;