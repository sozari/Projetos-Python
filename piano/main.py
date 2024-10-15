import time
import pygame
from pygame.locals import * #está importando coisas necessárias para lidar com gráficos

# Inicialização do Pygame
pygame.init()#inicializa o programa no pygame

# Definindo as dimensões da janela
largura = 800
altura = 200
tamanho_tecla = 60

# Definindo cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Criando a janela
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Piano Simples")

# Carregando sons das teclas
sons = {
    K_a: pygame.mixer.Sound("piano/midia/do-stretched.wav"),
    K_s: pygame.mixer.Sound("piano/midia/re-stretched.wav"),
    K_d: pygame.mixer.Sound("piano/midia/mi-stretched.wav"),
    K_f: pygame.mixer.Sound("piano/midia/fa-stretched.wav"),
    K_g: pygame.mixer.Sound("piano/midia/sol-stretched.wav"),
    K_h: pygame.mixer.Sound("piano/midia/la-stretched.wav"),
    K_j: pygame.mixer.Sound("piano/midia/si-stretched.wav"),
   
}
do = pygame.mixer.Sound("piano/midia/do-stretched.wav")
re = pygame.mixer.Sound("piano/midia/re-stretched.wav")
mi = pygame.mixer.Sound("piano/midia/mi-stretched.wav")
fa = pygame.mixer.Sound("piano/midia/fa-stretched.wav")
sol = pygame.mixer.Sound("piano/midia/sol-stretched.wav")
la = pygame.mixer.Sound("piano/midia/la-stretched.wav")
si = pygame.mixer.Sound("piano/midia/si-stretched.wav")

def roda_musica():
    do.play()
    time.sleep(0.5)
    re.play()

roda_musica()
# Loop principal
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            executando = False
        elif evento.type == KEYDOWN:
            if evento.key in sons:
                sons[evento.key].play()

    # Desenhar o piano na tela
    janela.fill(branco)
    for i, (tecla, som) in enumerate(sons.items()):
        pygame.draw.rect(janela, preto if i % 2 == 0 else branco, (i * tamanho_tecla, 0, tamanho_tecla, altura))
    pygame.display.flip()

# Finalizando o Pygame
pygame.quit()