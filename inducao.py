import numpy as np
import sys

def soma (k):
    resultado = 1

    for i in np.arange(2, k+1): #[2, k+1)
        resultado += i

    return resultado

def soma2(k):
    resultado = (k*(k+1))/2
    return int(resultado)

def main():  #função principal
    k = int(sys.argv[1])
    resultado = soma(k)
    print(f"Resultado de k={k}: {resultado}")

    resultado = soma2(k)
    print(f"Resultado-2 de k={k}: {resultado}")

if __name__ == '__main__': #chama a função principal
    main()







