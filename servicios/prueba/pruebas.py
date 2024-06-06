
#Extrae los atributos del string recibido del bus
def extract_string(input_string):
    input_string = input_string.decode()  # Convert byte string to regular string
    length = int(input_string[:5])
    service_name = input_string[5:10]  # Extract the next 5 characters as the service name
    command = input_string[10:length+10]  # Skip the service name and extract the rest of the string
    return service_name, command

#Extraer respuesta del string recibido del bus con status
def extract_string_bus(input_string):
    input_string = input_string.decode()  # Convert byte string to regular string
    length = int(input_string[:5])
    service_name = input_string[5:10]  # Extract the next 5 characters as the service name
    status = input_string[10]  # Extract the status character
    command = input_string[11:length+10]  # Skip the status and service name, and extract the rest of the string
    return service_name, status, command

# Genera el string para enviar al bus
def generate_string(service_name, command):
    length = len(command)
    input_string = f"{length:05d}{service_name[:5]}{command}".encode()
    return input_string



# Ejemplo recibiendo un string del bus
# result = extract_string(b"00005echosmeowmeowmeow")
# service_name, command = result
# print("Service Name:", service_name)
# print("Command:", command)

# Ejemplo generando un string para enviar al bus
# service_name = "echos"
# command = "meowmeowmeow"
# input_string = generate_string(service_name, command)
# print("Generated String:", input_string)

# Envia sinit al bus



