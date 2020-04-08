from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    
class IpCount(models.Model):    
    ip_address = models.GenericIPAddressField()
    last_date = models.DateField()
    count = models.IntegerField(default=0)