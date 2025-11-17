import pygame
import sys

pygame.init()

# Configuração da janela
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Colisão dos Quadrados")

# Cores
azul = (0, 0, 255)
vermelho = (255, 0, 0)
preto = (0, 0, 0)
branco = (255, 255, 255)

# Posições iniciais dos quadrados
x1, y1 = 100, 100
x2, y2 = 500, 100
tamanho = 50
velocidade = 5

# Definir os quadrados como pygame.Rect
quadrado1 = pygame.Rect(x1, y1, tamanho, tamanho)
quadrado2 = pygame.Rect(x2, y2, tamanho, tamanho)

# Fonte para a mensagem
fonte = pygame.font.SysFont('Arial', 30)

rodando = True
mensagem = ""

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Verificar quais teclas estão pressionadas
    teclas = pygame.key.get_pressed()

    # Mover o quadrado 1 com as teclas de direção
    if teclas[pygame.K_LEFT] and quadrado1.x > 0:
        quadrado1.x -= velocidade  # Move para a esquerda
    if teclas[pygame.K_RIGHT] and quadrado1.x < 800 - tamanho:
        quadrado1.x += velocidade  # Move para a direita
    if teclas[pygame.K_UP] and quadrado1.y > 0:
        quadrado1.y -= velocidade  # Move para cima
    if teclas[pygame.K_DOWN] and quadrado1.y < 600 - tamanho:
        quadrado1.y += velocidade  # Move para baixo

    # Verificar colisão entre os quadrados
    if quadrado1.colliderect(quadrado2):
        mensagem = "Os quadrados colidiram"

    # Preencher a tela com a cor preta
    tela.fill(preto)

    # Desenhar os quadrados
    pygame.draw.rect(tela, azul, quadrado1)
    pygame.draw.rect(tela, vermelho, quadrado2)

    # Exibir a mensagem, se houver colisão
    if mensagem:
        texto = fonte.render(mensagem, True, branco)
        texto_rect = texto.get_rect(center=(800 // 2, 600 // 2))
        tela.blit(texto, texto_rect)

    # Atualizar a tela
    pygame.display.update()

pygame.quit()
sys.exit()
