dolar_euro = 0.84
libra_euro = 1.15
euro_libra = 0.87
euro_dolar = 1.19
operacion = input("¿Que quiere convertir?\n"
                  "A - euro a dolar \n"
                  "B - euro a libra\n"
                  "C- dolar a euro\n"
                  "D - libra a euro\n")

cantidad = float(input("¿que cantidad desea cambiar?\n"))

if operacion == "A":
    print("Los dolares que le corresponden son: {} " .format(cantidad * euro_dolar) + "$")

elif operacion == "B":
    print("Las libras que le corresponden son: {} " .format(cantidad * euro_libra) + "£" )

elif operacion == "C":
    print("Los euros que le corresponden son: {} " .format(cantidad * dolar_euro) + "€")

elif operacion == "D":
     print("Los euros que le corresponden son: {} ".format(cantidad * libra_euro) + "€")

else: "Las opciones son A, B, C, D"





