# import numpy as np

# top = 20
# num_list = np.array(range(top)) + 1
# multiple = 2500

# # while not (multiple % num_list == 0).all():
# #     multiple += 1

# middle = top // 2
# found = False
# while not found:
#     multiple += 1
#     if (multiple % num_list[:middle] == 0).all():
#         if (multiple % num_list[middle:] == 0).all():
#             found = True
    

# found = False
# while not found:
#     divides = True
#     index = 0
#     while index < top and divides:
#         divides = (multiple % num_list[index] == 0)
#         index += 1
    
#     if index < top:
#         multiple += 1
#     else:
#         found = True

# print(multiple)

num = 0
divisable = False

while (not divisable):
    num += 20
    number = 20 

    while number > 0:
        divisable = (num % number == 0)
        
        if not divisable:
            break
        
        number -= 1
        
print(num)