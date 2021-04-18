import random

numero = random.randint(1, 10)

intento = input("¿ Cual es tu numero ? ")

if intento == numero :
    print("Felicidades! has adivinado el numero ")

if intento != numero :
    print("Losiento , ha fallado ! ")

print("El numero ganador era: {}".format(numero))