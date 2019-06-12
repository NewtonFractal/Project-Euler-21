import time
import math
start = time.time()
divisors_a = []
divisors_b = [1,2,4,71]
numbers = []

def Amicable_numbers(upper_bound):
    for x in range(1, upper_bound):
        for y in range(1,x):
            if x % y == 0:
                divisors_a.append(y)
        for a in range(1, sum(divisors_a)-1):
            if sum(divisors_a) % a == 0:
                divisors_b.append(a)
        if x == sum(divisors_b):
            numbers.append(x)
            divisors_a.clear()
            divisors_b.clear()
        else:
            divisors_a.clear()
            divisors_b.clear()

Amicable_numbers(10000)
print(sum(numbers))
end = time.time()
print(end - start)
