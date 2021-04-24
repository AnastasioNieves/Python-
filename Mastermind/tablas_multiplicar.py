numero = int(input("numero a multiplicar: "))

for n in range(0, 11):
    if n % 2 == 0:
        print("{} x {} = {}".format(n, numero, n * numero))