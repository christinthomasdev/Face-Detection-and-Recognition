import numpy as np 
import cv2
#from PIL import ImageFont, ImageDraw, Image  
cam = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt2.xml')
while(True):

	ret,frame = cam.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
	for (x, y, w, h) in faces:
		#print(x,y,w,h)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]

		img_item = "capfaceGray.png"
		img_item2 = "capfaceColor.png"
		cv2.imwrite(img_item, roi_gray)
		cv2.imwrite(img_item2, roi_color)

		color = (255,0,0)
		stroke = 2
		end_cord_x = x+w
		end_cord_y = y+w
		cv2.rectangle(frame,(x,y),(end_cord_x,end_cord_y), color, stroke) 
	
	#font = ImageFont.truetype("UbuntuMono-regular.ttf", 15)  
	font=cv2.FONT_HERSHEY_PLAIN
	font2=cv2.FONT_HERSHEY_COMPLEX
	img = cv2.rectangle(frame, (0,0), (400,160), (0,0,0), -1)

	cv2.putText(frame, 'FACE DETECTION', (20, 30), font2, 1, (0, 255, 0), 1)
	cv2.putText(frame, 'This Application detects faces', (20, 50), font, 1, (255, 255, 255), 1)
	cv2.putText(frame, 'and stores it as an image.', (20, 70), font, 1, (255, 255, 255), 1)

	cv2.putText(frame, 'A blue rectangle will be formed', (20, 90), font, 1, (255, 255, 255), 1)
	cv2.putText(frame, 'around the faces', (20, 110), font, 1, (255, 255, 255), 1)
	cv2.putText(frame, "Press 'q' to quit the application" , (20, 150), font, 1, (0, 0, 255), 1)

	cv2.imshow('frame',frame)

	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

cam.release()
cv2.destroyAllWindows()

#around your face