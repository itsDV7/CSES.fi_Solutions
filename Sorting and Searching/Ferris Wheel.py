n, x = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
ans = 0
i, j = 0, n - 1

while i < j:
    if p[i] + p[j] <= x:
        j -= 1
        i += 1
    else:
        j -= 1
    ans += 1
if i == j:
    ans += 1
print(ans)
