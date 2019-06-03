from django.db import models
from os_admin.models import AgentRegister
from os_client.models import Client

class Property(models.Model):
    no=models.AutoField(primary_key=True)
    agent_un=models.ForeignKey(AgentRegister,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    location=models.CharField(max_length=30)
    photo=models.ImageField(upload_to='property')
    size=models.CharField(max_length=30)
    price=models.CharField(max_length=30)
    facing=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    comment=models.CharField(max_length=30)
    add_date=models.DateField()
    sold_date=models.DateField()

class SoldProperty(models.Model):
    pno=models.ForeignKey(Property,on_delete=models.CASCADE)
    client_un=models.ForeignKey(Client,on_delete=models.CASCADE)
    date_of_sold=models.DateField()

class PropertyBlocked(models.Model):
    bno=models.AutoField(primary_key=True)
    pno=models.ForeignKey(Property,on_delete=models.CASCADE)
    client_un=models.ForeignKey(Client,on_delete=models.CASCADE)
    amount=models.IntegerField()