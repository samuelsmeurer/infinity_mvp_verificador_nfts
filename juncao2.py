import cv2
import time
from cryptography.fernet import Fernet
from email.headerregistry import Address
from operator import le
from polygonscan import PolygonScan


def callwebcan(x):
    data2 = data.find("0x")

    wallet = data[data2:42+data2]
    save = 0
    with PolygonScan("WDDZGYYWAGAC446V2JHQT93NW4F1TX6P9Q",False) as matic:
        save = (matic.get_acc_balance_by_token_and_contract_address("0x2977F845d2793461f58C0dc54eBD753076C5AD06",wallet))
        save = int(save)
        if save == 1:
            print("Bem vindo! Sua carteira {} está validado!".format(wallet))
            time.sleep(1)
        if save == 0:
            time.sleep(1)
            print("Infelizmente sua carteira {} não está permitida no evento!".format(wallet))


cap = cv2.VideoCapture(0)

# inicializa o cv2 detector de qrcode
detector = cv2.QRCodeDetector()
teste=0

while True:
    data = teste
    _, img = cap.read()
    data, bbox, _ = detector.detectAndDecode(img)
    if data != teste:    
        if data:
            time.sleep(1)
            a=data
            callwebcan(a)

    #termina programa com comando s
    cv2.imshow("QRCODEscanner", img)    
    if cv2.waitKey(1) == ord("s"):
        break


