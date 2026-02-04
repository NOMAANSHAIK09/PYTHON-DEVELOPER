from django.db import models
from django.contrib.auth.models import User 

MEAL_TYPE=(
    ('starter','starter'),
    ('main course','main course'),
    ('dessert','dessert'),
    ('beverage','beverage'),
)

STATUS=(
    (0,'unavailable'),
    (1,'available'),
)
class item(models.Model):
    meal=models.CharField(max_length=200)
    description=models.CharField(max_length=2000)
    price=models.FloatField()
    meal_type=models.CharField(choices=MEAL_TYPE)
    author =models.ForeignKey(User, on_delete=models.CASCADE )
    status=models.IntegerField(choices=STATUS,default=0)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.meal

