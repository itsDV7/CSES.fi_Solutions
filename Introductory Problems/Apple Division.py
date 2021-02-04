n = int(input())
p = list(map(int,input().strip().split()))[:n]

def minDiff(p, i, diff, totalSum):
  if i==0:
    return abs((totalSum - diff)-diff)
  return min(minDiff(p, i-1, diff+p[i-1], totalSum),minDiff(p, i-1, diff, totalSum))

print(minDiff(p, n, 0, sum(p)))
