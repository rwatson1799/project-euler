import numpy as np

nums = np.array(range(2,2000000))

def is_prime(num):
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True

# primes =(x for x in nums if is_prime(x))

total = 0

for num in nums:
    if is_prime(num):
        total += num

print(total)