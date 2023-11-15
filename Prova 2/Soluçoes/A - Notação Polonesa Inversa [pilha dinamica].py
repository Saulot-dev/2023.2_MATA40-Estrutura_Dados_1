class No:
    def __init__(self, v):
        self.valor = v
        self.next = None

class Pilha:
    def __init__(self):
        self.base = None
        self.topo = None

    def empilhar(self, no):
        if self.base == None:
            self.base = no
            self.topo = no
        else:
            self.topo.next = no
            self.topo = no
    
    def segundo(self):
        second = self.base
        if second.next:
            while second.next != self.topo:
                second = second.next
            return second
        else:
            return self.base
    
    def opera(self, op):
        match op:
            case "+":
                segundo = self.segundo()
                segundo.valor += self.topo.valor
                self.topo = segundo
                segundo.next = None
            case "-":
                segundo = self.segundo()
                segundo.valor -= self.topo.valor
                self.topo = segundo
                segundo.next = None
            case "*":
                segundo = self.segundo()
                segundo.valor *= self.topo.valor
                self.topo = segundo
                segundo.next = None
            case "/":
                segundo = self.segundo()
                if self.topo.valor != 0:
                    segundo.valor //= self.topo.valor
                else:
                    segundo.valor = 0
                self.topo = segundo
                segundo.next = None


pilha = Pilha()
operacoes = ["+", "-", "*", "/"]
for i in input().split():
    if i not in operacoes:
        v = int(i)
        no = No(v)
        pilha.empilhar(no)
    else:
        pilha.opera(i)
print(f'{pilha.base.valor}')