from django.db import models
class Contact(models.Model):
    fullname= models.CharField(max_length=122)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    message =models.TextField()
    date =models.DateField()
    def __str__(self):
        return self.fullname
# Create your models here.
class support(models.Model):
    name=models.CharField(max_length=122)
    phone= models.CharField(max_length=15)
    email=models.EmailField()
    program_participation = models.CharField(
        max_length=3,
        choices=[('yes', 'Yes'), ('no', 'No')]
    )
    address = models.TextField()
    def __str__(self):
        return self.name