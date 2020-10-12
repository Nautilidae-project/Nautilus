CREATE DATABASE Nautilus;

CREATE TABLE IF NOT EXISTS usuario(
	userId INT PRIMARY KEY AUTO_INCREMENT,
    nomeUsuario VARCHAR(20) NOT NULL,
    nomeEmpresa VARCHAR(30) NOT NULL,
    nomeFantasia VARCHAR(30) NULL,
    cnpj VARCHAR(15) NOT NULL,
    email VARCHAR(30) NOT NULL,
    tel INT NOT NULL,
    endereco VARCHAR(30) NOT NULL,
    cep INT NOT NULL,
    senha VARCHAR(20) NOT NULL
    );