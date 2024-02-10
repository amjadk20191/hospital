
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from django.db import transaction
from core.serializers import creatuser
from core.models import User


from core.serializers import UserSerializer

from patient.models import Patient,exp
from doctor.models import Doctor
from .models import Specialty




class DoctorSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=60,source="User.username")
    name=serializers.CharField(max_length=60,source="User.name")
    sex=serializers.CharField(max_length=60,source="User.sex")
    phone=serializers.CharField(max_length=20,source="User.phone")
    age=serializers.CharField(max_length=20,source="User.age")
    personal_id=serializers.FileField(source="User.personal_id")
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = Doctor
        fields = ['pk','name','username','personal_id','password','License','certificate','specialty','From','To','phone','age','sex','url']
    @transaction.atomic()

    def create(self, validated_data):
        user=creatuser(validated_data)
        user.groups.set([3])
        validated_data['User'] = user

        return super().create(validated_data)







class PatientSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=60,source="User.username")
    name=serializers.CharField(max_length=60,source="User.name")
    sex=serializers.CharField(max_length=60,source="User.sex")
    phone=serializers.CharField(max_length=60,source="User.phone")
    age=serializers.CharField(max_length=60,source="User.age")

    personal_id=serializers.FileField(source="User.personal_id")
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = Patient
        fields = ['pk','name','username','personal_id','password','High','Weight','sex','age','phone','medical_history','url']
    @transaction.atomic()

    def create(self, validated_data):
        user=creatuser(validated_data)
        user.groups.set([4])
        validated_data['User'] = user
        data=super().create(validated_data)

        exp.objects.create(Patient=data)


        return data






class  SpecialtySerializer(serializers.ModelSerializer):

    class Meta:
        model=Specialty
        fields=['pk','Name','url']





class receptionSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ['pk','name','username','personal_id','sex','phone','age','password','url']

    def create(self, validated_data):
        user=User.objects.create_user(**validated_data)
        user.groups.set([5])

        return user