ans = []
def hanoi(n, _from, _to, _via):
    if n==1:
        ans.append(f"{_from} {_to}")
    else:
        hanoi(n-1, _from, _via, _to)
        ans.append(f"{_from} {_to}")
        hanoi(n-1, _via, _to, _from)
 
n = int(input())
hanoi(n, 1,3,2)
 
print(len(ans))
print("\n".join(s for s in ans))
