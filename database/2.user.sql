-- public.users definition

-- Drop table

-- DROP TABLE public.users;
CREATE TABLE dmb.users (
	id serial4 NOT NULL,
	nome varchar(255) NULL,
	cpf_cnpj varchar(50) NULL,
	aniversario date NULL,
	sexo varchar(50) NULL,
	endereco varchar(255) NULL,
	cep numeric(8) NULL,
	cidade varchar(150) NULL,
	estado varchar(150) NULL,
	telefone varchar(50) NULL,
	empresa varchar(255) NULL,
	email varchar(255) NULL,
	login varchar(50) NULL,
	senha varchar(100) NULL,
	dtiniciocontrato date NOT NULL,
	dtfimcontrato date,
	statuscontrato varchar(100),   ----ativo, inativo, atrasado, etc
	CONSTRAINT users_pkey PRIMARY KEY (id)
);