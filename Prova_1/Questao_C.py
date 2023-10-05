import numpy as np

#Questao C - Detector de Plágio
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
