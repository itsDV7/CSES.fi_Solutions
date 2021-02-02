# Problem

Time limit: 1.00 s Memory limit: 512 MB

Your task is to divide the numbers 1,2,…,n into two sets of equal sum.

Input

The only input line contains an integer n.

Output

Print "YES", if the division is possible, and "NO" otherwise.

After this, if the division is possible, print an example of how to create the sets. First, print the number of elements in the first set followed by the elements themselves in a separate line, and then, print the second set in a similar way.

Constraints<br>
`1≤n≤10^6`

Example 1

Input:<br>
`7`

Output:
```
YES
4
1 2 4 7
3
3 5 6
```
Example 2

Input:<br>
`6`

Output:<br>
`NO`

# Solution
```
n = int(input())
sm = sum(range(1,n+1))
if sm%2==0:
  print("YES")
  if n%2==0:
    set1 = list(range(1,n//2,2)) + list(range(n,n//2,-2))
    set2 = list(range(2,n//2+1,2)) + list(range(n-1,n//2,-2))
  else:
    set1 = []
    set2 = []
    sm=sm//2
    for i in range(n,0,-1):
      if i <= sm:
        set1.append(i)
        sm = sm - i
      else:
        set2.append(i)
  print(len(set1))
  print(*set1)
  print(len(set2))
  print(*set2)
else:
  print("NO")
```
  
