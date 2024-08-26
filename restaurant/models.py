from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.


class Menu(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    description = models.TextField()
    img = models.ImageField(upload_to='static/img/ipload_images')
    price = models.IntegerField()

    def save(self, *args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    number_of_guest = models.IntegerField()
    date_of_booking = models.DateField()
    time_of_booking = models.TimeField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} Booking table in {self.date_of_booking} {self.time_of_booking}'
    
class Table(models.Model):
    number_of_table = models.PositiveIntegerField()
