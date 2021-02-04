def check(n):
  print(n)
  if n==1:
    return
  elif n%2==0:
    n=n//2 
    return check(n)
  else:
    n=(n*3)+1
    return check(n)
n=check(int(input()))
