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

def registro(service_name):
    print(service_name)
    check = True
    while check:
        print("Seleccione el tipo:")
            
        print("1. Conductor")
        print("2. Operador")

        op = input("Ingrese opción:")
        match op:
            case "1":
                type = "conductor"
                check = False
            case "2":
                type = "operador"
                check = False
            case _:
                print("Opción no válida. Por favor, ingrese 1 o 2.")
                
    username = input("Ingrese usuario: ")
    password = input("Ingrese password: ")

    message = generate_string(service_name, 'INS,{},{},{}'.format(username, password, type))
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
                return username, answer
        break
def registro_bus(service_name):
    print(service_name)
                
    patente = input("Ingrese patente: ")
    modelo = input("Ingrese modelo: ")
    estado = input("Ingrese estado: ")
    message = generate_string(service_name, 'INS,{},{},{}'.format(patente, modelo, estado))
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
                return patente, answer
        break
def registro_recorrido(service_name):
    print(service_name)
                
    id = input("Ingrese id: ")
    inicio = input("Ingrese inicio: ")
    final = input("Ingrese final: ")
    message = generate_string(service_name, 'INS,{},{},{}'.format(id, inicio, final))
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

def main():
    logged_in = False
    username = None
    user_type = None

    username, user_type = iniciar_sesion('LOGIN')

    if user_type == 'admin':
        logged_in = True
    else:
        print("Usuario no es un administrador. Saliendo del programa.")
        sock.close()
        return


    while logged_in:
        if logged_in:
            print("Hola {} de rol {}, seleccione una opción:".format(username, user_type))
        else:
            print("Seleccione una opción:")
            
        print("1. Registrar usuario")
        print("2. Registrar bus")
        print("3. Registrar recorrido")
        print("4. Salir")
        
        option = input("Ingrese opción: ")

        match option:
            case '1':
                registro("REGIS")
            case '2':
                registro_bus("BUSES")
            case '3':
                registro_recorrido("RECOR")
            case '4':
                print("Saliendo del programa.")
                sock.close()
                break
            case _:
                print("Opción no válida. Por favor, ingrese 1 o 2.")

if __name__ == "__main__":
    main()
