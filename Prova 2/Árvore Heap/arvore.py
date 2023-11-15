class No:
    def __init__(self, v):
        self.valor = v
        self.esq = None
        self.dir = None

class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, r, n):
        if self.raiz == None:
            self.raiz = n
        else:
            if n.valor <= r.valor: # testa se esquerda
                if r.esq == None:
                    r.esq = n
                else:
                    self.inserir(r.esq, n)
            else: # testa se direita
                if r.dir == None:
                    r.dir = n
                else:
                    self.inserir(r.dir, n)

    def preordem(self, r):
        if r:
            print(f'{r.valor}')
            self.preordem(r.esq)
            self.preordem(r.dir)

a = Arvore()
a.inserir(a.raiz, No(50))
a.inserir(a.raiz, No(10))
a.inserir(a.raiz, No(60))
a.inserir(a.raiz, No(5))
a.inserir(a.raiz, No(30))
a.inserir(a.raiz, No(55))
a.inserir(a.raiz, No(70))
a.inserir(a.raiz, No(4))
a.inserir(a.raiz, No(7))
a.preordem(a.raiz)
            









