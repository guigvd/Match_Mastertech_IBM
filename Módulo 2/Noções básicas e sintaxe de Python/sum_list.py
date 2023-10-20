# Escreva o código que calcula uma lista de números fornecidos

def sum_list(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum_list(list[1:])
    
num_list = [3, 5, 8, 9, 9]
print(sum_list(num_list))