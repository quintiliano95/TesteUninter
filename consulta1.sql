SELECT
    pessoa.nome AS pessoa,
    tipo.nome AS tipo,
    organizacao.nome AS organizacao,
    valor.valor AS valorHora,
    pessoa.totalHorasTrabalhadas,
    (pessoa.totalHorasTrabalhadas * valor.valor) AS receber
FROM
    pessoa
JOIN
    tipo ON pessoa.tipo = tipo.id
JOIN
    organizacao ON pessoa.organizacao = organizacao.id
JOIN
    valor ON pessoa.tipo = valor.tipo AND pessoa.organizacao = valor.organizacao;
