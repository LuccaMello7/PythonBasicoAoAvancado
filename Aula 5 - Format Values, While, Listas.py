"""
Formatando valores com modificadores - Aula 5

:s - Texto (strings)
:d - Inteiros (int)
:f - Float
:.(NÚMERO)F - Quantidade de casas decimais (float)
:(CARACTERE) (> OU < OU ^ )(Quantidade)( TIPO -s,d ou f)

> - Esquerda
< - Direita
^ - Centro

"""

num1 = 10
num2 = 3

divisao = num1 / num2
print( '{:.2f}.format(divisao)')

nome = 'Lucca Mello'
nome_formatado = '{:@>50}'.format(nome)

print(nome.lower()) # tudo minúsculo
print(nome.upper()) # TUDO MAIÚSCULO
print(nome.title()) # Primeiras letras Maiúsculas


###############################
# FATIAMENTO DE STRINGS
###############################

texto = 'python s2'

nova_string = texto[2:6]
print(nova_string)

nova_string0 = texto[:6]
print(nova_string0)

nova_string1 = texto[0::3]
print(nova_string1)

for letra in texto:
    print(letra)


##############################
# CALCULADORA SIMPLES PYTHON
##############################
while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    sair = input('Deseja sair? [s]im ou [n]ao:  ')

    if sair == 's':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número: ')
        continue

    num_1 = int(num1)
    num_2 = int(num_2)

    # + - / *

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num1 / num2)
    elif operador == '*':
        print(num1 * num2)
    else:
        print('Operador Inválido')
        