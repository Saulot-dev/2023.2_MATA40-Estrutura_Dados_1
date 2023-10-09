import numpy as np

#Questao F - Gerenciador de memoria

#mudei a logica criando a classe bloco e o atributo "tam" facilita as operaçoes, nao sendo mais necessario ficar percorrendo a lista encadeada Memoria. Ufa!!
#06/10/2023 já descobri o erro: 
    # Ao limpar um bloco ocupado, eu estava checando se o proximo estava livre pra aglutinar,
    # porém eu nao estava prevendo o caso em que o bloco está entre dois espaços lires, pois existe essa possibilidade.
    # Vou alterar somente a saída(dentro do display) para eliminar 0s duplicados tambem E DEPOIS EU CONSERTO O ALGORITMO.


# Fazer essa poha com lista duplamente encadeada, pensei que só poderia fazer 
# com encadeada simples. Mas, so far, encontrei o erro com o ultimo exemplo de entrada,
# na linha 60


class Bloco:
    def __init__(self, id, tam):
        self.id = id
        self.t = tam
        self.next = None
        
class Memoria:
    def __init__(self, max):
        self.head = self.new("0", max)
        self.max = max
        self.busy = 0
        self.free = max
        
    def new(self, id, max):
        b = Bloco(id, max)
        return b
    
    def insert(self, b_in):
        #ou tá toda livre ou toda ocupada
        if self.head.t == self.max:
            if self.head.id == "0":
                #insere novo bloco no head. A questao garante que será menor que self.max
                b_in.next = self.head
                self.head = b_in
                #update memoria free
                b_in.next.t -= b_in.t
                self.update_mem("busy", b_in.t)
            #else: nada acontece pois memoria está toda ocupada
        else:
            #casos em que memoria nao está toda livre nem toda cheia
            #se tiver espaco na memoria para alocar novo bloco (mesmo que esteja em blocos separados)
            if self.free >= b_in.t:
                tmp = self.head
                #percorre a lista à procura de um bloco com espaço para alocar b_in
                while tmp != None:
                    #Caso encontre um bloco vazio (pode ser o primeiro ou nao)
                    if tmp.id == "0":
                        #caso tenha mais tamanho que o necessario para alocar novo bloco
                        if tmp.t > b_in.t:
                            h = self.find_prev(tmp)
                            
                            if h != None:
                                h.next = b_in
                            #o erro estava aqui. pois h só é None, se h=tmp=self.head
                            else:
                                self.head = b_in
                            b_in.next = tmp
                            tmp.t -= b_in.t
                            self.update_mem("busy", b_in.t)
                            break
                        #caso o bloco livre seja do mesmo tamanho a ser inserido
                        elif tmp.t == b_in.t:
                            tmp.id = b_in.id
                            self.update_mem("busy", b_in.t)
                            break
                        #caso o tamanho do bloco livre seja menor que o bloco a ser inserido
                        else:
                            #verifica se o restante da memoria livre já nao pode alocar o novo bloco
                            if (self.free - tmp.t) < b_in.t:
                                break
                            #caso contrario, segue o loop
                    #caso contrario, segue o loop
                    tmp = tmp.next            
            # else: nada será feito pois nao tem memoria livre suficiente
    
    def libera(self, id):
        #nao esquecer do caso 0 X 0 && id = X
        tmp = self.head
        #para garantir, vou percorrer a lista inteira
        while tmp != None:
            #caso encontre o bloco a ser liberado
            if tmp.id == id:
                tmp.id = "0"
                self.update_mem("free", tmp.t)
                #aglutina bloco posterior
                if tmp.next != None:
                    if tmp.next.id == "0":
                        tmp.t += tmp.next.t
                        tmp.next = tmp.next.next
                #aglutina bloco anterior, caso exista
                prev = self.find_prev(tmp)
                #aqui tava dando runtime error
                if prev != None:
                    if prev.id == "0":
                        prev.t += tmp.t
                        prev.next = tmp.next 
                break
            tmp = tmp.next
            #else: segue o loop
    #busca o no anterior ao no em questao para fazer o link corretamente
    def find_prev(self, tmp):
        h = self.head
        # tmp é self.head.
        if h == tmp:
            return None
        else:
            while h.next != tmp:
                h = h.next
        return h
    #atualiza quantidade de memoria livre ou ocupada de acordo com a funcao (insert ou libera)
    def update_mem(self, op, t):
        if op == "busy":
            self.busy += t
            self.free -= t
        if op == "free":
            self.busy -= t
            self.free += t
                
    def display(self):
        tmp = self.head
        while tmp.next != None:
            if tmp.id == "0":
                print(int(tmp.id), end=" ")
            else:
                print(tmp.id, end=" ")
            tmp = tmp.next
        if tmp.id == "0":
            print(int(tmp.id))
        else:
            print(tmp.id)
        print(self.busy)
        print(self.free)
        
max, n = map(int, input().split())
mem = Memoria(max)
for i in np.arange(n):
    op, tam, id = input().split()
    op = int(op)
    tam = int(tam)
    if op == 1:
        b = Bloco(id, tam)
        mem.insert(b)
    elif op == 0:
        mem.libera(id)
mem.display()