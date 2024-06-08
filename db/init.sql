CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    type VARCHAR(50) NOT NULL
);

CREATE TABLE recorridos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    inicio VARCHAR(50) NOT NULL,
    final VARCHAR(50) NOT NULL
);

CREATE TABLE buses (
    id SERIAL PRIMARY KEY,
    patente VARCHAR(6) NOT NULL UNIQUE,
    modelo VARCHAR(50) NOT NULL,
    estado VARCHAR(50) NOT NULL
);

CREATE TABLE viajes (
    id SERIAL PRIMARY KEY,
    hora_inicio TIMESTAMP NOT NULL,
    hora_final TIMESTAMP NOT NULL,
    estado VARCHAR(50) NOT NULL,
    localizacion VARCHAR(255) NOT NULL,
    bus_id INT,
    conductor_id INT,
    recorrido_id INT,
    FOREIGN KEY (bus_id) REFERENCES buses(id),
    FOREIGN KEY (conductor_id) REFERENCES users(id),
    FOREIGN KEY (recorrido_id) REFERENCES recorridos(id)
);

CREATE TABLE incidentes (
    id SERIAL PRIMARY KEY,
    viaje_id INT NOT NULL,
    hora TIMESTAMP NOT NULL,
    localizacion VARCHAR(255) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    FOREIGN KEY (viaje_id) REFERENCES viajes(id)
);


INSERT into users (email, password, type) values ('usuario1', '1234', 'conductor'),
('usuario2', '1234', 'operador'),
('usuario3', '1234', 'admin'),
('usuario4', '1234', 'pasajero');
