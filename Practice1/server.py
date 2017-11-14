# -*- coding:utf-8 -*-
import socket

#二乗する関数
def Double(number):
    doubles=int(number)**2
    return str(doubles)

host = "127.0.0.1" 
port = 6000

#ソケットを作成する
serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.bind((host,port)) 
serversock.listen(10) 

#クライアントからの要求を待つ
print('Waiting for connections...')
clientsock, client_address = serversock.accept()

#クライアントからの通信後に処理をする部分
while True:
    #クライアントからのsendを受け取る
    rcvmsg = clientsock.recv(4096)
    rcvmsg=rcvmsg.decode("utf-8")
    #データがなければ処理をwhileを抜けて処理を終了する
    if rcvmsg == '':
      break
    #受信した値を二乗にして返す
    double_number=Double(rcvmsg)
    s_msg=double_number.encode("utf-8")
    #クライアントに返事を返す
    clientsock.send(s_msg)
    print("send")
#クライアントとの処理を終了する部分
clientsock.close()
