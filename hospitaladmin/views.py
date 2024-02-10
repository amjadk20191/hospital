from doctor.models import Doctor
from rest_framework import generics,viewsets,views
from .serializers import DoctorSerializer,PatientSerializer,SpecialtySerializer,receptionSerializer
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.parsers import FormParser,MultiPartParser
from patient.models import Patient
from .models import Specialty
from doctor.models import Prescription
from django.db.models import Sum
from django.contrib.auth.models import Group
from rest_framework.reverse import reverse
from doctor.models import Reservation
from core.models import User
from rest_framework.response import Response
from .permissions import adminonly,receptiononly
from patient.models import exp
from core.models import User
class  DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [ adminonly]

    def destroy(self, request, *args, **kwargs):
        instance = User.objects.get(doctor__pk=kwargs['pk'])
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
class  receptionViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = receptionSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [ adminonly]
    def get_queryset(self):
        reception_group = Group.objects.get(name='reception')
        queryset = reception_group.user_set.all()
        return queryset





class  PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [ adminonly]

    def destroy(self, request, *args, **kwargs):
            instance = User.objects.get(patient__pk=kwargs['pk'])
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)








class  SpecialtyViewSet(viewsets.ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    permission_classes = [ adminonly]




class  PayMoney(views.APIView):
    permission_classes = [ receptiononly]


    def post(self, request, *args, **kwargs):
        data = request.data
        if not 'username' in data :
            return Response({"username": " This field may not be blank"}, status=status.HTTP_400_BAD_REQUEST)

        if  not Patient.objects.filter(User__username=data['username']).exists():
            return Response( {"detail": "there no patient with is username "}, status=status.HTTP_400_BAD_REQUEST)
        id_patient=Patient.objects.filter(User__username=data['username'])[0].pk
        sum_of_Money=Reservation.objects.filter(Patient__User__username=data['username']).filter(payed=False).aggregate(Sum('Money'))['Money__sum']
        if sum_of_Money is None:
            return Response({"detail":"Installments have been paid"})
        response={
            "money":sum_of_Money,
            "pay":reverse("PayMoney", kwargs={"pk":id_patient}, request=request)

        }

        return Response(response)



class  PayMoney2(views.APIView):
    permission_classes = [ receptiononly]


    def post(self, request,pk, *args, **kwargs):

        money= Reservation.objects.filter(Patient__pk=pk).filter(payed=False).exclude(Money=0)
        if money.exists():
            money.update(payed=True)
            return Response({"detail": "done"})
        return Response({"detail": "error"}, status=status.HTTP_400_BAD_REQUEST)



