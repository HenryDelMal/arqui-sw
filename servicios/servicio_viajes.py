from include.bus_functions import *

service_name = "VIAJE"

#bdd_service = "SERBD"

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
            if (sinit == 1):
                 sinit = 0
                 print("sinit ok")
            else:
                # If is not a SINIT message, then is a command from the client
                incoming_svr, command = extract_string_client(data)
                print("Incoming for:",incoming_svr)
                if incoming_svr==service_name: # Check if the command is for me
                    print("That's for me")
                    print("Command:", command)

                    if command.startswith("GET"):
                        recorrido = command[3:]
                        query = "SELECT buses.patente, viajes.localizacion FROM buses JOIN viajes ON buses.id = viajes.bus_id WHERE viajes.recorrido_id = '{}' AND viajes.estado = 'en_curso';".format(recorrido)
                        answer = servbd_query(query)
                        if answer == "" or answer == "ERROR":
                            message = generate_string(service_name, "ERROR")
                            print('sending {!r}'.format (message))
                            sock.sendall (message)
                        else:
                            message = generate_string(service_name, answer)
                            print('sending {!r}'.format (message))
                            sock.sendall (message)

finally:
    print ('closing socket')
    sock.close()