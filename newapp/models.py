from django.db import models

class Member(models.Model):
    emp_id = models.CharField(max_length=20)
    emp_name = models.CharField(max_length=100)
    emp_desig = models.CharField(max_length=100)
