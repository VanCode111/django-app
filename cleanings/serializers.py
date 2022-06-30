from rest_framework import serializers
from .models import Cleaning, City
from rest_framework.serializers import ValidationError

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ['name', 'id']

class CleaningSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)

    class Meta:
        model = Cleaning
        fields = ['title', 'city', 'id', 'price', 'completed']

class CreateCleaningSerializer(serializers.ModelSerializer):
    def validate_price(self, price):
        if (price < 0):
            raise ValidationError('Цена не может быть отрицательной')
        return price

    class Meta:
        model = Cleaning
        fields = '__all__'

class CompletedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cleaning
        fields = ['completed']