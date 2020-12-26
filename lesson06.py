# Classe & Objetos

class Animal:
    planeta = "terra"

    def nascer(self):
        print("Nasci!")

    def comer(self):
        print("Comi!")


class Mamifero(Animal):

    def comer(self):
        print("Tomei leite!")


class Oviparos(Animal):

    def nascer(self):
        print("Ovo quebrado, nasci!")


class Especial(Mamifero, Animal):

    def nadar(self):
        print("Nadai!")


print("Gato: ")
gato = Mamifero()
gato.nascer()
gato.comer()

print("")

print("Papagaio: ")
papagaio = Oviparos()
papagaio.nascer()
papagaio.comer()

print("")

print("Ornitorrinco: ")
ornitorrinco = Especial()
ornitorrinco.nascer()
ornitorrinco.comer()
ornitorrinco.nadar()

print("")

print(f"O Gato nasceu no planeta {gato.planeta}.")
print(f"O Papagaio nasceu no planeta {papagaio.planeta}.")
print(f"O Ornitorrinco nasceu no planeta {ornitorrinco.planeta}.")


# OBS: MRO (Ex: Especial.mro()) Ordena os atributos e metodos
