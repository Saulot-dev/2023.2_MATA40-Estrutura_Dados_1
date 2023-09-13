import numpy as np
import sys

#n = (n-1)+(n-2)
#0, 1, 1, ?
#   p, u, p

#0, 1, 1, 2, 3, 5, 8, 13, ...
#                      ^
def fib(n):
    proximo = 0
    ultimo = 1
    penultimo = 0 

    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        for i in np.arange(2, n+1): #[i,f)
            proximo = ultimo + penultimo
            penultimo = ultimo
            ultimo = proximo

    return proximo

def main():
    n = int(sys.argv[1])
    print(f"Fib({n}) = {fib(n)}")

if __name__ == "__main__":
    main()




