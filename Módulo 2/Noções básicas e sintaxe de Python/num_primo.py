# Escreva um programa Python para testar se um número é primo.

import math

def isPrimo(num):
    if num < 1:
        return 'Nao e primo'
    elif num == 2:
        return 'E primo'
    elif num % 2 == 0:
        return 'Nao e primo'
    
    max_divisor = math.isqrt(num) + 1
    for i in range(3, max_divisor, 2):
        if num % i == 0:
            return 'Nao e primo'
        
    return 'E primo'

print(isPrimo(17))
print(isPrimo(15))