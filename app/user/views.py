from rest_framework import generics, authentication, permissions, viewsets, mixins, permissions, authentication
from user import serializers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user import permissions as userpermissions
from core import models
from item import permissions as itempermissions


# User Management

class CreateBuyerUserView(generics.CreateAPIView):
    serializer_class = serializers.BuyerUserSerializer

class CreateSellerUserView(generics.CreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,) 
    permission_classes = (permissions.IsAdminUser, )
    serializer_class = serializers.SellerUserSerializer

class CreateTokenView(ObtainAuthToken):
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_object(self):
        return self.request.user

class ManageBuyerUserView(generics.RetrieveUpdateAPIView):
    authentication_classes = (authentication.TokenAuthentication,) 
    permission_classes = (userpermissions.IsBuyer, )
    serializer_class = serializers.BuyerUserSerializer

    def get_object(self):
        return self.request.user

class ManageSellerUserView(generics.RetrieveUpdateAPIView):
    authentication_classes = (authentication.TokenAuthentication,) 
    permission_classes = (userpermissions.IsSeller, )
    serializer_class = serializers.SellerUserSerializer

    def get_object(self):
        return self.request.user




# Attr Management


class ListCreateUserAttr(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RetrieveUpdateDestroyUserAttr(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, itempermissions.IsOwnerOfItem)
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
    
class ListCreateAddress(ListCreateUserAttr):
    serializer_class = serializers.AddressSerializer
    queryset = models.Address.objects.all()

class RetrieveUpdateDestroyAddress(RetrieveUpdateDestroyUserAttr):
    permission_classes = (permissions.IsAuthenticated, itempermissions.IsOwnerOfItem)
    serializer_class = serializers.AddressSerializer
    queryset = models.Address.objects.all()

class ListCreateFinancialDetails(ListCreateUserAttr):
    permission_classes = (userpermissions.IsSeller,)
    serializer_class = serializers.FinancialDetailsSerializer
    queryset = models.FinancialDetails.objects.all()

class RetrieveUpdateDestroyFinancialDetails(RetrieveUpdateDestroyUserAttr):
    permission_classes = (userpermissions.IsSeller, itempermissions.IsOwnerOfItem)
    serializer_class = serializers.FinancialDetailsSerializer
    queryset = models.FinancialDetails.objects.all()













