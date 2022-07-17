import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('192.168.56.103', 1233))
resp = client.recv(2048)
# Input UserName
name = input(resp.decode())
client.send(str.encode(name))
resp = client.recv(2048)
# Input Password
password = input(resp.decode())
client.send(str.encode(password))
resp = client.recv(2048)
''' Response : Connection Status :
        1 : Success in register
        2 : Success to connect
        3 : Fail to login
'''
# Receive response
resp = client.recv(2048)
resp = resp.decode()

print(resp)
client.close()
