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

    if var >= 7:
        data, bbox, _ = detector.detectAndDecode(img)
    if data != a:
        a= data
        if data != "":
            print(data)
            cv2.waitKey(2000)
        var = -1
        #while cv2.waitKey(1000) != ord('q'):
        #    a = 2
    if var >= 50:
        var =8
    cv2.imshow("QRCODEscanner", img)
    if cv2.waitKey(1) == ord("H"):
        b = 2