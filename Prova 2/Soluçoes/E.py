#observaçao vendo a aula de heap. Eu poderia ter implementado o algoritmo de uma das questoes
# atras usando o "irmao direito". Era só linkar com todos os filhos do mesmo pai
# esquerdo apontando pro direito e, nos niveis mais profundos, com pais diferentes, eu
# linko o elemento com o pai.irmao_direito.filho esquerdo (mas tem um problema,
# o filho esquerdo do irmao direito do pai vai estar NONE. aí tem que usar a criatividade)

#tudo escrito acima é lixo. Muito trampo, muito processamento
#usando a fila fica mais fácil e leve

#Inserçao tudo ok
#Analisar fix-down
class No:
    def __init__(self, id, pri):
        self.id = id
        self.pri = pri
        self.esq = None
        self.dir = None
        self.pai = None

class Elemento: #vai ser um nó
    def __init__(self, no):
        self.no = no
        self.prox = None

class Fila:
    def __init__(self):
        self.inicio = None

    #pega elementos(nos) da arvore de cima pra baixo, esquerda pra direta
    #vai enfileirando e verificando se tem filhos até encontrar local vazio
    def enfileirar(self, elem): 
        if self.inicio is None:
            self.inicio = elem
        else:
            temp = self.inicio
            while temp.prox:
                temp = temp.prox
            temp.prox = elem
    #se nao tem local vazio, tira no da fila (FIFO)
    def desenfileirar(self): #remove o primeiro da filha
        if self.inicio:
            temp = self.inicio
            self.inicio = temp.prox
            return temp

class Heap:
    def __init__(self):
        self.raiz = None

    def inserir(self, no):
        if self.raiz == None:
            self.raiz = no
        else:
            self.inserir_subarvore(self.raiz, no)
    #usando fila, busca um local vazio para inserir
    #depois já dá o fix up para cumprir a propriedade da mini-heap
    def inserir_subarvore(self, r, no):
        f = Fila()
        f.enfileirar(Elemento(r))
        procurar = True
        while procurar:
            raiz_temp = (f.desenfileirar()).no #elemento.no
            if raiz_temp.esq:
                f.enfileirar(Elemento(raiz_temp.esq))
                if raiz_temp.dir:
                    f.enfileirar(Elemento(raiz_temp.dir))
                else: # se direita eh None
                    raiz_temp.dir = no
                    no.pai = raiz_temp
                    self.fix_up(no)
                    procurar = False
            else: # se esquerda eh None
                raiz_temp.esq = no
                no.pai = raiz_temp
                self.fix_up(no)
                procurar = False
    #ajeita arvore obrigando nós pai a terem prioridade mais alta (pai.pri < filhos.pri)
    def fix_up(self, no):
        if no.pai:
            if no.pri < no.pai.pri:
                temp = No(no.pai.id, no.pai.pri)
                no.pai.pri = no.pri
                no.pai.id = no.id
                no.pri = temp.pri
                no.id = temp.id
                self.fix_up(no.pai)

    #implementar remoçao de nó --que já foi processado--
    def find_last(self):
        r = self.raiz
        f = Fila()
        f.enfileirar(Elemento(r))
        procurar = True
        while procurar:
            raiz_temp = (f.desenfileirar()).no #elemento.no
            if raiz_temp.esq:
                f.enfileirar(Elemento(raiz_temp.esq))
                if raiz_temp.dir:
                    f.enfileirar(Elemento(raiz_temp.dir))
                else: # se direita eh None
                    ultimo = raiz_temp.esq
                    raiz_temp.esq = None
                    procurar = False
            else: # se esquerda eh None
                ultimo = raiz_temp
                if raiz_temp.pai.esq == raiz_temp:
                    raiz_temp.pai.esq = None
                else: #filho da direita
                    raiz_temp.pai.dir = None
                procurar = False
        self.raiz.id = ultimo.id
        self.raiz.pri = ultimo.pri
    
    def fix_down(self, r):
        if r.esq:
            #se tem filhos esq e dir
            if r.dir:
                if r.pri > r.esq.pri or r.pri > r.dir.pri: 
                    if r.esq.pri < r.dir.pri:
                        menor = r.esq
                    else:
                        menor = r.dir
                    temp = No(r.id, r.pri)
                    r.id = menor.id
                    r.pri = menor.pri
                    menor.id = temp.id
                    menor.pri = temp.pri
                    self.fix_down(menor)
            # tem filho esq e nao tem filho dir
            #entao sobe filho esq pro lugar do pai
            elif r.pri > r.esq.pri:
                menor = r.esq
                temp = No(r.id, r.pri)
                r.id = menor.id
                r.pri = menor.pri
                menor.id = temp.id
                menor.pri = temp.pri
                self.fix_down(menor)
                
        
    def preordem(self, r):
        if r:
            print(f'{r.id} {r.pri}')
            self.preordem(r.esq)
            self.preordem(r.dir)

n, q  = map(int, input().split())
h = Heap()
count = 0 #contador para frequencia do processador (q)
for i in range(n):
    id, pri = input().split()
    pri = int(pri)
    no = No(id, pri)
    count += 1
    h.inserir(no)
    if count == q:
        ultimo = h.find_last()
        h.fix_down(h.raiz)
        count = 0
h.preordem(h.raiz)