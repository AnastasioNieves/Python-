edad = int(input("¿ Que edad tiene? "))
tipo_carnet = input("digame su tipo de carnet (E para estudiante / P pensionista / F familia numerosa / N para ninguno) " )

if (edad <= 35 and edad >= 25 and tipo_carnet == "E") or edad < 10 or (edad > 65 and tipo_carnet == "P") or (tipo_carnet == "F"):
    print("se te ha aplicado el descuento")
else:
    print("no se te aplica el descuento")
