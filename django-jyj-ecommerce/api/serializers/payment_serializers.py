from rest_framework import serializers
from store.models import Category, Product

from payment.models import Payment

# dev_8_2_Fruit
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"