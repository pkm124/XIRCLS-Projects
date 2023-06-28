from rest_framework import serializers
from .models import User, Customer, Campany, Subject


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Customer
        fields = '__all__'

        
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Campany
        fields = '__all__'
        
        
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
