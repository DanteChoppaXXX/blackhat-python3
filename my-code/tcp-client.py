import socket

#define the server host and port
target_host = "127.0.0.1"
target_port = 7878

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect the client
client.connect((target_host,target_port))
#send some data
client.send(b"HELLO")
#receive some data
response = client.recv(4096)
#output the response
print(response.decode())
#close the connect
client.close()