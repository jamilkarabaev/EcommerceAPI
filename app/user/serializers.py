from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from core import models

class BuyerUserSerializer(serializers.ModelSerializer):
    """User serializer"""

    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'password', 'name', 'is_seller']
        read_only_fields = ['id', 'is_seller']
        extra_kwargs = {'password':{'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        return get_user_model().objects.create_buyer(**validated_data)


    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

class SellerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'password', 'name', 'is_seller']
        read_only_fields = ['id', 'is_seller']
        extra_kwargs = {'password': {'write_only': True, 'Address Endpointsmin_length': 5}}

    def create(self, validated_data):
        return get_user_model().objects.create_seller(**validated_data)
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user



class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(request=self.context.get('request'), username=email, password=password)
        if not user:
            msg = ('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')
    
        attrs['user'] = user
        return attrs

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = ['id', 'city', 'area', 'street', 'building', 'unit_number']
        read_only_fields = ['id']

class FinancialDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FinancialDetails
        fields = ['id', 'merchant_account', 'name']
        read_only_fields = ['id']




        


