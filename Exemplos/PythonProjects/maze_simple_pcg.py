import random

# Tamanho do labirinto (ímpar para facilitar a geração)
largura = 15
altura = 15

# Inicializa o labirinto com paredes
labirinto = [['#']*largura for _ in range(altura)]

# Função para checar se uma célula está dentro do labirinto
def dentro_do_labirinto(x, y):
    return 0 <= x < largura and 0 <= y < altura

# Função para checar se uma célula é uma fronteira válida
def fronteira_valida(x, y):
    if dentro_do_labirinto(x, y) and labirinto[y][x] == '#':
        vizinhos = [(x, y-2), (x, y+2), (x-2, y), (x+2, y)]
        contagem_celulas_livres = 0
        for vx, vy in vizinhos:
            if dentro_do_labirinto(vx, vy) and labirinto[vy][vx] == ' ':
                contagem_celulas_livres += 1
        return contagem_celulas_livres == 1
    return False

# Função para remover a parede entre duas células
def remover_parede(x, y):
    labirinto[y][x] = ' '

# Posição inicial (ímpar para garantir que seja uma célula válida)
x, y = random.randrange(1, largura, 2), random.randrange(1, altura, 2)
remover_parede(x, y)

# Lista para armazenar as fronteiras válidas
fronteiras = [(x, y-2), (x, y+2), (x-2, y), (x+2, y)]

# Gera o labirinto usando o algoritmo de Prim
while fronteiras:
    x, y = random.choice(fronteiras)
    if fronteira_valida(x, y):
        remover_parede(x, y)
        fronteiras.extend([(x, y-2), (x, y+2), (x-2, y), (x+2, y)])
    fronteiras.remove((x, y))

# Imprime o labirinto
for linha in labirinto:
    print(''.join(linha))