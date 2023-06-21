from django.db import models

# Create your models here.


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    cname = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    product = models.CharField(max_length=100)
    message = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
          return "Message from " + self.fname + self.lname + ' - ' + self.email
    


class Demo(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    cname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    product = models.CharField(max_length=100)
    demo_date = models.DateField()
    demo_time = models.TimeField()
    message = models.TextField()

    def __str__(self):
          return "Message from " + self.fname + self.lname + ' - ' + self.email

     
 