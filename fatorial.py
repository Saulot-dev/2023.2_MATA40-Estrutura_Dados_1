import numpy as np
import sys

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


def main(): #função principal do nosso código
    n = int(sys.argv[1])
    print(f"Fatorial de {n} = {fatorial(n)}")
    print(f"Fatorial (rec) de {n} = {fat(n)}")

if __name__ == '__main__': #chama a função principal
    main()



