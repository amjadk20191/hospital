from django.urls import path,include
from .views import AddReservation,ShowSpecialty,ShowDoctor,TimeReservation

urlpatterns = [
    path('addreservation/<int:pk>/', AddReservation.as_view(), name="addreservation"),
    path('showspecialty/', ShowSpecialty.as_view(), name="showspecialty"),
    path('timereservation/<int:pk>/', TimeReservation.as_view(), name="timereservation"),
    path('showdoctor/<int:pk>/', ShowDoctor.as_view(), name="showdoctor"),

]