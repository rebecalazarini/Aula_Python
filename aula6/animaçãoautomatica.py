import pygame
import sys

pygame.init()

tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Círculo que se mexe")

azul = (0, 233, 205)
preto = (0, 0, 0)

x = 400
y = 300
raio = 30
velocidade_x = 5
velocidade_y = 5

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    x += velocidade_x
    y += velocidade_y

    if x - raio <= 0 or x + raio >= 800:
        velocidade_x = -velocidade_x

    if y - raio <= 0 or y + raio >= 600:
        velocidade_y = -velocidade_y

    tela.fill(preto)

    pygame.draw.circle(tela, azul, (x, y), raio)

    pygame.display.update()

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
