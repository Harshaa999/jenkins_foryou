import socket

def authenticate(conn):
    # Server sends hello
    conn.send(b'hello')
    
    # Server receives username
    username = conn.recv(1024).decode()
    
    # Server receives password
    password = conn.recv(1024).decode()
    
    # Check username and password
    if username == "user" and password == "pass":
        conn.send(b'success')
    else:
        conn.send(b'failure')

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(1)
    print("Server listening...")
    
    conn, addr = server.accept()
    print(f"Connection from {addr}")
    
    authenticate(conn)
    
    conn.close()
    server.close()

if __name__ == "__main__":
    main()
