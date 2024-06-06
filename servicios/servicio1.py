from include.bus_functions import *

service_name = "serv1"

try:

    # Send SINIT to the bus
    message = generate_sinit(service_name)
    print ('sending {!r}'.format (message))
    sock.sendall (message)
    sinit = 1
    while True:
    # Look for the response
        amount_received = 0
        amount_expected = int(sock.recv(5))
        while amount_received < amount_expected:
            data = sock.recv (amount_expected - amount_received)
            amount_received += len(data)
            print ('received {!r}'.format (data))

            if data == b'sinitOK'+service_name.encode():
                 print("sinit ok")
                 break
        break




finally:
    print ('closing socket')
    sock.close()