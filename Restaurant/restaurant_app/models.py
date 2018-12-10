# Create your models here.
from django.db import models
from django.contrib.auth.models import User

Rating_Choices = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))

class Restaurant(models.Model):
    name = models.TextField()
    street = models.TextField()
    number = models.TextField()
    city = models.TextField()
    zipcode = models.TextField()
    state_or_province = models.TextField()
    county = models.TextField()
    telephone = models.TextField()

    def __str__(self):
        return self.name


class Dish(models.Model):
    restaurant = models.ForeignKey(Restaurant, null=True, on_delete=models.CASCADE, related_name='dishes')
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    name = models.TextField()
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=8)
    image = models.ImageField(upload_to='resturants')

    def __str__(self):
        return self.name


class Review(models.Model):
    dish = models.ForeignKey(Dish, null=True , on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    rating = models.PositiveIntegerField('Ratings', choices=Rating_Choices)
    comment = models.TextField()

    def __str__(self):
        return self.comment

