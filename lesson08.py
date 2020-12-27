import store
from store.models import Categoria, Produto

print(f"Nome da Loja: {store.NAME_STORE}")

cadeira = Produto('CadeiraGamer', categoria=Categoria('Moveis'))

teclado = Produto('TecladoX', categoria=Categoria('Eletronico'))

print(cadeira.nome)
print(teclado.nome)
