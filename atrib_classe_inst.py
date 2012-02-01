# coding: utf-8

"""
Demostração de atributos de classe x de instância

    >>> o = X(2, 'nonon')
    >>> o.a, o.b, o.c
    (77, 2, 'nonon')
    
O método c não é acessado via ``o.c``, porque todos os métodos são na verdade
atributos da classe, e ``o`` é uma instância. Ao acessar atributos via uma 
instância, os atributos da própria instância sempre têm prioridade.

    >>> o.c = 'bla'
    >>> o.c
    'bla'
    >>> o.__init__ = 'perigo'
    >>> o.__init__
    'perigo'
    
Mas a classe continua funcionando para criar novas instâncias:

    >>> oo = X(9, 'xyz')
    >>> oo.a, oo.b, oo.c
    (77, 9, 'xyz')

    
"""

class X(object):
    a = 77
    b = 0
    def __init__(self, b, c):
        self.b = b
        self.c = c
    def c(self):
        return self.c.upper()