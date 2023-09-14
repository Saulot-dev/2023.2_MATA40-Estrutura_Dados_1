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

    def limpar(self):
        self.tam = 0

def main():
    n = int(sys.argv[1])
    l = Lista(n)
    l.isEmpty()
    l.inserir(5)
    l.inserir(10)
    l.inserir(15)
    l.inserir(20)
    l.isEmpty()
    l.imprimir()
    l.limpar()
    l.isEmpty()
    l.imprimir()

if __name__ == "__main__":
    main()




