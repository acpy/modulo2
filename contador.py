class Contador(object):
    contagem = {}

    def __init__(self):
        pass
        
    def incluir(self, item):
        qtd = self.contagem.get(item, 0) + 1
        self.contagem[item] = qtd

    def contar(self, item):
        return self.contagem[item]
        
class ContadorTotalizador(Contador):
    def __init__(self):
        Contador.__init__(self)
        self.total = 0

    def incluir(self, item):
        Contador.incluir(self, item)
        self.total = self.total + 1
        