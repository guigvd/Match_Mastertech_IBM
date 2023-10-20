keys = ['nombre', 'apellidos', 'edad']
values = ['Guido', 'van Rossum', '60']
d = dict(zip(keys, values)) # Creamos el diccionario
for k in d:
    info = '{}: {}'.format(k, d[k])
# Texto formateado con claves y valores
    print(info)
# Apellidos: van Rossum
# edad: 60
# nombre: Guido
print(d)