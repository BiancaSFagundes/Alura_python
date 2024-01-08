#3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:

from colorama import init, Fore

# Inicializa a biblioteca colorama (necessário apenas no Windows)
init()

# Texto colorido
frase_colorida = f"{Fore.GREEN}A\n{Fore.CYAN}L\n{Fore.BLUE}U\n{Fore.RESET}R\n{Fore.YELLOW}A{Fore.RESET}"

# Imprime a frase colorida
print(frase_colorida)