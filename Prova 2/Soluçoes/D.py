class No:
    def __init__(self, v):
        self.valor = v
        self.esq = None
        self.dir = None
        self.on = True

class Arvore:
    def __init__(self):
        self.raiz = self.new_tree()

    def new_tree(self):
        return None
    
    def clear_tree(self):
        self.raiz = None

    def add(self, r, n):
        if self.raiz == None:
            self.raiz = n
        else:
            if n.valor <= r.valor: # testa se esquerda
                if r.esq == None:
                    r.esq = n
                else:
                    self.add(r.esq, n)
            else: # testa se direita
                if r.dir == None:
                    r.dir = n
                else:
                    self.add(r.dir, n)

        #def preordem_invertida_removendo(self, r):  Uma ideia


    def preordem_invertida(self, r):
        if r.dir:
            self.preordem_invertida(r.dir)
        print(r.valor, end=" ")
        # r.on = False
        if r.esq:
            self.preordem_invertida(r.esq)

a = Arvore()
n = int(input())
for i in input().split():
    v = int(i)
    no = No(v)
    a.add(a.raiz, no)
a.preordem_invertida(a.raiz)
