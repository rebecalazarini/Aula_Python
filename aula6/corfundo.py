import pygame
import sys

pygame.init()

tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Meu primeiro jogo")

azul = (0, 0, 255)
preto = (0, 0, 0)

fonte = pygame.font.SysFont('Arial', 50)

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill(azul)

    texto = fonte.render("Meu primeiro jogo", True, preto)
    texto_rect = texto.get_rect(center=(800 // 2, 600 // 2))

    tela.blit(texto, texto_rect)

    pygame.display.update()

pygame.quit()
sys.exit()
