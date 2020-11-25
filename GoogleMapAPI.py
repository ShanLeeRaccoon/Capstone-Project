import json
import urllib.request
import unidecode


endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = 'AIzaSyATP8bWLQMM4D4R2ILoKFGjZL69qcKoyJs'
origin = input("Where are you now?: ").replace(' ','+')

# destination = input("Where do you want to go?: ").replace(' ','+')

with open('/home/pi/Desktop/Capstone/backend/GPSrequest.json', 'r') as j:
    json_data = json.load(j)
    

destination= json_data["address"]


destination = destination.replace(' ','+')

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
with open('Best_route_data3.json', 'w') as json_file:
    json.dump(directions, json_file, indent = 4, sort_keys = True)