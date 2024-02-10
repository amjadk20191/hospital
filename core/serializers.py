
from .models import User

from rest_framework import serializers
from rest_framework.reverse import reverse
from django.db.models import Q
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from drf_writable_nested.serializers import WritableNestedModelSerializer

class TokenObtainPairSerializerNew(TokenObtainPairSerializer):
    def validate(self, attrs) :


         data= super().validate(attrs)
         data['type'] = self.user.groups.first().name
         data['name'] = self.user.name
         data['sex'] = self.user.sex
         data['phone'] = self.user.phone
         data['age'] = self.user.age
         if hasattr(self.user,'doctor'):
             data['specialty'] = self.user.doctor.specialty.Name

         return data






def creatuser(validated_data):
    userdata = validated_data.pop('User')
    use_data = {

        'username': userdata.pop('username'),
        'name': userdata.pop('name'),
        'phone': userdata.pop('phone'),
        'sex': userdata.pop('sex'),
        'age': userdata.pop('age'),
        'personal_id': userdata.pop('personal_id'),
        'password': validated_data.pop('password')
    }

    user_serializer = UserSerializer(data=use_data)
    user_serializer.is_valid(raise_exception=True)
    return user_serializer.save()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ['pk','name','username','personal_id','sex','phone','age','password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    def update(self, instance, validated_data):

        return User.objects.update_user(instance.pk,**validated_data)