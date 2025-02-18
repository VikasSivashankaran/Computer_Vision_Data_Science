import cv2

# Initialize the camera (index 0 for the default camera)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    # Capture a single frame
    ret, frame = cap.read()
    if ret:
        # Save the captured image
        cv2.imwrite("capture.jpg", frame)
        print("Image saved as 'capture.jpg'")
    else:
        print("Error: Could not capture image.")

# Release the camera
cap.release()