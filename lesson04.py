# Decorador

def header(function):
    def decorator(nome):
        print("Bem vindo ao meu site!")
        return function(nome)
    return decorator


def footer(function):
    def decorator(nome):
        print("Copyright© 2020\n")
        return function(nome)
    return decorator


@footer
@header
def produto(nome):
    print(f"Produto: {nome} - R$ 2k")
    print("")


# header()
# produto("Cadeira Gamer")
# footer()

produto("Cadeira Gamer")
