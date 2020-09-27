from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=20, null=True)
    STD = (
        ('8', '8'),
        ('9', '9'),
        ('10', '10')
    )
    std = models.IntegerField(choices=STD, blank=True, null=True)
    div = models.CharField(max_length=1, null=True)
    rollno = models.IntegerField(null=True)
    def __str__(self):
        return self.user.first_name + " " + str(self.father_name) + " " + self.user.last_name

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


