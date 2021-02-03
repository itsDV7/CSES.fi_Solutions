# Problem

Time limit: 1.00 s Memory limit: 512 MB

You have two coin piles containing a and b coins. On each move, you can either remove one coin from the left pile and two coins from the right pile, or two coins from the left pile and one coin from the right pile.

Your task is to efficiently find out if you can empty both the piles.

Input

The first input line has an integer t: the number of tests.

After this, there are t lines, each of which has two integers a and b: the numbers of coins in the piles.

Output

For each test, print "YES" if you can empty the piles and "NO" otherwise.

Constraints<br>
```
1≤t≤10^5
0≤a,b≤10^9
```
Example

Input:<br>
```
3
2 1
2 2
3 3
```
Output:<br>
```
YES
NO
YES
```

# Solution
```
t = int(input())
ans = []
while t:
  left, right = map(int,input().strip().split())
  if left==0 and right==0:
    ans.append("YES")
  elif left!=0 and right!=0:
    if left == 2*right or right == 2*left:
      ans.append("YES")
    elif left>2*right or right>2*left:
      ans.append("NO")
    elif left%3==0 and right%3==0:
      ans.append("YES")
    elif (left%3==2 and right%3==1) or (right%3==2 and left%3==1):
      ans.append("YES")
    else:
      ans.append("NO")
  else:
    ans.append("NO")
  t -= 1
print(*ans)
```
