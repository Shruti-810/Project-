from django.db import models

# Create your models here.


class register(models.Model):
    name=models.CharField(max_length=30)
    phone_no=models.IntegerField()
    email_id=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    cpassword=models.CharField(max_length=10)
    # def __init__(self,name,phone_no,email_id,password,cpassword):
    #     self.name=name
    #     self.phone_no=phone_no
    #     self.email_id=email_id
    #     self.password=password
    #     self.cpassword=cpassword
    def login_id(self):
        return self.email_id
    def login_pass(self):
        return self.password



