import string

texto_usuario = input("introduzca un texto: ")
letras_mayusculas = 0

for letra in texto_usuario:
    if letra in string.ascii_uppercase:
        letras_mayusculas += 1

print("Las letras mayusculas son: {}".format(letras_mayusculas))