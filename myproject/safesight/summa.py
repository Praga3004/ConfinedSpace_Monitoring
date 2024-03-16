import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Unable to capture frame from webcam")
        break

    # Process frame here (e.g., display it)

    cv2.imshow('Webcam Stream', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
