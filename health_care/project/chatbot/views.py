from django.shortcuts import render
from patient_management.models import Patient
import requests
import json
from datetime import datetime

def predict_disease(request):
    symptoms = ['headache', 'runny_nose', 'fever', 'cough', 'sore_throat', 'sneeze', 'fatigue', 'nausea']
    
    if request.method == 'POST':
        # Lấy dữ liệu từ JSON gửi từ client
        try:
            data = json.loads(request.body)
            patient_name = data.get('patient_name', 'Anonymous')
            patient_status = data.get('patient_status', 'outpatient')  # Mặc định là ngoại trú
            answers = {symptom: data.get(symptom, 'no') for symptom in symptoms}
            
            # Gửi yêu cầu đến API
            response = requests.post('http://localhost:3636/predict', json=answers)
            response.raise_for_status()
            prediction = response.json()
            disease = prediction.get('disease', 'Không có kết quả')
            
            # Lưu vào lịch sử dự đoán của bệnh nhân
            patient, created = Patient.objects.get_or_create(
                name=patient_name,
                defaults={
                    'age': 0,
                    'gender': 'other',
                    'address': '',
                    'phone': '',
                    'status': patient_status
                }
            )
            history = json.loads(patient.prediction_history or '[]')
            history.append({
                'disease': disease,
                'symptoms': answers,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
            patient.prediction_history = json.dumps(history)
            patient.status = patient_status
            patient.save()
            
            return render(request, 'health_predictor/index.html', {
                'symptoms': symptoms,
                'prediction': disease,
                'patient_name': patient_name,
                'patient_status': patient_status
            })
        except requests.exceptions.RequestException as e:
            return render(request, 'health_predictor/index.html', {
                'symptoms': symptoms,
                'error': f'Lỗi khi gọi API: {str(e)}',
                'patient_name': patient_name,
                'patient_status': patient_status
            })
        except json.JSONDecodeError:
            return render(request, 'health_predictor/index.html', {
                'symptoms': symptoms,
                'error': 'Dữ liệu gửi không hợp lệ',
                'patient_name': patient_name,
                'patient_status': patient_status
            })
    
    return render(request, 'health_predictor/index.html', {
        'symptoms': symptoms,
        'patient_statuses': Patient.STATUS_CHOICES
    })