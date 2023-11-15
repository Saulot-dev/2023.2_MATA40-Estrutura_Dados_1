from fila import *

class No:
    def __init__(self, v):
        self.valor = v
        self.esq = None
        self.dir = None
        self.pai = None

class Heap:
    def __init__(self):
        self.raiz = None

    def inserir(self, n):
        if self.raiz == None:
            self.raiz = n
        else:
            self.inserir_subarvore(self.raiz, n)

    def inserir_subarvore(self, r, n):
        f = Fila()
        f.enfileirar(Elemento(r))
        procurar = True
        while procurar:
            raiz_temp = (f.desenfileirar()).valor
            if raiz_temp.esq:
                f.enfileirar(Elemento(raiz_temp.esq))
                if raiz_temp.dir:
                    f.enfileirar(Elemento(raiz_temp.dir))
                else: # se direita eh None
                    raiz_temp.dir = n
                    n.pai = raiz_temp
                    self.fix_up(n)
                    procurar = False

            else: # se esquerda eh None
                raiz_temp.esq = n
                n.pai = raiz_temp
                self.fix_up(n)
                procurar = False

    def fix_up(self, n):
        if n.pai:
            if n.valor < n.pai.valor:
                temp = n.pai.valor
                n.pai.valor = n.valor
                n.valor = temp
                self.fix_up(n.pai)

    def imprimir(self):
        f = Fila()
        f.enfileirar(Elemento(self.raiz))
        print("Imprimindo Heap...")
        while f.inicio:
            temp = (f.desenfileirar()).valor
            print(f"{temp.valor}")
            if temp.esq:
                f.enfileirar(Elemento(temp.esq))

            if temp.dir:
                f.enfileirar(Elemento(temp.dir))

def main():
    h = Heap()
    h.inserir(No(9))
    h.inserir(No(10))
    h.inserir(No(11))
    h.inserir(No(12))
    h.inserir(No(13))
    h.inserir(No(14))
    h.inserir(No(15))
    
    h.imprimir()

    h.inserir(No(7))

    h.imprimir()

if __name__ == "__main__":
    main()
            









