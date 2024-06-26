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
                # print('Bienvenido {}.'.format(answer))
                return username, answer
        break

def cerrar_sesion():
    print("Sesión cerrada.")
    return None, None

def consultar_estado_bus(service_name):
    print(service_name)
    method = "GET"
    bus = input("Ingrese recorrido: ")

    message = generate_string(service_name, '{}'.format(method+bus))
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
                print('Próximos buses: \n\n{}\n'.format(answer))
            break
        break

def consultar_anuncios(service_name,user_type):
    print(service_name)   
    message = generate_string(service_name, 'GET,{}'.format(user_type))
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
                print(answer)
                return id, answer
        break
    pass


def main():
    logged_in = True
    username = 'usuario4'
    user_type = 'pasajero'

    #username, user_type = iniciar_sesion('LOGIN')

    if user_type == 'pasajero':
        logged_in = True
    else:
        print("Usuario no es un pasajero. Saliendo del programa.")
        sock.close()
        return


    while logged_in:
        if logged_in:
            print("¡Hola pasajero!, seleccione una opción:".format(username, user_type))
        else:
            print("Seleccione una opción:")
            
        print("1. Consultar recorrido")
        print("2. Consultar anuncios")
        print("3. Salir")
        
        option = input("Ingrese opción: ")

        if option == '1':
            consultar_estado_bus('VIAJE')
        elif option == '2':
            consultar_anuncios('ANUNC', user_type)
        elif option == '3':
            print("Saliendo del programa.")
            sock.close()
            break
        else:
            print("Opción no válida. Por favor, ingrese 1 o 2.")

if __name__ == "__main__":
    main()
