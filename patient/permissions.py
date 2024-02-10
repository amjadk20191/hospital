from rest_framework import permissions


class patientonly(permissions.BasePermission):


    def has_permission(self, request, view, *args, **kwargs):

        return request.user.groups.filter(name='patient').exists()
