import cv2

cap = cv2.VideoCapture(0)
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()
i=0
while True:
    _, img = cap.read()
    data, bbox, _ = detector.detectAndDecode(img)
    if data:
        i=i+1
        print(i)
        print(data)
    if cv2.waitKey(1) == ord("x"):
        break