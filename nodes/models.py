from django.db import models
from django.contrib import admin



# Create your models here.


class Node(models.Model):

    #the MAC address of the device the node sees
    device_id = models.CharField(max_length=75)
    #the RSSI of that device
    rssi_data = models.IntegerField()
    #the estimated distance of that device from the node in millimeters
    distance = models.IntegerField()
    #the time the reading took place
    timestamp = models.DateTimeField()
    #the id of the node making the observation
    node_id = models.CharField(max_length=50)
    #the confidence of the measurement in ??? units
    confidence = models.IntegerField() 
    #the location of the node making the observation in millimeters
    location_x = models.IntegerField()
    location_y = models.IntegerField()
    origin_x = models.IntegerField()
    origin_y = models.IntegerField()

admin.site.register(Node)