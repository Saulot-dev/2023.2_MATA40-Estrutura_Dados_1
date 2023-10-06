import numpy as np
#Questao 6 - Gerenciador de Memoria
    # poderia criar mais atributos na classe memoria para facilitar, por exempli um dicionario com id e tamanho de cada bloco de memoria e depois ir atualizando
    #Poderia criar a classe celula no lugar de bloco e criar uma outra classe bloco para conter os grupos de celulas
    #atualizar os free. ocupada e tam
    #se no final de tudo self.max maior que self.tam e a ultima saída da string for diferente de '0', adicionar '0' à saída pois ainda tem memória livre
    
#implementar a 3ª classe celula e mudar a zorra toda, mas antes, fazer no papel. 
#haverá uma lista encadeada de blocos
'''
class Bloco:
    def __init__(self):
        self.id = "0"
        self.pos = None
        self.next = None
class Memoria:

    def __init__(self, max):
        self.head = self.new()
        self.max = max
        self.tam = 1 #gambiarra
        self.ocupado = 0
        self.free = 1
        
    def new(self):
        bloco = Bloco()
        bloco.pos = 0
        return bloco
    def insert(self, op, q, id):
        alocado = ""
        liberado = ""
        bloco_i = self.head
        while (alocado != "True" or alocado != "False") and (liberado != "True" or liberado != "False"):
            #opcao de alocaçao
            if op == 1:
                #procura um espaço de memoria vazio
                while bloco_i.id != "0":
                    bloco_i = bloco_i.next
                #encontrou
                if bloco_i.id == "0":
                    bloco_ini = bloco_i
                    #calcula tamanho do bloco de memoria livre
                    while bloco_i.id == "0" and bloco_i.next != None:
                        bloco_i = bloco_i.next
                    bloco_fin = bloco_i
                    #verifica se tem espaco no bloco encontrado para alocar o novo bloco
                    #q é o tamanho do novo bloco
                    if q <= (bloco_fin.pos-bloco_ini.pos):
                        bloco_i = bloco_ini
                        while bloco_i != bloco_fin:
                            bloco_i.id = id
                            self.ocupada += 1
                            self.free -= 1
                            bloco_i = bloco_i.next
                        alocado = "True"
                        break
                    #se nao tiver espaço neste bloco
                    else:
                        #verifica se já é a ultima celula de memoria
                        if bloco_fin.pos == self.tam:
                            if self.max - self.tam >= q:
                                for i in np.arange(0, q):
                                    b = Bloco()
                                    b.id = id
                                    b.pos = pos_fin.pos + 1
                                    pos_fin.next = b
                                    self.ocupado += 1
                                    
                                    pos_fin = b
                                alocado = "True"
                                break
                            else:
                                alocado = "False"
                                break
                        #se nao for o ultimo bloco
                        else:
                            if self.max - pos_fin.pos >= q:
                                for i in np.arange(0, q):
                                    b = Bloco()
                                    b.id = id
                                    b.pos = pos_fin.pos + 1
                                    pos_fin.next = b
                                    self.ocupado += 1
                                    pos_fin = b
                                alocado = "True"
                                break
                            else:
                                alocado = "False"
                                break
                #memoria cheia
                else:
                    alocado = "False"
                    break
            #opcao de liberaçao
            if op == 0:
                #procura um espaço de memoria ocupado pelo id
                while bloco_i.id != id and bloco_i.next != None:
                    bloco_i = bloco_i.next
                #encontrou um id ocupando memoria
                if bloco_i.id == id:
                    while bloco_i.id == id:
                        bloco_i.id = "0"
                        self.ocupada += 1
                        self.free += 1
                        bloco_i = bloco_i.next
                    liberado = "True"
                    break
                #nenhum id correspondente ocupando memoria
                else:
                    liberado = "False"
                    break
    #TODO para otimizar, vou registrar o tam da lista, qtde ocupada e qtde free, já previamente
    #entao vou ter que tirar essa parte daqui da funcao display
    def display(self): #tam é pra facilitar o codigo, mas nao é o ideal
        bloco = self.head
        ocupada = 0
        free = 0
        saida = ""
        while bloco != None:
            if bloco.next != None:
                if bloco.id == bloco.next.id:
                    if bloco.id != "0":
                        ocupada += 1
                    else:
                        free += 1
                else:
                    if bloco.id != "0":
                        ocupada += 1
                    else:
                        free += 1
                    saida += bloco.id
                    saida += " "
                bloco = bloco.next
                continue
            #esse if e else aqui repetindo nao ficou bom
            if bloco.id != "0":
                ocupada += 1
            else:
                free += 1
            saida += bloco.id
            bloco = bloco.next #None
        print(saida)
        print(ocupada)
        print(free)
            # #ultimo diferente do penultimo
            # if (tam - (ocupada+free)) == 1:
            #     saida += bloco.id
            # else:
            #     saida +=
            # bloco = bloco.next #None
max, n = map(int, input().split())
mem = Memoria(max)
for i in np.arange(n):
    op, q, id = input().split()
    op = int(op)
    q = int(q)
    mem.insert(op, q, id)
mem.display()
'''

