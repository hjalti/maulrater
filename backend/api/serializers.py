from rest_framework import serializers
from api.models import Rating, Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'av_rating', 'rating_count']

class RatingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=0, max_value=2)
    restaurant_id = serializers.IntegerField()

    def validate_restaurant_id(self, value):
        try:
            Restaurant.objects.get(pk=value)
            return value
        except Restaurant.DoesNotExist:
            raise serializers.ValidationError("Restaurant does not exist")

    def create(self, validated_data):
        rating = Rating(rating=validated_data['rating'],
                restaurant=Restaurant.objects.get(pk=validated_data['restaurant_id']))
        rating.save()
        return rating

    class Meta:
        model = Rating
        fields = ['rating', 'restaurant_id']
