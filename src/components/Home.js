import React, { Component } from 'react';
import Map from './Map';
import { Button } from 'antd';
import Table from 'react-bootstrap/Table';
import Swal from 'sweetalert2';
import axios from 'axios';

class Home extends Component {
	constructor(props) {
		super(props);
		this.state = {
			start: " ",
			end: " ",
			redirect: false,
			lat:1,
			errorMsg: " ",
			lng:1,
			isLoading: false
		}
	

	}

	componentDidMount() {
		// fetch('http://192.168.0.11:8080/getGPS')
		// 	.then(response => response.json())
		// 	.then(data => this.setState({ lat: data.currentLat, lng: data.currentLng }));
		axios.get('http://192.168.102.137:8081/getGPS').then(resp => {
		// axios.get('http://192.168.43.90:8081/getGPS').then(resp => {

		this.setState({
			lat: resp.data.currentLat,
			lng: resp.data.currentLng
			
		});
		console.log(this.state.lat, this.state.lng);
		localStorage.setItem("currentLat", this.state.lat)
		localStorage.setItem("currentLng", this.state.lng)
		this.setState({
			isLoading: true
			
		});
		console.log("component")
	});
		
	}

	confirmLocation = (event) => {
		console.log('send location', this.state.testValue)
		// console.log()
		this.props.testDropping(this.state.testValue)
	}

	setErrorMsg(){
		this.setState({
			errorMsg:"wrongboi"
		})
	}
	//Button Click Function
	opensweetalert() {
		var validation = localStorage.getItem("endLocation")

		if(validation == "Please Select a location. "){
			Swal.fire({
				type: 'error',
				title: 'Oops...',
				text: 'Please enter a valid location.'
			  })
		}
		else{
		let targetLocation = {
			// address: localStorage.getItem("endLocation")
			address: localStorage.getItem("targetLat") + ", " + localStorage.getItem("targetLng")
		}
		console.log("print", targetLocation)

		axios.post('http://192.168.102.137:8081/saveData', targetLocation)
		// axios.post('http://192.168.43.90:8081/saveData', targetLocation)

		.then((response) => {
			console.log(response);
		  }, (error) => {
			console.log(error);
		  });

		Swal.fire({
			title: 'Location Confirmed!',
			text: "Directing to routing screen...",
			type: 'success',
		})
		setTimeout(() => { window.location = "DisplayRoute"; }, 3000);
	}
		
	}
	

	render() {
		if(this.state.isLoading!=true){
			return <div>Loading....</div>

		}else{
		
		localStorage.setItem("startLocation", this.props.app.startLocation)
		localStorage.setItem("endLocation", this.props.app.endLocation)
		// console.log("here:", this.props.app.startLocation)
		localStorage.setItem("currentLat", this.state.lat)
		localStorage.setItem("currentLng", this.state.lng)
		console.log("HI", this.state.lat)
		return (
			
			<div>
				<div style={{ margin: '0px' }}>
					<Map
						{...this.props}
						// google={this.props.google}
						// default center - fetch raspberry pi location 10.726560, 106.708471
						center={{ lat: parseFloat(this.state.lat), lng: parseFloat(this.state.lng) }}
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
					
					<p style={{ color: 'red' }}>{this.state.errorMsg}</p>
					<Button style={{ marginBottom: '10px' }} block onClick={() => this.opensweetalert()} class="btn btn-primary">Confirm location</Button>
					
					<h1></h1>
					<p></p>
				</div>
			</div>


		);
		}
	}
}

export default Home;