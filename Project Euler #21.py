import time
import math
divisor_sums = []
divisor_number = []
amicable = []
start = time.time()

def divisors(n):
    divisor_list = []
    for x in range(1, int(math.sqrt(n) + 1)):
        if n % x == 0:
            divisor_list.append(int(n / x))
            if x < math.sqrt(n):
                divisor_list.append(x)
    divisor_sums.append(sum(divisor_list) - n)
    divisor_number.append(n)
    
    
for x in range(1,10000):
    divisors(x)

end = time.time()
print(end - start)
