# Problem
Time limit: 1.00 s Memory limit: 512 MB

A permutation of integers 1,2,…,n is called beautiful if there are no adjacent elements whose difference is 1.

Given n, construct a beautiful permutation if such a permutation exists.

Input

The only input line contains an integer n.

Output

Print a beautiful permutation of integers 1,2,…,n. If there are several solutions, you may print any of them. If there are no solutions, print "NO SOLUTION".

Constraints<br>
`1≤n≤106`

Example 1

Input:<br>
`5`

Output:<br>
`4 2 5 3 1`

Example 2

Input:<br>
`3`

Output:<br>
`NO SOLUTION`

# Solution
```
n = int(input())
all_even = []
all_odd = []
if n == 1:
  print(1)
elif n <=3:
  print("NO SOLUTION")
else:
  for i in range(1,n+1):
    if i % 2 == 0:
      all_even.append(i)
    else:
      all_odd.append(i)
print(*all_even, *all_odd)
```
