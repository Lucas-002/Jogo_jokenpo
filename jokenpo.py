from random import randint
from time import sleep

itens = ['pedra', 'papel', 'tesoura']
computador = randint(0, 2)

#INDICE
print('{:-^40}'.format(' Welcome or Game '))
print("""(0) PEDRA
(1) PAPEL
(2) TESOURA""")
jogador = int(input('Qual é a sua opção: '))

print('\033[32mJO'), sleep(1)
print('\033[33mKEN'), sleep(1)
print('\033[36mPOOO'), sleep(1)

#LOGICA DO JOGO
print('\033[35m')
print('-==-==' * 4)
print('Computador jogou {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jogador]))
print('-==-==' * 4)
print('\033[m')

if computador == 0:  # PEDRA
    if jogador == 0:
        print('\033[33mIMPATE!')
    elif jogador == 1:
        print('\033[34mVOCÊ GANHOU!!!')
    elif jogador == 2:
        print('\033[31mVOCÊ PERDEU!!!')
elif computador == 1:  # PAPEL
    if jogador == 0:
        print('\033[31mVOCÊ PERDEU!!!')
    elif jogador == 1:
        print('\033[33mIMPATE!')
    elif jogador == 2:
        print('\033[34mVOCÊ GANHOU!!!')
elif computador == 2:  # TESOURA
    if jogador == 0:
        print('\033[34mVOCÊ GANHOU!!!')
    elif jogador == 1:
        print('\033[31mVOCÊ  PERDEU!!!')
    elif jogador == 2:
        print('\033[33mIMPATE!')
