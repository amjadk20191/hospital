from django.urls import path,include
from rest_framework import routers
from .views import DoctorViewSet,PatientViewSet,SpecialtyViewSet,PayMoney,PayMoney2,receptionViewSet







router = routers.DefaultRouter()
router.register(r'doctor', DoctorViewSet, basename="doctor")
router.register(r'patient', PatientViewSet, basename="patient")
router.register(r'specialty', SpecialtyViewSet, basename="specialty")
router.register(r'reception', receptionViewSet, basename="reception")
urlpatterns = [
    path('money/', PayMoney.as_view(), name="Money"),
    path('paymoney/<int:pk>/', PayMoney2.as_view(), name="PayMoney"),

    path('', include(router.urls)),

]