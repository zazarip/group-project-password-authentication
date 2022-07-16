import socket
import os
import threading
import hashlib


# Create Socket (TCP) Connection
ServerSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) 
host = '127.0.0.1'
port = 1233
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)
HashTable = {}

# Function : For each client 
def threaded_client(connection):
    connection.send(str.encode('ENTER USERNAME : ')) # Request Username
    name = connection.recv(2048)
    connection.send(str.encode('ENTER PASSWORD : ')) # Request Password
    password = connection.recv(2048)
    password = password.decode()
    name = name.decode()
    password=hashlib.sha256(str.encode(password)).hexdigest() # Password hash using SHA256
    
    #REGISTERATION PHASE
    #Register new user in Hashtable Dictionary
        if name not in Hashtable:
            Hashtable[name] = password
            conn.send(str.encode('SUCCESS IN REGISTRATION!'))
            print('Registered account: ',name)
            print("{:<8} {:<20}".format('USER','PASSWORD'))
            for k, v in HashTable.items():
                label, num = k, v
            print("{:<8} {:<20}".format(label,num))
            print("**********************")
            
        else: 
            #Check if the entered password is correct for existing user 
            if(HashTable[name] == password):
                conn.send(str.encode('Success to connect...'))
                print('Connected account: ', name)
            else:
                conn.send(str.encode('FAIL TO LOGIN!'))
                print(' Connection Denied: ',name)
                
            while True: 
                break 
                conn.close()
                
        while True: 
            Client, address = ServerSocket.accept()
            Client_handler = threading.Thread(
                    target = threaded client,
                    args = (Client,)
            )
            client_handler.start()
            ThreadCount += 1
            print('Connection Request: ' + str(ThreadCount))
  ServerSocket.close()
                
