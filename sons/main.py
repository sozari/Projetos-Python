import time
import pygame
from pygame.locals import * #está importando coisas necessárias para lidar com gráficos

# Inicialização do Pygame
pygame.init()#inicializa o programa no pygame


def main():
    morte = pygame.mixer.Sound("sons/midia/morte.mp3")
    moeda = pygame.mixer.Sound("sons/midia/moeda.mp3")
    comemoracao = pygame.mixer.Sound("sons/midia/comemoracao.mp3")

    print("Digite uma das opções")
    print("morte [1] / moeda [2] / comemoracao[3]")
   
    opc = input("")

    match opc:
        case '1':
            morte.play()
        case '2':
            moeda.play()
        case '3':
            comemoracao.play()
    time.sleep(10)

main()