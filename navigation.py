import json
import urllib.request
import html
from bs4 import BeautifulSoup
from extract import extract_element_from_json



# from gpiozero import InputDevice, OutputDevice
# from time import sleep, time
# from sense_hat import SenseHat
# from time import sleep

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
print(start_instruction)


print(start_point)
print(end_point)
print(maneuver)
print(start_lat)
print(start_lng)
print(end_lat)
print(end_lng)




# print(type(distros_dict))
# route = distros_dict["routes"]
# print(type(route))
