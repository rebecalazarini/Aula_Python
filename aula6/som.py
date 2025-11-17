import pygame
import sys  

pygame.init()

# Inicializar o mixer de áudio
pygame.mixer.init()

# Configuração da janela
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Som ao apertar Espaço")

# Cores
preto = (0, 0, 0)

# Carregar o som (substitua 'som.wav' pelo caminho correto para o arquivo de som)
som = pygame.mixer.Sound('dowlo')

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                som.play()  # Toca o som quando a tecla "Espaço" for pressionada

    tela.fill(preto)

    pygame.display.update()

pygame.quit()
sys.exit()
