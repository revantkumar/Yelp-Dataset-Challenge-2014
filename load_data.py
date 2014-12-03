__author__="gkrishnan"
import json
from pprint import pprint
json_data=open('json_data.json')

data = json.load(json_data)
num = 0 
for i in data:
	print "\nPlace" + str(num)+":"
	print i['lat']
	print i['lon']
	print i['name']
	print i['rating']
	num = num+1
json_data.close()