# Retorno da funções

# Void

def ola(nome):
    print(f"Olá, {nome}")


ola("Guilherme")

print("")


# Return


def soma(a: int, b: int):
    resultado = a + b
    return resultado


result = soma(5, 5)
print(f"Result: {result}")

print("")

# High ordem Function


def msg(header, footer):
    header()
    print("Olá, mundo!")
    footer()


def header():
    print("----Header----")


def footer():
    print("----Footer----")


msg(header=header, footer=footer)
