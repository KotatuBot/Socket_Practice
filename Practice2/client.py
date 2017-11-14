import socket

host = "127.0.0.1" 
port = 9000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

client.connect((host, port)) 
print("計算結果を返すサービスです")
print("実行する演算子を入力してください")
print("足し算--->add")
print("引き算--->sub")
print("掛け算--->mul")
print("割り算--->div")
operator=input()
print("1つ目の数を入力してください")
one_number=input()
print("2つ目の数を入力してください")
two_number=input()

#入力した値をカンマ区切りで連結する
#encodeする
send_data=operator+","+one_number+","+two_number
client.send(send_data.encode("utf-8")) 

#計算した値を受信する
#decodeで変換する
response = client.recv(4096).decode("utf-8")
print("[Result]")
print(response)
