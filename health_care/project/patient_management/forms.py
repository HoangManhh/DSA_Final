from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'gender', 'address', 'phone', 'status']
        widgets = {
            'gender': forms.Select(choices=[('male', 'Nam'), ('female', 'Nữ'), ('other', 'Khác')]),
            'status': forms.Select(),
            'address': forms.Textarea(attrs={'rows': 4}),
        }