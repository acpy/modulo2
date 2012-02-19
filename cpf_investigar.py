# coding: utf-8

"""

17.02.2012 - 7:25
Blog do Juca Kfouri
http://blogdojuca.uol.com.br/2012/02/sandro-rossel-depositou-na-conta-da-filha-de-ricardo-teixeira/

==================================================================
Presidente do Barça pagou R$ 3,8 mi à filha de 11 anos de Teixeira
==================================================================

Sandro Rosell depositou R$ 3.800.000 na conta de Antônia Wigand Teixeira, numa
agência do Bradesco, a de número 6592-7, na avenida América, Barra da Tijuca,
no dia 22 de junho do ano passado.

Rosell é sócio da Alianto, a empresa que recebeu R$ 9 milhões do governo de
Brasília, sem licitação, pelo amistoso da Seleção Brasileira contra Portugal,
em 2008, evento que está sob investigação do Ministério Público e mais que
suspeito de superfaturamento.

A Alianto foi também dona da VSV Agropecuária, que tinha sede na fazenda de
Teixeira em Piraí, interior do Rio, e cuja sócia, a secretária de Rossel,
Vanessa Precht, emitiu cheques em nome do cartola da CBF segundo apurou a
Polícia Civil em Brasília.

Rosell (Alexandre Rosell i Feliu, CPF- 05X.8Y9.W47-62) é atual presidente do
Barcelona e ex-homem forte no Brasil da Nike, fornecedora da CBF.

Uma das razões para anunciada saída de Teixeira da CBF e ida para Miami é
exatamente a filha Antônia (CPF- 16X.5Y4.W17-11) que, aos 11 anos, tem ouvido
comentários desagradáveis sobre o pai na escola, no Rio.
"""

from cpf import checar_cpf, so_digitos

rosell =   '05{X}.8{Y}9.{W}47-62' # 055.859.447-62 X=5, Y=5, W=4
teixeira = '16{X}.5{Y}4.{W}17-11'
mascara = rosell

validos = [mascara.format(X=x, Y=y, W=w) for x in range(10)
                                         for y in range(10)
                                         for w in range(10)
           if checar_cpf(mascara.format(X=x, Y=y, W=w))]

for num in validos:
    print so_digitos(num)

