CREATE TABLE clientes(id INTEGER NOT NULL PRIMARY KEY, Nome VARCHAR(100) NOT NULL, CPF VARCHAR(11) NOT NULL, Email VARCHAR(20) NOT NULL, Fone VARCHAR(20), UF VARCHAR(2) NOT NULL );
INSERT INTO clientes values(1, 'Regis', '00000000000', 'rg@email.com', '1100000000', 'SP');
INSERT INTO clientes values(2, 'Abigail', '11111111111', 'abigail@email.com', '1112345678', 'RJ');
INSERT INTO clientes values(3, 'Benedito', '22222222222', 'benedito@email.com', '1187654321', 'SP');
INSERT INTO clientes values(4, 'Zacarias', '33333333333', 'zacarias@email.com', '1199999999', 'RJ');
