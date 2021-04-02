from django.db import models

class Credit(models.Model):
    email=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    cnumber=models.IntegerField(max_length=16)
    cname=models.CharField(max_length=30)
    cdate=models.IntegerField(max_length=2)
    cyear=models.IntegerField(max_length=4)
    cvv=models.IntegerField(max_length=3)



class Debit(models.Model):
    dnumber=models.IntegerField(max_length=16)
    dname=models.CharField(max_length=30)
    ddate=models.IntegerField(max_length=2)
    dyear=models.IntegerField(max_length=4)
    debit_cvv=models.IntegerField(max_length=3)
