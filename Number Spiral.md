# Problem
Time limit: 1.00 s Memory limit: 512 MB

A number spiral is an infinite grid whose upper-left square has number 1. Here are the first five layers of the spiral:

![Image - first five layers of the spiral](https://cses.fi/file/bba36f2601b99c7edc15865aa2a49e680a271075f30e86aa0e4e18d00a779c21)

Your task is to find out the number in row y and column x.

Input

The first input line contains an integer t: the number of tests.

After this, there are t lines, each containing integers y and x.

Output

For each test, print the number in row y and column x.

Constraints
```
1 ≤ t ≤ 10^5
1 ≤ y , x ≤ 10^9
```
Example

Input:
```
3
2 3
1 1
4 2
```

Output:
```
8
1
15
```

# Solution
```
t = int(input())
ans = []
for i in range(t):
  row, col = list(map(int,input().strip().split()))
  if row % 2 == 0:
    row_start = row **2
  else:
    row_start = ((row - 1) **2) + 1
  if col % 2 != 0:
    col_start = col **2
  else:
    col_start = ((col - 1) **2) + 1

  if col >= row and col_start % 2 == 0:
    ans.append(col_start + row - 1)
  elif col > row and col_start % 2 != 0:
    ans.append(col_start - row + 1)
  elif col < row and row_start % 2 == 0:
    ans.append(row_start - col + 1)
  else:
    ans.append(row_start + col - 1)

print(*ans)
```
