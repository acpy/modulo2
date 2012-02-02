============================
Desafio: Baralho polimórfico
============================

Para os exercícios desta seção, use como base o código do exemplo `baralho.py`_.

.. _baralho.py: https://github.com/acpy/modulo2/blob/master/iteraveis/baralho.py

1. Implemente uma subclasse de ``Baralho`` chamada ``BaralhoInverso`` com um
método ``__iter__`` que produz um iterador para fornecer as cartas na ordem
inversa, ou seja, sem embaralhar, a primeira carta deve ser o ``<K de paus>``
em vez do ``<A de copas>``, como acontece na implementação atual.

1.1. **Bônus:** implemente três métodos, ``iter_genexp``, ``iter_genfun`` e
``iter_obj``, usando (respectivamente) uma expressão geradora, uma função
geradora e um objeto iterador.

2. Implemente uma subclasse de ``Baralho`` chamada ``BaralhoMisturado`` com
um método ``__iter__`` que produz um iterador para fornecer as cartas em uma
ordem aleatória. Note que este iterador deverá produzir exatamente 52 cartas,
e nenhuma deverá ser repetida. Seguindo a filosofia do padrão de projeto
*Iterator*, o iterador não deve alterar o estado interno do baralho, de modo
que possam existir vários iteradores ao mesmo tempo, cada um percorrendo as
cartas embaralhadas em uma ordem diferente.

**Dicas:** (1) não embaralhe a estrutura interna que contém as cartas, mas
gere uma série embaralhada de índices, e use esta série para determinar a
próxima carta; (2) use a função ``shuffle`` do módulo ``random`` para
embaralhar os índices.

----

**Bom trabalho!**

Qualquer dúvida, nos falamos pelo grupo `Academia Python`_!

.. _Academia Python: http://groups.google.com/group/academiapython

*Luciano Ramalho*
