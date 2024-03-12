from django.db import models

# Create your models here.
class Reg(models.Model):
    full_name = models.CharField(max_length=255)
    passport_details = models.TextField(blank=False)
    place_of_work = models.TextField(blank=False)
    insurance_policy = models.TextField(blank=False)
    insurance_company = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name