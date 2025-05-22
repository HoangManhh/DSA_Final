from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

# Khởi tạo Flask app và CORS
app = Flask(__name__)
CORS(app)

# Load mô hình và label encoder
model = joblib.load("model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Danh sách triệu chứng
symptoms = ['headache', 'runny_nose', 'fever', 'cough', 'sore_throat', 'sneeze', 'fatigue', 'nausea']

@app.route('/', methods=['GET'])
def hello():
    return "Hello World!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Lấy dữ liệu JSON từ request
        data = request.get_json()
        if not data:
            return jsonify({"error": "Không có dữ liệu JSON được gửi"}), 400

        # Kiểm tra xem tất cả triệu chứng có trong dữ liệu
        input_data = {symptom: data.get(symptom, "no") for symptom in symptoms}
        for symptom in symptoms:
            if input_data[symptom] not in ["yes", "no"]:
                return jsonify({"error": f"Giá trị của {symptom} phải là 'yes' hoặc 'no'"}), 400

        # Tạo DataFrame và dự đoán
        input_df = pd.DataFrame([input_data])
        input_df = input_df.replace({"yes": 1, "no": 0})
        pred = model.predict(input_df)[0]
        prediction = label_encoder.inverse_transform([pred])[0]

        # Trả về kết quả
        return jsonify({"disease": prediction})

    except Exception as e:
        return jsonify({"error": f"Lỗi khi xử lý: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=3636)