
from django.db import models
  
class registerdata(models.Model):

   username = models.CharField(max_length=100, blank=False)
   email = models.EmailField(max_length=100, blank=False)
   phone = models.CharField(max_length=100, blank=False)
   password = models.CharField(max_length=30,blank=False)
   access = models.CharField(max_length=100, blank=False)
   orphanname = models.CharField(max_length=30,blank=False)
   orphanemail = models.EmailField(max_length=100, blank=False,primary_key=True)   
   orphanaddress = models.CharField(max_length=30,blank=False)

   class Meta:
    db_table = "orphanage_details"

class User1(models.Model):
    username = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    phone = models.CharField(max_length=100, blank=False)
    subject = models.CharField(max_length=100, blank=False)
    message = models.CharField(max_length=200, blank=False)
    class Meta:
        db_table = "contact"