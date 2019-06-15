import time
import math

divisor_sums = []
amicable =[]
start = time.time()

def divisors(n):
    divisor_list = []
    for x in range(1, int(math.sqrt(n)+1)):
        if n % x == 0:
            divisor_list.append(int(n/x))
            if x < math.sqrt(n):
                divisor_list.append(x)
    if (sum(divisor_list)-n) < 10001:
        divisor_sums.append(sum(divisor_list)-n)
    else:
        divisor_sums.append(0)

for x in range(1,10001):
    divisors(x)

def Amicable_numbers(n):
    for x in range(1,n):
        y = divisor_sums[x-1]
        z = divisor_sums[y-1]
        if z == x:
            amicable.append(x)

Amicable_numbers(10000)
print(sum(amicable))
print(amicable)
end = time.time()
print(end - start)
