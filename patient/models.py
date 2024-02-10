from django.db import models
from core.models import User
from core.models import upload_path


class Patient (models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    High=models.PositiveIntegerField()
    Weight=models.DecimalField( max_digits = 5,decimal_places = 2)
    medical_history=models.TextField()
    medical=models.TextField(blank=True,default="")



class exp(models.Model):
    Patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    dis=models.CharField(blank=True,null=True,max_length=100)
    statuse=models.CharField(blank=True,null=True,max_length=100)
    gender=models.CharField(blank=True,null=True,max_length=100)
    semptoms=models.CharField(blank=True,null=True,max_length=100)
    pain=models.CharField(blank=True,null=True,max_length=100)
    location=models.CharField(blank=True,null=True,max_length=100)
    vomit=models.CharField(blank=True,null=True,max_length=100)
    pee=models.CharField(blank=True,null=True,max_length=100)
    heart=models.CharField(blank=True,null=True,max_length=100)
    breath=models.CharField(blank=True,null=True,max_length=100)

