# Crie uma função de registro que aceite qualquer
# número de argumentos e os imprima na tela em uma
# única linha. A linha deve começar com o prefixo
# ‘LOG:’.
# Modifica a função log para permitir que o usuário
# especifique qualquer prefixo desejado.
# Modificar a função log para que o prefixo tenha um
# valor padrão ‘LOG: ’.
# Modificar a função log para permitir ao usuário definir
# tanto o prefixo quanto o separador entre os
# argumentos. Ambos devem ser passados somente
# pelos nomes (não pela posição) 'sep' e 'prefix'. Estes
# não precisam ter um valor padrão.
# Modifica a função log para que agora 'sep' e 'prefix'
# tenham um valor padrão.
# Modifique a função log para aceitar o seguinte
# dicionário. Lembre-se de passá-lo desembalado com
# a sintaxe de asterisco duplo (**).


def log(*args, **kwargs):
    sep = kwargs.get("sep", " ")
    prefix = kwargs.get("prefix", "LOG: ")

    log_message = prefix + sep.join(str(arg) for arg in args)
    print(log_message)


# Chamada da função com prefixo personalizado e separador personalizado
log("Mensagem 1", "Mensagem 2", prefix="PREFIXO:", sep=" | ")

# Chamada da função com prefixo padrão e separador personalizado
log("Mensagem 3", "Mensagem 4", sep=" | ")

# Chamada da função com prefixo padrão e separador padrão
log("Mensagem 5", "Mensagem 6")

# Dicionário para ser passado desembalado com a sintaxe de asterisco duplo (**)
dicionario_args = {"arg1": 123, "arg2": "abc", "arg3": True}

# Chamada da função com desembalagem do dicionário
log(**dicionario_args)
