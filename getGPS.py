from gpsCoordinate import getCoordinate
from time import sleep
import json
status = {"status": "Stop"}
standby = True

def saveCoordinate():
    run = True
    while run:

        try:
            GPScoordinate = getCoordinate()
            #fake coordinate
            coordinate = {
                "currentLat": GPScoordinate[0],
                "currentLng": GPScoordinate[1]
            }
            
            # GPScoordinate = getCoordinate()
            
            print("Current coordinate: ", GPScoordinate)
            

           

            with open('/home/pi/Desktop/Capstone/originGPS.json', 'w') as outfile:
                json.dump(coordinate, outfile)
            run = False
        except Exception:
            pass


saveCoordinate()

while standby:
    sleep(1)
    with open('/home/pi/Desktop/Capstone/backend/getGPScommand.json') as f:
        data = json.load(f)
        statusValue = data['status']
        print(statusValue)


    if statusValue == "Fetch":
        saveCoordinate()
        with open('/home/pi/Desktop/Capstone/backend/getGPScommand.json', 'w') as c:
            json.dump(status, c)
        print("changed to stop")
        

    




