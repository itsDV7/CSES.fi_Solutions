# Problem
Time limit: 1.00 s Memory limit: 512 MB

Your task is to count for k=1,2,…,n the number of ways two knights can be placed on a k×k chessboard so that they do not attack each other.

Input

The only input line contains an integer n.

Output

Print n integers: the results.

Constraints<br>
`1≤n≤10000`

Example

Input:<br>
`8`

Output:
```
0
6
28
96
252
550
1056
1848
```

# Solution
```
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
```
