opcion = input("¿{I} ios o {A} Android ? ")

if opcion == "A": #Ha contestado android
    opcion = input("¿Tienes dinero ? (S/N) ")
    if opcion == "S": #tiene dinero
        opcion = input("¿Te importa la camara (S/N) ? ")
        if opcion == "S":
            print("El movil ideal para ti es el Google Pixel Supercamara ")
        elif opcion == "N":
            print("El movil ideal para ti es un Android Calidad-precio")
    elif opcion == "N":
        print("El movil ideal  para ti es el Android chino de 100 euros")

elif opcion == "I": #Ha contestado IOS
     opcion = input("¿Tienes dinero ? (S/N) ")

     if opcion == "S":
         print("Tu movil ideal es el iphone 12 pro max")
     elif opcion == "N":
         print("iphone de segunda mano")