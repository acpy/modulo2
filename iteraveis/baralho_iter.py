'''
    >>> b = Baralho()
    >>> for carta in b:                             # doctest:+ELLIPSIS
    ...     print carta
    <A de copas>
    <2 de copas>
    <3 de copas>
    <4 de copas>
    <5 de copas>
    ...
    >>> for carta in reversed(b):                   # doctest:+SKIP
    ...     print carta
    <K de paus>
    <Q de paus>
    <J de paus>
    <10 de paus>
    ...
    >>>

'''

class Carta(object):
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return '<%s de %s>' % (self.valor, self.naipe)

class Baralho(object):
    naipes = 'copas ouros espadas paus'.split()
    valores = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()

    def __init__(self):
        self.cartas = [Carta(v, n)
                        for n in self.naipes
                        for v in self.valores]

    def __getitem__(self, pos):
        raise NotImplementedError()
        return self.cartas[pos]

    def __len__(self):
        return len(self.cartas)
        
    def __iter__(self):
        return IteradorDeBaralho(self)    
        
class IteradorDeBaralho(object):
    
    def __init__(self, baralho):
        self.__baralho = baralho
        self.__posicao_atual = 0
        
    def next(self):
        if self.__posicao_atual == len(self.__baralho):
            raise StopIteration()
        atual = self.__baralho.cartas[self.__posicao_atual]
        self.__posicao_atual += 1
        return atual
        
    def __iter__(self):
        return self
        
        
        
        
        
        







        