
CREATE TABLE dmb.cliente (
	id serial4 NOT NULL,
    nome VARCHAR(300) NOT NULL,
    cpf_cnpj INT NOT NULL,
    telefone numeric(20,0),
    telefone2 numeric(20,0),
    telefone3 numeric(20,0),
    dtnascimento date NOT NULL,
    dtcadastro date autodatetime,
	CONSTRAINT users_pkey PRIMARY KEY (id)
);

CREATE TABLE dmb.fornecedor (
	id serial4 NOT NULL,
    nome VARCHAR(300) NOT NULL,
    cpf_cnpj INT NOT NULL,
    telefone numeric(20,0),
    telefone2 numeric(20,0),
    telefone3 numeric(20,0),
    dtcadastro date autodatetime,
	CONSTRAINT users_pkey PRIMARY KEY (id)
);