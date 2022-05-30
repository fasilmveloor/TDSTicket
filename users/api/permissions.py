from rest_framework.permissions import BasePermission

class IsTourist(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_tourist)

class IsTDS(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_tds)