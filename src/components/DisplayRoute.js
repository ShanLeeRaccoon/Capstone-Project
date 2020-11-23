import React, { Component } from 'react';
import { render } from 'react-dom';
import Map from './MapDraw';
import { Button } from 'antd';
import Table from 'react-bootstrap/Table'

const googleMapsApiKey = "AIzaSyATP8bWLQMM4D4R2ILoKFGjZL69qcKoyJs";



const App = props => {
  // const {places} = props;
  const places = [
    {latitude: 10.726675,longitude: 106.708340},
    {latitude: 10.728979, longitude: 106.695755}
  ]
  const {
    loadingElement,
    containerElement,
    mapElement,
    defaultCenter,
    defaultZoom
  } = props;

  

  return (
    <div>
    <Map
    {...props}
      googleMapURL="https://maps.googleapis.com/maps/api/js?key=AIzaSyATP8bWLQMM4D4R2ILoKFGjZL69qcKoyJs&libraries=places"
      // googleMapURL={
      //   'https://maps.googleapis.com/maps/api/js?key=' +
      //   googleMapsApiKey +
      //   '&libraries=geometry,drawing,places'
      // }
      markers={places}
      loadingElement={loadingElement || <div style={{height: `100%`}}/>}
      containerElement={containerElement || <div style={{height: "80vh"}}/>}
      mapElement={mapElement || <div style={{height: `100%`}}/>}
      defaultCenter={defaultCenter || {lat: 25.798939, lng: -80.291409}}
      defaultZoom={defaultZoom || 11}
    />
    <Table   style={{marginTop: '5px'}} striped bordered hover variant="dark">
						<tbody>
							<tr>
								<th>From</th>
								<td>{localStorage.getItem("startLocation")}</td>
							</tr>
							<tr>
								<th>To</th>
								<td>{localStorage.getItem("endLocation")}</td>
							</tr>

						</tbody>
					</Table>
          <p className="text-center">The SafeCycle device will now lead your way! Click return to assign new destination.</p>
    <Button style={{ marginBottom: '10px' }} block onClick={(e) => {
      e.preventDefault(); window.location.href='/'}} class="btn btn-primary">Return to Location Selection. </Button>
    </div>
  );
  
};


const places = [
  {latitude: 10.726675,longitude: 106.708340},
  {latitude: 10.728979, longitude: 106.695755}
]

render(<App defaultZoom={7} places={places} />, document.getElementById('root'));

export default App;