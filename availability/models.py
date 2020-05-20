from django.db import models
from doc_profile.models import Doctors_Profile
# Create your models here.
class Availability(models.Model):
    Doctor_ID=models.ForeignKey(Doctors_Profile,on_delete=models.CASCADE)
    Date=models.DateField(auto_now=False, auto_now_add=False)
    Avail_From=models.DateTimeField(auto_now=False, auto_now_add=True)
    Avail_To=models.DateTimeField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return 'Availeble doctor: ' + str(self.Doctor_ID)+' | Date: '+str(self.Date)+'| Availabel ID: '+str(self.id)