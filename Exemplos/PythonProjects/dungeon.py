import random

# Dicionário de regras gramaticais para o mapa do jogo Rogue
gramatica_rogue = {
    "Parede": ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    "Chao": [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    "Porta": ["/", "\\"],
    "Jogador": ["@", "@", "@", "@", "@", "@", "@", "@", "@", "@"],
    "Inimigo": ["E", "O", "T", "G"],
    "Item": ["$", "$", "$", "$", "$", "$", "$", "$", "$", "$"]
}

# Função para gerar um mapa Rogue aleatório
def gerar_mapa_rogue(largura, altura, gramatica):
    mapa = [[random.choice(gramatica["Parede"]) for _ in range(largura)] for _ in range(altura)]
    
    # Adiciona chão ao mapa
    for y in range(1, altura - 1):
        for x in range(1, largura - 1):
            if random.random() < 0.7:
                mapa[y][x] = random.choice(gramatica["Chao"])
    
    # Adiciona portas
    for _ in range(5):
        x, y = random.randint(1, largura - 2), random.randint(1, altura - 2)
        if mapa[y][x] == gramatica["Chao"][0]:
            mapa[y][x] = random.choice(gramatica["Porta"])
    
    # Adiciona jogador, inimigos e itens
    x, y = random.randint(1, largura - 2), random.randint(1, altura - 2)
    if mapa[y][x] == gramatica["Chao"][0]:
        mapa[y][x] = random.choice(gramatica["Jogador"])
    
    for _ in range(10):
        x, y = random.randint(1, largura - 2), random.randint(1, altura - 2)
        if mapa[y][x] == gramatica["Chao"][0]:
            mapa[y][x] = random.choice(gramatica["Inimigo"])
    
    for _ in range(10):
        x, y = random.randint(1, largura - 2), random.randint(1, altura - 2)
        if mapa[y][x] == gramatica["Chao"][0]:
            mapa[y][x] = random.choice(gramatica["Item"])
    
    return mapa

# Gerando e imprimindo o mapa Rogue
largura_do_mapa = 50
altura_do_mapa = 20
mapa_rogue = gerar_mapa_rogue(largura_do_mapa, altura_do_mapa, gramatica_rogue)

for linha in mapa_rogue:
    print("".join(linha))