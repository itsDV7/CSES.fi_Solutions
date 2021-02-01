# Problem
Time limit: 1.00 s Memory limit: 512 MB

The Tower of Hanoi game consists of three stacks (left, middle and right) and n round disks of different sizes. Initially, the left stack has all the disks, in increasing order of size from top to bottom.

The goal is to move all the disks to the right stack using the middle stack. On each move you can move the uppermost disk from a stack to another stack. In addition, it is not allowed to place a larger disk on a smaller disk.

Your task is to find a solution that minimizes the number of moves.

Input

The only input line has an integer n: the number of disks.

Output

First print an integer k: the minimum number of moves.

After this, print k lines that describe the moves. Each line has two integers a and b: you move a disk from stack a to stack b.

Constraints<br>
`1≤n≤16`

Example

Input:<br>
`2`

Output:
```
3
1 2
1 3
2 3
```

# Solution
```
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
```
