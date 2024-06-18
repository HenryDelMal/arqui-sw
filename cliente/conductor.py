from include.bus_functions import *
from datetime import datetime

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
def iniciar_viaje(service_name):
    print("pendiente")
    pass

def terminar_viaje(service_name):
    print("pendiente")
    pass

def consultar_ruta(service_name):
    print("pendiente")
    pass

def enviar_alerta(service_name):
    print(service_name)
    # INSERT into incidentes (viaje_id, hora, localizacion, descripcion) values (1, '2021-06-01 08:30:00', 'Maitencillo Adentro', 'Neumatico pinchado')
                
    id = input("Ingrese id del viaje: ")
    hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    localizacion = input("Ingrese localizacion: ")
    descripcion  = input("Ingrese descripcion: ")

    message = generate_string(service_name, 'INS,{},{},{},{}'.format(id, hora, localizacion, descripcion))
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
    pass


def main():
    logged_in = False
    username = None
    user_type = None

    username, user_type = iniciar_sesion('LOGIN')

    if user_type == 'conductor':
        logged_in = True
    else:
        print("Usuario no es un pasajero. Saliendo del programa.")
        sock.close()
        return


    while logged_in:
        if logged_in:
            print("Hola {} de rol {}, seleccione una opción:".format(username, user_type))
        else:
            print("Seleccione una opción:")
            
        print("1. Iniciar viaje")
        print("2. Terminar viaje")
        print("3. Consultar estado de ruta")
        print("4. Enviar alerta de incidente")
        
        print("5. Salir")
        
        option = input("Ingrese opción: ")
        match option:

            case '1':
                iniciar_viaje('VIAJE')
            case '2':
                terminar_viaje('VIAJE')
            case '3':
                consultar_ruta('VIAJE')
            case '4':
                enviar_alerta('INCID')
            case '5':
                print("Saliendo del programa.")
                sock.close()
                break
            case _:
                print("Opción no válida. Por favor, ingrese 1 o 2.")

if __name__ == "__main__":
    main()
