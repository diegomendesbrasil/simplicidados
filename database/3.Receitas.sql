
CREATE TABLE dmb.receita (
	id serial4 NOT NULL,
    iduser INT NOT NULL,
    DtVencimento date NOT NULL,
    dtrecebimento date,
    idcliente int NOT NULL,
    vlreceitaplanejado numeric(10,2) NOT NULL,
    vlreceitarecebido numeric(10,2) NOT NULL,
    parcelas INT NOT NULL,
	CONSTRAINT users_pkey PRIMARY KEY (id)
);