import socket

host = "127.0.0.1" 
port = 6000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

client.connect((host, port)) 
print("数字を入力してください")
messages=input()
messages=messages.encode("utf-8")
client.send(messages) 

response = client.recv(4096)
response=response.decode("utf-8")
print('Answer:%s' % response)
