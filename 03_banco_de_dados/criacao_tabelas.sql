-- Tabela para operadoras ativas
CREATE TABLE operadoras_ativas (
    registro_ans VARCHAR(20) PRIMARY KEY,
    cnpj VARCHAR(14),
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(100),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf CHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(2),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(255),
    cargo_representante VARCHAR(100),
    regiao_comercializacao VARCHAR(100),
    data_registro_ans DATE
);

-- Tabela para demonstrações contábeis trimestrais
CREATE TABLE demonstracoes_trimestrais (
    id SERIAL PRIMARY KEY,
    data_arquivo DATE,
    registro_ans VARCHAR(20) REFERENCES operadoras_ativas(registro_ans),
    codigo_conta_contabil VARCHAR(50),
    descricao_conta VARCHAR(255),
    valor_saldo_inicial DECIMAL(15,2),
    valor_saldo_final DECIMAL(15,2),
    ano INT GENERATED ALWAYS AS (EXTRACT(YEAR FROM data_arquivo)) STORED,
    trimestre INT GENERATED ALWAYS AS (EXTRACT(QUARTER FROM data_arquivo)) STORED
);

-- indices
CREATE INDEX idx_demtrim_registro_ans ON demonstracoes_trimestrais(registro_ans);
CREATE INDEX idx_demtrim_conta_contabil ON demonstracoes_trimestrais(codigo_conta_contabil);
CREATE INDEX idx_demtrim_ano_trimestre ON demonstracoes_trimestrais(ano, trimestre);