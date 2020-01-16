import math as m

def find_pythag_triplets(c):
    val = c ** 2
    b = 2
    a = m.sqrt(val - b ** 2)
    triplets = []

    while b < c or (not a.is_integer()): 
        b += 1
        a = m.sqrt(val - b ** 2)

        if a.is_integer() and a != 0:
            triplets.append((int(a), b))

    return set([tuple(sorted(t)) for t in triplets])


def special_pythagorean_triplet(total):
    c = 5
    while c < total:
        c += 1
        triplets = find_pythag_triplets(c)

        if triplets is None:
            continue
        else:
            for triplet in triplets:
                val = sum(triplet) + c
                if val == total:
                    print(triplet[0], triplet[1], c)
                    print(triplet[0] * triplet[1] * c)
                    break                  

special_pythagorean_triplet(1000)
# print(find_pythag_triplets(5))