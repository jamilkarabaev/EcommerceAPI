from django.urls import path, include
from item import views

name = 'item'

urlpatterns = [
    path('list/', views.ListItemView.as_view(), name='list'),
    path('retrieve/<int:pk>', views.RetrieveItemView.as_view(), name='retrieve'),
    #seller endpoints
    path('create/', views.CreateItemView.as_view(), name='create'),
    path('mylistings/', views.MyListedItemView.as_view(), name='mylistings'),
    path('edit/<int:pk>', views.RetrieveUpdateDestroyItemView.as_view(), name='update'),


]
