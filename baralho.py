# coding: utf-8

"""
Uma carta::

    >>> zape = Carta(4, 'paus')
    >>> zape
    <4 de paus>

"""


class Carta(object):
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe
    def __repr__(self):
        return '<%s de %s>' % (self.valor, self.naipe)
        
class Baralho(object):
    naipes = 'paus copas espadas ouros'.split()
    valores = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()

    def __init__(self):
        self.cartas = [Carta(v, n) 
                         for n in self.naipes
                         for v in self.valores]
    def __len__(self):
        return len(self.cartas)
        
    def __getitem__(self, pos):
        return self.cartas[pos]
        
        
if __name__=='__main__':
    import doctest
    doctest.testmod()
    