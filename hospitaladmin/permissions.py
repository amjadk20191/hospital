from rest_framework import permissions


class adminonly(permissions.BasePermission):


    def has_permission(self, request, view, *args, **kwargs):


        return request.user.groups.filter(name='admin').exists()



class receptiononly(permissions.BasePermission):


    def has_permission(self, request, view, *args, **kwargs):


        return request.user.groups.filter(name='reception').exists()




