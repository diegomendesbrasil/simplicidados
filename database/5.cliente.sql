
CREATE TABLE dmb.cliente (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(300) NOT NULL,
    cpf_cnpj VARCHAR(14) NOT NULL,
    telefone VARCHAR(15),
    telefone2 VARCHAR(15),
    telefone3 VARCHAR(15),
    dtnascimento DATE NOT NULL,
    dtcadastro DATE DEFAULT CURRENT_DATE
);