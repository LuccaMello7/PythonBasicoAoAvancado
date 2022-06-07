
   # Aula 6 - While - Contadores e Acumuladores


contador = 1
acumulador = 1

while contador <= 10:
        print(contador, acumulador)

        if contador > 5:
            break

        acumulador = acumulador + contador
        contador += 1


else: 
        print('Cheguei no ELSE.')
print('Isso será executado!')


"""
Outro Exemplo

"""
frase = 'o rato roeu a roupa do rei de roma'

len_frase = len(frase)

contador = 0

while contador < len_frase:
    print(frase[contador], contador)
    contador += 1