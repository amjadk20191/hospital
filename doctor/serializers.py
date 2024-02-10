
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from drf_extra_fields.fields import Base64ImageField,Base64FileField
import io
import zipfile
import rarfile
from core.serializers import UserSerializer
from .models import Doctor,Reservation,Prescription
from rest_framework.exceptions import ValidationError


class ShowReservationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=60, source="Patient.User.name", read_only=True)
    prescription=serializers.HyperlinkedIdentityField(view_name='prescription',lookup_field='pk',read_only=True)

    class Meta:
        model = Reservation
        fields = ['pk','Day','Time','name','prescription']





class MyBase64File(Base64FileField):
    ALLOWED_TYPES = [ 'zip', 'rar']

    def get_file_extension(self, filename, decoded_file):
        if zipfile.is_zipfile(io.BytesIO(decoded_file)):
            return 'zip'
        elif rarfile.is_rarfile(io.BytesIO(decoded_file)):
            return 'rar'
        else:
            raise ValidationError('Unsupported file type')

class PrescriptionSerializer(serializers.ModelSerializer):
    Image=MyBase64File()
    Day=serializers.DateField(source='Reservation.Day',read_only=True)
    specialty=serializers.CharField(source='Reservation.Doctor.specialty.Name',read_only=True)
    doctor=serializers.CharField(source='Reservation.Doctor.User.name',read_only=True)
    Money=serializers.IntegerField(write_only=True)
    class Meta:
        model = Prescription
        fields = ['pk','Diagnosis','treatment','symptoms','Day','specialty','doctor','Image','Money']

    def create(self, validated_data):

            validated_data['Reservation']=Reservation.objects.get(pk= self.context['view'].kwargs['pk'])
            Reservation.objects.filter(pk= self.context['view'].kwargs['pk']).update(Money=validated_data.pop('Money'))

            if hasattr(validated_data['Reservation'], 'prescription'):
                raise ValidationError('this Reservation already has Prescription')

            return super().create(validated_data)


