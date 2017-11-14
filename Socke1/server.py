# -*- coding:utf-8 -*-
import socket
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
    print ('Received -> %s' % (rcvmsg))
    #データがなければ処理をwhileを抜けて処理を終了する
    if rcvmsg == '':
      break
    print ('Recepi message...')
    s_msg = "Get answer"
    s_msg=s_msg.encode("utf-8")
    #クライアントに返事を返す
    clientsock.send(s_msg)
    print ("send message")
#クライアントとの処理を終了する部分
clientsock.close()
