password = "condicional"
intento = 1
password_usuario = input("password\n")


while password_usuario != password:
    print("password incorrecta")
    password_usuario = input("introduzca de nuevo su password\n")

    if password_usuario == password:
        print(f"su password es: {password_usuario}")
    else:
        intento += 1
        if intento == 3 :
            print("su cuenta ha sido bloqueada")
            break



