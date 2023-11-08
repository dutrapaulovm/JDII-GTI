import random
from collections import deque

# Tamanho do dungeon
largura = 10
altura  = 10

# Ponto inicial e final
ponto_inicial = (1, 1)
ponto_final   = (largura - 2, altura - 2)

# Função para verificar se uma célula está dentro do dungeon
def dentro_do_dungeon(x, y):
    return 0 <= x < largura and 0 <= y < altura

# Algoritmo de busca em largura para gerar o dungeon
def gerar_dungeon(largura, altura, ponto_inicial, ponto_final):
    dungeon = [['#'] * largura for _ in range(altura)]
    fila = deque([(ponto_inicial, [])])

    while fila:
        (x, y), caminho = fila.popleft()
        caminho = caminho + [(x, y)]

        if (x, y) == ponto_final:
            for cx, cy in caminho:
                dungeon[cy][cx] = ' '
            return dungeon

        movimentos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(movimentos)

        for dx, dy in movimentos:
            novo_x, novo_y = x + dx, y + dy
            if dentro_do_dungeon(novo_x, novo_y) and dungeon[novo_y][novo_x] == '#':
                fila.append(((novo_x, novo_y), caminho))

# Gerando o dungeon
dungeon_gerado = gerar_dungeon(largura, altura, ponto_inicial, ponto_final)

# Imprimindo o dungeon gerado
for linha in dungeon_gerado:
    print("".join(linha))