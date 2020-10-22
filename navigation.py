import json
import urllib.request
import html
from bs4 import BeautifulSoup
from extract import extract_element_from_json
from distance import distanceCal
from time import sleep
# from gpiozero import InputDevice, OutputDevice
# from time import sleep, time
# from sense_hat import SenseHat
# from time import sleep
def maneuverAction(action):
    if action == "turn-left":
        #turn Left action
        print("turn left")
    elif action == "turn-right":
        #turn right action
        print("turn right")
    elif action == "straight":
        #keep straight action
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

run = False
distance = 100
currentLat = 0
currentLng = 0
actionList = []
action_index = 0
target_coordinate_index = 0


with open('Best_route_data.json', 'r') as f:
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


for item in maneuver:
    if item != None:
        actionList.append(item)

for item in actionList:
    print(item)

print(type(maneuver))
print_route_data()
print(distanceCal(10.726724, 106.708470, 10.726529, 106.710106))

#set run to True to start program
run = True

while run:
    actionCount = len(actionList)
    print(actionCount)

    for i in range(actionCount):
        
        sleep(3)
        #get GPS data(current_lat, current_lng)
        #distance = distanceCal(current lat, current lng, end_lat[target_coordinate_index], end_lng[target_coordinate_index])
        
        # straight()
        
        if distance < 20:
            maneuverAction(actionList[action_index])
            action_index += 1
            target_coordinate_index += 1
    break
    

    

