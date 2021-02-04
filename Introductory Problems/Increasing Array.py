n = int(input())
x = list(map(int,input().strip().split()))[:n]
count = 0
for i in range(n-1):
  if x[i] > x[i+1]:
    count = count + (x[i]-x[i+1])
    x[i+1] = x[i]
print(count)
