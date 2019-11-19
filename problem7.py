def is_prime(num):
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True

count = 0
num = 1

while count < 10001:
    num += 1
    if (is_prime(num)):
        count += 1

print(num)