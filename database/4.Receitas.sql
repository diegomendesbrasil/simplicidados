
CREATE TABLE dmb.receita (
    id SERIAL PRIMARY KEY,
    iduser INT NOT NULL REFERENCES dmb.users(id),
    dtvencimento DATE NOT NULL,
    dtrecebimento DATE,
    idcliente INT NOT NULL REFERENCES dmb.cliente(id),
    vlreceitaplanejado NUMERIC(10, 2) NOT NULL,
    vlreceitarecebido NUMERIC(10, 2) NOT NULL,
    parcelas INT NOT NULL
);
