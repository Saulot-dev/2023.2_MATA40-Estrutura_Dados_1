#Dessa vez vou fazer a pilha do topo para a base
#Ainda assim tá dando erro

class No:
    def __init__(self, v):
        self.valor = v
        self.prev = None

class Pilha:
    def __init__(self):
        self.base = None
        self.topo = None

    def empilhar(self, no):
        if self.base == None:
            self.base = no
            self.topo = no
        else:
            no.prev = self.topo
            self.topo = no
    
    def opera(self, op):
        if op == "+":
            self.topo.prev.valor += self.topo.valor
            self.topo = self.topo.prev
        elif op == "-":
            self.topo.prev.valor -= self.topo.valor
            self.topo = self.topo.prev
        elif op == "*":
            self.topo.prev.valor *= self.topo.valor
            self.topo = self.topo.prev
        elif op == "/":
            if self.topo.valor != 0:
                self.topo.prev.valor //= self.topo.valor
            else:
                self.topo.prev.valor = 0
            self.topo = self.topo.prev


pilha = Pilha()
operacoes = ["+", "-", "*", "/"]
for i in input().split():
    if i not in operacoes:
        v = int(i)
        no = No(v)
        pilha.empilhar(no)
    else:
        c = str(i)
        pilha.opera(c)
print(f'{pilha.base.valor}')