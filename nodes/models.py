from django.db import models

# Create your models here.


class Node(models.Model):

    device_id = models.CharField(max_length=75)
    rssi_data = models.IntegerField()
    distance = models.IntegerField()
    timestamp = models.DateTimeField()
    node_id = models.CharField(max_length=50)
    confidence = models.IntegerField() 
    location_x = models.IntegerField()
    location_y = models.IntegerField()
    origin_x = models.IntegerField()
    origin_y = models.IntegerField()