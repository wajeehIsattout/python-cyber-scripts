import cv2
import os

# Get the path to the current user's Documents folder
user_docs_path = os.path.join(os.path.expanduser("~"), "Documents")

# Define the file path where the photo will be saved
output_path = os.path.join(user_docs_path, "webcam_photo.jpg")

# Open the camera
cap = cv2.VideoCapture(0)  # 0 is the default camera (use 1 for an external camera)

# Check if the camera is opened correctly
if not cap.isOpened():
    print("Error: Could not access the camera")
    exit()

# Capture a single frame
ret, frame = cap.read()

if ret:
    # Save the captured frame to a file
    cv2.imwrite(output_path, frame)
    print(f"Photo captured and saved to {output_path}")
else:
    print("Error: Could not capture image")

# Release the camera
cap.release()
cv2.destroyAllWindows()
