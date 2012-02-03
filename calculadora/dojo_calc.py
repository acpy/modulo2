
"""

    >>> calc = Calculadora()
    >>> calc.calcula([10])
    10
    >>> calcular([10, 20]) #doctest:+SKIP
    20
    >>> calcular([10, 20, '+']) #doctest:+SKIP
    30
    >>> calcular([10, 20, '*']) #doctest:+SKIP
    200
    >>> calcular([10, 2, '**']) #doctest:+SKIP
    100
    >>> calcular([10, 20, 30, '+']) #doctest:+SKIP
    50
    >>> pilha() #doctest:+SKIP
    [10]

"""
import operator as op

class Calculadora(object):
    
    entrada = []
    operacoes = {'+': op.add, '*':op.mul, '/': op.div, '-': op.sub, '**': op.pow}
            
    def pilha(self):
        pass
    
    
    def calcula(self, entrada):   
        if len(entrada) == 1:
            return entrada[0]
    
if __name__=='__main__':
    import doctest
    doctest.testmod(optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)      


"""
Codigo retirado na refatoracao:

p = []

def pilha():
    return p

def calcular(entradas):
    ultimo_elemento = entradas[-1]
    if entradas[-1] in operacoes:
        x, y = entradas[-3], entradas[-2]
        return operacoes[ultimo_elemento](x, y)
    else:
        p = entradas
        return entradas[-1]

"""        
