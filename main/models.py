from django.db import models
from django.utils import timezone

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self) -> str:
        return self.title

class ServiceType(models.Model):
    
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service')
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField()
    service = models.ForeignKey(ServiceType, on_delete=models.CASCADE, related_name='doctor')
    
    def __str__(self) -> str:
        return self.name
    
class AppointmentForm(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    service = models.ForeignKey(ServiceType, on_delete=models.CASCADE, related_name='type_service')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctors')
    
    def __str__(self) -> str:
        return self.name
    
class ClientForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=400)
    phone = models.IntegerField()
    message = models.TextField()

    def __str__(self) -> str:
        return self.name