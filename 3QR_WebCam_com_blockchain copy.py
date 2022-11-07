import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import time
from polygonscan import PolygonScan

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
var = 0
while True:
    _, frame = cap.read()
    var = var +1
    print(var)
    if var >= 7:
        decodedObjects = pyzbar.decode(frame)
        for data in decodedObjects:
            wallet = str(data[0])
            data2 = wallet.find("0x")
            if len(wallet) >= 40:
                    wallet = wallet[data2:42+data2]
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
            var = -1
#            cv2.waitKey(1000)

    if var >= 50:
        var =1

    cv2.imshow("QR Scanner", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
