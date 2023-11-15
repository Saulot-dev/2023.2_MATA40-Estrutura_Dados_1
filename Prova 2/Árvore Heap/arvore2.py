class No:
    def __init__(self, v):
        self.valor = v
        self.esq = None
        self.dir = None

class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, n):
        if self.raiz == None:
            self.raiz = n
        else:
            self.inserir_subarvore(self.raiz, n)

    def inserir_subarvore(self, r, n):
        if n.valor <= r.valor: # testa se esquerda
            if r.esq == None:
                r.esq = n
            else:
                self.inserir_subarvore(r.esq, n)
        else: # testa se direita
            if r.dir == None:
                r.dir = n
            else:
                self.inserir_subarvore(r.dir, n)

    def preordem(self, r):
        if r:
            print(f'{r.valor}')
            self.preordem(r.esq)
            self.preordem(r.dir)

def main():
    a = Arvore()
    a.inserir(No(50))
    a.inserir(No(10))
    a.inserir(No(60))
    a.inserir(No(5))
    a.inserir(No(30))
    a.inserir(No(55))
    a.inserir(No(70))
    a.inserir(No(4))
    a.inserir(No(7))
    a.preordem(a.raiz)

if __name__ == "__main__":
    main()
            









