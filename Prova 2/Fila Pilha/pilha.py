#import gc

class No:
    def __init__(self, v):
        self.valor = v
        self.prox = None

    def imprimir(self):
        return(f"Valor: {self.valor}")

class Pilha:
    def __init__(self):
        self.base = None
        self.topo = None

    def empilhar(self, n): #push
        if self.base == None:
            self.base = n
            self.topo = n
        else:
            self.topo.prox = n
            self.topo = n

    def desempilhar(self):
        if self.base != None:
            temp = self.base
            if temp == self.topo:
                self.base = None
                self.topo = None
                del temp
            else:
                while temp.prox != self.topo:
                    temp = temp.prox
                self.topo = temp
                temp = temp.prox
                del temp


    def imprimir(self): #da base para o topo
        if self.base == None:
            print("Pilha vazia")
        else:
            print("Imprimindo pilha...")
            temp = self.base
            while temp != self.topo:
                print(temp.imprimir())
                temp = temp.prox
            print(self.topo.imprimir())

def main():
    p = Pilha()
    p.imprimir()
    p.empilhar(No(10))
    p.imprimir()
    print("---")
    p.desempilhar()
    p.empilhar(No(100))
    p.empilhar(No(1000))
    p.empilhar(No(10000))
    p.imprimir()
    p.desempilhar()
    p.imprimir()
    p.empilhar(No(50000))
    p.imprimir()

if __name__ == "__main__":
    main()
            









