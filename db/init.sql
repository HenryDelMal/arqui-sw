CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    type VARCHAR(50) NOT NULL
);

CREATE TABLE recorridos (
    id INT PRIMARY KEY,
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

INSERT into recorridos (id, inicio, final) values (101, 'Maitencillo Adentro', 'Semillero'),
(102, 'Maitencillo Adentro', 'Maitencillo Afuera'),
(103, 'Maitencillo Adentro', 'Linares');

INSERT into buses (patente, modelo, estado) values ('AB1234', 'Mercedes Benz', 'Disponible'),
('CD5678', 'Volvo', 'En mantenimiento'),
('EF9012', 'Scania', 'En servicio');

INSERT into viajes (hora_inicio, hora_final, estado, localizacion, bus_id, conductor_id, recorrido_id) values ('2021-06-01 08:00:00', '2021-06-01 09:00:00', 'en_curso', 'Maitencillo Adentro', 1, 1, 101),
('2021-06-01 08:00:00', '2021-06-01 09:00:00', 'en_curso', 'Maitencillo Adentro', 2, 1, 102),
('2021-06-01 08:00:00', '2021-06-01 09:00:00', 'en_curso', 'Semillero', 3, 1, 103);

INSERT into incidentes (viaje_id, hora, localizacion, descripcion) values (1, '2021-06-01 08:30:00', 'Maitencillo Adentro', 'Neumatico pinchado'),
(2, '2021-06-01 08:30:00', 'Maitencillo Adentro', 'Neumatico pinchado'),
(3, '2021-06-01 08:30:00', 'Maitencillo Adentro', 'Incendio en el motor');