from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    
class IpCount(models.Model):    
    ip_address = models.GenericIPAddressField()
    count = models.IntegerField(default=1)