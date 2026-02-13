from rest_framework.permissions import BasePermission


class HasProfile(BasePermission):
    """ Custom permission to only allow users with profile """
    def has_permission(self, request, view):
        return hasattr(request.user, "profile")
