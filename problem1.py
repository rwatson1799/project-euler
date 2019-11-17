multiples = []

for num in range(1, 1000):
    if (num % 5 == 0) or (num % 3 == 0):
        multiples.append(num)

print(sum(multiples))