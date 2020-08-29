from django.urls import path, include
from user import views
from rest_framework.routers import DefaultRouter

app_name = 'user'


urlpatterns = [
    path('create-buyer/', views.CreateBuyerUserView.as_view(), name='create_buyer_user'),
    path('create-seller/', views.CreateSellerUserView.as_view(), name='create_seller_user'),
    path('login/', views.CreateTokenView.as_view(), name='create_token_user'),
    path('manage-buyer/', views.ManageBuyerUserView.as_view(), name='manage-buyer-user'),
    path('manage-seller/', views.ManageSellerUserView.as_view(), name='manage-seller-user'),
    path('addreses/', views.ListCreateAddress.as_view(), name='addresses'),
    path('addresses/<int:pk>/', views.RetrieveUpdateDestroyAddress, name='addresses-id'),
    path('financial-details/', views.ListCreateFinancialDetails.as_view(), name='financial-details'),
    path('financial-details/<int:pk>/', views.RetrieveUpdateDestroyFinancialDetails, name='financial-details-id'),


]