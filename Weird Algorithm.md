# Problem
Time limit: 1.00 s Memory limit: 512 MB

Consider an algorithm that takes as input a positive integer n. If n is even, the algorithm divides it by two, and if n is odd, the algorithm multiplies it by three and adds one. The algorithm repeats this, until n is one. For example, the sequence for n=3 is as follows:
3→10→5→16→8→4→2→1

Your task is to simulate the execution of the algorithm for a given value of n.

Input

The only input line contains an integer n.

Output

Print a line that contains all values of n during the algorithm.

Constraints<br>
`1≤n≤106`

Example

Input:<br>
`3`<br>
Output:<br>
`3 10 5 16 8 4 2 1`

# Solution
```
def check(n):
  print(n)
  if n==1:
    return
  elif n%2==0:
    n=n//2 
    return check(n)
  else:
    n=(n*3)+1
    return check(n)
n=check(int(input()))
```