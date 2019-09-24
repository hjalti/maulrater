from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    @property
    def av_rating(self):
        count = self.ratings.count()
        if count == 0:
            return 0
        return sum(r.rating for r in self.ratings.all()) / count

    @property
    def rating_count(self):
        return self.ratings.count()

class Rating(models.Model):

    def __str__(self):
        return f'{self.rating} ({self.restaurant.name})'

    rating = models.PositiveIntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='ratings')
    date = models.DateTimeField(auto_now_add=True)

