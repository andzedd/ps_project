from django.db import models

class Listing(models.Model):
    category = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    is_published = models.BooleanField(default=True)
    photo_main = models.ImageField(upload_to='photos/')
    photo_1 = models.ImageField(upload_to='photos/',blank=True)
    def __str__(self):
        return self.title