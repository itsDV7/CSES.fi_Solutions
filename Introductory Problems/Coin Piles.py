t = int(input())
ans = []
while t:
  left, right = map(int,input().strip().split())
  if left == 0 and right == 0:
    ans.append("YES")
  elif left != 0 and right != 0:
    if left == 2 * right or right == 2 * left:
      ans.append("YES")
    elif left > 2 * right or right > 2 * left:
      ans.append("NO")
    elif left % 3 == 0 and right % 3 == 0:
      ans.append("YES")
    elif (left % 3 == 2 and right % 3 == 1) or (right % 3 == 2 and left % 3 == 1):
      ans.append("YES")
    else:
      ans.append("NO")
  else:
    ans.append("NO")
  t -= 1
print(*ans)
