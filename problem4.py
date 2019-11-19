num1 = 999 
num2 = 999
highest_pal = 0
product = 0
middle = 0

while num2 > 99:
    product = str(num1 * num2)
    if int(product) > highest_pal:
        middle = len(product) // 2
        if (product[:middle] == product[middle:][::-1]):
            highest_pal = int(product)
    
    # Decrease numbers
    if num1 > 99:
        num1 -= 1
    else:
        num1 = 999
        num2 -= 1

print(highest_pal)