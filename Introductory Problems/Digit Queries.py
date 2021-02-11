def findNthDigit(n):
        digit = base = 1 
        while n > 9*base*digit:
                n -= 9*base*digit
                digit += 1
                base *= 10 
        q, r = divmod(n-1, digit)
        return int(str(base + q)[r])
 
for _ in range(int(input())):
        n = int(input())
        print(findNthDigit(n))
