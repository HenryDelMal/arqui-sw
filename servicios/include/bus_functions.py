import socket
import sys
# Create a TCP/IP socket
sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the bus is listening
bus_address = ('soabus', 5000)
print ('connecting to {} port {}'.format (*bus_address))
sock.connect (bus_address)

def generate_sinit(service_name):
    length = len(service_name)
    message = f"{length:05d}{'sinit'[:5]}{service_name}".encode()
    return message