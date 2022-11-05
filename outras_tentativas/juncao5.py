import cv2
import webbrowser
import time


cap = cv2.VideoCapture(0)
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()
a = ''
var = -1
data = "oie"
while True:
    _, img = cap.read()
    var = var +1 
    print(var)
    if var >= 7:
        data, bbox, _ = detector.detectAndDecode(img)
        print(data)

    if data != a:
        a= data
        print(data)
        cv2.waitKey(1000)
        var = -1
        #while cv2.waitKey(1000) != ord('q'):
        #    a = 2

    cv2.imshow("QRCODEscanner", img)
    if cv2.waitKey(1) == ord("H"):
        b = 2