# ATOMAÇÃO DE VERIFICAÇÃO

from math import pi

def calcArea(r):
    if r < 0:
        raise ValueError('Nao pode ser valor negativo')
    
    if type(r) not in [float, int]:
        raise TypeError('Somente numeros')
    
    areaC = pi*(r**2)
    return areaC

valores = [1, 3, 0, -1, -3, 2+3j, True,'ola']

for v in valores:
    areaCalc = calcArea(v)
    print('O valor passado e: ', v, 'A area calculada e: ', areaCalc)