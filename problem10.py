import numpy as np

def find_primes(top):
    nums = np.array(range(2, top + 1))
    primes = []

    while nums.size != 0:
        primes.append(nums[0])
        nums = nums[nums % primes[-1] != 0]

    return primes

# def find_primes(top):
#     nums = np.array(range(2, top + 1))
#     total = 0

#     while nums.size != 0:
#         total += nums[0]
#         nums = nums[nums % nums[0] != 0]

#     return total

# primes = find_primes(2000000)
# print(primes)

def sum_of_primes(top):
    primes = [2]
    for i in range(3, top + 1, 2):
        for prime in primes:
            if i % prime == 0:
                break
            if i < prime ** 2:
                primes.append(i)
                break
        else:
            primes.append(i)
    return sum(primes)

total = sum_of_primes(2000000)
print(total)

