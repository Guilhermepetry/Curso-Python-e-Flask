# Tipos basico ou Tipos escalares

from typing import Counter, List


inteiro: int = 5
flutuante: float = 6.1
online: bool = True
texto: str = "Guilherme"


# Inferência de tipos

numero = 3
fracao = 7.7
verdadeiro = True
nome = "Petry"

idade = 18


# Condicionais

if numero == 5:
    print("Numero igual a 5")
elif numero == 10:
    print("Numero igual a 10")
elif numero == 15:
    print("Numero igual a 15")
elif numero == 20:
    print("Numero igual a 20")
else:
    print("Numero não é igual a nenhuma alternativa ateriores")


# Função Bool()

print(bool(online is True))  # True

print(not bool(online))  # False

print(bool(idade >= 18 and online))  # True

print(bool(idade == 18 or online))  # True


# Ternario

print("Eu estou online!" if online else "Não estou online!")  # True


# Try & Except (EAFP)

a = 0
b = 10

try:
    b.upper()
    print(b // a)
except AttributeError as e:
    print("Error: ", str(e))
except ZeroDivisionError as e:
    print("Error: ", str(e))

# Estrutura de repetição

counter = 0

while counter < 21:
    print(f"Contador: {counter}")
    counter += 1
    if counter == 11:
        break


# Lista

cores: list = ["azul", "verde", "amarelo"]

cores.append("vermelha")
print(cores)  # ['azul', 'verde', 'amarelo', 'vermelha']


cores.insert(1, "branco")
print(cores)  # ['azul', 'branco', 'verde', 'amarelo', 'vermelha']

cores.remove("verde")
print(cores)  # ['azul', 'branco', 'amarelo', 'vermelha']


# Tuplas
identidade: tuple = ("Lucas", "1234567889-0", 15)

print(f"Nome: {identidade[0]}")
print(f"CPF: {identidade[1]}")
print(f"Idade: {identidade[2]}")

# Desempacotamento

nome, cpf, idade = identidade
print(nome, cpf, idade)

print("---------------//----------------------")

# Dicionários

pessoa: dict = {
    'nome': "João",
    'cpf': "123456789-0",
    'idade': 18,
    'cores': ["azul", "vermelho"]
}

print(f"Nome: {pessoa['nome']}")
print(f"CPF: {pessoa['cpf']}")
print(f"Idade: {pessoa['idade']}")
print(f"Idade: {pessoa['cores']}")

print("---------------//----------------------")

# Iterar

for cor in cores:
    print(cor)

for letra in "Lucas":
    print(letra)

for letra in "Lucas":
    if letra == "a":
        continue
    print(letra)

# List - Comprehension
print([letra for letra in "Lucas"])

# List - Comprehension filtrada
print([letra for letra in "Lucas" if letra != "a"])

# Iterar Dicionários
for chave in pessoa:
    print(chave, ": ", pessoa[chave])

for chave, valor in pessoa.items():
    print(chave, ": ", valor)
