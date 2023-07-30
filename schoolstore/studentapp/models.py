from django.db import models

# Create your models here.
from django.db.models import Model


from django.db import models

class Details(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    dob = models.DateTimeField()
    mail = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
