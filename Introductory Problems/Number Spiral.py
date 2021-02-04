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
