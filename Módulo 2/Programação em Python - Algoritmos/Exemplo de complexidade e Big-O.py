# Gerar uma lista de 100 mil de números aleatórios

import numpy as np
import time

start = time.time()

lista = list(np.random.randint(low=1, high=100000, size=100000))
# print(lista)

# end = time.time() - start

# print(f"Tempo de execução: {end:.10f} segundos")



# Complexidade Constante O(k) Constant Time

# def constante(x:list) -> list:
#     return x
# constante(x)



# Complexidade O(n) Linear Time

# def iterador_normal(x:list) -> list:
#     contador = len(x)
#     while(contador > 0):
#         contador -= 1
#         print(contador)
#     return x

# iterador_normal(lista)



# Complexidade O(n2) Quadratic Time

# def iterador_anidado(x:list) -> list:

#     contador_externo = len(x)//1000
#     contador_interno = len(x)//1000

#     while(contador_externo > 0):
#         contador_externo -= 1

#         for i in range(contador_interno):
#             i
#             return x

# iterador_anidado(lista)



# Complexidade O(log(n)) Logarithmic Time
def iterador_multiplicado(x: list) -> list:
    iterador = len(x)
    incremento = 1
    while(iterador > 0):
        iterador -= incremento
        incremento *= (incremento + 1)

    return x

listax = [1, 2, 3, 4]
iterador_multiplicado(listax)

end = time.time() - start
print(f"Tempo de execução: {end:.10f} segundos")