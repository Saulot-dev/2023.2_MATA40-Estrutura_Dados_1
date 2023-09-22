# import numpy as np

'''
# Produto Escalar
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
'''
Numero Primo
A ideia geral{
    Pressupor que n é primo até que se prove o contrário por meio de:

    ideia 1 {
        Verificar se é 2;
        Verificar se é divisível por 2 (caso n>2);
        Verificar se é divisível por 2 (caso n>5);
        etc;
    }
    ideia 2{
        A partir de n, um divisor e um contador
            n é o numero a ser verificado se é primo();
            o divisor é dado por {div e Z / div>0, div<=n};
            o contador é dado por {cont¹=0, (n%div == 0) => cont++} ;
            retornar valor de i;
            Complexidade 2n-1 ?
    }
}
'''

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
# Ideia 2
def divisores(n, div, cont):
    if n == div:
        return cont+1
    elif not(n%div):
        cont +=1
    divisores(n, div+1, cont)
n = int(input())
n_divisores = divisores(n, 1, 0)
if n_divisores > 2:
    print(0)
else:
    print(1)
'''
'''    
def sum_equals_3(x):
    dez_milhar = x/10000
    x %= 10000
    milhar = x/1000
    x %= 1000
    cent = x/100
    x %= 100
    dez = x/10
    x %= 10
    un = x
    if ((dez_milhar+milhar+cent+dez+un) % 3):
        return True

n = int(input())
primo = True

if not(n%2) or not(n%5) or sum_equals_3(x):
    primo = False
array = arr.array('i', range(2, n//2))
if primo:
    for i in range(0, n//2 - 2, 1):
        if array[i] < n:
            if not array[i]%2:
                array[i] = 0
            elif not array[i]%5:
                array[i] = 0
            elif sum_equals_3(array[i]):
                array[i] = 0
if primo:
    for i in range(2, n//2 - 2):
        if array[i] != 0:
            primo = False;
            break
if primo:
    print(1)
else:
    print(0)
'''
