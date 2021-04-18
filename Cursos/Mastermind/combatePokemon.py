from random import randint
import os

VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 90

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtel = VIDA_INICIAL_SQUIRTLE
TAMAÑO_BARRA_DE_VIDA = 10

while vida_pikachu > 0 and vida_squirtel > 0:
    #Se desenvuelven los turnos de combate

    # Turno de Pikachu
    print("Turno de pikachu\n")

    ataque_pikachu = randint(1, 2)


    if ataque_pikachu == 1:
        # Bola voltio
        print("pikachu usa Bola voltio\n")
        vida_squirtel -= 10

    else:
        print("pikachu uso Onda Trueno\n")
        vida_squirtel -= 11

    if vida_squirtel < 0:
        vida_squirtel = 0

    if vida_pikachu < 0:
        vida_pikachu = 0

    barras_vida_squitle = int(vida_squirtel * TAMAÑO_BARRA_DE_VIDA / VIDA_INICIAL_SQUIRTLE)

    print("Squirtle:    [{}{}] ({}/{})".format("*" * barras_vida_squitle, " " * (TAMAÑO_BARRA_DE_VIDA - barras_vida_squitle),
                                               vida_squirtel, VIDA_INICIAL_SQUIRTLE))

    barras_vida_pikachu = int(vida_pikachu * TAMAÑO_BARRA_DE_VIDA / VIDA_INICIAL_PIKACHU)

    print("pikachu:    [{}{}] ({}/{})".format("*" * barras_vida_pikachu, " " * (TAMAÑO_BARRA_DE_VIDA - barras_vida_pikachu),
                                              vida_pikachu, VIDA_INICIAL_PIKACHU))

    input("Enter para continuar...\n\n")
    os.system("cls")

    print("Turno Squirtle")

    ataque_squirtle = None

    while ataque_squirtle != "P" and ataque_squirtle != "A" and ataque_squirtle != "B":
        ataque_squirtle = input("¿ Que ataque desea realizar {P}lacaje, Pistola {A}gua o {B}urbuja, {N}ada\n")

    if ataque_squirtle == "P":
        print("Squirtel ataca con placaje\n")
        vida_pikachu -= 10

    elif ataque_squirtle == "A":
        print("Squirtel ataca con pistola agua\n")
        vida_pikachu -= 12

    elif ataque_squirtle == "B":
        print("Squirtel ataca con burbuja\n")
        vida_pikachu -= 9

    elif ataque_squirtle == "N" :
        print("squirtle no hace nada")



    print("Squirtle:    [{}{}] ({}/{})".format("*" * barras_vida_squitle, " " * (TAMAÑO_BARRA_DE_VIDA - barras_vida_squitle),
                                               vida_squirtel, VIDA_INICIAL_SQUIRTLE))

    print("pikachu:    [{}{}] ({}/{})".format("*" * barras_vida_pikachu, " " * (TAMAÑO_BARRA_DE_VIDA - barras_vida_pikachu),
                                              vida_pikachu, VIDA_INICIAL_PIKACHU))

    input("Enter para continuar...\n\n")
    os.system("cls")

if vida_pikachu > vida_squirtel:
    print("Pikachu Gana el combate")

else:
    print("Squirtel gana el combate")



