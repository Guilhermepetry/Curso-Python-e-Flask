# Property

class Animal:
    planeta = "terra"
    _animal_nasceu = False

    @property
    def nasceu(self):
        return self._animal_nasceu

    def nascer(self):
        self._animal_nasceu = True
        print("Nasci!")

    def comer(self):
        print("Comi!")


class Mamifero(Animal):

    def comer(self):
        print("Tomei leite!")


gato = Mamifero()
print(f"O gato nasceu: {gato.nasceu}")

gato.nascer()
print(f"O gato nasceu: {gato.nasceu}")
