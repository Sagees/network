import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('',0))
sock.sendto("hello".encode(), ('115.145.239.18',10080))
