# print('''Camiseta Unissex
# Tamanho: P, M, G, GG
# Material: 100% algodão
# Cores disponíveis: Preto, Branco, Vermelho''')

# print("Camiseta Unissex","Tamanho: P, M, G, GG","Material: 100% algodão","Cores disponíveis: Preto, Branco, Vermelho", sep ='\n')

# print('Camiseta Unissex', 'Tamanho: P, M, G, GG', 'Material: 100% algodão', 'Cores disponíveis: Preto, Branco, Vermelho')


# departamento = input("Digite o nome do departamento: ")
# responsavel = input("Digite o nome da pessoa responsável: ")
# print("O departamento de " + departamento + " é liderado por " + responsavel + ".")

# def classificar_musica(genero_favorito, genero_musica):
#     if genero_favorito == genero_musica:
#         return 'recomendada'
#     elif genero_favorito == 'Pop' or genero_favorito == 'Rock':
#         return 'neutra'
#     else:
#         return 'não recomendada'

# resultado = classificar_musica('Rock', 'Pop')
# print(resultado)

def configurar_tempo_foco():
    tempo = int(input("Digite o tempo de foco (25-45 min): "))
    if tempo < 25:
        print("Valor muito baixo. Configure um tempo maior ou igual a 25 minutos.")
    elif tempo > 45:
        print("Valor muito alto. Configure um tempo menor ou igual a 45 minutos.")
    else:
        print("Tempo configurado para", tempo, "minutos.")