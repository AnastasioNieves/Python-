lista_compra = []
compra = None

print("programa lista de la compra\n")

while True:
    compra = input("Que desea comprar? {Q} para salir: ")

    if compra == "Q":
        break

    elif compra in lista_compra:
        print("{} ya esta en la lista".format(lista_compra))

    else:
        if input("Seguro que quiere añadir {} a la lista? [S/N]".format(compra)) == "S":
            lista_compra.append(compra)



print("la lista de la compra es:")
print(lista_compra)
