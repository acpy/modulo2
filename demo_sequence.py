from collections import Sequence

class Fila(Sequence):
    def __init__(self, valores):
        self.__lista = valores[:]
    def __len__(self):
        return len(self.__lista)
    def __getitem__(self, pos):
        return self.__lista[pos]
        
