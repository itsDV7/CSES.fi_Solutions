def findNthDigit(n):
        digit = base = 1 
        while n > 9*base*digit:
                n -= 9*base*digit
                digit += 1
                base *= 10 
        p, q = divmod(n-1, digit)
        return int(str(base + p)[q])
 
for _ in range(int(input())):
        n = int(input())
        print(findNthDigit(n))
