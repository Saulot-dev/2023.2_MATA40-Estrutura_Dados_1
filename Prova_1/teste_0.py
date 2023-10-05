import numpy as np

''' # Questao 1 - inverte lista
class No:
    def __init__(self, v):
        self.id = v
        self.next = None

class Lista:
    def __init__(self):
        self.head = self.new_list()
        self.tail = No("tail")
        self.head.next = self.tail
    def new_list(self):
        head = No("head")
        return head

    def append(self, no):
        if self.head.next == self.tail:
            no.next = self.tail
            self.head.next = no
        else:
            tmp = self.head
            while tmp.next != self.tail:
                tmp = tmp.next
            tmp.next = no
            no.next = self.tail
            
    def display(self):
        if self.head.next == self.tail:
            print("Lista vazia")
        else:
            tmp = self.head.next
            while tmp != self.tail:
                print(tmp.id, end = " ")
                tmp = tmp.next
    def remove(self, x):
        tmp = self.head.next
        if x == 0:
            self.head.next = tmp.next
        else:
            for i in np.arange(0, x-1):
                tmp = tmp.next
            tmp.next = tmp.next.next
            
    def free_list(self):
        self.head = None
    
    def find_no(self, pos):
        if pos == -1:
            return self.head
        tmp = self.head.next
        for i in np.arange(0, pos):
                tmp = tmp.next
        return tmp    
            
    def inverte_sublista(self, x, y): #x e y inclusos
        left = self.find_no(x-1)
        right = self.find_no(y+1) #tá retornando certo?
        no_x = self.find_no(x)
        no_y = self.find_no(y)
        while no_x != no_y:
            no_i = no_x.next
            no_x.next = right
            right = no_x
            no_x = no_i
        no_y.next = right
        left.next = no_y

N = int(input())
vetor = np.array(list(map(int, input().split())))
l = Lista()
for i in vetor:
    item = No(i)
    l.append(item)

I = int(input()) #Numero de inversoes a serem realizadas
for i in np.arange(0, I, 1):
    X, Y = map(int, input().split()) # 0<=X<N-1 e 1<=Y<=N-1
    l.inverte_sublista(X, Y)
    #l.display()
    
R = int(input()) #Numero de remoçoes a serem realizadas R = [1, N-1]
for i in np.arange(0, R, 1):
    X = int(input()) #posiçao a ser removida
    l.remove(X)
    #l.display()
l.display()

'''

''' # Questao 2 - Mensagens Criptografadas
class Letra: 
    def __init__(self, crypt, rom):
        self.id = crypt
        self.roman = rom
        self.prev = None
        self.next = None
        
class Alfabet:
    def __init__(self):
        self.head = self.new_list()
        
    def new_list(self):
        return None

    def append(self, letra):
        if self.head == None:
            self.head = letra
            letra.next = letra
            letra.prev = letra
        else:
            if self.head.next == self.head:
                self.head.next = letra
                self.head.prev = letra
                letra.prev = self.head
                letra.next = self.head
            else:
                tmp = self.head
                while tmp.next != self.head:
                    tmp = tmp.next
                tmp.next = letra
                self.head.prev = letra
                letra.next = self.head
                letra.prev = tmp
            
    def free_list(self):
        self.head = None
        
    def decifra(self, pal_cifra, chave):
        letra = self.head
        decifrada = ""
        for i in pal_cifra:
            while letra.id != i:
                letra = letra.next
            for j in np.arange(0, chave):
                letra = letra.prev
            decifrada += letra.roman
        return decifrada
        
    def cifra(self, pal_roman, chave):
        letra = self.head
        cifrada = ""
        for i in pal_roman:
            while letra.roman != i:
                letra = letra.next
            for j in np.arange(0, chave):
                letra = letra.next
            cifrada += letra.id
        return cifrada
        

alfabeto = Alfabet()
for i in np.arange(0, 26):
    id, r = input().split()
    letra = Letra(id, r)
    alfabeto.append(letra)

chave = int(input())
pal_cifrada = input()
print(alfabeto.decifra(pal_cifrada, chave))
pal_romana = input()
print(alfabeto.cifra(pal_romana, chave))
'''

'''#Questao 3 - Detector de Plágio
class Letra:
    def __init__(self, id):
        self.id = id
        self.next = None
class Texto:
    def __init__(self):
         self.head = self.new_list()
    
    def new_list(self):
        return None
    
    def append(self, letra):
        if self.head == None:
            self.head = letra
        else:
            tmp = self.head
            while tmp.next != None:
                tmp = tmp.next
            tmp.next = letra
    
    def find_plagio(self, text1):
        plagio = False
        letra2 = self.head
        i = 0
        while letra2.next != None and plagio == False: #primeira camada é o texto do autor (original)
            letra1 = text1.head #aqui dá pra melhorar tbm para nao ficar repetindo toda vez
            if letra1.id == letra2.id: #deu match da 1ª letra do texto a ser analisado com a do texto original
                while letra1.next != None and letra2.next != None:#confere se as proximas letras dao match
                    letra1 = letra1.next
                    letra2 = letra2.next #N estou conferindo se os textos terminaram, que daria erra pois objeto seria None
                    if letra1.id != letra2.id:
                        plagio = False
                        break
                    else:#essa repetiçao nao está boa. dá pra melhorar
                        plagio = True
                if letra1.next == None and plagio == True:
                    break
                elif letra1.next != None and letra2.next == None:
                    plagio = False
                    break
            else:
                letra2 = letra2.next
            i += 1
        if plagio == True:
            return f"Plagio encontrado na posicao {i}!"
        else:
            return "Nenhum plagio detectado!"
        

text1 = Texto()
text2 = Texto()
for i in input():
    l = Letra(i)
    text1.append(l)
for i in input():
    l = Letra(i)
    text2.append(l)
print(text2.find_plagio(text1))
'''

