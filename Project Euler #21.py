import time
import math

divisor_sums = []
divisor_number = []
amicable = []

def divisors(n):
    divisor_list = []
    for x in range(1, int(math.sqrt(n) + 1)):
        if n % x == 0:
            divisor_list.append(int(n / x))
            if x < math.sqrt(n):
                divisor_list.append(x)
    divisor_sums.append(sum(divisor_list) - n)
    divisor_number.append(n)
    
    
for x in range(220,230):
    divisors(x)



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
