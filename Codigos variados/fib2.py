import numpy as np
import sys

#n = (n-1)+(n-2)
#0, 1, 1, ?
#   p, u, p

#0, 1, 1, 2, 3, 5, 8, 13, ...
#                      ^
def fib(n, n_temp):
    if n == n_temp:
        return 

def main():
    n = int(sys.argv[1])
    if n == 0:
        print(0)
    elif n <= 2:
        print(1)
    else:
        print(f"Fib({n}) = {fib(n, 3, )}")

if __name__ == "__main__":
    main()




