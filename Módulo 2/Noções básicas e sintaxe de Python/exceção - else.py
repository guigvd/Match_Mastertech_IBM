def divide(x, y):
    try:
        resultado = x/y
    except ZeroDivisionError:
        print('Nao pode dividir por zero')
    else:
        print('O reslultado e: ')
    finally:
        print('Executa o finally')
divide(4, 12)
# divide(4, 0)
