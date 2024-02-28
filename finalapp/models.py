from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass 

    
class Classroom(models.Model):
    name = models.CharField(max_length=100)
    doctor = models.ForeignKey(User, related_name='classrooms', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100, default='')
    student_id = models.IntegerField(default=0)
    classroom = models.ForeignKey(Classroom, related_name='students', on_delete=models.CASCADE, blank=True, null=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def transScore(self):
            if self.score>=95:
                return 'A+'
            if self.score>=90:
                return 'A'
            if self.score>=85:
                return 'B+'
            if self.score>=80:
                return 'B'
            if self.score>=75:
                return 'C+'
            if self.score>=70:
                return 'C'
            if self.score>=65:
                return 'D+'
            if self.score>=60:
                return 'D'
            if self.score<=60:
                return 'F'
            