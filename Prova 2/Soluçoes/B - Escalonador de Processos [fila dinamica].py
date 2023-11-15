class Elemento:
    def __init__(self, id, tempo):
        self.id = id
        self.tempo = tempo
        self.next = None
    
class Fila:
    def __init__(self, A, B):
        self.ini = None
        self.last = None
        self.tempo_total = 0
        self.run_time = A
        self.save_time = B
        self.letra = chr(ord("A") - 1)
    def input(self):
        for tempo in input().split():
            self.letra = chr(ord(self.letra) + 1)
            id = self.letra
            elem = Elemento(id, int(tempo))
            if self.ini == None:
                self.ini = elem
            elif self.ini.next == None:
                self.ini.next = elem
                self.last = elem
            else:
                self.last.next = elem
                self.last = elem

    def update(self):
        if self.ini.tempo >= self.run_time: # (tempo limite de execuçao do programa)
            self.tempo_total += self.run_time
            self.ini.tempo -= self.run_time
            #tira self.ini da fila
            if self.ini.tempo <= 0:
                self.output()	
                if self.ini.next:
                    self.ini = self.ini.next
                    #self.update()
                else:
                    self.ini = None
                    self.last = None
            #joga pro final da fila (ainda tem tempo)
            else:
                self.tempo_total += self.save_time
                if self.ini.next:
                    self.last.next = self.ini
                    self.last = self.ini
                    temp = self.ini.next
                    self.ini.next = None
                    self.ini = temp
                    #self.update()
        else: #tempo do processo < A (tempo limite de execuçao do programa)
            self.tempo_total += self.ini.tempo
            self.output()
            if self.ini.next:
                self.ini = self.ini.next
                #self.update()
            else:
                self.ini = None
                self.last = None
    def output(self):
        print(f'{self.ini.id} {self.tempo_total}')

A, B = map(int, input().split())
fila = Fila(A, B)
fila.input()
while fila.head:
    fila.update()