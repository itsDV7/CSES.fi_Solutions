n = int(input())
all_even = []
all_odd = []
if n == 1:
  print(1)
elif n <=3:
  print("NO SOLUTION")
else:
  for i in range(1,n+1):
    if i % 2 == 0:
      all_even.append(i)
    else:
      all_odd.append(i)
print(*all_even, *all_odd)
