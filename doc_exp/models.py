
from django.db import models
from datetime import date
from doc_profile.models import Doctors_Profile
# Create your models here.
class Experiance(models.Model):
    Exp_years_start=models.DateField(auto_now=False, auto_now_add=False)
    Exp_years_end=models.DateField(default=date.today(),auto_now=False, auto_now_add=False)
    Degrees=models.CharField(max_length=250)
    Degrees=models.CharField(max_length=250)
    Descreptions=models.TextField()
    docter=models.ForeignKey(Doctors_Profile,on_delete=models.CASCADE)