from django.contrib import admin
from .models import Service, ServiceType, Doctor, AppointmentForm, ClientForm 
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = []
    list_filter = []
    search_fields = []

@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = []
    list_filter = []
    search_fields = []
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = []
    list_filter = []
    search_fields = []
@admin.register(AppointmentForm)
class AppointmentFormAdmin(admin.ModelAdmin):
    list_display = []
    list_filter = []
    search_fields = []
@admin.register(ClientForm)
class ClientFormAdmin(admin.ModelAdmin):
    list_display = []
    list_filter = []
    search_fields = []