import React, { Component } from 'react';
import { render } from 'react-dom';
import Map from './MapDraw';

const googleMapsApiKey = "AIzaSyATP8bWLQMM4D4R2ILoKFGjZL69qcKoyJs";

const App = props => {
  const {places} = props;

  const {
    loadingElement,
    containerElement,
    mapElement,
    defaultCenter,
    defaultZoom
  } = props;

  return (
    <Map
      googleMapURL={
        'https://maps.googleapis.com/maps/api/js?key=' +
        googleMapsApiKey +
        '&libraries=geometry,drawing,places'
      }
      markers={places}
      loadingElement={loadingElement || <div style={{height: `100%`}}/>}
      containerElement={containerElement || <div style={{height: "80vh"}}/>}
      mapElement={mapElement || <div style={{height: `100%`}}/>}
      defaultCenter={defaultCenter || {lat: 25.798939, lng: -80.291409}}
      defaultZoom={defaultZoom || 11}
    />
  );
};


const places = [
  {latitude: 10.726675,longitude: 106.708340},
  {latitude: 10.728979, longitude: 106.695755}
]

render(<App defaultZoom={7} places={places} />, document.getElementById('root'));

export default App;