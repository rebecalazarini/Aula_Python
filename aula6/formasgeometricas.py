import pygame
import sys

pygame.init()

tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Meu Primeiro Jogo")

# Definir as cores
azul = (0, 0, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)

# Fonte para o texto
fonte = pygame.font.SysFont('Arial', 50)

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Preencher a tela com a cor azul
    tela.fill(azul)

    # Desenhar um retângulo
    pygame.draw.rect(tela, vermelho, (150, 100, 200, 100))  # (x, y, largura, altura)

    # Desenhar um círculo
    pygame.draw.circle(tela, verde, (600, 150), 50)  # (x, y, raio)

    # Desenhar uma linha
    pygame.draw.line(tela, preto, (100, 500), (700, 500), 5)  # (x1, y1, x2, y2, largura)

    # Exibir o texto
    texto = fonte.render("Meu primeiro jogo", True, preto)
    texto_rect = texto.get_rect(center=(800 // 2, 600 // 2))
    tela.blit(texto, texto_rect)

    # Atualizar a tela
    pygame.display.update()

pygame.quit()
sys.exit()
