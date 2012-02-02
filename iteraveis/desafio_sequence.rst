===============================================
Desafio: Explorando o protocolo de ``Sequence``
===============================================

1. Descrição do problema
-------------------------

Na turma 0 do curso *Python para quem sabe Python*, o participante João Paulo
Dubas sugeriu um exemplo para explorar o procolo (ou *interface*) da classe
abstrata ``collections.Sequence`` introduzida no Python 2.6. Este exercício é
baseado no exemplo proposto pelo João Paulo.

Pela documentação do Python, e pelo UML mostrado em aula, notamos que a classe
``Sequence`` declara ``__getitem__`` como método abstrato, mas fornece como
*mixins* os métodos ``__contains__``, ``__iter__``, ``__reversed__``,
``index``, e ``count``.

Isso significa que uma subclasse concreta de ``Sequence`` só precisa
implementar ``__getitem__`` para poder herdar automaticamente as
implementações dos 5 métodos mixin mencionados acima.

Claro que esta conveniência tem um preço, afinal não existe almoço de graça
(até no *Bom Prato* custa R$ 1). O preço é que a implementação possível para
``__contains__``, ``index`` e ``count``, a partir apenas da funcionalidade do
``__getitem__`` envolverá necessariamente uma busca linear.

Por exemplo, considerando uma subclasse concreta ``ListaOrdenada`` de
``Sequence``, implementando apenas o método ``__getitem__``, vamos criar uma
instância ``lo`` de ``ListaOrdenada``, contendo um milhão de itens::

    >>> lo = ListaOrdenada(range(10**6))

Para avaliar a expressão abaixo, Python acionará o método ``__contains___``,
herdado de ``Sequence``::

    >>> 500000 in lo
    True

Porém, a implementação mixin de ``__contains___`` só pode contar com a
implementação concreta de ``__getitem__``. Então, para responder a pergunta
acima Python terá que percorrer 500.000 itens. E para esta outra pergunta,
Python terá que percorrer todos os 1.000.000 de itens::

    >>> -1 in lo
    False

No entanto, sabendo que os itens de uma ``ListaOrdenada`` estão em ordem
ascendente, é possível fazer uma implementação muito mais eficiente de
``__contains___`` usando uma busca binária.

2. Sua missão
--------------

No repositório ``/oturing/ppqsp`` do GitHub você encontrará um módulo
`lista_ord.py`_, que implementa uma classe ``ListaOrdenada(Sequence)``. No
mesmo diretório há um módulo `busca_bin.py`_ que contém uma função
``busca_bin`` que faz a busca binária de um item em uma sequência ordenada.

.. _lista_ord.py: https://github.com/acpy/modulo2/blob/master/iteraveis/lista_ord.py
.. _busca_bin.py: https://github.com/acpy/modulo2/blob/master/iteraveis/busca_bin.py

Sua missão é usar a função ``busca_bin`` para implementar o método
``__contains__`` na classe ``ListaOrdenada``. Assegure-se de que os *doctests*
do módulo ``lista_ord.py`` continuam passando, e use a função ``desempenho``
do mesmo módulo para verificar se a sua implementação realmente ficou mais
rápida que a original.

3. Missão bônus 1
-----------------

Implemente o método ``ListaOrdenada.add`` para incluir um item na posição
correta de uma lista ordenada. Note que já há doctests prontos para verificar
o método ``add``, mas todos (exceto o primeiro) estão desligados com a
diretiva ``# doctest: +SKIP``.

Pergunta de arquiteto: no módulo ``collections`` existe também uma classe
abstrata ``MutableSequence``, com métodos abstratos como ``__setitem__`` e
``insert`` e mixins como ``append``, ``pop`` e ``remove``. Porque não fizemos
nossa ``ListaOrdenada`` uma subclasse de ``MutableSequence``, mas adotamos o
nome do método ``add`` da classe ``MutableSet``?

4. Missão bônus 2
-----------------

Na verdade, a função ``busca_bin`` faz mais do que dizer se o item existe: ela
informa a posição do item. Aproveitando este fato, refatore o código do
exercício 2 para implementar primeiro o método ``ListaOrdenada.index``,
respeitando a convenção de que ``index`` levanta ``ValueError`` se o item não
existe na sequência. Recomendo fazer TDD, ou seja, implemente primeiro o teste
para o caso mais simples possível do método ``index``, verifique que o teste
não passa, e então implemente o método para fazer este teste passar. Continue
assim: implemente um teste adicional, acrescente funcionalidade para passar o
teste, refatore se necessário.

Uma vez implementando ``index``, rafatore ``ListaOrdenada.__contains__`` para
usar o método ``ListaOrdenada.index`` (evitando duplicação de código). Isso
não vai exigir novos testes, mas apenas assegure-se de que os testes
anteriores continuam passando.

E finalmente, usando TDD, implemente uma versão eficiente do método
``ListaOrdenada.count`` que devolve a quantidade de ocorrências de um item em
uma ``ListaOrdenada``. Seu primeiro teste deve verificar o caso mais simples:
se ``count`` devolve 0 quando o item não ocorre na lista. Depois implemente
testes e a funcionalidade para quando só existe um item, e só então ataque o
problema de vários itens, sempre escrevendo os testes primeiro.

----

**Bom trabalho!**

Qualquer dúvida, nos falamos pelo grupo `Academia Python`_!

.. _Academia Python: http://groups.google.com/group/academiapython

*Luciano Ramalho*