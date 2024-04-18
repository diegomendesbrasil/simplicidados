CREATE TABLE dmb.users (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    cpf_cnpj VARCHAR(14) NOT NULL,
    aniversario DATE,
    sexo VARCHAR(50),
    endereco VARCHAR(255),
    cep VARCHAR(8),
    cidade VARCHAR(150),
    estado VARCHAR(150),
    telefone VARCHAR(15),
    empresa VARCHAR(255),
    email VARCHAR(255) NOT NULL,
    login VARCHAR(50) NOT NULL,
    senha BYTEA NOT NULL,
    dtiniciocontrato DATE NOT NULL,
    dtfimcontrato DATE,
    statuscontrato VARCHAR(100) NOT NULL
);
