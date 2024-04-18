CREATE TABLE dmb.fornecedor (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(300) NOT NULL,
    cpf_cnpj VARCHAR(14) NOT NULL,
    telefone VARCHAR(15),
    telefone2 VARCHAR(15),
    telefone3 VARCHAR(15),
    dtcadastro DATE DEFAULT CURRENT_DATE NOT NULL
);
