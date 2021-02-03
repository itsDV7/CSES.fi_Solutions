# Problem

Time limit: 1.00 s Memory limit: 512 MB

Your task is to calculate the number of trailing zeros in the factorial n!.

For example, `20!=2432902008176640000` and it has `4` trailing zeros.

Input

The only input line has an integer n.

Output

Print the number of trailing zeros in n!.

Constraints<br>
`1≤n≤10^9`

Example

Input:<br>
`20`

Output:<br>
`4`

# Solution
```
fact = int(input())
zeros = 0
while fact>=5:
  fact = fact//5
  zeros = zeros + fact
print(zeros)
```
