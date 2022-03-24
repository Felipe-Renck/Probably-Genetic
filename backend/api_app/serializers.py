from rest_framework import serializers
from .models import CartItem, Disease


class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=200)
    product_price = serializers.FloatField()
    product_quantity = serializers.IntegerField(required=False, default=1)

    class Meta:
        model = CartItem
        fields = ('__all__')

class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ('orpha_code', 'name', 'symptoms')

class InputParameterSerializer(serializers.Serializer):
    label = serializers.CharField()
    value = serializers.CharField()