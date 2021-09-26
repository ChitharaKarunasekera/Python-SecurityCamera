import cv2
import time
import datetime

# access and activate the webcam
cap = cv2.VideoCapture(0)  # the number of video devices

while (True):
    _, frame = cap.read()  # reading one frame from video capture device

    cv2.imshow("Camera", frame)  # title of the camera that shows the video frame

    # Avoid infinite loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release the webcam
cap.release()
cv2.destroyAllWindows()  # destroy the window that shows the video
