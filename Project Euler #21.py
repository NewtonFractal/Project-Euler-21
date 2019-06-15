import time
import math

divisor_sums = []
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


print(divisor_sums[219])
print(divisor_sums[283])
for x in range(1,10000):
    y = divisor_sums[x-1]
    z = divisor_sums[y-1]
    if y == z:
        print(x)






end = time.time()
print(end - start)
