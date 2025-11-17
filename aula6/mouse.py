import pygame
import sys

pygame.init()

tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Clique do Mouse")

preto = (0, 0, 0)
branco = (255, 255, 255)

fonte = pygame.font.SysFont('Arial', 30)

rodando = True
mensagem = ""

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            mensagem = f"Posição do Clique: ({x}, {y})"

    tela.fill(preto)

    if mensagem:
        texto = fonte.render(mensagem, True, branco)
        tela.blit(texto, (50, 50))

    pygame.display.update()

pygame.quit()
sys.exit()
