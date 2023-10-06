#Questao 4 - Multilista

import numpy as np

class No:
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
    
    def insert_n(self, no):
        if self.head_n == None:
            self.head_n = no
        else:
            tmp = self.head_n
            if no.nome < tmp.nome:
                no.next_n = tmp
                self.head_n = no
            elif tmp.next_n != None:
                inseriu = False
                while tmp.next_n != None:
                    if no.nome < tmp.next_n.nome:
                        no.next_n = tmp.next_n
                        tmp.next_n = no
                        inseriu = True
                        break
                    else:
                        tmp = tmp.next_n
                if not inseriu:
                    tmp.next_n = no
            else:
                tmp.next_n = no
    def insert_i(self, no):
        if self.head_i == None:
            self.head_i = no
        else:
            tmp = self.head_i
            if no.idade < tmp.idade:
                no.next_i = tmp
                self.head_i = no
            elif tmp.next_i != None:
                inseriu = False
                while tmp.next_i != None:
                    if no.idade < tmp.next_i.idade:
                        no.next_i = tmp.next_i
                        tmp.next_i = no
                        inseriu = True
                        break
                    else:
                        tmp = tmp.next_i
                if not inseriu:
                    tmp.next_i = no
            else:
                tmp.next_i = no
            
    def display(self):
        p = self.head_n
        i = self.head_i
        while p != None:
            print(f"{p.nome} {p.idade} | {i.nome} {i.idade}")
            p = p.next_n
            i = i.next_i
            
            

n = int(input())
lista = Multilista()
for i in np.arange(0, n):
    nome, idade = input().split()
    idade = int(idade)
    no = No(nome, idade)
    lista.insert_n(no)
    lista.insert_i(no)
lista.display()
