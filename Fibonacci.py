numero = int(input("Fatorial de: ") )

resultado=1
contador =1

while contador <= numero:
    resultado *= contador
    contador += 1

print(resultado)