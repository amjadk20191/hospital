from rest_framework import serializers
from django.db import transaction

from doctor.models import Doctor
from patient.models import Patient
from django.db.models import Max

from .models import Patient

from datetime import timedelta,datetime
from django.db.models import Q
from doctor.models import Doctor,Reservation
from hospitaladmin.models import Specialty
















class ShowReservationTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = ['Time']


class ShowAllReservationTimeSerializer(serializers.Serializer):
    Day0=ShowReservationTimeSerializer(many=True)
    Day1=ShowReservationTimeSerializer(many=True)
    Day2=ShowReservationTimeSerializer(many=True)
    Day3=ShowReservationTimeSerializer(many=True)
    Day4=ShowReservationTimeSerializer(many=True)
    Day5=ShowReservationTimeSerializer(many=True)
    Day6=ShowReservationTimeSerializer(many=True)










class ReservationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=60, source="Doctor.User.name", read_only=True)
    specialty = serializers.CharField(max_length=60, source="Doctor.specialty.Name", read_only=True)

    class Meta:
        model = Reservation
        fields = ['Day','Time','username','specialty']

    def create(self, validated_data):
        validated_data['Doctor']=Doctor.objects.get(pk= self.context['view'].kwargs['pk'])

        if  validated_data['Doctor'].From>validated_data['Time']:
            raise serializers.ValidationError({"detail": "the Reservation is too early "})

        time_end=(datetime.combine(datetime.min, validated_data['Time']) + timedelta(minutes=30)).time()

        if  validated_data['Doctor'].To<time_end:
            raise serializers.ValidationError({"detail": "the Reservation is too loang "})

        Reservations_times = Reservation.objects.values('Time').filter(
            Q(Doctor=validated_data['Doctor']) & Q(Day=validated_data['Day']))

        if Reservations_times.exists():


            for Reservation_time in Reservations_times :

                Reservation_time_end= (datetime.combine(datetime.min, Reservation_time['Time']) + timedelta(minutes=30)).time()

                if (Reservation_time['Time']<= validated_data['Time'] <Reservation_time_end)or (Reservation_time['Time']<= time_end<Reservation_time_end) :
                    raise serializers.ValidationError({"detail": "the Reservation cut with other Reservation "})
            if Reservations_times.filter(Patient=self.context['request'].user.patient).exists():
                raise serializers.ValidationError({"detail": "you have already Reservation in this day and the same doctor "})

        validated_data['Patient'] = self.context['request'].user.patient

        return super().create(validated_data)






class ShowSpecialtySerializer(serializers.ModelSerializer):
    Doctor=serializers.HyperlinkedIdentityField(view_name='showdoctor',lookup_field='pk',read_only=True)


    class Meta:
        model = Specialty
        fields = ['pk','Name','Doctor']







class ShowDoctorSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=60,source="User.name")
    sex=serializers.CharField(max_length=60,source="User.sex")
    Reservation=serializers.HyperlinkedIdentityField(view_name='addreservation',lookup_field='pk',read_only=True)
    ReservationTime=serializers.HyperlinkedIdentityField(view_name='timereservation',lookup_field='pk',read_only=True)


    class Meta:
        model = Doctor
        fields = ['pk','name','From','To','sex','Reservation','ReservationTime']











