import React from "react";
import {
  withGoogleMap,
  GoogleMap,
  withScriptjs,
  Marker,
  DirectionsRenderer
} from "react-google-maps";

class MapDirectionsRenderer extends React.Component {
  state = {
    directions: null,
    error: null
  };

  componentDidMount() {
    const { places, travelMode } = this.props;
    console.log("print", this.props)
    const waypoints = places.map(p =>({
        location: {lat: p.latitude, lng:p.longitude},
        stopover: true
    }))
    const origin = waypoints.shift().location;
    const destination = waypoints.pop().location;
    
    

    const directionsService = new window.google.maps.DirectionsService();
    directionsService.route(
      {
        origin: origin,
        destination: destination,
        travelMode: travelMode,
        waypoints: waypoints
      },
      (result, status) => {
        if (status === window.google.maps.DirectionsStatus.OK) {
          this.setState({
            directions: result
          });
        } else {
          this.setState({ error: result });
        }
      }
    );
  }

  render() {
    if (this.state.error) {
      return <h1>{this.state.error}</h1>;
    }
    return (this.state.directions && <DirectionsRenderer directions={this.state.directions} />)
  }
}

const Map = withScriptjs(
  withGoogleMap(props => (
    <GoogleMap
      defaultCenter={props.defaultCenter}
      defaultZoom={props.defaultZoom}
    >
     
      <MapDirectionsRenderer
        places={props.markers}
        travelMode={window.google.maps.TravelMode.DRIVING}
      />
    </GoogleMap>
  ))
);

export default Map;

// https://github.com/google-map-react/google-map-react-examples/blob/master/src/examples/Main.js#L69
// https://github.com/google-map-react/google-map-react/issues/712