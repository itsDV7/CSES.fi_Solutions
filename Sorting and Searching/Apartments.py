n,m,k = list(map(int, input().strip().split()))
desired = sorted(list(map(int, input().strip().split()))[:n])
apartments = sorted(list(map(int, input().strip().split()))[:m])

ans = 0
des_i = 0
for a in apartments:
    if des_i >= n:
        break
    while des_i < n - 1 and desired[des_i] + k < a:
        des_i += 1
    if desired[des_i] - k <= a <= desired[des_i] + k:
        ans += 1
        des_i += 1
print(ans)
