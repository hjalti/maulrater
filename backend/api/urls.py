from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('restaurants/', views.RestaurantList.as_view()),
    path('ratings/create/', views.RatingCreate.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
