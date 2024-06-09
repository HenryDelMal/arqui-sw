from include.bus_functions import *

service_name = "BUSES"

bus = input("Ingrese bus: ")

try:
    message = generate_string(service_name, '{}'.format(bus))
    print(message)
    sock.sendall (message)
    while True:
        amount_received = 0
        amount_expected = int(sock.recv(5))

        while amount_received < amount_expected:
            data = sock.recv (amount_expected - amount_received)
            amount_received += len(data)
            service_name, status, answer = extract_string_bus(data)
            if answer == "ERROR" or status == "NK":
                print("Error al ingresar.")
            else:
                print('Estado {}.'.format(answer))
            break
        break

finally:
    sock.close()