# from gpsCoordinate import getCoordinate

import json

coordinate = {
    "currentLat": 10.788910,
    "currentLng": 106.652562
}
# coordinate = getCoordinate()

print("Current coordinate: ", coordinate)
current_lat = coordinate["currentLat"]
current_lng = coordinate["currentLng"]

with open('GPS.json', 'w') as outfile:
    json.dump(coordinate, outfile)


