from django.db import models

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations
GENDER_CHOICES= [
    ('male', 'Man'),
    ('female', 'Woman'),
    ]
# Create your models here.
class Register(models.Model):
    username = models.CharField(max_length=12)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=12)
    confirmpassword = models.CharField(max_length=12)
    name = models.CharField(max_length=122)
    dob = models.CharField(max_length=12)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=100, default='male')
    city = models.CharField(max_length=10)
    
    
    

    def __str__(self):
        return self.name