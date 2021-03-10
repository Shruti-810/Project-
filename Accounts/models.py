from django.db import models

# Create your models here.


class register(models.Model):
    name=models.CharField(max_length=30)
    phone_no=models.IntegerField()
    email_id=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    cpassword=models.CharField(max_length=10)