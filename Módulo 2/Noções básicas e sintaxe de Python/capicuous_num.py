# Escreva um programa Python para testar se um número é capicuous. Ou seja, se ele lê o mesmo da direita para a esquerda que da esquerda para a direita.

num = '55'

num2 = num[::-1]

if num == num2:
    print('E um numero capicua!')
else:
    print('Nao e um numero capicua!')