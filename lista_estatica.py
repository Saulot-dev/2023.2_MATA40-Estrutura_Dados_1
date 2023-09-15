import numpy as np
import sys

class Lista:
    def __init__(self, m):
        self.max = m
        self.tam = 0
        self.elems = np.zeros(self.max)

    def isEmpty(self):
        if self.tam == 0:
            print(f"Lista Vazia")
            return True
        else:
            print(f"Há elementos")
            return False

    def imprimir(self):
        for i in np.arange(self.tam):
            print(self.elems[i])

    def inserir(self, e):
        if self.tam == self.max:
            print("Erro, lista cheia")
        else:
            self.elems[self.tam] = e
            self.tam += 1

    def insere_index(self, index, e):
        #assumindo que self.tam < self.max
        if self.tam < self.max:
            self.tam += 1
        if index < self.max:
            for i in np.arange(self.tam-1, index, -1):
                self.elems[i]= self.elems[i-1]
            self.elems[index] = e
        else:
            print("Invalid index. Out of range")
        
    def limpar(self):
        self.tam = 0
    
    def remover(self, n):
        #presumindo que n < self.tam
        for i in np.arange(n, self.tam-1, 1):
            self.elems[i] = self.elems[i+1]
        self.tam -= 1

def main():
    l = Lista(5)
    l.inserir(5)
    l.inserir(15)
    l.inserir(25)
    l.inserir(35)
    l.insere_index(10, 10)
    l.imprimir()
    


if __name__ == "__main__":
    main()