# JOGO DA VELHA - Trabalho da 3ª Avaliação
# Disciplina: Lógica, Algoritmos e Programação
# Curso: Tecnologia em Banco de Dados
# Faculdade PIT
#
# Desafios de lógica implementados:
#   1) Campeonato "melhor de 3"  -> função campeonato_melhor_de_tres()
#   2) Estatísticas da sessão    -> funções mostrar_estatisticas(),
#                                   maior_sequencia() e calcular_percentual()
#
# Observação: o programa foi utilizado apenas com o conteúdo/funções permitido no manual do trabalho.
# (sem import, random, lambda, list comprehension, try/except ou classes).


# ---------------------------------------------------------------------
# FUNÇÕES DO TABULEIRO (matriz = lista de listas)
# ---------------------------------------------------------------------

def criar_tabuleiro(tamanho):
    """Recebe o tamanho (ex.: 3) e devolve uma matriz quadrada de espaços."""
    tabuleiro = []                      # matriz: lista de linhas
    for i in range(tamanho):            # laço externo: cria cada linha
        linha = []                      # vetor: uma linha do tabuleiro
        for j in range(tamanho):        # laço interno: cria cada coluna
            linha.append(" ")           # casa vazia
        tabuleiro.append(linha)         # adiciona a linha pronta na matriz
    return tabuleiro


def mostrar_tabuleiro(tabuleiro):
    """Recebe a matriz e exibe o tabuleiro com números de linhas e colunas."""
    tamanho = len(tabuleiro)

    # Monta o cabeçalho (números das colunas) e a linha separadora.
    cabecalho = "     "
    separador = "    -"
    for j in range(tamanho):
        cabecalho = cabecalho + " " + str(j + 1) + "  "
        separador = separador + "----"
    print("\n" + cabecalho)
    print(separador)

    # for aninhado: i percorre as linhas e j percorre as colunas da matriz.
    for i in range(len(tabuleiro)):
        texto = " " + str(i + 1) + "  |"        # número da linha
        for j in range(len(tabuleiro[i])):
            texto = texto + " " + tabuleiro[i][j] + " |"
        print(texto)
        print(separador)


def contar_vazias(tabuleiro):
    """Recebe a matriz e devolve (return) quantas casas ainda estão vazias."""
    vazias = 0
    for i in range(len(tabuleiro)):             # percorre as linhas
        for j in range(len(tabuleiro[i])):      # percorre as colunas
            if tabuleiro[i][j] == " ":
                vazias = vazias + 1
    return vazias


def verificar_vitoria(tabuleiro, simbolo):
    """Recebe a matriz e um símbolo; devolve True se ele completou uma
    linha, coluna ou diagonal, e False caso contrário (usa laços)."""
    tamanho = len(tabuleiro)

    # Linhas: para cada linha i, confere todas as colunas j.
    for i in range(tamanho):
        venceu = True
        for j in range(tamanho):
            if tabuleiro[i][j] != simbolo:
                venceu = False
        if venceu:
            return True

    # Colunas: para cada coluna j, confere todas as linhas i.
    for j in range(tamanho):
        venceu = True
        for i in range(tamanho):
            if tabuleiro[i][j] != simbolo:
                venceu = False
        if venceu:
            return True

    # Diagonal principal: casas (0,0), (1,1), (2,2)...
    venceu = True
    for i in range(tamanho):
        if tabuleiro[i][i] != simbolo:
            venceu = False
    if venceu:
        return True

    # Diagonal secundária: casas (0,2), (1,1), (2,0)...
    venceu = True
    for i in range(tamanho):
        if tabuleiro[i][tamanho - 1 - i] != simbolo:
            venceu = False
    if venceu:
        return True

    return False


# ---------------------------------------------------------------------
# FUNÇÕES DE LEITURA COM VALIDAÇÃO (o programa nunca pode quebrar)
# ---------------------------------------------------------------------

