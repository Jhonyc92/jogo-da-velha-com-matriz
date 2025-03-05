# Inicializa o tabuleiro como uma lista vazia
tabuleiro = []

# Loop para adicionar 3 linhas ao tabuleiro
for i in range(3):
    
    # Cria uma linha vazia
    linha = []
    
    # Loop para adicionar 3 espaços em branco a cada linha
    for j in range(3):
        
        # Adiciona um espaço em branco à linha
        linha.append(' ')
        
    # Adiciona a linha completa ao tabuleiro
    tabuleiro.append(linha)

# Exibe o tabuleiro atual
def exibir_tabuleiro():
    
    # Loop para percorrer cada linha do tabuleiro
    for linha in tabuleiro:
        
        # Imprime a linha atual do tabuleiro, separando cada célula por "|"
        print("|".join(linha))
        
        # Imprime um separador para visualizar melhor as linhas do tabuleiro
        print("-" * 5)
    
# Verifica se o jogador atual é o vencedor
def verificar_vencedor(jogador):
    
    # Loop para percorrer as linhas e colunas do tabuleiro
    for i in range(3):
        
        # Inicializa variáveis para verificar se todas as células são iguais ao jogador
        todas_celulas_linha = True
        todas_celulas_coluna = True
        
        # Loop para percorrer cada  coluna(j) da linha atual (i)
        for j in range(3):

            # Verifica se a célula atual na linha (i) e coluna (j) é diferente do jogador
            # Se for diferente, atualiza a variável 'todas_celulas_linha' para False
            if tabuleiro[i][j] != jogador:
                todas_celulas_linha = False

            # Verifica se a célula atual na coluna (i) e linha (j) é diferente do jogador
            # Se for diferente, atualiza a variável 'todas_celulas_coluna' para False
            if tabuleiro[j][i] != jogador:
                todas_celulas_coluna = False

        # Se todas as células em uma linha ou coluna são iguais ao jogador
        if todas_celulas_linha or todas_celulas_coluna:
            return True

        # Verifica a diagonal principal (de cima à esquerda para baixo à direita)
        if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
            return True

        # Verifica a diagonal secundária (de cima à direita para baixo à esquerda)
        if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
            return True

        # Se nenhuma das condições acima for atendida, retorna False (não há vencedor)
        return False

# Permite ao jogador atual fazer uma jogada
def jogada(jogador):
    
    # Inicia um loop infinito para garantir que o jogador faça uma jogada válida
    while True:
        
        # Solicita ao jogador que insira a linha e a coluna onde deseja jogar
        jogada = input(f"Jogador {jogador}, escolha a linha e coluna (ex: 0 2): ")

        # Tenta converter a entrada do jogador em coordenadas de linha e coluna
        try:
            
            linha, coluna = map(int, jogada.split())
            
            # Verifica se a célula escolhida no tabuleiro está vazia (representada por um espaço em branco)
            if tabuleiro[linha][coluna] == ' ':

                # Se estiver vazia, atualiza a célula com o símbolo do jogador atual (X ou O)
                tabuleiro[linha][coluna] = jogador

                # Sai do loop, pois a jogada foi válida
                break

            # Se a célula já estiver ocupada (não estava vazia)
            else:

                # Informa ao jogador que a posição escolhida já está ocupada
                print("Posição já ocupada. Tente novamente.")

        # Se ocorrer um erro (entrada inválida ou fora do intervalo), informa ao jogador
        except:
            print("Entrada inválida. Tente novamente.")

# Loop principal do jogo
# Define o jogador inicial como 'X'
jogador_atual = 'X'

# Inicia um loop para as 9 possíveis jogadas no jogo da velha
for _ in range(9):
    
    # Exibe o tabuleiro atualizado
    exibir_tabuleiro()
    
    # Permite que o jogador atual faça sua jogada
    jogada(jogador_atual)
    
    # Verifica se a jogada resultou em uma vitória para o jogador atual
    if verificar_vencedor(jogador_atual):
        
        # Exibe o tabuleiro final
        exibir_tabuleiro()
        
        # Informa que o jogador atual venceu o jogo
        print(f"Jogador {jogador_atual} venceu!")
        
        # Encerra o loop, pois o jogo terminou
        break
    
    # Alterna o jogador atual (de 'X' para 'O' ou vice-versa)
    jogador_atual = 'O' if jogador_atual == 'X' else 'X'

# Caso o loop termine sem encontrar um vencedor (todas as 9 jogadas foram feitas)
else:
    
    # Exibe o tabuleiro final
    exibir_tabuleiro()
    
    # Informa que o jogo terminou em empate
    print("Empate!")
