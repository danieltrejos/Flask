DROP DATABASE IF EXISTS app_crud_juego;
CREATE DATABASE IF NOT EXISTS app_crud_juego;
USE app_crud_juego;

CREATE TABLE IF NOT EXISTS juegos(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL    
);

INSERT INTO juegos(nombre, descripcion, precio)
VALUES ('Supermetroid', 'Juego de arcade',50000);

INSERT INTO juegos (nombre, descripcion, precio)
VALUES ('%s','%s','%s');
