--3.5
-- Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU
-- AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?

SELECT 
    o.razao_social AS "Operadora",
    o.registro_ans AS "Registro ANS",
    SUM(d.valor_saldo_final) AS "Total de Despesas (R$)"
FROM 
    demonstracoes_trimestrais d
JOIN 
    operadoras_ativas o ON d.registro_ans = o.registro_ans
WHERE 
    d.descricao_conta LIKE 'EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
    AND d.data_arquivo = (SELECT MAX(data_arquivo) FROM demonstracoes_trimestrais)
GROUP BY 
    o.razao_social, o.registro_ans
ORDER BY 
    "Total de Despesas (R$)" DESC
LIMIT 10;



--3.5
-- Quais as 10 operadoras com maiores despesas nessa categoria no último ano?
SELECT 
    o.razao_social AS "Operadora",
    o.registro_ans AS "Registro ANS",
    SUM(d.valor_saldo_final) AS "Total de Despesas (R$)",
    MAX(d.ano) AS "Ano de Referência"
FROM 
    demonstracoes_trimestrais d
JOIN 
    operadoras_ativas o ON d.registro_ans = o.registro_ans
WHERE 
    d.descricao_conta ILIKE '%eventos/sinistros conhecidos ou avisados de assistência a saúde medico hospitalar%'
    AND d.ano = (SELECT MAX(ano) FROM demonstracoes_trimestrais)
GROUP BY 
    o.razao_social, o.registro_ans
ORDER BY 
    "Total de Despesas (R$)" DESC
LIMIT 10;