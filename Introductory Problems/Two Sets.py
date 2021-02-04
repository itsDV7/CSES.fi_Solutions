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
