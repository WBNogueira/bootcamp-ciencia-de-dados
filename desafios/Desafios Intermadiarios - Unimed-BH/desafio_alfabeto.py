import string

letra = input()

def lista_alfabeto():
    return list(string.ascii_uppercase)

print(lista_alfabeto().index(letra) + 1)