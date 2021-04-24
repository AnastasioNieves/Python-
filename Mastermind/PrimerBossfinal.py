import random



print("Juego de la mazmorra\n"
      "--------------------\n"
      "\n"
      "Despues de escuchar algunos rumores en la taberna del pueblo sobre una cueva que esconde un tesoro muy antigüo\n"
      "el cual se dice que alberga el fruto del eden , un poderoso artilugio de la antigüedad.\n"
      "Tu decides creer estos rumores y ir a explorar la cueva \n" 
      "Al llegar a la cueva ves una puerta :\n")

opcion = input("{A} Abres la puerta a lo loco | {B} Compruebas que es un camino seguro antes de abrir\n")

if opcion == "A":
      print("Abres la puerta y entras sin mirar que habia un mecanismo que activa una trampa al abrir la puerta\n"
            "Un hacha enorme te corta por la mitad\nGAME OVER")
      exit()

elif opcion == "B":
      print("Al comprobar la puerta te percatas de un mecanismo oculto:\n")
      opcion = input("{A} - Decides desactivar el mecanismo | {B} - Decides ignorarlo y continuar\n")
      if opcion == "B":
            print("Abres la puerta y entras pero el  mecanismo que viste activa una trampa al abrir la puerta\n"
                  "Un hacha enorme te corta por la mitad\nGAME OVER")
            exit()

      elif opcion == "A":
            print("Desactivas el mecanismo , abres la puerta y continuas el camino durante varios minutos hasta\n "
                  "que llegas a un claro y ves un esqueleto sosteniendo una joya extraña:\n")
            opcion = input("{A} - Decides cojer la joya | {B} - Decides no cojer la joya\n")
            if opcion == "A":
                  joya_inventario = True

            elif opcion == "B":
                  joya_inventario = False

numero_random_liche = random.randint(1, 100)

print("Continuas por el camino hasta llegar a una enorme sala llena de esqueletos y un porton de piedra al fondo\n"
      "cuando llegas al porton aparece ante ti un liche de aspecto dudoso y te dice: \n"
      "Si el tesoro quieres alcanzar este enigma deberas solventar\n"
      "Cuanto es 13 * {}".format(numero_random_liche))

opcion = int(input("¿Cual es el resultado?"))

if opcion == 13 * numero_random_liche :
      print("Era un trampa del liche y solo quiere robar el alma de gente inteligente\n"
            "Te roba el alma y mueres \n")
      exit()
elif opcion != 13 * numero_random_liche :
      print("El liche se rie de ti y dice que no llegaras muy lejos por lo que te abre el porton\n"
            "Tras el porton ves unas escalinatas que suben hacia una luz y una extraña al final de la habitacion\n"
            "¿ Que dices hacer?\n")
      opcion = input("{A} - Te rindes y subes las escaleras | {B} - decides comprobar la estatua extraña\n")

      if opcion == "A":
            print("Decides que esta aventura es demasiado peligrosa y que tu vida es mas valiosa\n"
                  "Subes las escaleras y sales de la cueva\n FIN")
      elif opcion == "B":
         print("Decides comprobar la estatua extraña, al mirarla de cerca ves que tiene un hueco extraño en el pecho\n"
               "te percatas que la forma del hueco coincide con la joya que viste antes.\n")
         if joya_inventario == True:
               print("Colocas la joya en la estatua y ves como se abre un camino secreto\n"
                     "de este sale un extraño brillo y entras a comprobar que es lo que provoca el brillo\n"
                     "al final del camino ves un precioso pedestal en el cual descansa el famoso artefacto\n"
                     "cuando lo cojes ves como adquieres un poder inigualable y te coviertes en el nuevo dios\n FIN.")

         elif joya_inventario == False:
               print("recuerdas que no cojiste la joya y tras llorar te rindes y abandonas\nGAME OVER")
               exit()
