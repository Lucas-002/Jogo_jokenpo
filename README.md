# Pedra, Papel e Tesoura

## Descrição
Este é um jogo clássico de "Pedra, Papel e Tesoura" criado em Python. Ele permite que o jogador enfrente o computador, que faz escolhas aleatórias, e mostra o resultado do confronto de forma divertida.

## Funcionalidades
- O jogador escolhe entre as opções: Pedra, Papel ou Tesoura.
- O computador escolhe aleatoriamente uma das três opções.
- Exibe animações de contagem regressiva antes de revelar o resultado.
- Determina e exibe o vencedor com mensagens coloridas para realçar o resultado.

## Requisitos
- Python 3.6 ou superior.

## Como Jogar
1. Execute o script no terminal ou em um ambiente Python.
2. Escolha sua jogada digitando:
   - `0` para Pedra
   - `1` para Papel
   - `2` para Tesoura
3. O computador escolherá automaticamente sua jogada.
4. O resultado será exibido, mostrando:
   - O que você e o computador jogaram.
   - Quem ganhou a rodada.

### Exemplo de Execução
#### Entrada:
```plaintext
Escolha sua jogada:
(0) PEDRA
(1) PAPEL
(2) TESOURA
Qual é a sua opção: 1
```
#### Saída:
```plaintext
JO
KEN
POOO
----------------------------------------
Computador jogou pedra
Você jogou papel
----------------------------------------
VOCÊ GANHOU!!!
```

## Lógica do Jogo
1. **Empate:** O jogador e o computador escolhem a mesma opção.
2. **Vitória do Jogador:**
   - Pedra vence Tesoura.
   - Papel vence Pedra.
   - Tesoura vence Papel.
3. **Vitória do Computador:** O contrário das condições de vitória do jogador.

## Observações
- Se o jogador inserir uma entrada inválida, o programa solicitará que escolha novamente até que a entrada seja válida.
- Mensagens coloridas tornam o jogo mais interativo e amigável.

## Possíveis Melhorias
- Adicionar mais opções como "Lagarto" e "Spock" (variante do jogo).
- Implementar placar acumulativo entre o jogador e o computador.
- Criar uma interface gráfica para o jogo.


