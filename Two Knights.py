import operator as op
from functools import reduce

def comb(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

k = int(input())
print(0)
for i in range(2,k+1):
    print(comb(i*i,2)-4*(i-1)*(i-2))
