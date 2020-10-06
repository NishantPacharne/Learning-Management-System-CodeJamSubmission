from django.db import models
from users.models import *
from datetime import date


class Subject(models.Model):
    name = models.CharField(max_length=100, null=True)
    teacher = models.OneToOneField(Teacher, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name

class Meeting(models.Model):
    topic = models.CharField(max_length=200, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True, auto_now=False, null=True)
    STATUS = (
        ('Incomplete', 'Incomplete'),
        ('Concluded', 'Concluded'),
        ('Deleted', 'Deleted')
    )
    STD = (
        ('8', '8'),
        ('9', '9'),
        ('10', '10')
    )
    std = models.CharField(max_length=3, choices=STD, null=True)
    link = models.URLField(max_length=500, null=True)
    status = models.CharField(max_length=40, null=True, choices=STATUS, default="Incomplete")
    participents = models.ManyToManyField(Student, blank=True)
    time = models.TimeField(auto_now_add=False, null=True)

    def __str__(self):
        return self.topic

# q n a section models


class Question(models.Model):
    title = models.CharField(max_length=100, null=True)
    text = models.TextField(null=True)
    image = models.ImageField(null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    STATUS = (
        ('Unanswered', 'Unanswered'),
        ('Answered', 'Answered')
    )
    status = models.TextField(default='Unanswered', choices=STATUS, null=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    std = models.IntegerField(null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title



