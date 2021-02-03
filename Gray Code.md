# Problem

Time limit: 1.00 s Memory limit: 512 MB

A Gray code is a list of all 2n bit strings of length n, where any two successive strings differ in exactly one bit (i.e., their Hamming distance is one).

Your task is to create a Gray code for a given length n.

Input

The only input line has an integer n.

Output

Print 2n lines that describe the Gray code. You can print any valid solution.

Constraints<br>
`1≤n≤16`

Example

Input:<br>
`2`

Output:<br>
```
00
01
11
10
```

# Solution
```
def gray_code(n):
    def gray_code_recurse (g,n):
        k=len(g)
        if n<=0:
            return

        else:
            for i in range (k-1,-1,-1):
                char='1'+g[i]
                g.append(char)
            for i in range (k-1,-1,-1):
                g[i]='0'+g[i]

            gray_code_recurse (g,n-1)

    g=['0','1']
    gray_code_recurse(g,n-1)
    return g

def main():
    n=int(input())
    g = gray_code (n)

    if n>=1:
        for i in range (len(g)):
            print(g[i])

main()
```
