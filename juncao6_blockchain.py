import cv2
import time
from polygonscan import PolygonScan


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
            data2 = data.find("0x")
            if len(data) >= 40:
                wallet = data[data2:42+data2]
                save = 0
                with PolygonScan("WDDZGYYWAGAC446V2JHQT93NW4F1TX6P9Q",False) as matic:
                    save = (matic.get_acc_balance_by_token_and_contract_address("0xa661E867871E4D6479504c6ED296bEEbe6CAfF6d",wallet))
                    save = int(save)
                    if save == 1:
                        print("Bem vindo! Sua carteira {} está validado!".format(wallet))
                        time.sleep(1)
                    if save == 0:
                        time.sleep(1)
                        print("Infelizmente sua carteira {} não está permitida no evento!".format(wallet))
            else:
                print("sua informação {} não representa uma carteira virtual!".format(data))
            cv2.waitKey(2000)
        var = -1
        #while cv2.waitKey(1000) != ord('q'):
        #    a = 2

    cv2.imshow("QRCODEscanner", img)
    if cv2.waitKey(1) == ord("H"):
        b = 2