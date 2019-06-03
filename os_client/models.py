from django.db import models

class Client(models.Model):
    name=models.CharField(max_length=30)
    address=models.TextField()
    username=models.CharField(primary_key=True,max_length=30)
    password=models.CharField(max_length=30)
    photo=models.ImageField(upload_to='client')
    contact=models.IntegerField()
    otp=models.IntegerField()


class Complaint(models.Model):
    cno=models.IntegerField(primary_key=30)
    client_un=models.ForeignKey(Client,on_delete=models.CASCADE)
    comment=models.CharField(max_length=30)
