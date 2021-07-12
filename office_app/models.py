from django.db import models

# Create your models here.


class Employee(models.Model):
    name=models.CharField(max_length=100)
    eid=models.IntegerField()
    exp=models.IntegerField()
    address=models.TextField()
    contact=models.CharField(max_length=100)


    def __str__(self):
        return self.name
