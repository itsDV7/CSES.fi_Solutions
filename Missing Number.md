# Problem
Time limit: 1.00 s Memory limit: 512 MB

You are given all numbers between 1,2,…,n except one. Your task is to find the missing number.

Input

The first input line contains an integer n.

The second line contains n−1 numbers. Each number is distinct and between 1 and n (inclusive).

Output

Print the missing number.

Constraints<br>
`2≤n≤2⋅105`

Example

Input:<br>
`5`<br>
`2 3 1 5`

Output:<br>
`4`

# Solution
```
n = int(input())
print(n * (n + 1) // 2 - sum(map(int, input().split())))
```