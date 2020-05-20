from django.db import models

# Create your models here.
class Doctors_Profile(models.Model):
    First_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    Speciality=models.CharField(max_length=50)
    Phone=models.CharField(max_length=50)
    Email=models.EmailField(max_length=254)
    Password=models.CharField(max_length=50)
    def __str__(self):
        return 'Doctor: ' + str(self.id)
    class Meta:
        verbose_name = 'Docter Profile'
        verbose_name_plural = 'Docters Profiles'
