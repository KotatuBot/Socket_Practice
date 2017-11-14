import socketserver

#サーバで処理する関数を定義
#文字列から計算を行う関数
def calculate(datas):
    #データを分ける
    data_list=datas.split(",")
    if data_list[0]=="add":
        result=int(data_list[1])+int(data_list[2])
    elif data_list[0]=="sub":
        result=int(data_list[1])-int(data_list[2])
    elif data_list[0]=="mul":
        result=int(data_list[1])*int(data_list[2])
    elif data_list[0]=="div":
        result=int(data_list[1])/int(data_list[2])
    else:
        pass

    return str(result)




#IPアドレスとポート番号を設定する
Host="127.0.0.1"
port=9000

#StreamRequestHandlerを継承して新しいクラスを定義する
#ここでのhandleの中身はユーザが勝手に設定してよい
class Myhandler(socketserver.StreamRequestHandler):
    def handle(self):
        while True:
            #以下からのself.requestはクライアントからの要求に対する属性
            #クライアントからのデータを受け取る
            data=self.request.recv(1024).decode("utf-8")
            #受信データがなければwhileをぬける
            if len(data)==0:
                break
            #関数を呼び出す
            result=calculate(data)
            #クライアントに計算結果を返す
            self.request.send(result.encode("utf-8"))
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


