letras = list('abcdefghijklmnopqrstuvwxyz')
vogal = 'aeiou'

for i, letra in enumerate(letras):
    if letra in vogal:
        print('{} - na posicao: {}' .format(letra, i))