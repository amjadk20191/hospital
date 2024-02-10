from django.contrib import admin

from .models import Patient, exp


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'User',
        'High',
        'Weight',
        'medical_history',
        'medical',
    )
    list_filter = ('User',)


@admin.register(exp)
class expAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'Patient',
        'dis',
        'statuse',
        'gender',
        'semptoms',
        'pain',
        'location',
        'vomit',
        'pee',
        'heart',
        'breath',
    )
    list_filter = ('Patient',)
