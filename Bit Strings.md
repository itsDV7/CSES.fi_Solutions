# Problem

Time limit: 1.00 s Memory limit: 512 MB

Your task is to calculate the number of bit strings of length n.

For example, if n=3, the correct answer is 8, because the possible bit strings are 000, 001, 010, 011, 100, 101, 110, and 111.

Input

The only input line has an integer n.

Output

Print the result modulo 10<sup>9</sup>+7.

Constraints<br>
`1≤n≤10^6`

Example

Input:<br>
`3`

Output:<br>
`8`

# Solution
```
n = int(input())
print(pow(2,n,10**9+7))
```
