
CREATE TABLE dmb.despesa (
	id serial4 NOT NULL,
    iduser INT NOT NULL,
    DtVencimento date NOT NULL,
    dtpagamento date,
    idFornecedor int NOT NULL,
    vldespesa numeric(10,2) NOT NULL,
    vlpago numeric(10,2) NOT NULL,
    parcelas INT NOT NULL,
	CONSTRAINT users_pkey PRIMARY KEY (id)
);