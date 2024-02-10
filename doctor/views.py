from .models import Doctor,Reservation,Prescription
from rest_framework import generics,viewsets
from .serializers import ShowReservationSerializer,PrescriptionSerializer
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.parsers import FormParser,MultiPartParser
from core.models import User
from rest_framework import status
from rest_framework.response import Response
from patient.models import Patient

from datetime import date
from .permissions import doctoronly
class ShowReservation(generics.ListAPIView):
    serializer_class = ShowReservationSerializer
    permission_classes = [ doctoronly]



    def get_queryset(self):
        self.queryset = Reservation.objects.filter(Doctor=self.request.user.doctor)
        return super().get_queryset()

class PrescriptionListCreate(generics.ListCreateAPIView):
    serializer_class = PrescriptionSerializer
    permission_classes = [ doctoronly]

    def get_queryset(self):
        pk = self.kwargs['pk']
        reservation= Reservation.objects.get(pk=pk)

        self.queryset = Prescription.objects.filter(Reservation__Patient=reservation.Patient)
        return super().get_queryset()



    def get(self, request, *args, **kwargs):
        data= super().get(request,*args, **kwargs).data
        pk = kwargs['pk']
        patient=Patient.objects.get(reservation__pk=pk)
        user=User.objects.get(pk=patient.User.pk)
        today=date.today()
        bithday=user.age


        response={

            'name':user.name,
            'sex':user.sex,
            'age':today.year-bithday.year-((today.month,today.day)<(bithday.month,bithday.day)),
            'Weight': patient.Weight,
            'High': patient.High,
            'medical':patient.medical,
            'medical_history': patient.medical_history,
            'Prescriptions': data,


        }
        return Response(response)


