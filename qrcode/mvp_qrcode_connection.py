import mysql.connector
import pymysql.cursors
import cv2
import webbrowser
import datetime
import time
from cryptography.fernet import Fernet

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


ticketusado = list()
def callwebcan(x):

    with conexao.cursor() as cursor:
        conexao.commit()
        cursor.execute('select * from ticketusado')
        ticketusado = cursor.fetchall()
    cursor.close()
    x = x.upper()
    id = 1000
    try:    
        encontrado = 0
        for i in range(len(ticketusado)):
            id =id +1
            if ticketusado[i][1] == x:
                print('ACESSO NEGADO!!! O ticket {} já foi utilizado no dia {} '.format(x,ticketusado[i][2]))
                encontrado += 1
                return 0

                
                
        if encontrado ==0:
            print("entrei aqui")
            with conexao.cursor() as cursor:
                print(a)
                cursor.execute('insert into ticketusado values( {}, "{}" , "{}")'.format(id,x,datetime.datetime.now()))
                conexao.commit()
            cursor.close()
            encontrado +=1  
            print('O seu ingresso "{}" acabou de ser utilizado!'.format(data))
            time.sleep(3)
            return 0

    except:
        print("return")
        return 0

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
            a=data
            callwebcan(a)

    #termina programa com comando s
    cv2.imshow("QRCODEscanner", img)    
    if cv2.waitKey(1) == ord("s"):
        break

