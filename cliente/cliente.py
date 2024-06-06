from include.bus_functions import *

service_name = "serv1"

try:
    print ("Send command")
    message = generate_string(service_name, "meowmeowmeow")
    print('sending {!r}'.format (message))
    sock.sendall (message)
    while True:
    # Look for the response
        amount_received = 0
        amount_expected = int(sock.recv(5))

        while amount_received < amount_expected:
            data = sock.recv (amount_expected - amount_received)
            amount_received += len(data)
            print ('received {!r}'.format (data))
            service_name, status, answer = extract_string_bus(data)
            print("Status:", status)
            print("Service Name:", service_name)
            print("Answer:", answer)
                

finally:
    print ('closing socket')
    sock.close()