import numpy as np
import sys

#n = (n-1)+(n-2)
#0, 1, 1, 2, 3, 5, 8, 13, ... 

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def main():
    n = int(sys.argv[1])
    print(f"Fib({n}) = {fib(n)}")

if __name__ == '__main__':
    main()


