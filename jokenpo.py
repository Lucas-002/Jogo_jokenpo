from random import randint
from time import sleep

# Definindo os itens do jogo
itens = ['pedra', 'papel', 'tesoura']
computador = randint(0, 2)

# Indice
print('{:-^40}'.format(' Welcome to the Game '))
print("""Escolha sua jogada:
(0) PEDRA
(1) PAPEL
(2) TESOURA""")

# Verificação de entrada do jogador
while True:
    try:
        jogador = int(input('Qual é a sua opção: '))
        if jogador in [0, 1, 2]:
            break
        else:
            print("Opção inválida! Por favor, escolha 0, 1 ou 2.")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número (0, 1 ou 2).")

# Contagem regressiva
print('\033[32mJO')
sleep(1)
print('\033[33mKEN')
sleep(1)
print('\033[36mPOOO')
sleep(1)

# Lógica do jogo
print('\033[35m')
print('-==-==' * 4)
print(f'Computador jogou {itens[computador]}')
print(f'Você jogou {itens[jogador]}')
print('-==-==' * 4)
print('\033[m')

# Resultados possíveis
resultados = [
    ['\033[33mEMPATE!', '\033[34mVOCÊ GANHOU!!!', '\033[31mVOCÊ PERDEU!!!'],
    ['\033[31mVOCÊ PERDEU!!!', '\033[33mEMPATE!', '\033[34mVOCÊ GANHOU!!!'],
    ['\033[34mVOCÊ GANHOU!!!', '\033[31mVOCÊ PERDEU!!!', '\033[33mEMPATE!']
]

# Imprimindo resultado
print(resultados[computador][jogador])
