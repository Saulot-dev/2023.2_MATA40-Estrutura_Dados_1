import numpy as np

''' Produto Escalar

import array as arr

def prodesc(a, b, n):
    if n == 0:
        return a[0]*b[0]
    produto = a[n] * b[n] + prodesc(a, b, n-1)
    return produto
    
n = int(input())
a = arr.array('i', list(map(int, input().split())))
b = arr.array('i', list(map(int, input().split())))
print(prodesc(a, b, n-1))
'''


''' Questao 2 (numero primo)

n = int(input())
cont = 0
for i in range(1, n+1, 1):
    if not (n%i):
        cont += 1
if cont > 2:
    print(0)
else:
    print(1)
'''

'''Questao C - Soma Diagonal

def main():
    n = int(input())
    array = np.arange(n*n).reshape((n,n))
    for i in np.arange(n):
        array[i] = list(map(int, input().split()))
    array_traco = 0
    for i in np.arange(n):
        for j in np.arange(n):
            if i == j:
                array_traco += array[i][j]
    # por que resultado está saindo tipo float?
    # array_traco = int(array_traco)
    return array_traco

print(main())
'''
Esta ideia tá ruim
n = int(input()) #  0<=n<=25
def fib(n_atual, n, x):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    if x == 0: # n > 2, entao iniciam-se n_atual e x
        n_atual = 3
        x_ant = 0
        x_atual = 1
    if n_atual == n:
        return x + n_atual
    fib(n_atual+1, n, x_atual, x_atual)

print(fib(0, n, 0))
    


