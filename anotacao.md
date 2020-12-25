# Curso Python 

## Terminal args
- `python -C`
- `python -V`
- `python -M`

obs: Ipython

## Ambiente virtual (Video do youtube - CodeShow)

- `python -m venv .venv` 

### Força a execução do ambiente virtual do python

- `.venv/bin/python -V`

### Ativa o ambiente virtual

- `source .venv/bin/activate`

Obs1: Verifique o a localização do binário do python com o comando `which python` .

Obs2: Atualize o *pip* com `pip install --upgrade pip` .

### Instalando o IPython  

- `pip install ipython`

## Input & Output (IO)

### Stdin e Stdout 

O meio mais comum do usuário passar informações a um programa é via teclado. Por isto mesmo, ele é considerado a entrada padrão, e é daí que vem o nome ***Standard Input (stdin)***, ***Standard Output (stdout)*** e ***Standard Error (stderr)***.

### Abstrações

stdin:
 - `input()`

stdout:
 - `print()` 

Files:
  - Abrir `open('NomeDoArquivo.txt')`
  - Ler `open('NomeDoArquivo.txt').read()`
  - Sobrescrever `open('NomeDoArquivo.txt', 'm').write('texto')`
  - Escrever `open('NomeDoArquivo.txt', 'a').write('texto')` 

