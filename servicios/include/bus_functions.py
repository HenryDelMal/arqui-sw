import socket
import sys
# Create a TCP/IP socket
sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the bus is listening
bus_address = ('soabus', 5000)
print ('connecting to {} port {}'.format (*bus_address))
sock.connect (bus_address)

def generate_sinit(service_name):
    length = len('sinit'+service_name)
    message = f"{length:05d}{'sinit'}{service_name}".encode()
    return message

def extract_string_bus(input_string):
    input_string = input_string.decode()  # Convert byte string to regular string
    length = int(input_string[:5])
    service_name = input_string[5:10]  # Extract the next 5 characters as the service name
    status = input_string[10]  # Extract the status character
    command = input_string[11:length+10]  # Skip the status and service name, and extract the rest of the string
    return service_name, status, command