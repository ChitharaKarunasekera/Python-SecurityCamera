import cv2
import time
import datetime

# access and activate the webcam
cap = cv2.VideoCapture(0)  # the number of video devices

# setup cascade classifier
# pass through a classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")  # to identify face
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")  # to identify body

recording = True

frame_size = (int(cap.get(3)), int(cap.get(4)))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")#formate of recordings
out = cv2.VideoWriter("video.mp4", fourcc, 20, frame_size)

while (True):
    _, frame = cap.read()  # reading one frame from video capture device

    # gives a new image in gay scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # the image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # returns a list of positions of all faces in frame
    bodies = face_cascade.detectMultiScale(gray, 1.3, 5)  # returns a list of positions of all bodies in frame

    if len(faces) + len(bodies) > 0:
        recording = True

    out.write(frame)

    # Draw where the faces are. The position of the face
    #
    # for (x, y, width, height) in faces:
    #     # on the frame named frame, draws a rectangle around face
    #     cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)

    cv2.imshow("Camera", frame)  # title of the camera that shows the video frame

    # Avoid infinite loop
    if cv2.waitKey(1) == ord('q'):
        break

out.release()
# Release the webcam
cap.release()
cv2.destroyAllWindows()  # destroy the window that shows the video
