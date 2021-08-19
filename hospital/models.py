from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    
    phone = PhoneNumberField(null=False, blank=False)
    def __str__(self):
    	return f" {self.pk}){self.first_name} {self.last_name}"

    def get_absolute_url(self):
    	return reverse('patient_list')	


class Message(models.Model):
    message = models.TextField()   	
	
    def __str__(self):
        return self.message
