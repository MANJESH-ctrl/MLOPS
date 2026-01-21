FROM python:3.10-slim

WORKDIR /app

COPY flask_app/ /app/

COPY models/preprocessing_encoders.pkl /app/models/preprocessing_encoders.pkl

COPY models/feature_scalers.pkl /app/models/feature_scalers.pkl

COPY models/feature_names.pkl /app/models/feature_names.pkl

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

#local
# CMD ["python", "app.py"]  

#Prod
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--timeout", "120", "app:app"]