import numpy as np
#Questao 4 - Multilista

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