'''#Questao 4 - Multilista

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.next_n = None
        self.next_i = None
    
class Multilista:
    def __init__(self):
        self.head_n = self.new_list()
        self.head_i = self.new_list()
    def new_list(self):
        return None
    
    def insert(self, pessoa):
        if self.head_n == None and self.head_i == None:
            self.head_n = pessoa
            self.head_i = pessoa
        else:
            #classificacao para nome
            pessoa_tmp = self.head_n
            while pessoa_tmp.next_n != None:
                if pessoa.nome > pessoa_tmp.next_n.nome:
                    pessoa_tmp = pessoa_tmp.next_n
                else:
                    break
            #nome da pessoa adicionada é menor que a da 2 pessoa ou só tem um elemento no conjunto
            if pessoa_tmp == self.head_n:
                if pessoa.nome > self.head_n.nome:
                    pessoa.next_n = self.head_n.next_n
                    self.head_n.next_n = pessoa
                else:
                    pessoa.next_n = self.head_n
                    self.head_n = pessoa
            else:
                pessoa.next_n = pessoa_tmp.next_n
                pessoa_tmp.next_n = pessoa
                
            #classificacao para idade
            pessoa_tmp = self.head_i
            while pessoa_tmp.next_i != None:
                if pessoa.idade > pessoa_tmp.next_i.idade:
                    pessoa_tmp = pessoa_tmp.next_i
                else:
                    break
            #idade da pessoa adicionada é menor que a da 2 pessoa ou só tem um elemento no conjunto
            if pessoa_tmp == self.head_i:
                if pessoa.idade > self.head_i.idade:
                    pessoa.next_i = self.head_i.next_i
                    self.head_i.next_i = pessoa
                else:
                    pessoa.next_i = self.head_i
                    self.head_i = pessoa
            else:
                pessoa.next_i = pessoa_tmp.next_i
                pessoa_tmp.next_i = pessoa 
    def display(self):
        p = self.head_n
        i = self.head_i
        while p != None:
            print(f"{p.nome} {p.idade} | {i.nome} {i.idade}")
            p = p.next_n
            i = i.next_i
            
            

n = int(input())
conjunto = Multilista()
for pessoa in np.arange(n):
    nome, idade = input().split()
    idade = int(idade)
    pessoa = Pessoa(nome, idade)
    conjunto.insert(pessoa)
conjunto.display()
'''

#Questao 6 - Gerenciador de Memoria

class Bloco:
    def __init__(self):
        self.id = "0"
        self.pos = None
        self.next = None
class Memoria:
    def __init__(self, tam):
        self.head = None
        self.new(tam)
        
    def new(self, tam):
        bloco_tmp = Bloco()
        bloco_tmp.pos = 0
        self.head = bloco_tmp
        for i in np.arange(1, tam):
            bloco_i = Bloco()
            bloco_i.pos = i
            bloco_tmp.next = bloco_i
            bloco_tmp = bloco_i
    def insert(self, op, q, id, tam):
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
                    pos_ini = bloco_i.pos
                    #calcula tamanho do bloco de memoria livre
                    while bloco_i.id == "0" and bloco_i.next != None:
                        bloco_i = bloco_i.next
                    pos_fin = bloco_i.pos
                    #verifica se tem espaco no bloco encontrado para alocar o novo bloco
                    #q é o tamanho do novo bloco
                    if q <= (pos_fin-pos_ini):
                        bloco_ini = self.head
                        #volta para o inicio do bloco que contem espaço suficiente
                        while bloco_ini.pos != pos_ini:
                            bloco_ini = bloco_ini.next
                        bloco_fin = bloco_ini
                        #preenche os ids dos espaços necessarios de memoria do bloco com o id do input
                        i = 0
                        for i in np.arange(q):
                            bloco_fin.id = id
                            bloco_fin = bloco_fin.next
                        alocado = "True"
                        break
                    #se nao tiver espaço neste bloco
                    else:
                        #verifica se já é o ultimo bloco de memoria
                        if pos_fin == tam:
                            alocado = "False"
                            break
                        #se nao for, procura proximo bloco vazio
                        else:
                            if tam - pos_fin > q:
                                break
                            else:
                                continue
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
                        bloco_i = bloco_i.next
                    liberado = "True"
                    break
                #nenhum id correspondente ocupando memoria
                else:
                    liberado = "False"
                    break
    def display(self, tam): #tam é pra facilitar o codigo, mas nao é o ideal
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
tam, n = map(int, input().split())
mem = Memoria(tam)
for i in np.arange(n):
    op, q, id = input().split()
    op = int(op)
    q = int(q)
    mem.insert(op, q, id, tam)
mem.display(tam)