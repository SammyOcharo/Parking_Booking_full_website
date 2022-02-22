from django.db import models



# Create your models here.

class PreBook(models.Model):
    Name =models.CharField(max_length=100, blank=False, default=0)
    Email = models.EmailField(null=False)
    Phone = models.CharField(max_length=15, default=0)
    Location = models.CharField(max_length=50, default=0)
    Parking_Slot = models.CharField(max_length=50, default=0)
    Parking_Date = models.DateField(default=0)

    def __str__(self):
        return self.Name

class GetInTouch(models.Model):
    Name = models.CharField(max_length=25, blank=False, default=0)
    Email = models.EmailField(null=False)
    Message = models.TextField(null=False, default='')

    def __str__(self):
        return self.Name















