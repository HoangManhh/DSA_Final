from django.db import models

class Patient(models.Model):
    STATUS_CHOICES = [
        ('outpatient', 'Bệnh nhân ngoại trú'),
        ('inpatient', 'Bệnh nhân nội trú'),
        ('emergency', 'Bệnh nhân cấp cứu'),
        ('follow_up', 'Bệnh nhân tái khám'),
    ]
    
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('male', 'Nam'), ('female', 'Nữ'), ('other', 'Khác')])
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='outpatient')
    created_at = models.DateTimeField(auto_now_add=True)
    prediction_history = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.get_status_display()}"