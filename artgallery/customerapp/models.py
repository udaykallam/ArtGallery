from django.db import models

class Feedback(models.Model):
    name=models.CharField(max_length=200,blank=False)
    phone=models.CharField(max_length=12,blank=False,unique=True)
    email=models.EmailField(max_length=100,blank=False)
    feedback=models.CharField(max_length=1000,blank=False)
    class Meta:
        db_table="FeedBack"

    def __str__(self):
        return self.name

class Address(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,blank=False)
    phone=models.CharField(max_length=12,blank=False,unique=True)
    altphone=models.CharField(max_length=12,blank=False)
    email=models.EmailField(max_length=100,blank=False)
    pincode=models.CharField(max_length=10,blank=False)
    address=models.CharField(max_length=1000,blank=False)
    title=models.CharField(max_length=1000,blank=False)
    price=models.CharField(max_length=100,blank=False)
    class Meta:
        db_table="Address"

    def __str__(self):
        return self.name



