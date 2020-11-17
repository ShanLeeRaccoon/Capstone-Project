import React, { Component } from 'react';
import Map from './Map';
import {Button } from 'antd';

class Home extends Component {
	constructor(props) {
		super(props);
		this.state = {
			
		};
	}

	confirmLocation = (event) => {
		console.log('send location')
	}

	render() {
		return(
			<div>
			<div style={{ margin: '0px' }}>
			<Map
				google={this.props.google}
				// default center - fetch raspberry pi location 10.726560, 106.708471
				center={{lat: 10.726560, lng: 106.708471}}
				zoom={15}
			/>
			<br/>
			<br/>
			<br/>
			<Button type="primary" block onClick={this.confirmLocation} class="btn btn-primary">Confirm location</Button>
			</div>
			</div>
			
			
		);
	}
}

export default Home;