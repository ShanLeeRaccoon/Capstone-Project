import json
import urllib.request
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = 'AIzaSyATP8bWLQMM4D4R2ILoKFGjZL69qcKoyJs'
origin = input("Where are you now?: ").replace(' ','+')
destination = input("Where do you want to go?: ").replace(' ','+')

nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,api_key)
request = endpoint + nav_request
response = urllib.request.urlopen(request).read()
directions = json.loads(response)
print(directions)
with open('Best_route_data3.json', 'w') as json_file:
    json.dump(directions, json_file, indent = 4, sort_keys = True)