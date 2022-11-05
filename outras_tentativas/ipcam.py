import cv2

video = cv2.VideoCapture(0)

ip = "https://192.168.100.52:8080"

video.open(ip)

while True:
    check, img = video.read()
    cv2.imshow("img",img)
    cv2.waitKey(1)