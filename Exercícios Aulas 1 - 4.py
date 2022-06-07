"""
EXERCÍCIOS 

1) 

Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que o número não é inteiro

2)

Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito,
exiba a saudação apropriada. Ex: Bom Dia 0 -11, Boa Tarde 12 - 17 e Boa Noite 18-23.

3)

Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras 
ou menos escreve 'Seu nome é curto!' Se tiver entre 5 e 6 letras, escreva 'Seu
nome é normal' maior que 6 letras escreva: 'Seu nome é grande'

"""


#############################################
# Exercício 1
#############################################

num = input('Digite um número inteiro: ')


if num.isdigit():
    num = int(num)

    if (num % 2 == 0):
        print('Este número é PAR ')
    else:
        print('Este número é ÍMPAR ')

else: 
    print('Isso não é um número inteiro!')


#############################################
# Exercício 2
#############################################
horario = input('Digite um horário (0-23): ')

if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print('Horário deve estar entre 0 e 23 horas. ')
    else:
        if horario <= 11:
            print('Bom Dia!')
        elif horario <= 17:
            print('Boa Tarde!')
        else:
            print('Boa Noite!')

else:
    print('Por favor, digite um horário entre 0 e 23. ')

#############################################
# Exercício 3
#############################################

nome = input('Digite seu nome ')

tamanho = len(nome)

if tamanho <= 4:
    print('Seu nome é curto! ')
elif tamanho <= 6:
    print('Seu nome é normal! ')
else:
    print('Seu nome é grande')