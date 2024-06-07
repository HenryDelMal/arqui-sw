CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    type VARCHAR(50) NOT NULL
);

CREATE TABLE recorridos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    inicio VARCHAR(50) NOT NULL,
    final VARCHAR(50) NOT NULL
);

CREATE TABLE buses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patente VARCHAR(6) NOT NULL UNIQUE,
    modelo VARCHAR(50) NOT NULL,
    estado VARCHAR(50) NOT NULL
);

CREATE TABLE viajes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hora_inicio DATETIME NOT NULL,
    hora_final DATETIME NOT NULL,
    estado VARCHAR(50) NOT NULL,
    bus_id INT NOT NULL,
    conductor_id INT NOT NULL,
    recorrido_id INT NOT NULL,
    localizacion VARCHAR(255) NOT NULL,
    FOREIGN KEY (bus_id) REFERENCES buses(id),
    FOREIGN KEY (conductor_id) REFERENCES users(id),
    FOREIGN KEY (recorrido_id) REFERENCES recorridos(id)

CREATE TABLE incidentes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    viaje_id INT NOT NULL,
    hora DATETIME NOT NULL,
    localizacion VARCHAR(255) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    FOREIGN KEY (viaje_id) REFERENCES viajes(id)
);