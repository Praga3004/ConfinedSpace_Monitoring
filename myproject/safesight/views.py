from django.shortcuts import render, HttpResponse
import datetime
import cv2
from ultralytics import YOLO

# Load the YOLOv8 model (outside the view function for efficiency)
model = YOLO('safesight\\best.pt')  # Replace with your model path

def detect_objects(request):
    if request.method == 'GET':
        return render(request, 'camera_stream.html')  # Render template for camera access
    else:
        return HttpResponse('Invalid request')
