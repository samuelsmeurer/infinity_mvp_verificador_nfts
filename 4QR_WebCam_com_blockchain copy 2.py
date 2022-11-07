import mysql.connector
import pymysql.cursors
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import time
from polygonscan import PolygonScan
from cryptography.fernet import Fernet
import datetime

#lendo chave de criptografia
file = open('qrcode/chave.key', 'rb')
chave_lida = file.read()
file.close()

cifra = Fernet(chave_lida)

#pegando informações do db criptografada
file = open('qrcode/dados_bd.txt', 'rb')
arquivo = file.read()

#descriptando a as informações do db a partir da chave
texto = cifra.decrypt(arquivo)

#criando variável com as infos descriptografadas
arq = str(texto, 'utf-8')
file.close()

#realizando tratamento dos dadospara ler as informações
arq = arq.split('\n')

#lendo as informações e realizando a conexão com db
dados = []
for linha in range(len(arq)):
    dados.append(arq[linha].rstrip())

try:
    conexao = pymysql.connect(
        host = dados[0],
        port = int(dados[1]),
        user = dados[2],
        password = dados[3],
        database = dados[4],
    )
    conectado = True
    bd = dados[4]

except:
    print('Impossível se conectar ao Banco de Dados!')

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
var = 0
id = 1000
ticketusado = list()

def verificador_polygon():

    for data in decodedObjects:
            wallet = str(data[0])
            data2 = wallet.find("0x")
            if len(wallet) >= 40:
                    wallet = wallet[data2:42+data2]
                    save = 0
                    with PolygonScan("WDDZGYYWAGAC446V2JHQT93NW4F1TX6P9Q",False) as matic:
                        save = (matic.get_acc_balance_by_token_and_contract_address("0xa661E867871E4D6479504c6ED296bEEbe6CAfF6d",wallet))
                        save = int(save)
                        save2 =0
                        with conexao.cursor() as cursor:
                            conexao.commit()
                            cursor.execute('select * from ticketusado')
                            ticketusado = cursor.fetchall()
                        cursor.close()
                        for i in range(len(ticketusado)):
#                            id =id +1
                            if ticketusado[i][1] == wallet:
                                print('ACESSO NEGADO!!! O ticket {} já foi utilizado no dia {} '.format(wallet,ticketusado[i][2]))
                                return 0
                            else:
                                save2 = 1
                        save3 = save *save2
                        if save3 == 1:
                            with conexao.cursor() as cursor:
                                cursor.execute('insert into ticketusado values( {}, "{}" , "{}")'.format(id,wallet,datetime.datetime.now()))
                                conexao.commit()
                            cursor.close()
                            print('O seu ingresso "{}" acabou de ser utilizado!'.format(data))
                            time.sleep(1)
                        if save == 0:
                            time.sleep(1)
                            print("Infelizmente sua carteira {} não está permitida no evento!".format(wallet))
            else:
                print("sua informação {} não representa uma carteira virtual!".format(data))


while True:
    _, frame = cap.read()
    var = var +1
    if var >= 7:
        decodedObjects = pyzbar.decode(frame)
        verificador_polygon()
        var = -1
    if var >= 50:
        var =1

    cv2.imshow("QR Scanner", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
