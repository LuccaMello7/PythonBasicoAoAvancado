"""
AULA  3 - CONDIÇÕES IF, ELIF, ELSE

"""

"""
OPERADORES RELACIONAIS

==
>
>=
<
<=
!= 

"""



num_1 = 2
num_2 = '2'

exp = (num_1 == num_2)
print(exp)



num_1 = 2
num_2 = 2

exp = (num_1 > num_2)
print(exp)


nome = input('Qual seu nome? ')
idade = input('Qual sua idade? ')
idade = int(idade)

#LIMITE PARA PEGAR EMPRÉSTIMO
idade_min = 20
idade_max = 50

if idade >= idade_min and idade <= idade_max:
    print(f'{nome} pode pegar o empréstimo ')
else:
    print(f'{nome} NÃO pode pegar o empréstimo ')



"""
OPERADORES LÓGICOS

AND
OR
NOT IN

"""
# Verdadeiro E Falso == Falso
#comp1 and comp2 

# Verdadeiro OU Verdadeiro =  Verdadeiro
#comparacao1 OR comparacao2

# NOT = INVERSOR

a = 2
b = 3

if not b > a:
    print('B é maior que A.')
else:
    print('A é maior que B.')


nome = 'lucca'

if 'u' in nome:
    print('Existe a letra U no seu nome.')
else:
    print('Não existe.')