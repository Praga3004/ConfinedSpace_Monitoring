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

def video_feed(request):
    # FourCC code for video recording (adjust as needed)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    # Flag for recording status
    is_recording = False

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Unable to capture frame from webcam")
            break

        results = model(frame)
        labels = ['boots', 'face_mask', 'face_nomask', 'glasses', 'goggles', 'hand_glove', 'hand_noglove', 'head_helmet', 'head_nohelmet', 'person', 'shoes', 'vest']

        detected_objects = []
        for result in results:
            boxes = result.boxes
            for box in boxes:
                cls_id = labels[int(box.cls.item())]
                confidence = box.conf.item()

                # Update recording status based on detected labels
                if cls_id in ['hand_noglove', 'head_nohelmet', 'face_nomask'] and not is_recording:
                    is_recording = True
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    video_writer = cv2.VideoWriter(f'recording_{timestamp}.avi', fourcc, 20.0, (frame.shape[1], frame.shape[0]))
                    print("Start recording!")

                elif cls_id in ['hand_glove', 'head_helmet', 'face_mask'] and is_recording:
                    is_recording = False
                    video_writer.release()
                    print("Stop recording and save video!")

                detected_objects.append({
                    'label': cls_id,
                    'confidence': confidence
                })

        # Optionally process the frame for display (e.g., draw bounding boxes)
        # ... (your logic to draw bounding boxes and labels on the frame)

        # Record frame if recording is active
        if is_recording:
            video_writer.write(frame)

        # Display the frame (assuming you have a mechanism to send the frame data to the client)
        # ... (your logic to send the frame data to the client-side for display)

        # Exit loop if 'q' key is pressed
        if cv2.waitKey(1) == ord('q'):
            break

    # Release resources
    if is_recording:
        video_writer.release()
    cap.release()
    cv2.destroyAllWindows()

    return HttpResponse('Streaming stopped')