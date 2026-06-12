CREATE DATABASE IF NOT EXISTS Myapp_base;

USE Myapp_base;

CREATE TABLE IF NOT EXISTS info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mesaj VARCHAR(255) NOT NULL
);

INSERT INTO info (mesaj)
VALUES ('Conexiunea dinte my sql flask a fost realizat cu succes');