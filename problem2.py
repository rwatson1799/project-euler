import numpy as np

fibonacci = [1, 2]

val = sum(fibonacci)
while val < 4e6:
    fibonacci.append(val)
    val = sum(fibonacci[-2:]) #sum the last two terms

print(fibonacci)

even_fib = (x for x in fibonacci if x % 2 == 0)
print(even_fib)
print(sum(even_fib))

