'''
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''

import pygame

music = input('Digite o nome do arquivo de aúdio que deseja executar (o arquivo precisa estar na mesma pasta que o código): ')

pygame.init()

pygame.mixer.music.load(music)

pygame.mixer.music.play()

input()

pygame.event.wait()
