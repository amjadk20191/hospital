


from rest_framework import permissions







class IsOwnerOrReadOnly(permissions.BasePermission):


    def has_object_permission(self, request, view, obj):

        return obj.user == request.user


class IsOwnerPhoto(permissions.BasePermission):
   
    def has_object_permission(self, request, view, obj):

        return obj.product.user == request.user


class doctoronly(permissions.BasePermission):


    def has_permission(self, request,view,*args, **kwargs):


        return  request.user.groups.filter(name='doctor').exists()




