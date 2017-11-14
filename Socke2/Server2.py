import socketserver

#IPアドレスとポート番号を設定する
Host="127.0.0.1"
port=6000

#StreamRequestHandlerを継承して新しいクラスを定義する
#ここでのhandleの中身はユーザが勝手に設定してよい
class Myhandler(socketserver.StreamRequestHandler):
    def handle(self):
        while True:
            #以下からのself.requestはクライアントからの要求に対する属性
            #クライアントからのデータを受け取る
            data=self.request.recv(1024).decode("utf-8")
            print(data)
            #受信データがなければwhileをぬける
            if len(data)==0:
                break
            request_data="GETS".encode("utf-8")
            #クライアントにデータを送信する 
            self.request.send(request_data)
        #ハンドルを閉じる
        self.request.close()

#実際のmainはここからははじまる
#TCPサーバを作成する
#引数にはIPとポート番号,自分が定義したハンドルクラスを設定
server=socketserver.TCPServer((Host,port),Myhandler)
#getsocknameは現在自分が設定したソケットの情報が表示される
print("listen", server.socket.getsockname())
#サーバを永久に稼働させる
server.serve_forever()