def ler_numero(mensagem, minimo, maximo):
    """Mostra a mensagem e repete a leitura até o jogador digitar um número
    inteiro entre minimo e maximo. Devolve esse número."""
    while True:
        entrada = input(mensagem).strip()       # strip() tira espaços extras
        if entrada.isdigit():                   # letra, símbolo ou vazio = False
            numero = int(entrada)               # conversão segura
            if numero >= minimo and numero <= maximo:
                return numero
        print("Entrada inválida! Digite um número de " +
              str(minimo) + " a " + str(maximo) + ".")


def ler_sim_nao(mensagem):
    """Pergunta S/N até receber uma resposta válida.
    Devolve True para 'S' e False para 'N'."""
    respostas_validas = {"S", "N"}              # conjunto de respostas aceitas
    while True:
        resposta = input(mensagem).strip().upper()
        if resposta in respostas_validas:       # consulta com in
            return resposta == "S"
        print("Resposta inválida! Digite S para sim ou N para não.")


def ler_nome(mensagem, nome_outro):
    """Lê um nome não vazio e diferente de nome_outro (ignora maiúsculas).
    Devolve o nome digitado. Em nome_outro, use "" se não houver outro."""
    while True:
        nome = input(mensagem).strip()
        if nome == "":
            print("O nome não pode ficar vazio.")
        elif nome.upper() == nome_outro.upper():
            print("Os jogadores precisam ter nomes diferentes.")
        else:
            return nome


def ler_jogada(tabuleiro, casas_usadas, nome, simbolo):
    """Pede linha e coluna até o jogador escolher uma casa livre.
    Registra a posição no conjunto casas_usadas e devolve a tupla
    (linha, coluna) já em índices da matriz (0 a tamanho-1)."""
    tamanho = len(tabuleiro)
    while True:
        print("\nVez de " + nome + " (" + simbolo + ")")
        linha = ler_numero("Escolha a linha (1 a " + str(tamanho) + "): ",
                           1, tamanho) - 1
        coluna = ler_numero("Escolha a coluna (1 a " + str(tamanho) + "): ",
                            1, tamanho) - 1
        posicao = (linha, coluna)               # tupla com a jogada

        if posicao not in casas_usadas and tabuleiro[linha][coluna] == " ":
            casas_usadas.add(posicao)           # marca a casa como usada
            return posicao
        print("Essa casa já está ocupada. Escolha outra posição.")


# ---------------------------------------------------------------------
# FUNÇÕES DE PLACAR, HISTÓRICO E ESTATÍSTICAS
# ---------------------------------------------------------------------

def calcular_percentual(parte, total):
    """Recebe uma parte e o total; devolve a porcentagem (float) com uma
    casa decimal. Se o total for 0, devolve 0.0."""
    if total == 0:
        return 0.0
    return int(parte * 1000 / total + 0.5) / 10


def mostrar_placar(placar, jogadores):
    """Recebe o dicionário do placar e a tupla de jogadores e exibe as
    vitórias, os empates e as porcentagens."""
    total = placar["X"] + placar["O"] + placar["Empates"]
    print("\n========== PLACAR ==========")
    print(jogadores[0][0] + " (X): " + str(placar["X"]) + " vitória(s) - " +
          str(calcular_percentual(placar["X"], total)) + "%")
    print(jogadores[1][0] + " (O): " + str(placar["O"]) + " vitória(s) - " +
          str(calcular_percentual(placar["O"], total)) + "%")
    print("Empates: " + str(placar["Empates"]) + " - " +
          str(calcular_percentual(placar["Empates"], total)) + "%")
    print("============================")


def mostrar_historico(historico, jogadores):
    """Exibe o vetor com o resultado de cada partida ("X", "O" ou "Empates")."""
    print("\n======= HISTÓRICO =======")
    if len(historico) == 0:
        print("Nenhuma partida foi concluída.")
    else:
        for i in range(len(historico)):
            if historico[i] == "X":
                texto = jogadores[0][0] + " (X) venceu"
            elif historico[i] == "O":
                texto = jogadores[1][0] + " (O) venceu"
            else:
                texto = "Empate"
            print(str(i + 1) + "ª partida: " + texto)
    print("=========================")


