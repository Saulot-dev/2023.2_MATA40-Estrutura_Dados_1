import numpy as np

#import do sys:
    #dá pra uma funcao chamar a outra, já passando os parametros de maneira mais rápida, por aí...;
    
import sys

#Implementaçao de Recursividade:
    #Primeira coisa é definir o "caso base";
    

def fat(n): # recursividade
    if n == 1: #case base | condição de parada
        return 1

    resultado = n * fat(n-1)

    return resultado

def fatorial(n): # O(n)
    resultado = 1

    for i in np.arange(2, n+1): #[2, k+1)
        resultado *= i

    return resultado

# duvida:
    # recursividade ajuda, em C, na questao de alocaçao e liberaçao de memória? Respondida;
    # Estratégia linear;
    


def fib1(n):
    resultado = 0
    
    if n == 0:
        return 0
    elif n == 1:
        return 1;
    else:
        resultado = fib(n-1) + fib(n-2)

def fib2(n):
    proximo = 0
    ultimo = 1
    penultimo = 0
    
    
    
def main(): #função principal do nosso código
    n = int(sys.argv[1])
    print(f"Fatorial de {n} = {fatorial(n)}")
    print(f"Fatorial (rec) de {n} = {fat(n)}")

if __name__ == '__main__': #chama a função principal
    main()



