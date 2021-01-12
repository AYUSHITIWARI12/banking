from django.db import models

class Viewcustomer(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    account = models.CharField(max_length=255)
    cif = models.CharField(max_length=255)
    branchcode = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    amount = models.CharField(max_length=10000)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return 'Transaction done to' + self.name + '-' + self.account

class Userhistory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    account = models.CharField(max_length=255)
    amount = models.CharField(max_length=10000)
    timeStamp = models.DateTimeField(auto_now_add=True,blank=True)