# Máquina de Turing

# import numpy as np

class Celula:
    def __init__(self, id):
        self.id = id
        self.next = None
        self.prev = None
class Lista:
    def __init__(self):
        self.head = None
        self.atual = None
    def move_esq(self):
        if l.atual.prev == None:
            tmp = Celula("b")
            tmp.next = l.atual
            l.atual.prev = tmp
            l.head = tmp
            l.atual = tmp
        else:
            l.atual = l.atual.prev
    def move_dir(self):
        if l.atual.next == None:
            tmp = Celula("b")
            tmp.prev = l.atual
            l.atual.next = tmp
            l.atual = tmp
        else:
            l.atual = l.atual.next
    def transicao(self, s, d):
        if s != "b":
            l.atual.id = s
            if d == "E":
                self.move_esq()
            else:
                self.move_dir()
        else:
            if l.atual.prev == None or l.atual.next == None:
                l.atual.id = s
                if d == "E":
                    self.move_esq()
                else:
                    self.move_dir()
            elif l.atual.prev.id == "b" or l.atual.next.id == "b":
                l.atual.id = s
                if d == "E":
                    self.move_esq()
                else:
                    self.move_dir()
            else:
                if d == "E":
                    self.move_esq()
                else:
                    self.move_dir()
    def display(self):
        tmp = self.head
        while tmp != None:
            if tmp.id != "b":
                print(tmp.id, end="")
            tmp = tmp.next
l = Lista()
for i in input():
    cel = Celula(i)
    if l.head == None:
        l.head = cel
    else:
        tmp = l.head
        while tmp.next != None:
            tmp = tmp.next
        tmp.next = cel
        cel.prev = tmp
l.atual = l.head
n = int(input())
for i in range(0, n):
    s, d = input().split()
    l.transicao(s,d)
l.display()