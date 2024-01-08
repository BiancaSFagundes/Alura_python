# Exercícios

# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos
# correspondem aos valores esperados determinados por você.

user_correto = 'alura'
senha_correta = 'alura123'

user = input('Digite o nome de usuário:')
senha = input('Digite a senha: ')

if user == user_correto and senha == senha_correta:
    print('Login bem sucedido!')

else:
    print('Credencial inválidas. Tente novamente.')