from django.contrib import admin

from .models import Doctor, Reservation, Prescription


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'User',
        'License',
        'certificate',
        'specialty',
        'From',
        'To',
    )
    list_filter = ('User', 'specialty')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'Doctor', 'Patient', 'Day', 'Time', 'Money', 'payed')
    list_filter = ('Doctor', 'Patient', 'Day')


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'Reservation', 'Diagnosis','treatment','symptoms', 'Image')
    list_filter = ('Reservation', )
