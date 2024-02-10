from django.shortcuts import render
from .serializers import ReservationSerializer,ShowSpecialtySerializer,ShowDoctorSerializer,ShowAllReservationTimeSerializer

from rest_framework import generics,viewsets
from rest_framework.reverse import reverse
from rest_framework import status
from .models import  Patient
from hospitaladmin.models import Specialty
from doctor.models import Doctor,Reservation
from django.db.models import Q
import datetime
from rest_framework.response import Response
from .permissions import patientonly



class TimeReservation(generics.GenericAPIView):
    serializer_class =ShowAllReservationTimeSerializer
    permission_classes = [ patientonly]

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        self.queryset = Reservation.objects.filter(Doctor__pk=pk).filter(Q(Day__gt=datetime.date.today())|Q(Q(Day=datetime.date.today())&Q(Time__gt= datetime.datetime.now().time())))

        return super().get_queryset()

    def get(self, request, *args, **kwargs):
         queryset = self.filter_queryset(self.get_queryset())

         times = {}
         for i in range(7):
             day = datetime.date.today() + datetime.timedelta(days=i)
             times[f'Day{i}'] = list(queryset.filter(Day=day))


         serializer = self.get_serializer(times)
         return Response(serializer.data)


class ShowDoctor(generics.ListAPIView):
    serializer_class = ShowDoctorSerializer
    permission_classes = [ patientonly]

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        self.queryset = Doctor.objects.filter(specialty=pk)
        return super().get_queryset()
class ShowSpecialty(generics.ListAPIView):
    serializer_class = ShowSpecialtySerializer
    queryset = Specialty.objects.all()
    permission_classes = [ patientonly]



class  AddReservation(generics.CreateAPIView):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
    permission_classes = [ patientonly]



