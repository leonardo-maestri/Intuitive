-- Importação do arquivo de operadoras ativas
COPY operadoras_ativas FROM 'C:\INTUITIVE\03_banco_de_dados\Dados\Relatorio_cadop.csv' 
WITH (FORMAT CSV, DELIMITER ';', HEADER true, ENCODING 'LATIN1');


-- Importação de todos os arquivos trimestrais
-- 2023
COPY demonstracoes_trimestrais (data_arquivo, registro_ans, codigo_conta_contabil, descricao_conta, valor_saldo_inicial, valor_saldo_final)
FROM 'C:\INTUITIVE\03_banco_de_dados\Dados\1T2023.csv'
WITH (FORMAT CSV, DELIMITER ';', HEADER true, ENCODING 'LATIN1');

COPY demonstracoes_trimestrais (data_arquivo, registro_ans, codigo_conta_contabil, descricao_conta, valor_saldo_inicial, valor_saldo_final)
FROM 'C:\INTUITIVE\03_banco_de_dados\Dados\2T2023.csv'
WITH (FORMAT CSV, DELIMITER ';', HEADER true, ENCODING 'LATIN1');

COPY demonstracoes_trimestrais (data_arquivo, registro_ans, codigo_conta_contabil, descricao_conta, valor_saldo_inicial, valor_saldo_final)
FROM 'C:\INTUITIVE\03_banco_de_dados\Dados\3T2023.csv'
WITH (FORMAT CSV, DELIMITER ';', HEADER true, ENCODING 'LATIN1');

COPY demonstracoes_trimestrais (data_arquivo, registro_ans, codigo_conta_contabil, descricao_conta, valor_saldo_inicial, valor_saldo_final)
FROM 'C:\INTUITIVE\03_banco_de_dados\Dados\4T2023.csv'
WITH (FORMAT CSV, DELIMITER ';', HEADER true, ENCODING 'LATIN1');

-- 2024
COPY demonstracoes_trimestrais (data_arquivo, registro_ans, codigo_conta_contabil, descricao_conta, valor_saldo_inicial, valor_saldo_final)
FROM 'C:\INTUITIVE\03_banco_de_dados\Dados\1T2024.csv'
WITH (FORMAT CSV, DELIMITER ';', HEADER true, ENCODING 'LATIN1');

COPY demonstracoes_trimestrais (data_arquivo, registro_ans, codigo_conta_contabil, descricao_conta, valor_saldo_inicial, valor_saldo_final)
FROM 'C:\INTUITIVE\03_banco_de_dados\Dados\2T2024.csv'
WITH (FORMAT CSV, DELIMITER ';', HEADER true, ENCODING 'LATIN1');

COPY demonstracoes_trimestrais (data_arquivo, registro_ans, codigo_conta_contabil, descricao_conta, valor_saldo_inicial, valor_saldo_final)
FROM 'C:\INTUITIVE\03_banco_de_dados\Dados\3T2024.csv'
WITH (FORMAT CSV, DELIMITER ';', HEADER true, ENCODING 'LATIN1');

COPY demonstracoes_trimestrais (data_arquivo, registro_ans, codigo_conta_contabil, descricao_conta, valor_saldo_inicial, valor_saldo_final)
FROM 'C:\INTUITIVE\03_banco_de_dados\Dados\4T2024.csv'
WITH (FORMAT CSV, DELIMITER ';', HEADER true, ENCODING 'LATIN1');