#Questao F - Gerenciador de memoria

#mudei a logica criando a classe bloco e o atributo "tam" facilita as operaçoes, nao sendo mais necessario ficar percorrendo a lista encadeada Memoria. Ufa!!
class Bloco:
    def __init__(self, id, tam):
        self.id = id
        self.tam = tam
        self.next = None
        
class Memoria:
    def __init__(self, max):
        self.head = self.new("0", max)
        self.max = max
        #self.tam = 0
        self.ocupada = 0
        self.livre = max
    def new(self, id, max):
        b = Bloco(id, max)
        return b
    
    def insert(self, bloco_in):
        b = self.head
        if b.id == "0" and b.tam >= bloco_in.tam:
            #codigos abaixo = X
            if b.tam > bloco_in.tam:
                bloco_in.next = b
                self.head = bloco_in
                b.tam -= bloco_in.tam
                self.ocupada += bloco_in.tam
                self.livre -= bloco_in.tam
            elif b.tam == bloco_in.tam:
                bloco_in.next = b.next
                self.head = bloco_in
                self.ocupada += bloco_in.tam
                self.livre -= bloco_in.tam
        elif self.livre >= bloco_in.tam:
            nao_achou_bloco = True
            b_prev = b
            while nao_achou_bloco == True and b_prev.next != None:
                if b_prev.next.tam >= bloco_in.tam and b_prev.next.id == "0":
                    nao_achou_bloco = False
                else:
                    b_prev = b_prev.next
            achou_bloco = not nao_achou_bloco
            if achou_bloco == True:
            #codigo abaixo = X modificando self.head po b_prev
                if b_prev.next.tam > bloco_in.tam:
                    bloco_in.next = b_prev.next
                    b_prev.next = bloco_in
                    bloco_in.next.tam -= bloco_in.tam
                    self.ocupada += bloco_in.tam
                    self.livre -= bloco_in.tam
                elif b_prev.next.tam == bloco_in.tam:
                    bloco_in.next = b_prev.next.next
                    b_prev.next = bloco_in
                    self.ocupada += bloco_in.tam
                    self.livre -= bloco_in.tam
    
    def libera(self, bloco_in):
        b = self.head
        #caso a memoria nao esteja toda livre ou toda ocupada
        if b.next != None:
            #inicio da memoria
            if b.id == bloco_in.id:
                #codigo abaixo = Y
                if b.next.id == "0":
                    b.id = "0"
                    self.ocupada -= b.tam
                    self.livre += b.tam
                    b.tam += b.next.tam
                    b.next = b.next.next
                else:
                    b.id = "0"
                    self.ocupada -= b.tam
                    self.livre += b.tam
            #meio ou final da memoria
            else:
                nao_achou_bloco = True
                while nao_achou_bloco == True and b.next != None:
                    b = b.next
                    if b.id == bloco_in.id:
                        nao_achou_bloco = False
                achou_bloco = not nao_achou_bloco
                if achou_bloco == True:
                    #meio da memoria
                    if b.next != None:
                        #codigo abaixo = Y
                        if b.next.id == "0":
                            b.id = "0"
                            self.ocupada -= b.tam
                            self.livre += b.tam
                            b.tam += b.next.tam
                            b.next = b.next.next
                        else:
                            b.id = "0"
                            self.ocupada -= b.tam
                            self.livre += b.tam
                    #final da memoria
                    elif b.next == None:
                        b.id = "0"
                        self.ocupada -= b.tam
                        self.livre += b.tam
        #caso a memoria esteja toda livre ou toda ocupada
        elif b.next == None and b.id != "0":
            b.id = "0"
            self.ocupada -= b.tam
            self.livre += b.tam #ou self.livre = self.max
     
    '''# 0 saindo como char
    def display(self):
    saida = [""]
    b = self.head
    while b.next != None:
        saida += b.id
        saida += " "
        b = b.next
    saida += b.id
    print(saida)
    print(self.ocupada)
    print(self.livre)
    '''
    # 0 saindo como int
    def display(self):
        saida = []
        b = self.head
        while b.next != None:
            if b.id == "0":
                saida.append(int(b.id))
            else:
                saida.append(b.id)
            b = b.next
        if b.id == "0":
            saida.append(int(b.id))
        else:
            saida.append(b.id)
        #COLOCAREI um codigo para remover ids de blocos ocupados duplicados
        saida_nova = []
        for i in saida:
            if i in saida_nova and i != 0:
                continue
            else:
                saida_nova.append(i)
        print(*saida)
        print(self.ocupada)
        print(self.livre)
max, n = map(int, input().split())
mem = Memoria(max)
for i in np.arange(n):
    op, tam, id = input().split()
    op = int(op)
    tam = int(tam)
    b = Bloco(id, tam)
    if op == 1:
        mem.insert(b)
    elif op == 0:
        mem.libera(b)
mem.display()