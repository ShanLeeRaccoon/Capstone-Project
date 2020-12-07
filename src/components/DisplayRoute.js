import React, { Component } from 'react';
import { render } from 'react-dom';
import Map from './MapDraw';
import { Button } from 'antd';
import Table from 'react-bootstrap/Table'

const googleMapsApiKey = "AIzaSyATP8bWLQMM4D4R2ILoKFGjZL69qcKoyJs";



const App = props => {
  // const {places} = props;
  
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
      defaultCenter={defaultCenter || {lat: 10.726675, lng:  106.708340}}
      defaultZoom={defaultZoom || 15}
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
      e.preventDefault(); window.location.href='/'; localStorage.clear()}} class="btn btn-primary">Return to Location Selection. </Button>
    </div>
  );
  
};


let targetLat = parseFloat(localStorage.getItem("targetLat"))
let targetLng = parseFloat(localStorage.getItem("targetLng"))
let currentLat = parseFloat(localStorage.getItem("currentLat"))
let currentLng = parseFloat(localStorage.getItem("currentLng"))
console.log("Print lat and long here: ", targetLat, targetLng)
const places = [
  {latitude: currentLat,longitude: currentLng},
  {latitude: targetLat, longitude: targetLng}
]

render(<App defaultZoom={7} places={places} />, document.getElementById('root'));

export default App;