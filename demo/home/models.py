from django.db import models
from django.contrib.auth.models import User
class Teams(models.Model):
    name = models.CharField(max_length=30)
    players = models.CharField(max_length=1000)
    bowlers = models.IntegerField()
    batsman=models.IntegerField()
    wicketkeeper=models.IntegerField()
    coach=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    def __str__(self):
        return self.name


class BaseUser(User):
    mobile=models.CharField(max_length=11)
    address=models.CharField(max_length=30)
    gender=models.CharField(max_length=6)
    dob=models.DateField(auto_now_add=True)
    
