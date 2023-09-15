from rest_framework import serializers
from .models import Cart , Order , OrderDetail , CartDetail



class CartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model =  CartDetail
        fields = '__all__'
        
        
        
        
class CartSerializer(serializers.ModelSerializer):
    cart_detail = CartDetailSerializer(many=True)
    class Meta:
        model = Cart
        fields = '__all__'
               