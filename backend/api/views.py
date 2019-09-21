from rest_framework import generics

from api.serializers import RatingSerializer, RestaurantSerializer
from api.models import Restaurant

class RestaurantList(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RatingCreate(generics.CreateAPIView):
    serializer_class = RatingSerializer
