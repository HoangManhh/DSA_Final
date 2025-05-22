from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialty', 'phone', 'email', 'title']
        widgets = {
            'specialty': forms.TextInput(attrs={'placeholder': 'Ví dụ: Nội khoa, Nhi khoa'}),
            'title': forms.Select(),
        }