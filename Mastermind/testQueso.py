texto = "Bienvenido al Test del queso "
print(texto + "\n" + "-" * len(texto) + "\n")

puntuacion = 0
opcion = input("Pregunta 1: Que haces cuando ves una tabla de quesos \n"
               "A - Salgo corriendo \n"
               "B - Pruebo uno de los quesos o incluso varios \n"
               "C - No puedo evitar devorarla \n")

if opcion == "A":
    puntuacion = puntuacion + 0


elif opcion == "B":
    puntuacion = puntuacion + 5


elif opcion == "C":
    puntuacion = puntuacion + 10
else:
    print("Las opciones son A B C")
    exit()

opcion = input("Pregunta 2: ¿Como te gusta la hamburguesa?  \n"
               "A - sin queso \n"
               "B - con queso \n"
               "C - Con extra de queso \n ")

if opcion == "A":
    puntuacion = puntuacion + 0


elif opcion == "B":
    puntuacion = puntuacion + 5


elif opcion == "C":
    puntuacion = puntuacion + 10
else:
    print("Las opciones son A B C")
    exit()

opcion = input("Pregunta 3: ¿Eres intolerante a la lactosa \n"
               "A - Si \n"
               "B - A veces \n"
               "C - No \n ")

if opcion == "A":
    puntuacion = puntuacion + 0


elif opcion == "B":
    puntuacion = puntuacion + 5


elif opcion == "C":
    puntuacion = puntuacion + 10
else:
    print("Las opciones son A B C")
    exit()

if puntuacion >= 25:
    print("Resultado: Felicidades, eres un fanatico del queso")

elif puntuacion >= 15:
    print("Resultado: Felicidades, eres una persona que le gusta el queso")
else:
    print("Resultado: Felicidades, no te gusta el queso")



print(puntuacion)