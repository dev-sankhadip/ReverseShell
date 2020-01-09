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