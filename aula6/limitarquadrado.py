import pygame
import sys

pygame.init()

# Configuração da janela
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Movimento do Quadrado")

# Cores
azul = (0, 0, 255)
preto = (0, 0, 0)

# Posições iniciais do quadrado
x = 400
y = 300
tamanho = 50
velocidade = 5

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Verificar quais teclas estão pressionadas
    teclas = pygame.key.get_pressed()

    # Mover o quadrado com limitações de tela
    if teclas[pygame.K_LEFT] and x > 0:
        x -= velocidade  # Move para a esquerda
    if teclas[pygame.K_RIGHT] and x < 800 - tamanho:
        x += velocidade  # Move para a direita
    if teclas[pygame.K_UP] and y > 0:
        y -= velocidade  # Move para cima
    if teclas[pygame.K_DOWN] and y < 600 - tamanho:
        y += velocidade  # Move para baixo

    # Preencher a tela com a cor preta
    tela.fill(preto)

    # Desenhar o quadrado
    pygame.draw.rect(tela, azul, (x, y, tamanho, tamanho))

    # Atualizar a tela
    pygame.display.update()

pygame.quit()
sys.exit()
