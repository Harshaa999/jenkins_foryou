import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))
    
    # Client receives hello
    print(client.recv(1024).decode())
    
    # Client sends username
    client.send(b'user')
    
    # Client sends password
    client.send(b'pass')
    
    # Client receives success or failure
    print(client.recv(1024).decode())
    
    client.close()

if __name__ == "__main__":
    main()
