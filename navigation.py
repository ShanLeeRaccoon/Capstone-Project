import json
import urllib.request
import html
from bs4 import BeautifulSoup
from extract import extract_element_from_json
from distance import distanceCal
from time import sleep
from gpsCoordinate import getCoordinate
from motortest import *
from sense_hat import SenseHat
from bearing import calculate_initial_compass_bearing



def maneuverAction(action):
    if action == "turn-left":
        #turn Left action
        left()
        print("turn left")
    elif action == "turn-right":
        #turn right action
        right()
        print("turn right")
    elif action == "straight":
        #keep straight action
        straight()
        print("straight")
    else:
        print("straight")
    


def print_route_data():
    print(start_instruction)
    print(start_point)
    print(end_point)
    print(maneuver)
    print(start_lat)
    print(start_lng)
    print(end_lat)
    print(end_lng)

run_program = True
cal = False
run = False
distance = 0
currentLat = 0
currentLng = 0
actionList = []
run_nav_status = {"status": "Stop"}
bearing_value = {"value": 0}
compass_command_run = {"status": "Run"}
compass_command_stop = {"status": "Stop"}

# travel = False

while run_program:
    sense.clear()
    sleep(1)
    with open('/home/pi/Desktop/Capstone/backend/run_nav_command.json') as c:
        data = json.load(c)
        statusValue = data['status']
        print("Run Navigation: ", statusValue)
        if statusValue == "Run":
            cal = True

    while cal:

        #open the route data
        with open('Best_route_data3.json', 'r') as f:
            distros_dict = json.load(f)

        start_point = extract_element_from_json(distros_dict, ["routes", "legs","start_address"])
        end_point = extract_element_from_json(distros_dict, ["routes", "legs","end_address"])
        start_instruction = extract_element_from_json(distros_dict, ["routes", "legs","steps","html_instructions"])
        maneuver = extract_element_from_json(distros_dict, ["routes", "legs","steps","maneuver"])
        start_lat = extract_element_from_json(distros_dict, ["routes", "legs","steps","start_location","lat"])
        start_lng = extract_element_from_json(distros_dict, ["routes", "legs","steps","start_location","lng"])
        end_lat = extract_element_from_json(distros_dict, ["routes", "legs","steps","end_location","lat"])
        end_lng = extract_element_from_json(distros_dict, ["routes", "legs","steps","end_location","lng"])
        start_instruction = BeautifulSoup(start_instruction[0], "lxml").text

        #delete starting point maneuver(None)
        del maneuver[0]
        for item in maneuver: 
            # if item != None
            actionList.append(item)

        #put action into action list
        for item in actionList:
            print(item)

        print_route_data()
        print("Distance calculator test....(180 meters)",distanceCal(10.726724, 106.708470, 10.726529, 106.710106))
        #set run to True to start program
        run = True
        cal = False

    while run:
        actionCount = len(actionList)
        print("Number of actions:", actionCount)
        action_index = 0
        target_coordinate_index = 0
        
        ##first step here
        run_first_step = True
        proceed_first_step = True
        while run_first_step:
            try:
                while proceed_first_step:
                    sleep(3)
                    with open('/home/pi/Desktop/Capstone/backend/run_nav_command.json') as j:
                            data = json.load(j)
                            statusValue = data['status']
                            print("Run Navigation: ", statusValue)
                            if statusValue == "Stop":
                                with open('/home/pi/Desktop/Capstone/run_compass.json', 'w') as s:
                                    json.dump(compass_command_stop, s)
                                run_first_step = False
                                proceed_first_step = False
                                cal = False
                                run = False
                                proceed_final_step = False
                                break
                    coordinate = getCoordinate()
                    print("Current coordinate: ", coordinate)
                    
                    pointA = (float(coordinate[0]), float(coordinate[1]))
                    # pointA = (10.728983, 106.717241)
                    # print(type(pointA))
                    # print(pointA)
                    pointB = (end_lat[target_coordinate_index], end_lng[target_coordinate_index])
                    bearing = calculate_initial_compass_bearing(pointA, pointB) 
                    print("bearing: ", bearing)
                    bearing_value['value'] = bearing
                    with open('/home/pi/Desktop/Capstone/bearing.json', 'w') as b:
                        json.dump(bearing_value, b)

                    with open('/home/pi/Desktop/Capstone/run_compass.json', 'w') as a:
                        json.dump(compass_command_run, a)

                    distance = distanceCal(coordinate[0], coordinate[1], end_lat[target_coordinate_index], end_lng[target_coordinate_index])
                    print("next turn coordinate: ", end_lat[target_coordinate_index],", ", end_lng[target_coordinate_index])
                    print("Distance to next turn: ", distance, " meter")

                    if distance < 20:
                        
                        print("Action Proceed")
                        with open('/home/pi/Desktop/Capstone/run_compass.json', 'w') as s:
                            json.dump(compass_command_stop, s)
                        maneuverAction(actionList[action_index])
                        action_index += 1
                        target_coordinate_index += 1
                        proceed_first_step = False
                        run_first_step = False

            except Exception:
                    pass

        actionCount = actionCount - 1            

        
        for i in range(actionCount):
            travel = True
            proceed = True
            distance = 100
           
            while travel:
                try:
                    while proceed:
                        proceed_final_step = True
                        
                        #read run_nav_command
                        with open('/home/pi/Desktop/Capstone/backend/run_nav_command.json') as c:
                            data = json.load(c)
                            statusValue = data['status']
                            print("Run Navigation: ", statusValue)
                            if statusValue == "Stop":     
                                proceed = False
                                travel = False
                                cal = False
                                run = False
                                proceed_final_step = False
                                break
                        straight()
                        sleep(3)
                        #get GPS data(current_lat, current_lng)
                        coordinate = getCoordinate()
                        print("Current coordinate: ", coordinate)
                        current_lat = coordinate[0]
                        current_lng = coordinate[1]

                        distance = distanceCal(current_lat, current_lng, end_lat[target_coordinate_index], end_lng[target_coordinate_index])
                        print("next turn coordinate: ", end_lat[target_coordinate_index],", ", end_lng[target_coordinate_index])
                        print("Distance to next turn: ", distance, " meter")
                        # straight()
                        
                        if distance < 50:
                            print("Action Proceed")
                            maneuverAction(actionList[action_index])
                            action_index += 1
                            target_coordinate_index += 1
                            travel = False
                            proceed = False

                except Exception:
                    pass
        #final step
        
        travel_end = False
        proceed_end = False
        distance = 100
        if proceed_final_step == True:
            travel_end = True
            proceed_end = True
            distance = 100

        while travel_end:
            print("Final step")
            try:
                while proceed_end:
                    straight()
                    sleep(2)
                    coordinate = getCoordinate()
                    print("Current coordinate: ", coordinate)

                    current_lat = coordinate[0]
                    current_lng = coordinate[1]
                    

                    distance = distanceCal(current_lat, current_lng, end_lat[target_coordinate_index], end_lng[target_coordinate_index])
                    print("Distance to destination: ", distance, " meter")

                    if distance < 30:
                        #Show sth on sensehat
                        print("Destination arrived")
                        with open('/home/pi/Desktop/Capstone/backend/run_nav_command.json', 'w') as r:
                            json.dump(run_nav_status, r)
                        sense.clear()
                        travel_end = False
                        proceed_end = False
            except Exception:
                pass
        
        
        break
    

    

