# Escreva um programa para produzir a série Fibonacci em Python.

# n = int(input('Informe o numero '))
n = 5

first = 0
second = 1
sum = 0
count = 1

print('Sequencia de Fibonacci: ')
while(count <= n):
    print(sum)
    sum = first+second
    first = second
    second = sum
    count+=1