def maior_sequencia(historico, simbolo):
    """Percorre o vetor do histórico e devolve a maior quantidade de
    vitórias seguidas do símbolo informado."""
    atual = 0
    maior = 0
    for resultado in historico:
        if resultado == simbolo:
            atual = atual + 1
            if atual > maior:
                maior = atual
        else:
            atual = 0                           # a sequência foi interrompida
    return maior


def mostrar_estatisticas(historico, jogadores):
    """Desafio 'Estatísticas da sessão': total de partidas, vitórias (count),
    empates, porcentagens e maior sequência de vitórias de cada jogador."""
    total = len(historico)
    vitorias_x = historico.count("X")
    vitorias_o = historico.count("O")
    empates = historico.count("Empates")

    print("\n===== ESTATÍSTICAS DA SESSÃO =====")
    print("Total de partidas: " + str(total))
    print(jogadores[0][0] + " (X): " + str(vitorias_x) + " vitória(s), " +
          str(calcular_percentual(vitorias_x, total)) + "%, maior sequência: " +
          str(maior_sequencia(historico, "X")))
    print(jogadores[1][0] + " (O): " + str(vitorias_o) + " vitória(s), " +
          str(calcular_percentual(vitorias_o, total)) + "%, maior sequência: " +
          str(maior_sequencia(historico, "O")))
    print("Empates: " + str(empates) + ", " +
          str(calcular_percentual(empates, total)) + "%")
    print("==================================")


# ---------------------------------------------------------------------
# FUNÇÕES DE PARTIDA E CAMPEONATO
# ---------------------------------------------------------------------

def jogar_partida(jogadores, placar, historico):
    """Executa uma partida completa com um tabuleiro novo, atualiza o placar
    (dicionário) e o histórico (vetor). Devolve "X", "O" ou "Empates"."""
    tabuleiro = criar_tabuleiro(3)              # tabuleiro novo a cada partida
    casas_usadas = set()                        # conjunto: posições já jogadas
    jogadas = []                                # vetor: jogadas feitas na partida
    simbolo_atual = "X"                         # texto: quem joga agora
    rodada = 1                                  # inteiro: contador de rodadas
    resultado = "Empates"
    encerrada = False                           # booleano: a partida acabou?

    while not encerrada:
        print("\n--- Rodada " + str(rodada) + " ---")
        mostrar_tabuleiro(tabuleiro)

        # jogadores é uma tupla de tuplas: (nome, símbolo) de cada jogador.
        if simbolo_atual == "X":
            jogador = jogadores[0]
        else:
            jogador = jogadores[1]

        posicao = ler_jogada(tabuleiro, casas_usadas, jogador[0], simbolo_atual)
        jogadas.append(posicao)
        tabuleiro[posicao[0]][posicao[1]] = simbolo_atual

        if verificar_vitoria(tabuleiro, simbolo_atual):
            mostrar_tabuleiro(tabuleiro)
            print("\n" + jogador[0] + " (" + simbolo_atual + ") venceu a partida!")
            resultado = simbolo_atual
            encerrada = True
        elif contar_vazias(tabuleiro) == 0:
            mostrar_tabuleiro(tabuleiro)
            print("\nA partida terminou empatada!")
            resultado = "Empates"
            encerrada = True
        else:
            # Passa a vez para o outro jogador.
            if simbolo_atual == "X":
                simbolo_atual = "O"
            else:
                simbolo_atual = "X"
            rodada = rodada + 1

    # Mostra a lista de jogadas (cada uma é uma tupla linha, coluna).
    texto_jogadas = ""
    for posicao in jogadas:
        texto_jogadas = (texto_jogadas + "(" + str(posicao[0] + 1) + "," +
                         str(posicao[1] + 1) + ") ")
    print("Jogadas da partida (linha,coluna): " + texto_jogadas)

    placar[resultado] = placar[resultado] + 1   # atualiza o dicionário
    historico.append(resultado)                 # atualiza o vetor
    mostrar_placar(placar, jogadores)
    return resultado


