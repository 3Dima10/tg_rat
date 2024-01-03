import cv2
from time import sleep

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 20)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

codec = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('video.mp4', codec, 25.0, (1280, 720))

while True:
    ret, frame = cap.read()
    cv2.imshow('Web-camera', frame)
    out.write(frame)

    sleep(20)
    break

out.release()
cap.release()
cv2.destroyWindow()