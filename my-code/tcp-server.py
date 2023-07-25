import socket
import threading

#define the address and port 
host = "0.0.0.0"
port = 7878

def main():
    #create the socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #bind the socket to the defined address and port (using the bind method)
    server.bind((host, port))
    #listen for incoming connection (using the listen method)(in this case 5 maximum connections)
    server.listen(5)
    print(f"[*] Listening on {host}:{port}")

    #create a connection loop
    while True:
        client, address = server.accept()
        print(f"[*] Accepted connection from {address[0]}:{address[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f"[*] Received: {request.decode('utf-8')}")
        print(client_socket.getpeername())
        sock.send(b"WELCOME TO THE PYTHON CLAN KIRIKO")

if __name__ == "__main__":
    main()