def campeonato_melhor_de_tres(jogadores, placar, historico):
    """Desafio 'Campeonato melhor de 3': repete partidas até que um jogador
    alcance 2 vitórias na série e anuncia o campeão. Empate não pontua."""
    vitorias_serie = {"X": 0, "O": 0}           # dicionário: placar da série
    print("\nCAMPEONATO MELHOR DE 3")
    print("A série termina quando um jogador conquistar 2 vitórias.")

    while vitorias_serie["X"] < 2 and vitorias_serie["O"] < 2:
        resultado = jogar_partida(jogadores, placar, historico)
        if resultado in vitorias_serie:         # só "X" ou "O" pontuam
            vitorias_serie[resultado] = vitorias_serie[resultado] + 1
        else:
            print("Empate: a partida não conta ponto na série.")

        print("\nParcial do campeonato:")
        print(jogadores[0][0] + ": " + str(vitorias_serie["X"]))
        print(jogadores[1][0] + ": " + str(vitorias_serie["O"]))
        if vitorias_serie["X"] < 2 and vitorias_serie["O"] < 2:
            print("A próxima partida começará.")

    if vitorias_serie["X"] == 2:
        print("\nCAMPEÃO: " + jogadores[0][0] + "!")
    else:
        print("\nCAMPEÃO: " + jogadores[1][0] + "!")


def mostrar_regras():
    """Apresenta as regras do Jogo da Velha."""
    print("\nREGRAS DO JOGO")
    print("- O tabuleiro possui 3 linhas e 3 colunas.")
    print("- Dois jogadores participam: X e O (X começa).")
    print("- Os jogadores alternam as jogadas, informando linha e coluna.")
    print("- Vence quem completar uma linha, coluna ou diagonal.")
    print("- Se todas as casas forem preenchidas sem vencedor, há empate.")
    print("- No campeonato melhor de 3, vence quem ganhar duas partidas.")


# ---------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------------------

def main():
    """Lê os nomes, cria placar e histórico e controla o menu com while."""
    print("================================")
    print("       JOGO DA VELHA")
    print("================================")
    nome_x = ler_nome("Nome do jogador X: ", "")
    nome_o = ler_nome("Nome do jogador O: ", nome_x)

    # Tuplas: dados fixos de cada jogador (nome, símbolo).
    jogador1 = (nome_x, "X")
    jogador2 = (nome_o, "O")
    jogadores = (jogador1, jogador2)

    # Dicionário: placar acumulado durante toda a execução.
    placar = {"X": 0, "O": 0, "Empates": 0}

    # Vetor: guarda o resultado de cada partida ("X", "O" ou "Empates").
    historico = []

    opcao = 0
    while opcao != 5:
        print("\n========== MENU ==========")
        print("1 - Jogar uma partida")
        print("2 - Campeonato melhor de 3")
        print("3 - Ver regras")
        print("4 - Ver placar e histórico")
        print("5 - Sair (mostra estatísticas)")
        print("==========================")
        opcao = ler_numero("Escolha uma opção (1 a 5): ", 1, 5)

        if opcao == 1:
            jogando = True
            while jogando:                      # jogar novamente sem reiniciar
                jogar_partida(jogadores, placar, historico)
                jogando = ler_sim_nao("\nJogar novamente? (S/N): ")
        elif opcao == 2:
            campeonato_melhor_de_tres(jogadores, placar, historico)
        elif opcao == 3:
            mostrar_regras()
        elif opcao == 4:
            mostrar_placar(placar, jogadores)
            mostrar_historico(historico, jogadores)
        else:
            print("\nEncerrando o jogo...")
            mostrar_estatisticas(historico, jogadores)
            mostrar_historico(historico, jogadores)
            print("Obrigado por jogar!")


main()
