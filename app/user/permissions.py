from rest_framework import permissions


class IsBuyer(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.user.is_anonymous == True:
            return False
        else:
            return request.user.is_buyer == True
        



class IsSeller(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.user.is_anonymous == True:
            return False
        else:
            return request.user.is_seller == True
       


