from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20, null=False,blank=False)
    country = models.CharField(max_length=20, null=False, blank=False)
    district = models.CharField(max_length=20, null=False, blank=False)
    town = models.CharField(max_length=20, null=False, blank=False)
    zip_code = models.CharField(max_length=20, null=False, blank=False)
    phone_number1 = models.IntegerField(default=0, null=False, blank=False)
    phone_number2 = models.IntegerField(default=0, null=False, blank=False)
    email = models.EmailField()

    def __str__(self):
        return self.country 
        