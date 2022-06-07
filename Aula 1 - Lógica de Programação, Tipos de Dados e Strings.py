"""
PYTHON BÁSICO - LÓGICA DE PROGRAMAÇÃO
"""

print('Hello World!', 'Lucca', sep = '-')



"""
TIPOS DE DADOS

STR - String
INT - Inteiros
FLOAT - Real / Ponto Flutuante
BOOL - booleano

"""
print('Luiz', type('Luiz')) # Luiz <class 'str'>   
print(10, type(10)) # 10 <class 'int'> 
print(25.34, type(25.34)) # 25.34 <class 'float'>
print('l' == 'L', type('l' =='L')) # False <class 'bool'> 

# Conversão de Tipos

print(type('Luiz'), bool('luiz')) # <class 'str'> True
print('10', type('10'), type(10)) # 10 <class 'str'> <class 'int'>

print('10' + '10') #1010

# String: nome
print('Lucca', type('Lucca')) # Lucca <class 'str'>

# Idade: int
print(31, type(31)) #31 <class 'int'>

#Altura: float
print(1.75, type(1.75)) # 1.75 <class 'float'>

# É maior de idade
print(31 > 18 , type(31 > 18)) # True <class 'bool'>


"""

OPERADORES ARITMÉTICOS

+ ADIÇÃO
- SUBTRAÇÃO
* MULTIPLICAÇÃO
/ DIVISÃO
// DIVISÃO NÚMERO INTEIRO
** EXPONENCIAÇÃO
% RESTO DA DIVISÃO - MÓDULO
() ALTERAR PRECEDÊNCIA


"""

print('Multiplicação',10 * 10) # Multiplicação 100
print('Adição', 10 + 10) # Adição 20
print('Subtração', 10 - 10) #Subtração 0
print('Exponenciação', 10**10) # Exponenciação 10.000.000.000
print('Divisão Número Inteiro', 10.59 // 3 ) # Divisão Número Inteiro 3.0   
print('Precedência Lógica', 5+2 *10) # Precedência Lógica 25
print('Precedência Lógica', (5+2) *10) # Precedência Lógica 70


nome = 'Lucca Mello'
idade = 31
altura = 1.75
e_maior = idade > 18
peso = 112
imc = (peso / (altura ** 2))

"""
FORMATAÇÃO DE STRING

"""
print(nome, 'tem', idade, 'anos de idade e seu IMC é: ', imc)
print(f'{nome} tem {idade} anos de idade e seu IMC é: {imc:.2f} ')
print('{} tem {} anos de idade e seu IMC é: {:.2f}'.format(nome, idade, imc))


"""
EXERCÍCIO

Criar variáveis para nome, idade, altura e peso de uma pessoa
Criar variável para o ano atual
Obter o ano de nascimento da pessoa 
Obter o IMC da pessoa com 2 casas decimais
Exibir um testo na tela com os valores usando F-Strings

"""

name = 'Lucca'
age = 31
alt = 1.75
weight = 112
immc = weight / (alt * alt)
ano_atual = 2022
nascimento = ano_atual - age


print('{} tem {} anos e seu IMC é: {:.2f}. Ele nasceu no ano de {}, portanto tem {} e estamos no ano de {} '.format(name, age, immc, nascimento, age, ano_atual))