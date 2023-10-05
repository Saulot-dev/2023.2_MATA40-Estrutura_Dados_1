import numpy as np

# Questao B - Mensagens Criptografadas
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
