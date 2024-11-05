import pygame
import pygame.ftfont
from pygame.locals import *
from sys import exit
from random import random
from operator import neg

pygame.init()

fps = 45
relogio = pygame.time.Clock()

tela_largura = 1080
tela_altura = 720
tela = pygame.display.set_mode((tela_largura, tela_altura))

pygame.display.set_caption('Jogo do Lukashi')

fonte = pygame.font.SysFont('arial', 25, True, False)

obj_largura = 100
obj_altura = 100
o_x = tela_largura/2 - obj_largura/2
o_y = 0 - obj_altura
obj_velocidade = 7


player_largura = 50
player_altura = 50
p_x = 30
p_y = tela_altura / 2 - player_altura / 2
p_velocidade = 14

comida_largura = 15
comida_altura = 15
comida_x = tela_largura * random() - comida_largura
comida_y = tela_altura * random() - comida_altura

pontos = 0

while True:
    relogio.tick(fps)
    tela.fill((0,0,0))

    texto_pontos = f'Score: {pontos}'
    texto_pontos_formatado = fonte.render(texto_pontos, True, (255,255,255))


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    rect_comida = pygame.draw.rect(tela, (255,255,0), (comida_x, comida_y, comida_largura, comida_altura))


    rect_player = pygame.draw.rect(tela, (0,255,0), (p_x, p_y, player_largura, player_altura))
    if pygame.key.get_pressed()[K_a]:
        p_x -= p_velocidade
    if pygame.key.get_pressed()[K_d]:
        p_x += p_velocidade
    if pygame.key.get_pressed()[K_w]:
        p_y -= p_velocidade
    if pygame.key.get_pressed()[K_s]:
        p_y += p_velocidade
        

    rect_obj = pygame.draw.rect(tela, (255,0,0), (o_x, o_y, obj_largura, obj_altura))
    o_y += obj_velocidade
    if o_y > tela_altura + obj_altura:
        o_y = 0 - obj_altura

    if rect_player.colliderect(rect_obj):
        p_x = 0
        p_y = 0
        comida_x = tela_largura * random()
        comida_y = tela_altura * random()
        obj_velocidade = 7
        o_y = 0 - obj_altura
        pontos = 0

    if rect_player.colliderect(rect_comida):
        pontos += 1
        comida_x = tela_largura * random()
        comida_y = tela_altura * random()
        obj_velocidade += 1
        



    
    tela.blit(texto_pontos_formatado, (tela_largura - tela_largura/4, 40))

    pygame.display.update()