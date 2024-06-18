from include.bus_functions import *

def iniciar_sesion(service_name):
    print(service_name)
    username = input("Ingrese usuario: ")
    password = input("Ingrese password: ")

    message = generate_string(service_name, '{},{}'.format(username, password))
    sock.sendall(message)
    while True:
        amount_received = 0
        amount_expected = int(sock.recv(5))

        while amount_received < amount_expected:
            data = sock.recv(amount_expected - amount_received)
            amount_received += len(data)
            service_name, status, answer = extract_string_bus(data)
            if answer == "ERROR" or status == "NK":
                print("Error al ingresar.")
                return None, None
            else:
                print('Bienvenido {}.'.format(answer))
                return username, answer
        break

def cerrar_sesion():
    print("Sesión cerrada.")
    return None, None

def consultar_estado_bus(service_name):
    print(service_name)
    bus = input("Ingrese bus: ")

    message = generate_string(service_name, '{}'.format(bus))
    sock.sendall(message)
    while True:
        amount_received = 0
        amount_expected = int(sock.recv(5))

        while amount_received < amount_expected:
            data = sock.recv(amount_expected - amount_received)
            amount_received += len(data)
            service_name, status, answer = extract_string_bus(data)
            if answer == "ERROR" or status == "NK":
                print("Error al consultar el estado del bus.")
            else:
                print('Estado del bus: {}.'.format(answer))
            break
        break

def get_list(service_name):
    message = generate_string(service_name, '{}'.format("GET_LIST"))
    sock.sendall(message)
    while True:
        amount_received = 0
        amount_expected = int(sock.recv(5))

        while amount_received < amount_expected:
            data = sock.recv(amount_expected - amount_received)
            amount_received += len(data)
            service_name, status, answer = extract_string_bus(data)
            if answer == "ERROR" or status == "NK":
                print("Error.")
                return -1
            else:
                return answer
        break


def registro_viaje(service_name):
    print(service_name)
    hora_i = input('Ingrese tiempo de inicio en formato "aaaa-mm-dd hh:mm:ss": ')
    hora_f = input('Ingrese tiempo de termino en formato "aaaa-mm-dd hh:mm:ss": ')
    estado = input('Ingrese estado: ')
    localizacion = input('Ingrese localizacion: ')
    bus_id = input('Ingrese el bus\n' + get_list("BUSES")+'\n')
    conductor_id = input('Ingrese el conductor\n' + get_list("REGIS")+'\n')
    recorrido_id = input('Ingrese el recorrido\n' + get_list("RECOR")+'\n')

    # INSERT into viajes (hora_inicio, hora_final, estado, localizacion, bus_id, conductor_id, recorrido_id)
    # values ('2021-06-01 08:00:00', '2021-06-01 09:00:00', 'en_curso', 'Maitencillo Adentro', 1, 1, 101)

    message = generate_string(service_name, 'INS,{},{},{},{},{},{},{}'.format(hora_i, hora_f, estado, localizacion, bus_id, conductor_id, recorrido_id))
    sock.sendall(message)
    while True:
        amount_received = 0
        amount_expected = int(sock.recv(5))

        while amount_received < amount_expected:
            data = sock.recv(amount_expected - amount_received)
            amount_received += len(data)
            service_name, status, answer = extract_string_bus(data)
            if answer == "ERROR" or status == "NK":
                print("Error al ingresar.")
                return None, None
            else:
                print('Se ha ingresado correctamente')
                return id, answer
        break
def registro_anuncio(service_name):
    print(service_name)
    fecha = input('Ingrese fecha del mensaje en formato "aaaa-mm-dd hh:mm:ss": ')
    contenido = input('Ingrese el contenido del anuncio: ')

    # INSERT into viajes (hora_inicio, hora_final, estado, localizacion, bus_id, conductor_id, recorrido_id)
    # values ('2021-06-01 08:00:00', '2021-06-01 09:00:00', 'en_curso', 'Maitencillo Adentro', 1, 1, 101)

    message = generate_string(service_name, 'INS,{},{}'.format(contenido, fecha))
    sock.sendall(message)
    while True:
        amount_received = 0
        amount_expected = int(sock.recv(5))

        while amount_received < amount_expected:
            data = sock.recv(amount_expected - amount_received)
            amount_received += len(data)
            service_name, status, answer = extract_string_bus(data)
            if answer == "ERROR" or status == "NK":
                print("Error al ingresar el anuncio.")
                return None, None
            else:
                print('Se ha registrado el anuncio correctamente')
                return id, answer
        break

def consultar_viajes(service_name):
    print("pendiente")
    pass


def main():
    logged_in = False
    username = None
    user_type = None

    username, user_type = iniciar_sesion('LOGIN')

    if user_type:
        logged_in = True


    while logged_in:
        if logged_in:
            print("Hola {} de rol {}, seleccione una opción:".format(username, user_type))
        else:
            print("Seleccione una opción:")
            
        print("1. Registrar un viaje")
        print("2. Consultar estado del bus")
        print("3. Consultar viajes")
        print("4. Registrar anuncio")
        print("5. Salir")
        
        option = input("Ingrese opción: ")

        match option:
            case '1':
                registro_viaje("VIAJE")
            case '2':
                consultar_estado_bus('BUSES')
            case '3':
                consultar_viajes('VIAJE')
            case '4':
                registro_anuncio('ANUNC')
            case '5':
                print("Saliendo del programa.")
                sock.close()
                break
            case _:
                print("Opción no válida. Por favor, ingrese 1, 2, 3, 4 o 5.")

if __name__ == "__main__":
    main()
