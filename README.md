# Jogo da Velha — Trabalho da 3ª Avaliação

**Disciplina:** Lógica, Algoritmos e Programação  
**Curso:** Tecnologia em Banco de Dados  
**Instituição:** Faculdade PIT  
**Professor:** M.Sc. Tiago Martins Ribeiro

## Autora
- Damaris Adriele Santos Rodrigues (trabalho individual)

## Descrição
Jogo da Velha para dois jogadores, executado no terminal. O tabuleiro é uma matriz (lista de listas) criada e exibida por funções, percorrida com `for` aninhado. O programa tem menu com `while`, regras, validação de todas as entradas (nunca fecha com erro), placar em dicionário, histórico em vetor, opção de jogar novamente sem reiniciar e dois desafios de lógica.

## Como executar
1. Instale o Python 3.
2. Baixe o arquivo `jogo_da_velha.py`.
3. Abra o terminal na pasta do arquivo.
4. Execute: `python jogo_da_velha.py`

Não são utilizadas bibliotecas externas nem comandos `import`.

## Regras
- O tabuleiro tem 3 linhas e 3 colunas.
- Dois jogadores: X (começa) e O. Cada jogada informa linha e coluna (1 a 3).
- Vence quem completar uma linha, coluna ou diagonal com o seu símbolo.
- Se as nove casas forem preenchidas sem vencedor, há empate.

## Menu
1. Jogar uma partida (ao final, pergunta se quer jogar novamente)
2. Campeonato melhor de 3
3. Ver regras
4. Ver placar e histórico
5. Sair (mostra as estatísticas da sessão)

## Desafios de lógica implementados
1. **Campeonato "melhor de 3"** (básico): função `campeonato_melhor_de_tres()`. Um dicionário conta as vitórias da série e ela termina quando alguém chega a 2 vitórias. Empates não pontuam.
2. **Estatísticas da sessão** (básico): função `mostrar_estatisticas()`, com apoio de `maior_sequencia()` e `calcular_percentual()`. Mostra total de partidas, vitórias (`count()`), empates, porcentagens e maior sequência de vitórias.

## Estruturas de dados usadas
| Estrutura | Onde |
|---|---|
| Matriz | `tabuleiro` (lista de listas) |
| Vetor | `historico` (resultado de cada partida) e `jogadas` (posições jogadas) |
| Dicionário | `placar` e `vitorias_serie` |
| Tupla | `(nome, símbolo)` de cada jogador e `posicao = (linha, coluna)` |
| Conjunto | `casas_usadas` e `{"S", "N"}` |

## Funções
- `criar_tabuleiro(tamanho)`: cria a matriz e devolve (`return`) o tabuleiro.
- `mostrar_tabuleiro(tabuleiro)`: exibe a matriz com números de linhas e colunas.
- `contar_vazias(tabuleiro)`: devolve a quantidade de casas livres.
- `verificar_vitoria(tabuleiro, simbolo)`: devolve `True`/`False` conferindo linhas, colunas e diagonais com laços.
- `ler_numero(mensagem, minimo, maximo)`: valida números (`strip()` e `isdigit()`).
- `ler_sim_nao(mensagem)`: valida S/N usando um conjunto.
- `ler_nome(mensagem, nome_outro)`: valida nomes não vazios e diferentes.
- `ler_jogada(tabuleiro, casas_usadas, nome, simbolo)`: lê e valida a jogada, devolvendo a tupla `(linha, coluna)`.
- `calcular_percentual(parte, total)`: devolve a porcentagem.
- `mostrar_placar(placar, jogadores)`: exibe o placar em dicionário.
- `mostrar_historico(historico, jogadores)`: exibe o vetor de resultados.
- `maior_sequencia(historico, simbolo)`: devolve a maior sequência de vitórias.
- `mostrar_estatisticas(historico, jogadores)`: desafio de estatísticas.
- `jogar_partida(jogadores, placar, historico)`: executa uma partida e devolve o resultado.
- `campeonato_melhor_de_tres(jogadores, placar, historico)`: desafio do campeonato.
- `mostrar_regras()`: exibe as regras.
- `main()`: lê os nomes e controla o menu.

## Divisão de tarefas
Trabalho realizado de forma individual por Damaris Adriele Santos Rodrigues, responsável por todas as funções, pelos testes, pelo README, pelo relatório e pelo vídeo.

## Entrega
- Repositório GitHub: https://github.com/damarysadry/Tabuleiro_da_dry
- Vídeo no YouTube: [AGUARDANDO LINK]
