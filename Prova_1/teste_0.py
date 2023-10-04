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

'''#Questao 4 - Multilista'''


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.next_pessoa = None
        self.next_idade = None
    
class Multilista:
    