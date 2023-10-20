# Busca linear
names = ['Gabriel', 'Ana', 'Pedro', 'Caio', 'Joice']
found = 'Pedro'

def buscarNome(nome, lista):
    for n in lista:
        if nome == n:
            return 'Nome encontrado'
    return 'Nome nao encontrado'

print(buscarNome(found, names))



# Busca binária
def buscarNome(nome, lista):
    tamanhoLista = len(lista)
    inicio = 0
    fim = tamanhoLista -1

    while inicio <= fim:
        meio = (inicio + fim)//2
        if lista[meio] == nome:
            return ('Nome na posicao: '+str(meio))
        elif lista[meio] < nome:
            inicio = meio+1
        elif lista[meio] > nome:
            fim = meio-1
    return 'Nao achei'

namesOrd = sorted(names)
print(buscarNome(found, namesOrd))
