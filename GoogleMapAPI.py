import json
import urllib.request
import unidecode
from time import sleep

cal_route_status = {"status": "Stop"}
run_nav_status = {"status": "Run"}

standby = True

def cal_route():
    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
    api_key = 'AIzaSyATP8bWLQMM4D4R2ILoKFGjZL69qcKoyJs'
    # origin = input("Where are you now?: ").replace(' ','+')

    # destination = input("Where do you want to go?: ").replace(' ','+')

    with open('/home/pi/Desktop/Capstone/backend/destinationGPS.json', 'r') as j:
        json_data = json.load(j)
    destination= json_data["address"]


    with open('/home/pi/Desktop/Capstone/originGPS.json', 'r') as k:
        json_data = json.load(k)
    origin = str(json_data["currentLat"]) + ", " + str(json_data["currentLng"])

    # print(origin)




    destination = destination.replace(' ','+')
    origin = origin.replace(' ','+')

    origin = unidecode.unidecode(origin)
    destination = unidecode.unidecode(destination)
    print(origin)
    print(destination)

    nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,api_key)
    request = endpoint + nav_request
    response = urllib.request.urlopen(request).read()
    directions = json.loads(response)
    print(directions)
    print(origin, destination)
    with open('/home/pi/Desktop/Capstone/Best_route_data3.json', 'w') as json_file:
        json.dump(directions, json_file, indent = 4, sort_keys = True)

while standby:
    sleep(1)
    with open('/home/pi/Desktop/Capstone/backend/cal_route_command.json') as f:
        data = json.load(f)
        statusValue = data['status']
        print(statusValue)
    if statusValue == "Cal":
        cal_route()
        with open('/home/pi/Desktop/Capstone/backend/cal_route_command.json', 'w') as c:
            json.dump(cal_route_status, c)
        print("cal route changed to stop")

        with open('/home/pi/Desktop/Capstone/backend/run_nav_command.json', 'w') as d:
            json.dump(run_nav_status, d)
        print("Run nav changed to run")