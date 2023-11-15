class Elemento:
    def __init__(self, v):
        self.valor = v
        self.prox = None

class Fila:
    def __init__(self):
        self.inicio = None

    def enfileirar(self, n): 
        if self.inicio is None:
            self.inicio = n
        else:
            temp = self.inicio
            while temp.prox:
                temp = temp.prox

            temp.prox = n

    def desenfileirar(self):
        if self.inicio:
            temp = self.inicio
            self.inicio = temp.prox
            return temp

    def imprimir(self):
        print("Imprimindo fila...")
        if self.inicio:
            temp = self.inicio
            while temp:
                print(f"{temp.valor}")
                temp = temp.prox

f = Fila()
f.imprimir()
f.enfileirar(Elemento(10))
f.enfileirar(Elemento(100))
f.enfileirar(Elemento(1000))
f.enfileirar(Elemento(10000))
f.imprimir()
f.desenfileirar()
f.imprimir()
f.enfileirar(Elemento(50000))
f.imprimir()
