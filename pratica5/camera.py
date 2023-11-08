import cv2
import os
import time
from picamera2 import Picamera2
from gpiozero import LED

face_detector = cv2.CascadeClassifier(
 	cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cv2.startWindowThread()

picam2 = Picamera2()

camera_config = picam2.create_preview_configuration(main = {"format" : "XRGB8888", "size": (640, 480)})
picam2.configure(camera_config)

led = LED(18)

#picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888',"size": (640, 480)})

picam2.start()
output_directory = "detected_faces"

os.makedirs(output_directory, exist_ok=True)

while True:
	im = picam2.capture_array()
	grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

	faces = face_detector.detectMultiScale(grey, 1.1, 5)


	for (x, y, w, h) in faces:
		cv2.rectangle(im, (x, y), (x+w, y+h), (0, 255, 0))

		timestamp = int(time.time())
		filename = os.path.join(output_directory, f"faces_{timestamp}.jpg")

		cv2.imwrite(filename, im[y:y+h, x:x+w])

		led.on()
		time.sleep(1)
		led.off()

	cv2.imshow("Camera", im)

	cv2.waitKey(1)
