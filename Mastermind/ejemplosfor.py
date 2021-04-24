lista_numeros = []
numero_usuario = int(input("introduzca un numero en la lista: "))
lista_numeros.append(numero_usuario)

while input(" Desea introducir otro numero ? [S/N] ") == "S":
    numero_usuario = int(input("introduzca un numero en la lista: "))
    lista_numeros.append(numero_usuario)

numero_lower = lista_numeros[0]
numero_bigger = lista_numeros[0]

for numero in lista_numeros[1:]:
    if numero_lower > numero:
        numero_lower = numero

    if numero_bigger < numero:
        numero_bigger = numero

print("el numero menor es {} , el numero mayor es {}. ".format(numero_lower, numero_bigger))
