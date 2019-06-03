from django.db import models
class Admin(models.Model):
    contact_no=models.IntegerField(primary_key=True)
    password=models.CharField(max_length=30)
    otp=models.IntegerField()

class AgentRegister(models.Model):
    agent_no=models.IntegerField()
    name=models.CharField(max_length=30)
    username=models.CharField(max_length=30,primary_key=True)
    password=models.CharField(max_length=30)
    otp=models.IntegerField()
    photo=models.ImageField(upload_to='agent')
    address=models.TextField()
    contact_no=models.IntegerField()

