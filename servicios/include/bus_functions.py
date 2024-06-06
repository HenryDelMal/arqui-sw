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
    service_name = input_string[:5]  # Extract the first 5 characters as the service name
    status = input_string[5:7]  # Extract the next 2 characters as the status
    command = input_string[7:]  # The rest of the string is the command
    return service_name, status, command

def generate_string(service_name, command):
    length = len(command)
    input_string = f"{length:05d}{service_name[:5]}{command}".encode()
    return input_string

def extract_string_client(input_string):
    input_string = input_string.decode()  # Convert byte string to regular string
    service_name = input_string[:5]  # Extract the first 5 characters as the service name
    command = input_string[5:]  # Skip the service name and extract the rest of the string
    return service_name, command