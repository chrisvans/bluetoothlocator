# Create your views here.
import json
import datetime
from models import Node
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def node_input(request):
	# the request body will have an array of observations
	# [
	# 	{
	# 		"device_id":"C5E2F0FF1863",
	# 		"rssi_data":-65,
	# 		"distance": 25,
	# 		"timestamp": 1387043362,
	# 		"node_id":"node_1",
	# 		"confidence":2,
	# 		"location_x":0,
	# 		"location_y":54
	# 	},
	# 	{
	# 		"device_id":"CCFCFB24C005",
	# 		"rssi_data":-64,
	# 		"distance": 10,
	# 		"timestamp": 1387043362,
	# 		"node_id":"node_1",
	# 		"confidence":3,
	# 		"location_x":0,
	# 		"location_y":54
	# 	}
	# ]
	#load the JSON in
	data = json.loads(request.body)
	for item in data:
		dt = datetime.datetime.fromtimestamp(float(item['timestamp']))
		Node.objects.create(device_id=item['device_id'], rssi_data=item['rssi_data'], distance=item['distance'], timestamp=dt, node_id=item['node_id'], confidence=item['confidence'], location_x=item['location_x'], location_y=item['location_y'], origin_x=0, origin_y=0)
	



	response_data = {}
	response_data['status'] = 'OK'


	# #the MAC address of the device the node sees
    # device_id = models.CharField(max_length=75)
    # #the RSSI of that device
    # rssi_data = models.IntegerField()
    # #the estimated distance of that device from the node
    # distance = models.IntegerField()
    # #the time the reading took place
    # timestamp = models.DateTimeField()
    # #the id of the node making the observation
    # node_id = models.CharField(max_length=50)
    # #the confidence of the measurement in ??? units
    # confidence = models.IntegerField() 
    # #the location of the node making the observation
    # location_x = models.IntegerField()
    # location_y = models.IntegerField()
    # origin_x = models.IntegerField()
    # origin_y = models.IntegerField()
	return HttpResponse(json.dumps(response_data), content_type="application/json")