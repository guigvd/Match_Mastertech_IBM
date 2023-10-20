# Realizar uma soma dos elementos de um tuple.

test_tup = (7, 8, 9, 1, 10, 7)

def sum_tuple(tuple):
    return sum(list(tuple))

print("The original is: "+ str(test_tup))
print("The summation is: "+ str(sum_tuple(test_tup)))