fibonacci = [1, 2]
even_fib = [2]

val = sum(fibonacci)
while val < 4e6:
    fibonacci.append(val)
    if val % 2 == 0:
        even_fib.append(val)

    val = sum(fibonacci[-2:]) #sum the last two terms

print(fibonacci)
print(even_fib)
print(sum(even_fib))