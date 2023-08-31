#get the data from the models and comvert to jason

from rest_framework import serializers
from .models import Product , Brand

class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = '__all__'
        
        
        
        
        
        
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'        