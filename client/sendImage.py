import cv2
import requests
import io

uri = 'https://node-red-001.au-syd.mybluemix.net/sendImage'

cap = cv2.VideoCapture(0)
cv2.namedWindow("Camera", cv2.WINDOW_AUTOSIZE)

while True:
	res, frame = cap.read()
	if res:
		resized = cv2.resize(frame, (frame.shape[1] // 2, frame.shape[0] // 2))
		_, img_encoded = cv2.imencode('.jpg', frame)
		files = {'file': ("image.jpg", io.BytesIO(img_encoded), 'image/jpeg')}
		r = requests.post(uri, files=files)
		print(r.text)
		cv2.imshow("Camera", resized)
		cv2.waitKey(4000)