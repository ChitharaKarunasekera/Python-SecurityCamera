import cv2
import time
import datetime

# access and activate the webcam
cap = cv2.VideoCapture(0)  # the number of video devices

# setup cascade classifier
# pass through a classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")  # to identify face
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")  # to identify body

detection = False
detection_stopped_time = None
timer_started = False
SECONDS_TO_RECORD_AFTER_DETECTION = 5;

frame_size = (int(cap.get(3)), int(cap.get(4)))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # format of recordings

while (True):
    _, frame = cap.read()  # reading one frame from video capture device

    # gives a new image in gay scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # the image
    # detecting faces and bodies
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # returns a list of positions of all faces in frame
    bodies = face_cascade.detectMultiScale(gray, 1.3, 5)  # returns a list of positions of all bodies in frame

    # if a face or body is detected,
    if len(faces) + len(bodies) > 0:
        # check if recording was started
        if detection:
            timer_started = False  # reset timer

        # if recording was not started,
        else:
            detection = True  # stared recording
            concurrent_time = datetime.datetime.now().strftime(
                "%d-%m-%Y-%H-%M-%S")  # make file name the time of detection
            out = cv2.VideoWriter(f"{concurrent_time}.mp4", fourcc, 20, frame_size)
            print("Started Recording!")
    # if recording is on, keep recoring if the timer is not expired and keep recording if faces are detected
    elif detection:
        if timer_started:
            if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                detection = False
                timer_started = False
                out.release()
                print("Stop Recording!")
        else:
            timer_started = True
            detection_stopped_time = time.time()

    if detection:
        out.write(frame)

    # Draw where the faces are. The position of the face
    #
    # for (x, y, width, height) in faces:
    #     # on the frame named frame, draws a rectangle around face
    #     cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)

    # will be faster if the frame is not displayed
    cv2.imshow("Camera", frame)  # title of the camera that shows the video frame

    # Avoid infinite loop
    if cv2.waitKey(1) == ord('q'):
        break

out.release()
# Release the webcam
cap.release()
cv2.destroyAllWindows()  # destroy the window that shows the video
