import React, { Component } from 'react';
import Map from './Map';
import { Button } from 'antd';
import Table from 'react-bootstrap/Table'

class Home extends Component {
	constructor(props) {
		super(props);
		this.state = {
			start: " ",
			end: " ",
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

	render() {
		
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

					<Button style={{ marginBottom: '10px' }}  block onClick={this.confirmLocation} class="btn btn-primary">Confirm location</Button>
					<h1></h1>
					<p></p>
				</div>
			</div>


		);
	}
}

export default Home;