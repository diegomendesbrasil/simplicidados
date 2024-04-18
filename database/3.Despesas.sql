
CREATE TABLE dmb.despesa (
    id SERIAL PRIMARY KEY,
    iduser INT NOT NULL REFERENCES dmb.users(id),
    dtvencimento DATE NOT NULL,
    dtpagamento DATE,
    idfornecedor INT NOT NULL REFERENCES dmb.fornecedor(id),
    vldespesa NUMERIC(10, 2) NOT NULL,
    vlpago NUMERIC(10, 2) NOT NULL,
    parcelas INT NOT NULL
);
