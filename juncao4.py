import cv2
import webbrowser
import time


cap = cv2.VideoCapture(0)
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()
a = ''
while True:
    _, img = cap.read()
    
    data, bbox, _ = detector.detectAndDecode(img)

    if data != a:
        a= data
        print(data)
        img = 0
        cap.release()
        cv2.waitKey(1000)
        #while cv2.waitKey(1000) != ord('q'):
        #    a = 2

    cv2.imshow("QRCODEscanner", img)
    if cv2.waitKey(1) == ord("H"):
        b = 2