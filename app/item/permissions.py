from rest_framework import permissions

class IsOwnerOfItem(permissions.BasePermission):
    def has_object_permission(self, request, view, object):

        return request.user == object.seller