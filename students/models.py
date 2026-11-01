from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    gender=models.CharField(max_length=10)
    phone=models.CharField(max_length=10)



