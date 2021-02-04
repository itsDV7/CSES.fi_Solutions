from itertools import permutations

in_string = input().strip()
ans = [''.join(p) for p in permutations(in_string)]
ans = sorted(set(ans))
print(len(ans))
print(*ans)
