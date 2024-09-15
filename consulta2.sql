SELECT
    organizacao.nome AS organizacao,
    tipo.nome AS tipo,
    SUM(pessoa.totalHorasTrabalhadas * valor.valor) AS custo
FROM
    pessoa
JOIN
    tipo ON pessoa.tipo = tipo.id
JOIN
    organizacao ON pessoa.organizacao = organizacao.id
JOIN
    valor ON pessoa.tipo = valor.tipo AND pessoa.organizacao = valor.organizacao
GROUP BY
    organizacao.nome, tipo.nome;
