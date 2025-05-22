from django.db import models

class Doctor(models.Model):
    TITLE_CHOICES = [
        ('medical_doctor', 'Bác sĩ thường'),
        ('attending_physician', 'Bác sĩ điều trị chính'),
        ('department_head', 'Trưởng khoa'),
        ('resident', 'Bác sĩ nội trú'),
        ('intern', 'Bác sĩ thực tập'),
    ]
    
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    title = models.CharField(max_length=50, choices=TITLE_CHOICES, default='medical_doctor')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.get_title_display()}"