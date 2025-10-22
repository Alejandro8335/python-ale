import socket
import time

# import modules
from B_assembler import Assembler

# create a socket object and set client
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setblocking(False)
# create a client object and set client
ESP32_IP = "192.168.100.219"
ESP32_PORT = 8080