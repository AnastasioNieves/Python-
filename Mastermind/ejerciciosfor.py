
texto_usuario = input("introduzca su frase: ")
espacios = 0
comas = 0
puntos = 0

for letra in texto_usuario:

    if letra  == ",":

        comas += 1

    if letra == " ":

        espacios += 1

    if letra == ".":

        puntos += 1



print(" he encontrado estas comas: {}".format(comas))
print(" he encontrado estos espacios: {}".format(espacios))
print(" he encontrado estos puntos: {}".format(puntos))