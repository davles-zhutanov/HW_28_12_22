from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField()
    student = models.CharField(max_length=20)
    mentor = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}-{self.date}-{self.student}-{self.mentor}'

class Student(models.Model):
    name = models.CharField(max_length=20)
    birth_date = models.DateField(max_length=30)

    def __str__(self):
        return f"{self.name}-{self.birth_date}"

class Mentor(models.Model):
    name = models.CharField(max_length=20)
    experience = models.IntegerField()

    def __str__(self):
        return f'{self.name}-{self.experience}'