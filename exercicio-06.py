# Exercícios

# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias 
# de acordo com as seguintes condições:

# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

Idade = int(input('Informa a sua idade: '))

if 0 < Idade <= 12:
    print('É uma criança. ')
elif 12 < Idade <= 18:
    print('É um adolescente. ')
#else:
elif Idade > 18:
    print('É um adulto(a).')