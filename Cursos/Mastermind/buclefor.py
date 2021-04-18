









#para recorrer una coleccion elemento por elemento

for i in [1,2,3,4,5]:
    print("miguele")

print("\n\n")

#para imprimir los elementos de mi coleccion

coleccion = [1,2,3,4,5,"miguele"]

for i in coleccion:
    print(f"Elemento: {i}")

print("\n\n")



coleccion = {"Alejandro":22, "maria":24,"jose":45,"miguele":24 }
# para mostrar el elemento mas el valor a la vez.
for clave,valor in coleccion.items():
    print(f" {clave} -> {valor}")

print("\n\n")

#para recorer strings

coleccion = "miguele"
for i in coleccion:
    print(f"{i}")

print("\n\n")

#para imprimirlo en la misma linea separados por algun elemento

coleccion = "miguele"
for i in coleccion:
    print(f"{i}",end=".")

print("\n\n")

#funcion for.range

n=5

for i in range(0,5):
    print(i, "migule")
print("fin")