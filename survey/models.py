from django.db import models

# Create your models here.
class Data(models.Model):
    Q1 = [
       ('q1', 'Yes'),
       ('q1', 'No')
    ]
    Q2 = [
       ('q2', 'Yes'),
       ('q2', 'No')
    ]
    Q3 = [
       ('q3', 'Yes'),
       ('q3', 'No')
    ]
    Q4 = [
       ('q4', 'Yes'),
       ('q4', 'No')
    ]
    Q5 = [
       ('q5', 'Yes'),
       ('q5', 'No')
    ]
    Q6 = [
       ('q6', 'Yes'),
       ('q6', 'No')
    ]

    county = models.CharField(max_length = 50)
    facility = models.IntegerField()
    management = models.TextField(max_length = 300)
    q1 = models.CharField(max_length = 10, choices = Q1)
    q2 = models.CharField(max_length = 10, choices = Q2)
    q3 = models.CharField(max_length = 10, choices = Q3)
    q4 = models.CharField(max_length = 10, choices = Q4)
    challenges = models.TextField(max_length = 500)
    q5 = models.CharField(max_length = 10, choices = Q5)
    features = models.TextField(max_length = 500)
    q6 = models.CharField(max_length = 10, choices = Q6)
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length = 50)
    phone = models.IntegerField()
    email = models.EmailField(max_length = 50)
    
    def __str__(self):
        return self.county
    


