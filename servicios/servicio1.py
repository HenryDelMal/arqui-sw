from include.bus_functions import *

try:
    # Send data
    message = b'00010sinitservi'
    print ('sending {!r}'.format (message))
    sock.sendall (message)
    sinit = 1
    while True:
    # Look for the response
        amount_received = 0
        amount_expected = 10
        while amount_received < amount_expected:
            data = sock.recv (16)
            amount_received += len(data)
            print ('received {!r}'.format (data))
            if data == b'00010sinitok':
                print("sinit ok")
                break
        break
finally:
    print ('closing socket')
    sock.close()