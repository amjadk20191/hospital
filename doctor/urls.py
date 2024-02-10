from django.urls import path,include
from rest_framework import routers
from .views import ShowReservation,PrescriptionListCreate
router = routers.DefaultRouter()
urlpatterns = [
    path('showreservation/', ShowReservation.as_view(), name="showreservation"),
    path('prescription/<int:pk>/', PrescriptionListCreate.as_view(), name="prescription"),

    path('', include(router.urls)),

]