from rest_framework import serializers
from .models import Country, State, City, Departement, User, Product, Period, Reparation


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country',]
        
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'
        
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
        
class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = '__all__'

class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class RepationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reparation
        fields = '__all__'
