from django.db import models
import uuid
# Create your models here.


class Patients(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True)
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Phone = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254)
    gender = models.CharField(default='Other', max_length=50)
    D_Of_B = models.DateField(auto_now=False, auto_now_add=False)
    Password = models.CharField(max_length=50)
    image = models.ImageField(default='default', upload_to='Patient/image',
                              height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return 'Patient: ' + str(self.id)

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
