# Funções

def ola(nome, maiuscula=False):

    if maiuscula:
        msg = f"Olá, {nome}!".upper()
    else:
        msg = f"Olá, {nome}!"

    print(msg)


ola(nome="Guilherme")
ola("Lucas")

ola("Karla", maiuscula=True)
ola("Karla", True)

print("")

# Desempacotamento


def ola02(nome, cpf, idade=18):
    print(f"Olá, {nome}!")
    print(f"CPF: {cpf}!")
    print(f"Idade: {idade}!")


pessoa = ["Guilherme", "123456789-9", 21]
ola02(*pessoa)

print("")

pessoa02 = {
    'nome': "Lucas",
    'cpf': "1234567899-8",
    'idade': 15
}

ola02(**pessoa02)

print("")


# Args & Kwarg


def ola03(nome, cpf, idade, *args, **kwargs):
    print(f"Olá, {nome}!")
    print(f"CPF: {cpf}!")
    print(f"Idade: {idade}!")
    print(f"Args: {args}!")
    print(f"Kwargs: {kwargs}!")


ola03("João",
      "123456789-8",
      18,
      True,
      "Verdadeiro",
      1,
      cor="azul",
      dia=1)

print("")
