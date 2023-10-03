import numpy as np

'''
# Questao 1 - inverte lista
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

'''
#Está funcionando, porem acusando tempo limite excedido
#Farei sem head e tail
class Letra:
    def __init__(self, crypt, rom):
        self.id = crypt
        self.roman = rom
        self.prev = None
        self.next = None

class Alfabet:
    def __init__(self):
        self.head = self.new_list("head")
        self.tail = self.new_list("tail")
        self.head.next = self.tail
        self.head.prev = self.tail
        self.tail.next = self.head
        self.tail.prev = self.head
        
    def new_list(self, id):
        return Letra(id, "")

    def append(self, item):
        if self.head.next == self.tail:
            self.head.next = item
            item.next = self.tail
            item.prev = self.head
            self.tail.prev = item
        else:
            penultimo = self.tail.prev
            penultimo.next = item
            item.prev = penultimo
            item.next = self.tail
            self.tail.prev = item
            
    def free_list(self):
        self.head = None
        self.tail = None
        
    def decifra(self, pal_cifra, chave):
        letra = self.head.next
        decifrada = ""
        for i in pal_cifra:
            while letra.id != i:
                letra = letra.next
            for j in np.arange(0, chave):
                letra = letra.prev
            decifrada += letra.roman
        return decifrada
        
    def cifra(self, pal_roman, chave):
        letra = self.head.next
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